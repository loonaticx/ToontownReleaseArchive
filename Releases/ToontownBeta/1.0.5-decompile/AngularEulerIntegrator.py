# Source Generated with Decompyle++
# File: AngularEulerIntegrator.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import FFIExternalObject
import AngularIntegrator
classDefined = 0

def generateClass_AngularEulerIntegrator():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class AngularEulerIntegrator(AngularIntegrator.AngularIntegrator, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpandaphysics._inP9fJJxp7V()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            


    globals()['AngularEulerIntegrator'] = AngularEulerIntegrator

