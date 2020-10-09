# Source Generated with Decompyle++
# File: CollisionNode.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import BitMask32
import CollisionSolid
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

def generateClass_CollisionNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CollisionNode(NamedNode.NamedNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPHwcaqY2r(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPHwcaA7Tv()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPHwcacNV3()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setCollideMask(self, mask):
            returnValue = libpanda._inPHwcaqxyb(self.this, mask.this)
            return returnValue

        
        def setFromCollideMask(self, mask):
            returnValue = libpanda._inPHwcac6OW(self.this, mask.this)
            return returnValue

        
        def setIntoCollideMask(self, mask):
            returnValue = libpanda._inPHwcaRJtW(self.this, mask.this)
            return returnValue

        
        def getFromCollideMask(self):
            returnValue = libpanda._inPHwcaRWwI(self.this)
            returnObject = BitMask32.BitMask32(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getIntoCollideMask(self):
            returnValue = libpanda._inPHwcaqPQJ(self.this)
            returnObject = BitMask32.BitMask32(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setCollideGeom(self, flag):
            returnValue = libpanda._inPHwcaHZ_H(self.this, flag)
            return returnValue

        
        def getCollideGeom(self):
            returnValue = libpanda._inPHwcaykPh(self.this)
            return returnValue

        
        def getNumSolids(self):
            returnValue = libpanda._inPHwcajyJk(self.this)
            return returnValue

        
        def getSolid(self, n):
            returnValue = libpanda._inPHwcacudZ(self.this, n)
            returnObject = CollisionSolid.CollisionSolid(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def removeSolid(self, n):
            returnValue = libpanda._inPHwcaJX5l(self.this, n)
            return returnValue

        
        def addSolid(self, solid):
            returnValue = libpanda._inPHwcaxwYW(self.this, solid.this)
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


    globals()['CollisionNode'] = CollisionNode

