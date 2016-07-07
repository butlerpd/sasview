import sys
import subprocess
import unittest
import webbrowser
import logging

from PyQt4.QtGui import *
from PyQt4.QtTest import QTest
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from mock import MagicMock

# Local
from DataExplorer import DataExplorerWindow
from UI.AcknowledgementsUI import Acknowledgements
from AboutBox import AboutBox
from WelcomePanel import WelcomePanel

from GuiManager import GuiManager
from UI.MainWindowUI import MainWindow
from UnitTesting.TestUtils import QtSignalSpy

app = QApplication(sys.argv)

class GuiManagerTest(unittest.TestCase):
    '''Test the Main Window functionality'''
    def setUp(self):
        '''Create the tested object'''
        class MainSasViewWindow(MainWindow):
            # Main window of the application
            def __init__(self, reactor, parent=None):
                super(MainSasViewWindow, self).__init__(parent)
        
                # define workspace for dialogs.
                self.workspace = QWorkspace(self)
                self.setCentralWidget(self.workspace)

        self.manager = GuiManager(MainSasViewWindow(None), None)

    def tearDown(self):
        '''Destroy the GUI'''
        self.manager = None

    def testDefaults(self):
        """
        Test the object in its default state
        """
        self.assertIsInstance(self.manager.filesWidget, DataExplorerWindow)
        self.assertIsInstance(self.manager.dockedFilesWidget, QDockWidget)
        self.assertEqual(self.manager.dockedFilesWidget.features(), QDockWidget.NoDockWidgetFeatures)
        self.assertEqual(self.manager._workspace.dockWidgetArea(self.manager.dockedFilesWidget), Qt.LeftDockWidgetArea)
        self.assertIsInstance(self.manager.ackWidget, Acknowledgements)
        self.assertIsInstance(self.manager.aboutWidget, AboutBox)
        self.assertIsInstance(self.manager.welcomePanel, WelcomePanel)

    def testUpdatePerspective(self):
        """
        """
        pass

    def testUpdateStatusBar(self):
        """
        """
        pass

    def testSetData(self):
        """
        """
        pass

    def testSetData(self):
        """
        """
        pass

    def testQuitApplication(self):
        """
        Test that the custom exit method is called on shutdown
        """
        # Must mask sys.exit, otherwise the whole testing process stops.
        sys.exit = MagicMock()

        # Say No to the close dialog
        QMessageBox.question = MagicMock(return_value=QMessageBox.No)

        # Open, then close the manager
        self.manager.quitApplication()

        # See that the MessageBox method got called
        self.assertTrue(QMessageBox.question.called)

        # Say Yes to the close dialog
        QMessageBox.question = MagicMock(return_value=QMessageBox.Yes)

        # Open, then close the manager
        self.manager.quitApplication()

        # See that the MessageBox method got called
        self.assertTrue(QMessageBox.question.called)

    def testCheckUpdate(self):
        """
        Tests the SasView website version polling
        """
        self.manager.processVersion = MagicMock()
        version = {'update_url'  : 'http://www.sasview.org/sasview.latestversion', 
                   'version'     : '3.1.2',
                   'download_url': 'https://github.com/SasView/sasview/releases'}
        self.manager.checkUpdate()

        self.manager.processVersion.assert_called_with(version)

        pass

    def testProcessVersion(self):
        """
        Tests the version checker logic
        """
        # 1. version = 0.0.0
        version_info = {u'version' : u'0.0.0'}
        spy_status_update = QtSignalSpy(self.manager, self.manager.communicate.statusBarUpdateSignal)

        self.manager.processVersion(version_info)

        self.assertEqual(spy_status_update.count(), 1)
        message = 'Could not connect to the application server. Please try again later.'
        self.assertIn(message, str(spy_status_update.signal(index=0)))

        # 2. version < LocalConfig.__version__
        version_info = {u'version' : u'0.0.1'}
        spy_status_update = QtSignalSpy(self.manager, self.manager.communicate.statusBarUpdateSignal)

        self.manager.processVersion(version_info)

        self.assertEqual(spy_status_update.count(), 1)
        message = 'You have the latest version of SasView'
        self.assertIn(message, str(spy_status_update.signal(index=0)))

        # 3. version > LocalConfig.__version__
        version_info = {u'version' : u'999.0.0'}
        spy_status_update = QtSignalSpy(self.manager, self.manager.communicate.statusBarUpdateSignal)
        webbrowser.open = MagicMock()

        self.manager.processVersion(version_info)

        self.assertEqual(spy_status_update.count(), 1)
        message = 'Version 999.0.0 is available!'
        self.assertIn(message, str(spy_status_update.signal(index=0)))

        webbrowser.open.assert_called_with("https://github.com/SasView/sasview/releases")

        # 4. couldn't load version
        version_info = {}
        logging.error = MagicMock()
        spy_status_update = QtSignalSpy(self.manager, self.manager.communicate.statusBarUpdateSignal)

        self.manager.processVersion(version_info)

        # Retrieve and compare arguments of the mocked call
        message = "guiframe: could not get latest application version number"
        args, _ = logging.error.call_args
        self.assertIn(message, args[0])

        # Check the signal message
        message = 'Could not connect to the application server.'
        self.assertIn(message, str(spy_status_update.signal(index=0)))

    def testActions(self):
        """
        """
        pass

    #### FILE ####
    def testActionLoadData(self):
        """
        Menu File/Load Data File(s)
        """
        # Mock the system file open method
        QFileDialog.getOpenFileNames = MagicMock(return_value=None)

        # invoke the action
        self.manager.actionLoadData()

        # Test the getOpenFileName() dialog called once
        self.assertTrue(QFileDialog.getOpenFileNames.called)

    def testActionLoadDataFolder(self):
        """
        Menu File/Load Data Folder
        """
        # Mock the system file open method
        QFileDialog.getExistingDirectory = MagicMock(return_value=None)

        # invoke the action
        self.manager.actionLoad_Data_Folder()

        # Test the getOpenFileName() dialog called once
        self.assertTrue(QFileDialog.getExistingDirectory.called)

    #### VIEW ####
    def testActionHideToolbar(self):
        """
        Menu View/Hide Toolbar
        """
        # Need to display the main window to initialize the toolbar.
        self.manager._workspace.show()

        # Check the initial state
        self.assertTrue(self.manager._workspace.toolBar.isVisible())
        self.assertEqual('Hide Toolbar', self.manager._workspace.actionHide_Toolbar.text())

        # Invoke action
        self.manager.actionHide_Toolbar()

        # Assure changes propagated correctly
        self.assertFalse(self.manager._workspace.toolBar.isVisible())
        self.assertEqual('Show Toolbar', self.manager._workspace.actionHide_Toolbar.text())

        # Revert
        self.manager.actionHide_Toolbar()

        # Assure the original values are back
        self.assertTrue(self.manager._workspace.toolBar.isVisible())
        self.assertEqual('Hide Toolbar', self.manager._workspace.actionHide_Toolbar.text())


    #### HELP ####
    def testActionDocumentation(self):
        """
        Menu Help/Documentation
        """
        #Mock the QWebView method
        QWebView.show = MagicMock()

        # Assure the filename is correct
        self.assertIn("index.html", self.manager._helpLocation)

        # Invoke the action
        self.manager.actionDocumentation()

        # Check if show() got called
        self.assertTrue(QWebView.show.called)

    def testActionTutorial(self):
        """
        Menu Help/Tutorial
        """
        # Mock subprocess.Popen
        subprocess.Popen = MagicMock()

        tested_location = self.manager._tutorialLocation

        # Assure the filename is correct
        self.assertIn("Tutorial.pdf", tested_location)

        # Invoke the action
        self.manager.actionTutorial()

        # Check if popen() got called
        self.assertTrue(subprocess.Popen.called)

        #Check the popen() call arguments
        subprocess.Popen.assert_called_with([tested_location], shell=True)

    def testActionAcknowledge(self):
        """
        Menu Help/Acknowledge
        """
        self.manager.actionAcknowledge()

        # Check if the window is actually opened.
        self.assertTrue(self.manager.ackWidget.isVisible())
        self.assertIn("developers@sasview.org", self.manager.ackWidget.label.text())

    def testActionCheck_for_update(self):
        """
        Menu Help/Check for update
        """
        # Just make sure checkUpdate is called.
        self.manager.checkUpdate = MagicMock()

        self.manager.actionCheck_for_update()

        self.assertTrue(self.manager.checkUpdate.called)
             
       
if __name__ == "__main__":
    unittest.main()

