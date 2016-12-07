import unittest

from UnitTesting import AboutBoxTest
from UnitTesting import DataExplorerTest
from UnitTesting import WelcomePanelTest
from UnitTesting import DroppableDataLoadWidgetTest
from UnitTesting import GuiManagerTest
from UnitTesting import GuiUtilsTest
from UnitTesting import MainWindowTest
from UnitTesting import TestUtilsTest
from UnitTesting import PlotHelperTest
from UnitTesting import PlotterTest
from UnitTesting import Plotter2DTest
from UnitTesting import SasviewLoggerTest
from UnitTesting import ScalePropertiesTest
from UnitTesting import KiessigCalculatorTest
from UnitTesting import DensityCalculatorTest

def suite():
    suites = (
        unittest.makeSuite(AboutBoxTest.AboutBoxTest,          'test'),
        unittest.makeSuite(DataExplorerTest.DataExplorerTest,  'test'),
        unittest.makeSuite(WelcomePanelTest.WelcomePanelTest,  'test'),
        unittest.makeSuite(DroppableDataLoadWidgetTest.DroppableDataLoadWidgetTest, 'test'),
        unittest.makeSuite(GuiManagerTest.GuiManagerTest,      'test'),
        unittest.makeSuite(GuiUtilsTest.GuiUtilsTest,          'test'),
        unittest.makeSuite(MainWindowTest.MainWindowTest,      'test'),
        unittest.makeSuite(TestUtilsTest.TestUtilsTest,        'test'),
        unittest.makeSuite(PlotHelperTest.PlotHelperTest,       'test'),
        unittest.makeSuite(PlotterTest.PlotterTest,          'test'),
        unittest.makeSuite(Plotter2DTest.Plotter2DTest,        'test'),
        unittest.makeSuite(SasviewLoggerTest.SasviewLoggerTest,    'test'),
        unittest.makeSuite(ScalePropertiesTest.ScalePropertiesTest,  'test'),
        unittest.makeSuite(KiessigCalculatorTest.KiessigCalculatorTest, 'test'),
        unittest.makeSuite(DensityCalculatorTest.DensityCalculatorTest, 'test'),
    )
    return unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main(defaultTest="suite")

