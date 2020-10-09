# Source Generated with Decompyle++
# File: Camera.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ProjectionNode
import Node
import DisplayRegion
import Projection
import TypeHandle
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import BoundedObject
import BoundingVolume
import TypeHandle
import ReferenceCount
import TypeHandle
import Node
import TypeHandle
import NodeRelation
import Ostream
import BoundedObject
import ReferenceCount
import Writable
import TypedWritable
import BoundingVolume
import Namable
import Ostream
import TypeHandle
import NamedNode
import Namable
import TypeHandle
import Node
import NodeRelation
import Ostream
import BoundedObject
import ReferenceCount
import ProjectionNode
import Projection
import Point3
import TypeHandle
classDefined = 0

def generateClass_Camera():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Camera(ProjectionNode.ProjectionNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPAJa78cNS(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPAJa76q2f()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPAJa7JqLD:
                libpanda._inPAJa7JqLD(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPAJa709VC()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setActive(self, active):
            returnValue = libpanda._inPAJa7wqAN(self.this, active)
            return returnValue

        
        def isActive(self):
            returnValue = libpanda._inPAJa7Jy9N(self.this)
            return returnValue

        
        def setScene(self, scene):
            returnValue = libpanda._inPAJa7Sn_B(self.this, scene.this)
            return returnValue

        
        def getScene(self):
            returnValue = libpanda._inPAJa74cJc(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getNumDrs(self):
            returnValue = libpanda._inPAJa79OJh(self.this)
            return returnValue

        
        def getDr(self, index):
            returnValue = libpanda._inPAJa7ZghY(self.this, index)
            returnObject = DisplayRegion.DisplayRegion(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setProjection(self, projection):
            returnValue = libpanda._inPAJa7hu9M(self.this, projection.this)
            return returnValue

        
        def overloaded_setFov_ptrCamera_float(self, hfov):
            returnValue = libpanda._inPAJa7C62k(self.this, hfov)
            return returnValue

        
        def overloaded_setFov_ptrCamera_float_float(self, hfov, vfov):
            returnValue = libpanda._inPAJa7BQsx(self.this, hfov, vfov)
            return returnValue

        
        def setHfov(self, hfov):
            returnValue = libpanda._inPAJa7M__Q(self.this, hfov)
            return returnValue

        
        def setVfov(self, vfov):
            returnValue = libpanda._inPAJa779hW(self.this, vfov)
            return returnValue

        
        def setAspect(self, aspect):
            returnValue = libpanda._inPAJa7YmB8(self.this, aspect)
            return returnValue

        
        def setNearFar(self, cnear, cfar):
            returnValue = libpanda._inPAJa7jARh(self.this, cnear, cfar)
            return returnValue

        
        def setNear(self, cnear):
            returnValue = libpanda._inPAJa7TSgB(self.this, cnear)
            return returnValue

        
        def setFar(self, cfar):
            returnValue = libpanda._inPAJa7dv0z(self.this, cfar)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setFov(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setFov_ptrCamera_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_setFov_ptrCamera_float_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['Camera'] = Camera

