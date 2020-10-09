# Source Generated with Decompyle++
# File: DiscEmitter.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import BaseParticleEmitter
import ReferenceCount
import TypeHandle
import BaseParticleEmitter
import Point3
import Vec3
classDefined = 0

def generateClass_DiscEmitter():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DiscEmitter(BaseParticleEmitter.BaseParticleEmitter, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inPKBUAF0qQ()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstDiscEmitter(self, copy):
            self.this = libpandaphysics._inPKBUAS0XE(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inPKBUAZU1H:
                libpandaphysics._inPKBUAZU1H(self.this)
            

        
        def setRadius(self, r):
            returnValue = libpandaphysics._inPKBUA1vPM(self.this, r)
            return returnValue

        
        def setOuterAngle(self, oAngle):
            returnValue = libpandaphysics._inPKBUApayy(self.this, oAngle)
            return returnValue

        
        def setInnerAngle(self, iAngle):
            returnValue = libpandaphysics._inPKBUAtBbY(self.this, iAngle)
            return returnValue

        
        def setOuterMagnitude(self, oMag):
            returnValue = libpandaphysics._inPKBUAMWik(self.this, oMag)
            return returnValue

        
        def setInnerMagnitude(self, iMag):
            returnValue = libpandaphysics._inPKBUAqQKK(self.this, iMag)
            return returnValue

        
        def setCubicLerping(self, clerp):
            returnValue = libpandaphysics._inPKBUA8TAE(self.this, clerp)
            return returnValue

        
        def getRadius(self):
            returnValue = libpandaphysics._inPKBUApo_c(self.this)
            return returnValue

        
        def getOuterAngle(self):
            returnValue = libpandaphysics._inPKBUAYhU_(self.this)
            return returnValue

        
        def getInnerAngle(self):
            returnValue = libpandaphysics._inPKBUAO_9j(self.this)
            return returnValue

        
        def getOuterMagnitude(self):
            returnValue = libpandaphysics._inPKBUAKS4h(self.this)
            return returnValue

        
        def getInnerMagnitude(self):
            returnValue = libpandaphysics._inPKBUAkFgH(self.this)
            return returnValue

        
        def getCubicLerping(self):
            returnValue = libpandaphysics._inPKBUAQZ2y(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], DiscEmitter):
                    return self.overloaded_constructor_ptrConstDiscEmitter(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <DiscEmitter> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['DiscEmitter'] = DiscEmitter

