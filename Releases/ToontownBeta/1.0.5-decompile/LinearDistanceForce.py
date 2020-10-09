# Source Generated with Decompyle++
# File: LinearDistanceForce.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Point3
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import BaseForce
import ForceNode
import Vec3
import PhysicsObject
import TypeHandle
import LinearForce
import TypeHandle
classDefined = 0

def generateClass_LinearDistanceForce():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class LinearDistanceForce(LinearForce.LinearForce, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        FTONEOVERRCUBED = 2
        FTONEOVERRSQUARED = 1
        FTONEOVERR = 0
        
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
            

        
        def getClassType():
            returnValue = libpandaphysics._inP9fJJx9Kf()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setRadius(self, r):
            returnValue = libpandaphysics._inP9fJJgz9d(self.this, r)
            return returnValue

        
        def setFalloffType(self, ft):
            returnValue = libpandaphysics._inP9fJJleHZ(self.this, ft)
            return returnValue

        
        def setForceCenter(self, p):
            returnValue = libpandaphysics._inP9fJJchEK(self.this, p.this)
            return returnValue

        
        def getRadius(self):
            returnValue = libpandaphysics._inP9fJJznAO(self.this)
            return returnValue

        
        def getFalloffType(self):
            returnValue = libpandaphysics._inP9fJJYL7e(self.this)
            return returnValue

        
        def getForceCenter(self):
            returnValue = libpandaphysics._inP9fJJQlIy(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getScalarTerm(self):
            returnValue = libpandaphysics._inP9fJJLm3k(self.this)
            return returnValue


    globals()['LinearDistanceForce'] = LinearDistanceForce

