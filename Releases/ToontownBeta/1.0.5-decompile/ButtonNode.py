# Source Generated with Decompyle++
# File: ButtonNode.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ClientBase
import ButtonHandle
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

def generateClass_ButtonNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ButtonNode(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, client, deviceName):
            self.this = libpanda._inPOfOPGRYg(client.this, deviceName)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPOfOPHVKc()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def isValid(self):
            returnValue = libpanda._inPOfOPPCp7(self.this)
            return returnValue

        
        def getNumButtons(self):
            returnValue = libpanda._inPOfOPtmKT(self.this)
            return returnValue

        
        def setButtonMap(self, index, button):
            returnValue = libpanda._inPOfOPZIds(self.this, index, button.this)
            return returnValue

        
        def getButtonMap(self, index):
            returnValue = libpanda._inPOfOPJTX8(self.this, index)
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getButtonState(self, index):
            returnValue = libpanda._inPOfOP_3kS(self.this, index)
            return returnValue

        
        def isButtonKnown(self, index):
            returnValue = libpanda._inPOfOPB8uC(self.this, index)
            return returnValue


    globals()['ButtonNode'] = ButtonNode

