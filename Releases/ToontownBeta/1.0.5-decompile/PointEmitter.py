# Source Generated with Decompyle++
# File: PointEmitter.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import BaseParticleEmitter
import Point3
import ReferenceCount
import TypeHandle
import BaseParticleEmitter
import Point3
import Vec3
classDefined = 0

def generateClass_PointEmitter():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PointEmitter(BaseParticleEmitter.BaseParticleEmitter, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inPKBUAlvW_()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstPointEmitter(self, copy):
            self.this = libpandaphysics._inPKBUAakUT(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inPKBUAZU1H:
                libpandaphysics._inPKBUAZU1H(self.this)
            

        
        def setLocation(self, p):
            returnValue = libpandaphysics._inPKBUAEdeR(self.this, p.this)
            return returnValue

        
        def getLocation(self):
            returnValue = libpandaphysics._inPKBUAAuJU(self.this)
            returnObject = Point3.Point3(None)
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
                if isinstance(_args[0], PointEmitter):
                    return self.overloaded_constructor_ptrConstPointEmitter(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <PointEmitter> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['PointEmitter'] = PointEmitter

