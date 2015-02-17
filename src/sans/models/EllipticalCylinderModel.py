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
   src\sans\models\include\elliptical_cylinder.h
   AND RE-RUN THE GENERATOR SCRIPT
"""

from sans.models.BaseComponent import BaseComponent
from sans.models.sans_extension.c_models import CEllipticalCylinderModel

def create_EllipticalCylinderModel():
    """
       Create a model instance
    """
    obj = EllipticalCylinderModel()
    # CEllipticalCylinderModel.__init__(obj) is called by
    # the EllipticalCylinderModel constructor
    return obj

class EllipticalCylinderModel(CEllipticalCylinderModel, BaseComponent):
    """ 
    Class that evaluates a EllipticalCylinderModel model. 
    This file was auto-generated from src\sans\models\include\elliptical_cylinder.h.
    Refer to that file and the structure it contains
    for details of the model.
    
    List of default parameters:

    * r_minor         = 20.0 [A]
    * scale           = 1.0 
    * r_ratio         = 1.5 
    * length          = 400.0 [A]
    * sldCyl          = 4e-06 [1/A^(2)]
    * sldSolv         = 1e-06 [1/A^(2)]
    * background      = 0.0 [1/cm]
    * cyl_theta       = 90.0 [deg]
    * cyl_phi         = 0.0 [deg]
    * cyl_psi         = 0.0 [deg]

    """
        
    def __init__(self, multfactor=1):
        """ Initialization """
        self.__dict__ = {}
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        #apply(CEllipticalCylinderModel.__init__, (self,)) 

        CEllipticalCylinderModel.__init__(self)
        self.is_multifunc = False
		        
        ## Name of the model
        self.name = "EllipticalCylinderModel"
        ## Model description
        self.description = """
         Model parameters: r_minor = the radius of minor axis of the cross section
		r_ratio = the ratio of (r_major /r_minor >= 1)
		length = the length of the cylinder
		sldCyl = SLD of the cylinder
		sldSolv = SLD of solvent -
		background = incoherent background
        """
       
        ## Parameter details [units, min, max]
        self.details = {}
        self.details['r_minor'] = ['[A]', None, None]
        self.details['scale'] = ['', None, None]
        self.details['r_ratio'] = ['', None, None]
        self.details['length'] = ['[A]', None, None]
        self.details['sldCyl'] = ['[1/A^(2)]', None, None]
        self.details['sldSolv'] = ['[1/A^(2)]', None, None]
        self.details['background'] = ['[1/cm]', None, None]
        self.details['cyl_theta'] = ['[deg]', None, None]
        self.details['cyl_phi'] = ['[deg]', None, None]
        self.details['cyl_psi'] = ['[deg]', None, None]

        ## fittable parameters
        self.fixed = ['cyl_phi.width',
                      'cyl_theta.width',
                      'cyl_psi.width',
                      'length.width',
                      'r_minor.width',
                      'r_ratio.width']
        
        ## non-fittable parameters
        self.non_fittable = []
        
        ## parameters with orientation
        self.orientation_params = ['cyl_phi',
                                   'cyl_theta',
                                   'cyl_psi',
                                   'cyl_phi.width',
                                   'cyl_theta.width',
                                   'cyl_psi.width']

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
        return (create_EllipticalCylinderModel, tuple(), state, None, None)
        
    def clone(self):
        """ Return a identical copy of self """
        return self._clone(EllipticalCylinderModel())   
       	
    def run(self, x=0.0):
        """ 
        Evaluate the model
        
        :param x: input q, or [q,phi]
        
        :return: scattering function P(q)
        
        """
        return CEllipticalCylinderModel.run(self, x)
   
    def runXY(self, x=0.0):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q, or [qx, qy]
        
        :return: scattering function P(q)
        
        """
        return CEllipticalCylinderModel.runXY(self, x)
        
    def evalDistribution(self, x):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q[], or [qx[], qy[]]
        
        :return: scattering function P(q[])
        
        """
        return CEllipticalCylinderModel.evalDistribution(self, x)
        
    def calculate_ER(self):
        """ 
        Calculate the effective radius for P(q)*S(q)
        
        :return: the value of the effective radius
        
        """       
        return CEllipticalCylinderModel.calculate_ER(self)
        
    def calculate_VR(self):
        """ 
        Calculate the volf ratio for P(q)*S(q)
        
        :return: the value of the volf ratio
        
        """       
        return CEllipticalCylinderModel.calculate_VR(self)
              
    def set_dispersion(self, parameter, dispersion):
        """
        Set the dispersion object for a model parameter
        
        :param parameter: name of the parameter [string]
        :param dispersion: dispersion object of type DispersionModel
        
        """
        return CEllipticalCylinderModel.set_dispersion(self,
               parameter, dispersion.cdisp)
        
   
# End of file

