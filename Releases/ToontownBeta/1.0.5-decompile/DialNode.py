# Source Generated with Decompyle++
# File: DialNode.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ClientBase
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
import DataNode
import TypeHandle
classDefined = 0

def generateClass_DialNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DialNode(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, client, deviceName):
            self.this = libpanda._inPOfOPgXUp(client.this, deviceName)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPOfOPtjS5()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def isValid(self):
            returnValue = libpanda._inPOfOPhBaa(self.this)
            return returnValue

        
        def getNumDials(self):
            returnValue = libpanda._inPOfOPibgJ(self.this)
            return returnValue

        
        def readDial(self, index):
            returnValue = libpanda._inPOfOPM_Fp(self.this, index)
            return returnValue

        
        def isDialKnown(self, index):
            returnValue = libpanda._inPOfOPWp5l(self.this, index)
            return returnValue


    globals()['DialNode'] = DialNode

