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
         DO NOT MODIFY THIS FILE, MODIFY ..\c_extensions\capcyl.h
         AND RE-RUN THE GENERATOR SCRIPT

"""

from sans.models.BaseComponent import BaseComponent
from sans_extension.c_models import CCappedCylinderModel
import copy    

def create_CappedCylinderModel():
    obj = CappedCylinderModel()
    #CCappedCylinderModel.__init__(obj) is called by CappedCylinderModel constructor
    return obj

class CappedCylinderModel(CCappedCylinderModel, BaseComponent):
    """ 
    Class that evaluates a CappedCylinderModel model. 
    This file was auto-generated from ..\c_extensions\capcyl.h.
    Refer to that file and the structure it contains
    for details of the model.
    List of default parameters:
         scale           = 1.0 
         rad_cyl         = 20.0 [A]
         len_cyl         = 400.0 [A]
         rad_cap         = 40.0 [A]
         sld_capcyl      = 1e-006 [1/A^(2)]
         sld_solv        = 6.3e-006 [1/A^(2)]
         background      = 0.0 [1/cm]
         theta           = 0.0 [deg]
         phi             = 0.0 [deg]

    """
        
    def __init__(self):
        """ Initialization """
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        #apply(CCappedCylinderModel.__init__, (self,)) 
        CCappedCylinderModel.__init__(self)
        
        ## Name of the model
        self.name = "CappedCylinderModel"
        ## Model description
        self.description ="""Calculates the scattering from a cylinder with spherical section end-caps.
		That is, a sphereocylinder
		with end caps that have a radius larger than
		that of the cylinder and the center of the
		end cap radius lies within the cylinder.
		Note: As the length of cylinder -->0,
		it becomes a ConvexLens.
		It must be that rad_cyl <(=) rad_cap.
		[Parameters];
		scale: volume fraction of spheres,
		background:incoherent background,
		rad_cyl: radius of the cylinder,
		len_cyl: length of the cylinder,
		rad_cap: radius of the semi-spherical cap,
		sld_capcyl: SLD of the capped cylinder,
		sld_solv: SLD of the solvent."""
       
        ## Parameter details [units, min, max]
        self.details = {}
        self.details['scale'] = ['', None, None]
        self.details['rad_cyl'] = ['[A]', None, None]
        self.details['len_cyl'] = ['[A]', None, None]
        self.details['rad_cap'] = ['[A]', None, None]
        self.details['sld_capcyl'] = ['[1/A^(2)]', None, None]
        self.details['sld_solv'] = ['[1/A^(2)]', None, None]
        self.details['background'] = ['[1/cm]', None, None]
        self.details['theta'] = ['[deg]', None, None]
        self.details['phi'] = ['[deg]', None, None]

        ## fittable parameters
        self.fixed=['rad_cyl.width', 'len_cyl', 'rad_cap', 'phi.width', 'theta.width']
        
        ## non-fittable parameters
        self.non_fittable = []
        
        ## parameters with orientation
        self.orientation_params = ['phi', 'theta', 'phi.width', 'theta.width']

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
        return (create_CappedCylinderModel,tuple(), state, None, None)
        
    def clone(self):
        """ Return a identical copy of self """
        return self._clone(CappedCylinderModel())   
       	
   
    def run(self, x=0.0):
        """ 
        Evaluate the model
        
        :param x: input q, or [q,phi]
        
        :return: scattering function P(q)
        
        """
        
        return CCappedCylinderModel.run(self, x)
   
    def runXY(self, x=0.0):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q, or [qx, qy]
        
        :return: scattering function P(q)
        
        """
        
        return CCappedCylinderModel.runXY(self, x)
        
    def evalDistribution(self, x=[]):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q[], or [qx[], qy[]]
        
        :return: scattering function P(q[])
        
        """
        return CCappedCylinderModel.evalDistribution(self, x)
        
    def calculate_ER(self):
        """ 
        Calculate the effective radius for P(q)*S(q)
        
        :return: the value of the effective radius
        
        """       
        return CCappedCylinderModel.calculate_ER(self)
        
    def set_dispersion(self, parameter, dispersion):
        """
        Set the dispersion object for a model parameter
        
        :param parameter: name of the parameter [string]
        :param dispersion: dispersion object of type DispersionModel
        
        """
        return CCappedCylinderModel.set_dispersion(self, parameter, dispersion.cdisp)
        
   
# End of file
