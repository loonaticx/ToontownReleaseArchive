# Source Generated with Decompyle++
# File: Character.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CharacterJointBundle
import ComputedVertices
import PartGroup
import Ostream
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
import PartBundleNode
import PartBundle
import TypeHandle
classDefined = 0

def generateClass_Character():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Character(PartBundleNode.PartBundleNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
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
            returnValue = libpanda._inPnRYR6bxW()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getBundle(self):
            returnValue = libpanda._inPnRYRFpjU(self.this)
            returnObject = CharacterJointBundle.CharacterJointBundle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def getComputedVertices(self):
            returnValue = libpanda._inPnRYRBUYe(self.this)
            returnObject = ComputedVertices.ComputedVertices(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getNumParts(self):
            returnValue = libpanda._inPnRYRN0OF(self.this)
            return returnValue

        
        def getPart(self, n):
            returnValue = libpanda._inPnRYRRVvH(self.this, n)
            returnObject = PartGroup.PartGroup(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def writeParts(self, out):
            returnValue = libpanda._inPnRYRhbhZ(self.this, out.this)
            return returnValue

        
        def writePartValues(self, out):
            returnValue = libpanda._inPnRYRv8P2(self.this, out.this)
            return returnValue

        
        def update(self):
            returnValue = libpanda._inPnRYRhvfb(self.this)
            return returnValue


    globals()['Character'] = Character

