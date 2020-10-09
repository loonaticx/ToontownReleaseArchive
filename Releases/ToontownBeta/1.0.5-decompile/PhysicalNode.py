# Source Generated with Decompyle++
# File: PhysicalNode.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Physical
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

def generateClass_PhysicalNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PhysicalNode(NamedNode.NamedNode, FFIExternalObject.FFIExternalObject):
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
            self.this = libpandaphysics._inP9fJJJnir(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inP9fJJHirZ()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstPhysicalNode(self, copy):
            self.this = libpandaphysics._inP9fJJR3mA(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpandaphysics._inP9fJJh7u_()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def assign(self, copy):
            returnValue = libpandaphysics._inP9fJJbKZV(self.this, copy.this)
            returnObject = PhysicalNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def clear(self):
            returnValue = libpandaphysics._inP9fJJoc_W(self.this)
            return returnValue

        
        def getPhysical(self, index):
            returnValue = libpandaphysics._inP9fJJ_758(self.this, index)
            returnObject = Physical.Physical(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getNumPhysicals(self):
            returnValue = libpandaphysics._inP9fJJAHea(self.this)
            return returnValue

        
        def addPhysical(self, physical):
            returnValue = libpandaphysics._inP9fJJfF4_(self.this, physical.this)
            return returnValue

        
        def addPhysicalsFrom(self, other):
            returnValue = libpandaphysics._inP9fJJ_Q7z(self.this, other.this)
            return returnValue

        
        def overloaded_removePhysical_ptrPhysicalNode_ptrPhysical(self, physical):
            returnValue = libpandaphysics._inP9fJJsUjS(self.this, physical.this)
            return returnValue

        
        def overloaded_removePhysical_ptrPhysicalNode_int(self, index):
            returnValue = libpandaphysics._inP9fJJHxfn(self.this, index)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                elif isinstance(_args[0], PhysicalNode):
                    return self.overloaded_constructor_ptrConstPhysicalNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <PhysicalNode> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def removePhysical(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_removePhysical_ptrPhysicalNode_int(_args[0])
                elif isinstance(_args[0], Physical.Physical):
                    return self.overloaded_removePhysical_ptrPhysicalNode_ptrPhysical(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <Physical.Physical> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['PhysicalNode'] = PhysicalNode

