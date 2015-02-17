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
   src\sans\models\include\core_shell_cylinder.h
   AND RE-RUN THE GENERATOR SCRIPT
"""

from sans.models.BaseComponent import BaseComponent
from sans.models.sans_extension.c_models import CCoreShellCylinderModel

def create_CoreShellCylinderModel():
    """
       Create a model instance
    """
    obj = CoreShellCylinderModel()
    # CCoreShellCylinderModel.__init__(obj) is called by
    # the CoreShellCylinderModel constructor
    return obj

class CoreShellCylinderModel(CCoreShellCylinderModel, BaseComponent):
    """ 
    Class that evaluates a CoreShellCylinderModel model. 
    This file was auto-generated from src\sans\models\include\core_shell_cylinder.h.
    Refer to that file and the structure it contains
    for details of the model.
    
    List of default parameters:

    * radius          = 20.0 [A]
    * scale           = 1.0 
    * thickness       = 10.0 [A]
    * length          = 400.0 [A]
    * core_sld        = 1e-06 [1/A^(2)]
    * shell_sld       = 4e-06 [1/A^(2)]
    * solvent_sld     = 1e-06 [1/A^(2)]
    * background      = 0.0 [1/cm]
    * axis_theta      = 90.0 [deg]
    * axis_phi        = 0.0 [deg]

    """
        
    def __init__(self, multfactor=1):
        """ Initialization """
        self.__dict__ = {}
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        #apply(CCoreShellCylinderModel.__init__, (self,)) 

        CCoreShellCylinderModel.__init__(self)
        self.is_multifunc = False
		        
        ## Name of the model
        self.name = "CoreShellCylinderModel"
        ## Model description
        self.description = """
        P(q,alpha)= scale/Vs*f(q)^(2) + bkg,
		where: f(q)= 2(core_sld
		- solvant_sld)* Vc*sin[qLcos(alpha/2)]
		/[qLcos(alpha/2)]*J1(qRsin(alpha))
		/[qRsin(alpha)]+2(shell_sld-solvent_sld)
		*Vs*sin[q(L+T)cos(alpha/2)][[q(L+T)
		*cos(alpha/2)]*J1(q(R+T)sin(alpha))
		/q(R+T)sin(alpha)]
		
		alpha:is the angle between the axis of
		the cylinder and the q-vector
		Vs: the volume of the outer shell
		Vc: the volume of the core
		L: the length of the core
		shell_sld: the scattering length density
		of the shell
		solvent_sld: the scattering length density
		of the solvent
		bkg: the background
		T: the thickness
		R+T: is the outer radius
		L+2T: The total length of the outershell
		J1: the first order Bessel function
		theta: axis_theta of the cylinder
		phi: the axis_phi of the cylinder...
        """
       
        ## Parameter details [units, min, max]
        self.details = {}
        self.details['radius'] = ['[A]', None, None]
        self.details['scale'] = ['', None, None]
        self.details['thickness'] = ['[A]', None, None]
        self.details['length'] = ['[A]', None, None]
        self.details['core_sld'] = ['[1/A^(2)]', None, None]
        self.details['shell_sld'] = ['[1/A^(2)]', None, None]
        self.details['solvent_sld'] = ['[1/A^(2)]', None, None]
        self.details['background'] = ['[1/cm]', None, None]
        self.details['axis_theta'] = ['[deg]', None, None]
        self.details['axis_phi'] = ['[deg]', None, None]

        ## fittable parameters
        self.fixed = ['axis_phi.width',
                      'axis_theta.width',
                      'length.width',
                      'radius.width',
                      'thickness.width']
        
        ## non-fittable parameters
        self.non_fittable = []
        
        ## parameters with orientation
        self.orientation_params = ['axis_phi',
                                   'axis_theta',
                                   'axis_phi.width',
                                   'axis_theta.width']

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
        return (create_CoreShellCylinderModel, tuple(), state, None, None)
        
    def clone(self):
        """ Return a identical copy of self """
        return self._clone(CoreShellCylinderModel())   
       	
    def run(self, x=0.0):
        """ 
        Evaluate the model
        
        :param x: input q, or [q,phi]
        
        :return: scattering function P(q)
        
        """
        return CCoreShellCylinderModel.run(self, x)
   
    def runXY(self, x=0.0):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q, or [qx, qy]
        
        :return: scattering function P(q)
        
        """
        return CCoreShellCylinderModel.runXY(self, x)
        
    def evalDistribution(self, x):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q[], or [qx[], qy[]]
        
        :return: scattering function P(q[])
        
        """
        return CCoreShellCylinderModel.evalDistribution(self, x)
        
    def calculate_ER(self):
        """ 
        Calculate the effective radius for P(q)*S(q)
        
        :return: the value of the effective radius
        
        """       
        return CCoreShellCylinderModel.calculate_ER(self)
        
    def calculate_VR(self):
        """ 
        Calculate the volf ratio for P(q)*S(q)
        
        :return: the value of the volf ratio
        
        """       
        return CCoreShellCylinderModel.calculate_VR(self)
              
    def set_dispersion(self, parameter, dispersion):
        """
        Set the dispersion object for a model parameter
        
        :param parameter: name of the parameter [string]
        :param dispersion: dispersion object of type DispersionModel
        
        """
        return CCoreShellCylinderModel.set_dispersion(self,
               parameter, dispersion.cdisp)
        
   
# End of file

