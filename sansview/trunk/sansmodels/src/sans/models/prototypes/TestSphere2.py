#!/usr/bin/env python
""" Provide functionality for a C extension model

	WARNING: THIS FILE WAS GENERATED BY WRAPPERGENERATOR.PY
 	         DO NOT MODIFY THIS FILE, MODIFY testsphere.h
 	         AND RE-RUN THE GENERATOR SCRIPT

    @author: Mathieu Doucet / UTK
    @contact: mathieu.doucet@nist.gov
"""

from sans.models.BaseComponent import BaseComponent
from sans_extension.prototypes.c_models import CTestSphere2
import copy    
    
class TestSphere2(CTestSphere2, BaseComponent):
    """ Scattering model based on a cylinder """
        
    def __init__(self):
        """ Initialization """
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        CTestSphere2.__init__(self)
        
        ## Name of the model
        self.name = "TestSphere2"
   
    def clone(self):
        """ Return a identical copy of self """
        obj = TestSphere2()
        obj.params = copy.deepcopy(self.params)
        return obj   
    
    def run(self, x=0.0):
        """ Evaluate the model
            @param x: input q, or [q,phi]
            @return: scattering function P(q)
        """
        
        return CTestSphere2.run(self, x)
   
# End of file
