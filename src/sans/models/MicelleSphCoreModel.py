##############################################################################
# This software was developed by the University of Tennessee as part of the
# Distributed Data Analysis of Neutron Scattering Experiments (DANSE)
# project funded by the US National Science Foundation.
#
# If you use DANSE applications to do scientific research that leads to
# publication, we ask that you acknowledge the use of the software with the
# following sentence:
#
# This work benefited from DANSE software developed under NSF award DMR-0520547
#
# Copyright 2008-2011, University of Tennessee
##############################################################################

""" 
Provide functionality for a C extension model

.. WARNING::

   THIS FILE WAS GENERATED BY WRAPPERGENERATOR.PY
   DO NOT MODIFY THIS FILE, MODIFY
   src\sans\models\include\micelleSphCore.h
   AND RE-RUN THE GENERATOR SCRIPT
"""

from sans.models.BaseComponent import BaseComponent
from sans.models.sans_extension.c_models import CMicelleSphCoreModel

def create_MicelleSphCoreModel():
    """
       Create a model instance
    """
    obj = MicelleSphCoreModel()
    # CMicelleSphCoreModel.__init__(obj) is called by
    # the MicelleSphCoreModel constructor
    return obj

class MicelleSphCoreModel(CMicelleSphCoreModel, BaseComponent):
    """ 
    Class that evaluates a MicelleSphCoreModel model. 
    This file was auto-generated from src\sans\models\include\micelleSphCore.h.
    Refer to that file and the structure it contains
    for details of the model.
    
    List of default parameters:

    * scale           = 1.0 
    * ndensity        = 8.94e+15 [1/cm^(3)]
    * v_core          = 62624.0 [A^3]
    * v_corona        = 61940.0 [A^(3)]
    * rho_solv        = 6.4e-06 [1/A^(2)]
    * rho_core        = 3.4e-07 [1/A^(2)]
    * rho_corona      = 8e-07 [1/A^(2)]
    * radius_core     = 45.0 [A]
    * radius_gyr      = 20.0 [A]
    * d_penetration   = 1.0 
    * n_aggreg        = 6.0 
    * background      = 0.0 [1/cm]

    """
        
    def __init__(self, multfactor=1):
        """ Initialization """
        self.__dict__ = {}
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        #apply(CMicelleSphCoreModel.__init__, (self,)) 

        CMicelleSphCoreModel.__init__(self)
        self.is_multifunc = False
		        
        ## Name of the model
        self.name = "MicelleSphCoreModel"
        ## Model description
        self.description = """
        
		Model parameters:
		ndensity : number density of micelles
		v_core: volume block in core
		v_corona: volume block in corona
		rho_solv: sld of solvent
		rho_core: sld of core
		rho_corona: sld of corona
		radius_core: radius of core
		radius_gyr: radius of gyration of chains in corona
		d_penetration: close to unity, mimics non-penetration of gaussian chains
		n_aggreg: aggregation number of the micelle
		background: incoherent background
		scale : scale factor
        """
       
        ## Parameter details [units, min, max]
        self.details = {}
        self.details['scale'] = ['', None, None]
        self.details['ndensity'] = ['[1/cm^(3)]', None, None]
        self.details['v_core'] = ['[A^3]', None, None]
        self.details['v_corona'] = ['[A^(3)]', None, None]
        self.details['rho_solv'] = ['[1/A^(2)]', None, None]
        self.details['rho_core'] = ['[1/A^(2)]', None, None]
        self.details['rho_corona'] = ['[1/A^(2)]', None, None]
        self.details['radius_core'] = ['[A]', None, None]
        self.details['radius_gyr'] = ['[A]', None, None]
        self.details['d_penetration'] = ['', None, None]
        self.details['n_aggreg'] = ['', None, None]
        self.details['background'] = ['[1/cm]', None, None]

        ## fittable parameters
        self.fixed = ['radius_core.width',
                      'radius_gyr.width']
        
        ## non-fittable parameters
        self.non_fittable = []
        
        ## parameters with orientation
        self.orientation_params = []

        ## parameters with magnetism
        self.magnetic_params = []

        self.category = None
        self.multiplicity_info = None
        
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
        return (create_MicelleSphCoreModel, tuple(), state, None, None)
        
    def clone(self):
        """ Return a identical copy of self """
        return self._clone(MicelleSphCoreModel())   
       	
    def run(self, x=0.0):
        """ 
        Evaluate the model
        
        :param x: input q, or [q,phi]
        
        :return: scattering function P(q)
        
        """
        return CMicelleSphCoreModel.run(self, x)
   
    def runXY(self, x=0.0):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q, or [qx, qy]
        
        :return: scattering function P(q)
        
        """
        return CMicelleSphCoreModel.runXY(self, x)
        
    def evalDistribution(self, x):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q[], or [qx[], qy[]]
        
        :return: scattering function P(q[])
        
        """
        return CMicelleSphCoreModel.evalDistribution(self, x)
        
    def calculate_ER(self):
        """ 
        Calculate the effective radius for P(q)*S(q)
        
        :return: the value of the effective radius
        
        """       
        return CMicelleSphCoreModel.calculate_ER(self)
        
    def calculate_VR(self):
        """ 
        Calculate the volf ratio for P(q)*S(q)
        
        :return: the value of the volf ratio
        
        """       
        return CMicelleSphCoreModel.calculate_VR(self)
              
    def set_dispersion(self, parameter, dispersion):
        """
        Set the dispersion object for a model parameter
        
        :param parameter: name of the parameter [string]
        :param dispersion: dispersion object of type DispersionModel
        
        """
        return CMicelleSphCoreModel.set_dispersion(self,
               parameter, dispersion.cdisp)
        
   
# End of file

