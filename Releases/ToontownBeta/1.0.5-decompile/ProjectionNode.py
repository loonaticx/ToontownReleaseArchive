# Source Generated with Decompyle++
# File: ProjectionNode.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Projection
import Point3
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
classDefined = 0

def generateClass_ProjectionNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ProjectionNode(NamedNode.NamedNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPAJa7Tc36(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPAJa7FgyZ()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPAJa7JqLD:
                libpanda._inPAJa7JqLD(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPAJa7_1zm()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setProjection(self, projection):
            returnValue = libpanda._inPAJa7I4R8(self.this, projection.this)
            return returnValue

        
        def shareProjection(self, projection):
            returnValue = libpanda._inPAJa7Lh7k(self.this, projection.this)
            return returnValue

        
        def getProjection(self):
            returnValue = libpanda._inPAJa7Cj_V(self.this)
            returnObject = Projection.Projection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def isInView(self, pos):
            returnValue = libpanda._inPAJa7phri(self.this, pos.this)
            return returnValue

        
        def getHfov(self):
            returnValue = libpanda._inPAJa7Hg5g(self.this)
            return returnValue

        
        def getVfov(self):
            returnValue = libpanda._inPAJa7nILl(self.this)
            return returnValue

        
        def overloaded_setFov_ptrProjectionNode_float(self, hfov):
            returnValue = libpanda._inPAJa7MCcT(self.this, hfov)
            return returnValue

        
        def overloaded_setFov_ptrProjectionNode_float_float(self, hfov, vfov):
            returnValue = libpanda._inPAJa7qQe0(self.this, hfov, vfov)
            return returnValue

        
        def setHfov(self, hfov):
            returnValue = libpanda._inPAJa7yd2C(self.this, hfov)
            return returnValue

        
        def setVfov(self, vfov):
            returnValue = libpanda._inPAJa7SyHH(self.this, vfov)
            return returnValue

        
        def getAspect(self):
            returnValue = libpanda._inPAJa7aXUW(self.this)
            return returnValue

        
        def setAspect(self, aspect):
            returnValue = libpanda._inPAJa7odQ_(self.this, aspect)
            return returnValue

        
        def setNearFar(self, cnear, cfar):
            returnValue = libpanda._inPAJa7tvHd(self.this, cnear, cfar)
            return returnValue

        
        def getNear(self):
            returnValue = libpanda._inPAJa7qZ2K(self.this)
            return returnValue

        
        def setNear(self, cnear):
            returnValue = libpanda._inPAJa7M9ys(self.this, cnear)
            return returnValue

        
        def getFar(self):
            returnValue = libpanda._inPAJa7WVMp(self.this)
            return returnValue

        
        def setFar(self, cfar):
            returnValue = libpanda._inPAJa7GSAp(self.this, cfar)
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
                    return self.overloaded_setFov_ptrProjectionNode_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_setFov_ptrProjectionNode_float_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['ProjectionNode'] = ProjectionNode

