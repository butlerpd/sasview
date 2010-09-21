import wx
import sys

import copy,numpy
from danse.common.plottools.PlotPanel import PlotPanel
from danse.common.plottools.plottables import Graph
from sans.guiframe.dataFitting import Theory1D
import pylab

DEFAULT_CMAP= pylab.cm.jet

_BOX_WIDTH = 76
_STATICBOX_WIDTH = 400
_SCALE = 1e-6

#SLD panel size 
if sys.platform.count("win32")>0:
    _STATICBOX_WIDTH = 380
    PANEL_SIZE = 420
    FONT_VARIANT = 0
else:
    _STATICBOX_WIDTH = 410
    PANEL_SIZE = 450
    FONT_VARIANT = 1
    

            
class SLDPanel(wx.Dialog):
    """
    Provides the SLD profile plot panel.
    """
    ## Internal nickname for the window, used by the AUI manager
    window_name = "SLD Profile"
    ## Name to appear on the window title bar
    window_caption = "SLD Profile"
    ## Flag to tell the AUI manager to put this panel in the center pane
    CENTER_PANE = True
    def __init__(self, parent=None,base=None,data =None, id = -1, *args, **kwds):
        kwds["style"] =  wx.DEFAULT_DIALOG_STYLE
        kwds["size"] = wx.Size(_STATICBOX_WIDTH*2,PANEL_SIZE) 
        wx.Dialog.__init__(self, parent, id = id,  *args, **kwds)
        if data != None:
            
            #Font size 
            kwds =[]
            self.SetWindowVariant(variant=FONT_VARIANT)

            self.SetTitle("Scattering Length Density Profile")
            self.parent = base
            self.data = data
            self.str = self.data.__str__()

            ## when 2 data have the same id override the 1 st plotted
            self.name = self.data.name
            
            # Panel for 2D plot
            self.plotpanel    = SLDplotpanel(self, -1, style=wx.TRANSPARENT_WINDOW)
            self.cmap = DEFAULT_CMAP
            ## Create Artist and bind it
            self.subplot = self.plotpanel.subplot

            self._setup_layout()
            self.newplot=Theory1D(self.data.x,self.data.y)
            self.newplot.name = 'SLD'
            self.plotpanel.add_image(self.newplot) 

            self.Centre()
            self.Layout()
            
    
    def _setup_layout(self):
        """
        Set up the layout
        """
        #  panel
        sizer = wx.GridBagSizer(14,14)
        
        sizer.Add(self.plotpanel,(0, 0), (13, 13), wx.EXPAND | wx.LEFT| wx.RIGHT, 15)

        #-----Button------------1
        id = wx.NewId()
        button_reset = wx.Button(self, id, "Close")
        button_reset.SetToolTipString("Close...")
        button_reset.Bind(wx.EVT_BUTTON, self._close, id = button_reset.GetId()) 
        sizer.Add(button_reset, (13, 12), flag=wx.RIGHT | wx.BOTTOM, border=15)

        sizer.AddGrowableCol(2)
        sizer.AddGrowableRow(3)
        self.SetSizerAndFit(sizer)
        button_reset.SetFocus()
        self.Centre()
        self.Show(True)

    def _close(self, event):
        """
        Close the dialog
        """
        
        self.Close(True)

    def _draw_model(self,event):
        """
         on_close, update the model2d plot
        """
        pass

           
class SLDplotpanel(PlotPanel):
    """
    Panel
    """
    def __init__(self, parent, id = -1, color = None, dpi = None, **kwargs):
        """
        """
        PlotPanel.__init__(self, parent, id=id, color=color, dpi=dpi, **kwargs)
        # Keep track of the parent Frame
        self.parent = parent
        # Internal list of plottable names (because graph 
        # doesn't have a dictionary of handles for the plottables)
        self.plots = {}
        self.graph = Graph()


         
    def add_image(self, plot):
        """
        Add image(Theory1D)
        """
        self.plots[plot.name] = plot
        #init graph
        self.gaph = Graph()
        #add plot
        self.graph.add(plot)
        #add axes
        self.graph.xaxis('\\rm{Radius} ', '\\AA')
        self.graph.yaxis('\\rm{SLD} ', '\\AA^{-2}')


        #draw
        self.graph.render(self)
        self.subplot.figure.canvas.draw_idle()
        
    def onContextMenu(self, event):
        """
        Default context menu for a plot panel
        
        """
        pass
    
    def on_set_focus(self, event):
        """
        send to the parenet the current panel on focus
        
        """
        #Not implemented
        pass

    def on_kill_focus(self, event):
        """
        reset the panel color
        
        """
        #Not implemented
        pass


class ViewerFrame(wx.Frame):
    """
    Add comment
    """
    def __init__(self, parent, id, title):
        """
        comment
        :param parent: parent panel/container
        """
        # Initialize the Frame object
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(950,850))
        
        # Panel for 1D plot
        self.plotpanel    = SLDplotpanel(self, -1, style=wx.RAISED_BORDER)

class ViewApp(wx.App):
    def OnInit(self):
        frame = ViewerFrame(None, -1, 'testView')    
        frame.Show(True)
        self.SetTopWindow(frame)
        
        return True
               
if __name__ == "__main__": 
    app = ViewApp(0)
    app.MainLoop()     
