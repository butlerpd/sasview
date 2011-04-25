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
         DO NOT MODIFY THIS FILE, MODIFY ..\c_extensions\rpa.h
         AND RE-RUN THE GENERATOR SCRIPT

"""

from sans.models.BaseComponent import BaseComponent
from sans_extension.c_models import CRPAModel
import copy    

def create_RPAModel():
    obj = RPAModel()
    #CRPAModel.__init__(obj) is called by RPAModel constructor
    return obj

class RPAModel(CRPAModel, BaseComponent):
    """ 
    Class that evaluates a RPAModel model. 
    This file was auto-generated from ..\c_extensions\rpa.h.
    Refer to that file and the structure it contains
    for details of the model.
    List of default parameters:
         lcase_n         = 0.0 
         ba              = 5.0 
         bb              = 5.0 
         bc              = 5.0 
         bd              = 5.0 
         Kab             = -0.0004 
         Kac             = -0.0004 
         Kad             = -0.0004 
         Kbc             = -0.0004 
         Kbd             = -0.0004 
         Kcd             = -0.0004 
         scale           = 1.0 
         background      = 0.0 [1/cm]
         Na              = 1000.0 
         Phia            = 0.25 
         va              = 100.0 
         La              = 1e-012 
         Nb              = 1000.0 
         Phib            = 0.25 
         vb              = 100.0 
         Lb              = 1e-012 
         Nc              = 1000.0 
         Phic            = 0.25 
         vc              = 100.0 
         Lc              = 1e-012 
         Nd              = 1000.0 
         Phid            = 0.25 
         vd              = 100.0 
         Ld              = 0.0 

    """
        
    def __init__(self):
        """ Initialization """
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        #apply(CRPAModel.__init__, (self,)) 
        CRPAModel.__init__(self)
        
        ## Name of the model
        self.name = "RPAModel"
        ## Model description
        self.description ="""  THIS FORMALISM APPLIES TO MULTICOMPONENT POLYMER MIXTURES IN THE
		HOMOGENEOUS (MIXED) PHASE REGION ONLY.;
		CASE 0: C/D BINARY MIXTURE OF HOMOPOLYMERS
		CASE 1: C-D DIBLOCK COPOLYMER
		CASE 2: B/C/D TERNARY MIXTURE OF HOMOPOLYMERS
		CASE 3: B/C-D MIXTURE OF HOMOPOLYMER B AND
		DIBLOCK COPOLYMER C-D
		CASE 4: B-C-D TRIBLOCK COPOLYMER
		CASE 5: A/B/C/D QUATERNARY MIXTURE OF HOMOPOLYMERS
		CASE 6: A/B/C-D MIXTURE OF TWO HOMOPOLYMERS A/B
		AND A DIBLOCK C-D
		CASE 7: A/B-C-D MIXTURE OF A HOMOPOLYMER A AND A
		TRIBLOCK B-C-D
		CASE 8: A-B/C-D MIXTURE OF TWO DIBLOCK COPOLYMERS
		A-B AND C-D
		CASE 9: A-B-C-D FOUR-BLOCK COPOLYMER
		See details in the model function help"""
       
        ## Parameter details [units, min, max]
        self.details = {}
        self.details['lcase_n'] = ['', None, None]
        self.details['ba'] = ['', None, None]
        self.details['bb'] = ['', None, None]
        self.details['bc'] = ['', None, None]
        self.details['bd'] = ['', None, None]
        self.details['Kab'] = ['', None, None]
        self.details['Kac'] = ['', None, None]
        self.details['Kad'] = ['', None, None]
        self.details['Kbc'] = ['', None, None]
        self.details['Kbd'] = ['', None, None]
        self.details['Kcd'] = ['', None, None]
        self.details['scale'] = ['', None, None]
        self.details['background'] = ['[1/cm]', None, None]
        self.details['Na'] = ['', None, None]
        self.details['Phia'] = ['', None, None]
        self.details['va'] = ['', None, None]
        self.details['La'] = ['', None, None]
        self.details['Nb'] = ['', None, None]
        self.details['Phib'] = ['', None, None]
        self.details['vb'] = ['', None, None]
        self.details['Lb'] = ['', None, None]
        self.details['Nc'] = ['', None, None]
        self.details['Phic'] = ['', None, None]
        self.details['vc'] = ['', None, None]
        self.details['Lc'] = ['', None, None]
        self.details['Nd'] = ['', None, None]
        self.details['Phid'] = ['', None, None]
        self.details['vd'] = ['', None, None]
        self.details['Ld'] = ['', None, None]

        ## fittable parameters
        self.fixed=[]
        
        ## non-fittable parameters
        self.non_fittable = ['lcase_n', 'Na', 'Phia', 'va', 'La', 'Nb', 'Phib', 'vb', 'Lb', 'Nc', 'Phic', 'vc', 'Lc', 'Nd', 'Phid', 'vd', 'Ld']
        
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
        return (create_RPAModel,tuple(), state, None, None)
        
    def clone(self):
        """ Return a identical copy of self """
        return self._clone(RPAModel())   
       	
   
    def run(self, x=0.0):
        """ 
        Evaluate the model
        
        :param x: input q, or [q,phi]
        
        :return: scattering function P(q)
        
        """
        
        return CRPAModel.run(self, x)
   
    def runXY(self, x=0.0):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q, or [qx, qy]
        
        :return: scattering function P(q)
        
        """
        
        return CRPAModel.runXY(self, x)
        
    def evalDistribution(self, x=[]):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q[], or [qx[], qy[]]
        
        :return: scattering function P(q[])
        
        """
        return CRPAModel.evalDistribution(self, x)
        
    def calculate_ER(self):
        """ 
        Calculate the effective radius for P(q)*S(q)
        
        :return: the value of the effective radius
        
        """       
        return CRPAModel.calculate_ER(self)
        
    def set_dispersion(self, parameter, dispersion):
        """
        Set the dispersion object for a model parameter
        
        :param parameter: name of the parameter [string]
        :param dispersion: dispersion object of type DispersionModel
        
        """
        return CRPAModel.set_dispersion(self, parameter, dispersion.cdisp)
        
   
# End of file
