# Source Generated with Decompyle++
# File: BaseParticleEmitter.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Point3
import Vec3
import ReferenceCount
import TypeHandle
classDefined = 0

def generateClass_BaseParticleEmitter():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class BaseParticleEmitter(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        ETRADIATE = 1
        ETEXPLICIT = 0
        ETCUSTOM = 2
        
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
            if libpandaphysics and libpandaphysics._inPKBUAZU1H:
                libpandaphysics._inPKBUAZU1H(self.this)
            

        
        def makeCopy(self):
            returnValue = libpandaphysics._inPKBUAjXL2(self.this)
            returnObject = BaseParticleEmitter(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def generate(self, pos, vel):
            returnValue = libpandaphysics._inPKBUAJJVs(self.this, pos.this, vel.this)
            return returnValue

        
        def setEmissionType(self, et):
            returnValue = libpandaphysics._inPKBUAoaPb(self.this, et)
            return returnValue

        
        def setAmplitude(self, a):
            returnValue = libpandaphysics._inPKBUAtP5P(self.this, a)
            return returnValue

        
        def setAmplitudeSpread(self, as):
            returnValue = libpandaphysics._inPKBUA_4at(self.this, as)
            return returnValue

        
        def setOffsetForce(self, of):
            returnValue = libpandaphysics._inPKBUACCmc(self.this, of.this)
            return returnValue

        
        def setExplicitLaunchVector(self, elv):
            returnValue = libpandaphysics._inPKBUAxZg_(self.this, elv.this)
            return returnValue

        
        def setRadiateOrigin(self, ro):
            returnValue = libpandaphysics._inPKBUAX6GF(self.this, ro.this)
            return returnValue

        
        def getEmissionType(self):
            returnValue = libpandaphysics._inPKBUA4hj6(self.this)
            return returnValue

        
        def getAmplitude(self):
            returnValue = libpandaphysics._inPKBUArjT9(self.this)
            return returnValue

        
        def getAmplitudeSpread(self):
            returnValue = libpandaphysics._inPKBUA3dLN(self.this)
            return returnValue

        
        def getOffsetForce(self):
            returnValue = libpandaphysics._inPKBUAZ27B(self.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getExplicitLaunchVector(self):
            returnValue = libpandaphysics._inPKBUALhW0(self.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getRadiateOrigin(self):
            returnValue = libpandaphysics._inPKBUAopd8(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject


    globals()['BaseParticleEmitter'] = BaseParticleEmitter

