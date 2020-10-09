# Source Generated with Decompyle++
# File: RingEmitter.pyo (Python 2.0)

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

def generateClass_RingEmitter():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class RingEmitter(BaseParticleEmitter.BaseParticleEmitter, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inPKBUA3Zk2()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstRingEmitter(self, copy):
            self.this = libpandaphysics._inPKBUAaFcu(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inPKBUAZU1H:
                libpandaphysics._inPKBUAZU1H(self.this)
            

        
        def setRadius(self, r):
            returnValue = libpandaphysics._inPKBUAA9Xu(self.this, r)
            return returnValue

        
        def setAngle(self, angle):
            returnValue = libpandaphysics._inPKBUAvRIl(self.this, angle)
            return returnValue

        
        def getRadius(self):
            returnValue = libpandaphysics._inPKBUAwQJ_(self.this)
            return returnValue

        
        def getAngle(self):
            returnValue = libpandaphysics._inPKBUAKz9k(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], RingEmitter):
                    return self.overloaded_constructor_ptrConstRingEmitter(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <RingEmitter> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['RingEmitter'] = RingEmitter

