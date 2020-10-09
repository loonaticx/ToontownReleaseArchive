# Source Generated with Decompyle++
# File: LineEmitter.pyo (Python 2.0)

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

def generateClass_LineEmitter():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class LineEmitter(BaseParticleEmitter.BaseParticleEmitter, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inPKBUAfo71()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLineEmitter(self, copy):
            self.this = libpandaphysics._inPKBUAojIy(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inPKBUAZU1H:
                libpandaphysics._inPKBUAZU1H(self.this)
            

        
        def setEndpoint1(self, point):
            returnValue = libpandaphysics._inPKBUAdfGJ(self.this, point.this)
            return returnValue

        
        def setEndpoint2(self, point):
            returnValue = libpandaphysics._inPKBUA9atJ(self.this, point.this)
            return returnValue

        
        def getEndpoint1(self):
            returnValue = libpandaphysics._inPKBUAz_0h(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getEndpoint2(self):
            returnValue = libpandaphysics._inPKBUATCci(self.this)
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
                if isinstance(_args[0], LineEmitter):
                    return self.overloaded_constructor_ptrConstLineEmitter(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <LineEmitter> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['LineEmitter'] = LineEmitter

