# Source Generated with Decompyle++
# File: LinearForce.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
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
classDefined = 0

def generateClass_LinearForce():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class LinearForce(BaseForce.BaseForce, FFIExternalObject.FFIExternalObject):
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
            

        
        def getClassType():
            returnValue = libpandaphysics._inP9fJJ92vs()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setAmplitude(self, a):
            returnValue = libpandaphysics._inP9fJJT_2L(self.this, a)
            return returnValue

        
        def setMassDependent(self, m):
            returnValue = libpandaphysics._inP9fJJDUvI(self.this, m)
            return returnValue

        
        def getAmplitude(self):
            returnValue = libpandaphysics._inP9fJJNwPK(self.this)
            return returnValue

        
        def getMassDependent(self):
            returnValue = libpandaphysics._inP9fJJUo05(self.this)
            return returnValue

        
        def setVectorMasks(self, x, y, z):
            returnValue = libpandaphysics._inP9fJJBXuL(self.this, x, y, z)
            return returnValue

        
        def makeCopy(self):
            returnValue = libpandaphysics._inP9fJJregT(self.this)
            returnObject = LinearForce(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()


    globals()['LinearForce'] = LinearForce

