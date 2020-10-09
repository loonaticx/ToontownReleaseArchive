# Source Generated with Decompyle++
# File: ForceNode.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import BaseForce
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

def generateClass_ForceNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ForceNode(NamedNode.NamedNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpandaphysics._inP9fJJIby9(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inP9fJJOHml()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstForceNode(self, copy):
            self.this = libpandaphysics._inP9fJJzLI_(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpandaphysics._inP9fJJ_pOV()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def assign(self, copy):
            returnValue = libpandaphysics._inP9fJJI7dt(self.this, copy.this)
            returnObject = ForceNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def clear(self):
            returnValue = libpandaphysics._inP9fJJVxNM(self.this)
            return returnValue

        
        def getForce(self, index):
            returnValue = libpandaphysics._inP9fJJKNtU(self.this, index)
            returnObject = BaseForce.BaseForce(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getNumForces(self):
            returnValue = libpandaphysics._inP9fJJEDQ4(self.this)
            return returnValue

        
        def addForce(self, force):
            returnValue = libpandaphysics._inP9fJJRBwh(self.this, force.this)
            return returnValue

        
        def addForcesFrom(self, other):
            returnValue = libpandaphysics._inP9fJJq7Jz(self.this, other.this)
            return returnValue

        
        def overloaded_removeForce_ptrForceNode_ptrBaseForce(self, f):
            returnValue = libpandaphysics._inP9fJJa6aF(self.this, f.this)
            return returnValue

        
        def overloaded_removeForce_ptrForceNode_int(self, index):
            returnValue = libpandaphysics._inP9fJJ3qKj(self.this, index)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                elif isinstance(_args[0], ForceNode):
                    return self.overloaded_constructor_ptrConstForceNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <ForceNode> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def removeForce(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_removeForce_ptrForceNode_int(_args[0])
                elif isinstance(_args[0], BaseForce.BaseForce):
                    return self.overloaded_removeForce_ptrForceNode_ptrBaseForce(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BaseForce.BaseForce> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['ForceNode'] = ForceNode

