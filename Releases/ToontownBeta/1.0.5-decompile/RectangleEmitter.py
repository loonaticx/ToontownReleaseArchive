# Source Generated with Decompyle++
# File: RectangleEmitter.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import BaseParticleEmitter
import Point2
import ReferenceCount
import TypeHandle
import BaseParticleEmitter
import Point3
import Vec3
classDefined = 0

def generateClass_RectangleEmitter():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class RectangleEmitter(BaseParticleEmitter.BaseParticleEmitter, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inPKBUAjMsE()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstRectangleEmitter(self, copy):
            self.this = libpandaphysics._inPKBUAcsSt(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inPKBUAZU1H:
                libpandaphysics._inPKBUAZU1H(self.this)
            

        
        def setMinBound(self, vmin):
            returnValue = libpandaphysics._inPKBUA4Yx9(self.this, vmin.this)
            return returnValue

        
        def setMaxBound(self, vmax):
            returnValue = libpandaphysics._inPKBUA9O9N(self.this, vmax.this)
            return returnValue

        
        def getMinBound(self):
            returnValue = libpandaphysics._inPKBUAG0Of(self.this)
            returnObject = Point2.Point2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getMaxBound(self):
            returnValue = libpandaphysics._inPKBUAO1av(self.this)
            returnObject = Point2.Point2(None)
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
                if isinstance(_args[0], RectangleEmitter):
                    return self.overloaded_constructor_ptrConstRectangleEmitter(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <RectangleEmitter> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['RectangleEmitter'] = RectangleEmitter

