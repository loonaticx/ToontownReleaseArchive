# Source Generated with Decompyle++
# File: ZSpinParticleFactory.pyo (Python 2.0)

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

def generateClass_ZSpinParticleFactory():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ZSpinParticleFactory(BaseParticleFactory.BaseParticleFactory, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inPKBUA7xSj()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstZSpinParticleFactory(self, copy):
            self.this = libpandaphysics._inPKBUA4BlG(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inPKBUAMtlV:
                libpandaphysics._inPKBUAMtlV(self.this)
            

        
        def setInitialAngle(self, angle):
            returnValue = libpandaphysics._inPKBUACqKd(self.this, angle)
            return returnValue

        
        def setFinalAngle(self, angle):
            returnValue = libpandaphysics._inPKBUA3a2T(self.this, angle)
            return returnValue

        
        def setInitialAngleSpread(self, spread):
            returnValue = libpandaphysics._inPKBUASCQY(self.this, spread)
            return returnValue

        
        def setFinalAngleSpread(self, spread):
            returnValue = libpandaphysics._inPKBUA5Kya(self.this, spread)
            return returnValue

        
        def getInitialAngle(self):
            returnValue = libpandaphysics._inPKBUASUF9(self.this)
            return returnValue

        
        def getFinalAngle(self):
            returnValue = libpandaphysics._inPKBUANzT9(self.this)
            return returnValue

        
        def getInitialAngleSpread(self):
            returnValue = libpandaphysics._inPKBUAck1c(self.this)
            return returnValue

        
        def getFinalAngleSpread(self):
            returnValue = libpandaphysics._inPKBUAnv0_(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], ZSpinParticleFactory):
                    return self.overloaded_constructor_ptrConstZSpinParticleFactory(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <ZSpinParticleFactory> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['ZSpinParticleFactory'] = ZSpinParticleFactory

