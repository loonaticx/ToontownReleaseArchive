# Source Generated with Decompyle++
# File: AnimBundleNode.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import AnimBundle
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

def generateClass_AnimBundleNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class AnimBundleNode(NamedNode.NamedNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrAnimBundle(self, bundle):
            self.this = libpanda._inPn9gMVTzG(bundle.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstAnimBundleNode(self, copy):
            self.this = libpanda._inPn9gMFEmL(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPn9gMQ4v8:
                libpanda._inPn9gMQ4v8(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPn9gMRnUG()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def assign(self, copy):
            returnValue = libpanda._inPn9gMgIAK(self.this, copy.this)
            returnObject = AnimBundleNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getBundle(self):
            returnValue = libpanda._inPn9gMpKzB(self.this)
            returnObject = AnimBundle.AnimBundle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], AnimBundleNode):
                    return self.overloaded_constructor_ptrConstAnimBundleNode(_args[0])
                elif isinstance(_args[0], AnimBundle.AnimBundle):
                    return self.overloaded_constructor_ptrAnimBundle(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <AnimBundleNode> <AnimBundle.AnimBundle> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['AnimBundleNode'] = AnimBundleNode

