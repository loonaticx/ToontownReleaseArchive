# Source Generated with Decompyle++
# File: BaseForce.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ForceNode
import Vec3
import PhysicsObject
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
classDefined = 0

def generateClass_BaseForce():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class BaseForce(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
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
            returnValue = libpandaphysics._inP9fJJuxv7()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getActive(self):
            returnValue = libpandaphysics._inP9fJJde3t(self.this)
            return returnValue

        
        def setActive(self, active):
            returnValue = libpandaphysics._inP9fJJJqYE(self.this, active)
            return returnValue

        
        def isLinear(self):
            returnValue = libpandaphysics._inP9fJJpQu9(self.this)
            return returnValue

        
        def getForceNode(self):
            returnValue = libpandaphysics._inP9fJJ4PV0(self.this)
            returnObject = ForceNode.ForceNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def getVector(self, po):
            returnValue = libpandaphysics._inP9fJJzjvx(self.this, po.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject


    globals()['BaseForce'] = BaseForce

