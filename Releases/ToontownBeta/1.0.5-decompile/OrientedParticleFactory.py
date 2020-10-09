# Source Generated with Decompyle++
# File: OrientedParticleFactory.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import BaseParticleFactory
import LOrientationf
import ReferenceCount
import TypeHandle
import BaseParticleFactory
import BaseParticle
classDefined = 0

def generateClass_OrientedParticleFactory():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class OrientedParticleFactory(BaseParticleFactory.BaseParticleFactory, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inPKBUA2_6k()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstOrientedParticleFactory(self, copy):
            self.this = libpandaphysics._inPKBUAhLtO(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inPKBUAMtlV:
                libpandaphysics._inPKBUAMtlV(self.this)
            

        
        def setInitialOrientation(self, o):
            returnValue = libpandaphysics._inPKBUAEgbz(self.this, o.this)
            return returnValue

        
        def setFinalOrientation(self, o):
            returnValue = libpandaphysics._inPKBUAxVg_(self.this, o.this)
            return returnValue

        
        def getInitialOrientation(self):
            returnValue = libpandaphysics._inPKBUAZqGs(self.this)
            returnObject = LOrientationf.LOrientationf(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getFinalOrientation(self):
            returnValue = libpandaphysics._inPKBUA4_lw(self.this)
            returnObject = LOrientationf.LOrientationf(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], OrientedParticleFactory):
                    return self.overloaded_constructor_ptrConstOrientedParticleFactory(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <OrientedParticleFactory> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['OrientedParticleFactory'] = OrientedParticleFactory

