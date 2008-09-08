#!/usr/bin/env python
"""
	This software was developed by the University of Tennessee as part of the
	Distributed Data Analysis of Neutron Scattering Experiments (DANSE)
	project funded by the US National Science Foundation.

	If you use DANSE applications to do scientific research that leads to
	publication, we ask that you acknowledge the use of the software with the
	following sentence:

	"This work benefited from DANSE software developed under NSF award DMR-0520547."

	copyright 2008, University of Tennessee
"""

""" Provide functionality for a C extension model

	WARNING: THIS FILE WAS GENERATED BY WRAPPERGENERATOR.PY
 	         DO NOT MODIFY THIS FILE, MODIFY ../c_extensions/sphere.h
 	         AND RE-RUN THE GENERATOR SCRIPT

"""

from sans.models.BaseComponent import BaseComponent
from sans_extension.c_models import CSphereModel
import copy    
    
class SphereModel(CSphereModel, BaseComponent):
    """ Class that evaluates a SphereModel model. 
    	This file was auto-generated from ../c_extensions/sphere.h.
    	Refer to that file and the structure it contains
    	for details of the model.
    	List of default parameters:
         scale           = 1e-006 
         radius          = 60.0 A
         contrast        = 1.0 A-2
         background      = 0.0 cm-1

    """
        
    def __init__(self):
        """ Initialization """
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        CSphereModel.__init__(self)
        
        ## Name of the model
        self.name = "SphereModel"

		## Parameter details [units, min, max]
        self.details = {}
        self.details['scale'] = ['', None, None]
        self.details['radius'] = ['A', None, None]
        self.details['contrast'] = ['A-2', None, None]
        self.details['background'] = ['cm-1', None, None]

   
    def clone(self):
        """ Return a identical copy of self """
        obj = SphereModel()
        obj.params = copy.deepcopy(self.params)
        return obj   
   
    def run(self, x = 0.0):
        """ Evaluate the model
            @param x: input q, or [q,phi]
            @return: scattering function P(q)
        """
        
        return CSphereModel.run(self, x)
   
    def runXY(self, x = 0.0):
        """ Evaluate the model in cartesian coordinates
            @param x: input q, or [qx, qy]
            @return: scattering function P(q)
        """
        
        return CSphereModel.runXY(self, x)
        
    def set_dispersion(self, parameter, dispersion):
        """
            Set the dispersion object for a model parameter
            @param parameter: name of the parameter [string]
            @dispersion: dispersion object of type DispersionModel
        """
        return CSphereModel.set_dispersion(self, parameter, dispersion.cdisp)
        
   
# End of file
