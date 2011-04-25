#!/usr/bin/env python

##############################################################################
#	This software was developed by the University of Tennessee as part of the
#	Distributed Data Analysis of Neutron Scattering Experiments (DANSE)
#	project funded by the US National Science Foundation.
#
#	If you use DANSE applications to do scientific research that leads to
#	publication, we ask that you acknowledge the use of the software with the
#	following sentence:
#
#	"This work benefited from DANSE software developed under NSF award DMR-0520547."
#
#	copyright 2008, University of Tennessee
##############################################################################


""" 
Provide functionality for a C extension model

:WARNING: THIS FILE WAS GENERATED BY WRAPPERGENERATOR.PY
         DO NOT MODIFY THIS FILE, MODIFY ..\c_extensions\corefourshell.h
         AND RE-RUN THE GENERATOR SCRIPT

"""

from sans.models.BaseComponent import BaseComponent
from sans_extension.c_models import CCoreFourShellModel
import copy    

def create_CoreFourShellModel():
    obj = CoreFourShellModel()
    #CCoreFourShellModel.__init__(obj) is called by CoreFourShellModel constructor
    return obj

class CoreFourShellModel(CCoreFourShellModel, BaseComponent):
    """ 
    Class that evaluates a CoreFourShellModel model. 
    This file was auto-generated from ..\c_extensions\corefourshell.h.
    Refer to that file and the structure it contains
    for details of the model.
    List of default parameters:
         scale           = 1.0 
         rad_core0       = 60.0 [A]
         sld_core0       = 6.4e-006 [1/A^(2)]
         thick_shell1    = 10.0 [A]
         sld_shell1      = 1e-006 [1/A^(2)]
         thick_shell2    = 10.0 [A]
         sld_shell2      = 2e-006 [1/A^(2)]
         thick_shell3    = 10.0 [A]
         sld_shell3      = 3e-006 [1/A^(2)]
         thick_shell4    = 10.0 [A]
         sld_shell4      = 4e-006 [1/A^(2)]
         sld_solv        = 6.4e-006 [1/A^(2)]
         background      = 0.001 [1/cm]

    """
        
    def __init__(self):
        """ Initialization """
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        #apply(CCoreFourShellModel.__init__, (self,)) 
        CCoreFourShellModel.__init__(self)
        
        ## Name of the model
        self.name = "CoreFourShellModel"
        ## Model description
        self.description =""" Calculates the scattering intensity from a core-4 shell structure.
		scale = scale factor * volume fraction
		rad_core0: the radius of the core
		sld_core0: the SLD of the core
		thick_shelli: the thickness of the i'th shell from the core
		sld_shelli: the SLD of the i'th shell from the core
		sld_solv: the SLD of the solvent
		background: incoherent background"""
       
        ## Parameter details [units, min, max]
        self.details = {}
        self.details['scale'] = ['', None, None]
        self.details['rad_core0'] = ['[A]', None, None]
        self.details['sld_core0'] = ['[1/A^(2)]', None, None]
        self.details['thick_shell1'] = ['[A]', None, None]
        self.details['sld_shell1'] = ['[1/A^(2)]', None, None]
        self.details['thick_shell2'] = ['[A]', None, None]
        self.details['sld_shell2'] = ['[1/A^(2)]', None, None]
        self.details['thick_shell3'] = ['[A]', None, None]
        self.details['sld_shell3'] = ['[1/A^(2)]', None, None]
        self.details['thick_shell4'] = ['[A]', None, None]
        self.details['sld_shell4'] = ['[1/A^(2)]', None, None]
        self.details['sld_solv'] = ['[1/A^(2)]', None, None]
        self.details['background'] = ['[1/cm]', None, None]

        ## fittable parameters
        self.fixed=['thick_shell4.width', 'thick_shell1.width', 'thick_shell2.width', 'thick_shell3.width', 'rad_core0.width']
        
        ## non-fittable parameters
        self.non_fittable = []
        
        ## parameters with orientation
        self.orientation_params = []

    def __setstate__(self, state):
        """
        restore the state of a model from pickle
        """
        self.__dict__, self.params, self.dispersion = state
        
    def __reduce_ex__(self, proto):
        """
        Overwrite the __reduce_ex__ of PyTypeObject *type call in the init of 
        c model.
        """
        state = (self.__dict__, self.params, self.dispersion)
        return (create_CoreFourShellModel,tuple(), state, None, None)
        
    def clone(self):
        """ Return a identical copy of self """
        return self._clone(CoreFourShellModel())   
       	
   
    def run(self, x=0.0):
        """ 
        Evaluate the model
        
        :param x: input q, or [q,phi]
        
        :return: scattering function P(q)
        
        """
        
        return CCoreFourShellModel.run(self, x)
   
    def runXY(self, x=0.0):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q, or [qx, qy]
        
        :return: scattering function P(q)
        
        """
        
        return CCoreFourShellModel.runXY(self, x)
        
    def evalDistribution(self, x=[]):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q[], or [qx[], qy[]]
        
        :return: scattering function P(q[])
        
        """
        return CCoreFourShellModel.evalDistribution(self, x)
        
    def calculate_ER(self):
        """ 
        Calculate the effective radius for P(q)*S(q)
        
        :return: the value of the effective radius
        
        """       
        return CCoreFourShellModel.calculate_ER(self)
        
    def set_dispersion(self, parameter, dispersion):
        """
        Set the dispersion object for a model parameter
        
        :param parameter: name of the parameter [string]
        :param dispersion: dispersion object of type DispersionModel
        
        """
        return CCoreFourShellModel.set_dispersion(self, parameter, dispersion.cdisp)
        
   
# End of file
