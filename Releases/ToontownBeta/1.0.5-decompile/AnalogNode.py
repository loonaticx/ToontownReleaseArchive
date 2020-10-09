# Source Generated with Decompyle++
# File: AnalogNode.pyo (Python 2.0)

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

def generateClass_AnalogNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class AnalogNode(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, client, deviceName):
            self.this = libpanda._inPOfOPkOWk(client.this, deviceName)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPOfOPCcld()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def isValid(self):
            returnValue = libpanda._inPOfOPe9F9(self.this)
            return returnValue

        
        def getNumControls(self):
            returnValue = libpanda._inPOfOPH5B0(self.this)
            return returnValue

        
        def getControlState(self, index):
            returnValue = libpanda._inPOfOPOk5b(self.this, index)
            return returnValue

        
        def isControlKnown(self, index):
            returnValue = libpanda._inPOfOP43_i(self.this, index)
            return returnValue

        
        def setOutput(self, channel, index, flip):
            returnValue = libpanda._inPOfOP8Ab3(self.this, channel, index, flip)
            return returnValue

        
        def clearOutput(self, channel):
            returnValue = libpanda._inPOfOPtapo(self.this, channel)
            return returnValue

        
        def getOutput(self, channel):
            returnValue = libpanda._inPOfOP43LB(self.this, channel)
            return returnValue

        
        def isOutputFlipped(self, channel):
            returnValue = libpanda._inPOfOPrFX_(self.this, channel)
            return returnValue


    globals()['AnalogNode'] = AnalogNode

