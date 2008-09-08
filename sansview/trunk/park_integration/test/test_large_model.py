"""
    Unit tests for fitting module 
"""
import unittest
from sans.guitools.plottables import Theory1D
from sans.guitools.plottables import Data1D
from sans.fit.AbstractFitEngine import Data,Model
import math
class testFitModule(unittest.TestCase):
    """ test fitting """
    def test_cylinder_park(self):
        """ test fitting large model with park"""
        #load data
        from sans.fit.Loader import Load
        load= Load()
        load.set_filename("cyl_testdata.txt")
        load.set_values()
        data11 = Data1D(x=[], y=[],dx=None, dy=None)
        load.load_data(data11)
        data1=Data(sans_data=data11)
        
        
        #Importing the Fit module
        from sans.fit.Fitting import Fit
        fitter= Fit('park')
        
        # Receives the type of model for the fitting
        from sans.models.CylinderModel import CylinderModel
        model1  = CylinderModel()
        model =Model(model1)
        
        #Do the fit SCIPY
        
        import math
        #pars1=['background','contrast', 'length']
        pars1=['background','contrast',\
                'cyl_phi','cyl_theta','length','radius','scale']
        pars1.sort()
        fitter.set_model(model,"M1",1,pars1)
        fitter.set_data(data1,1)
      
        result=fitter.fit()
        print "park",result.fitness,result.cov, result.pvec
        self.assert_(result.fitness)
        
     
    def test_cylinder_scipy(self):
        """ test fitting large model with scipy"""
        #load data
        from sans.fit.Loader import Load
        load= Load()
        load.set_filename("cyl_testdata.txt")
        load.set_values()
        data11 = Data1D(x=[], y=[],dx=None, dy=None)
        load.load_data(data11)
        data1=Data(sans_data=data11)
        
        
        #Importing the Fit module
        from sans.fit.Fitting import Fit
        fitter= Fit('scipy')
        
        # Receives the type of model for the fitting
        from sans.models.CylinderModel import CylinderModel
        model1  = CylinderModel()
        model =Model(model1)
        
        #Do the fit SCIPY
        fitter.set_data(data1,1)
        import math
        #pars1=['background','contrast', 'length']
        pars1=['background','contrast',\
                'cyl_phi','cyl_theta','length','radius','scale']
        pars1.sort()
        fitter.set_model(model,"M1",1,pars1)
        fitter.set_data(data1,1)
      
        result=fitter.fit()
        print "scipy",result.fitness,result.cov, result.pvec
        self.assert_(result.fitness)
        
    