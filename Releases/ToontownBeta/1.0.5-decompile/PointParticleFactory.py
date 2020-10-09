# Source Generated with Decompyle++
# File: PointParticleFactory.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import BaseParticleFactory
import ReferenceCount
import TypeHandle
import BaseParticleFactory
import BaseParticle
classDefined = 0

def generateClass_PointParticleFactory():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PointParticleFactory(BaseParticleFactory.BaseParticleFactory, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inPKBUAs3mT()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstPointParticleFactory(self, copy):
            self.this = libpandaphysics._inPKBUAqqLp(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inPKBUAMtlV:
                libpandaphysics._inPKBUAMtlV(self.this)
            

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], PointParticleFactory):
                    return self.overloaded_constructor_ptrConstPointParticleFactory(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <PointParticleFactory> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['PointParticleFactory'] = PointParticleFactory

