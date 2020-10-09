# Source Generated with Decompyle++
# File: BaseParticleFactory.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import BaseParticle
import ReferenceCount
import TypeHandle
classDefined = 0

def generateClass_BaseParticleFactory():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class BaseParticleFactory(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inPKBUAMtlV:
                libpandaphysics._inPKBUAMtlV(self.this)
            

        
        def setLifespanBase(self, lb):
            returnValue = libpandaphysics._inPKBUAbquU(self.this, lb)
            return returnValue

        
        def setLifespanSpread(self, ls):
            returnValue = libpandaphysics._inPKBUAWqHH(self.this, ls)
            return returnValue

        
        def setMassBase(self, mb):
            returnValue = libpandaphysics._inPKBUAUI4l(self.this, mb)
            return returnValue

        
        def setMassSpread(self, ms):
            returnValue = libpandaphysics._inPKBUAG4QM(self.this, ms)
            return returnValue

        
        def setTerminalVelocityBase(self, tvb):
            returnValue = libpandaphysics._inPKBUAPnEZ(self.this, tvb)
            return returnValue

        
        def setTerminalVelocitySpread(self, tvs):
            returnValue = libpandaphysics._inPKBUA5mWX(self.this, tvs)
            return returnValue

        
        def getLifespanBase(self):
            returnValue = libpandaphysics._inPKBUAm6u1(self.this)
            return returnValue

        
        def getLifespanSpread(self):
            returnValue = libpandaphysics._inPKBUA2Xl2(self.this)
            return returnValue

        
        def getMassBase(self):
            returnValue = libpandaphysics._inPKBUAveQT(self.this)
            return returnValue

        
        def getMassSpread(self):
            returnValue = libpandaphysics._inPKBUA4_ih(self.this)
            return returnValue

        
        def getTerminalVelocityBase(self):
            returnValue = libpandaphysics._inPKBUA7Bre(self.this)
            return returnValue

        
        def getTerminalVelocitySpread(self):
            returnValue = libpandaphysics._inPKBUAfZy2(self.this)
            return returnValue

        
        def allocParticle(self):
            returnValue = libpandaphysics._inPKBUAlBlF(self.this)
            returnObject = BaseParticle.BaseParticle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def populateParticle(self, bp):
            returnValue = libpandaphysics._inPKBUApnK_(self.this, bp.this)
            return returnValue


    globals()['BaseParticleFactory'] = BaseParticleFactory

