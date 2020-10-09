# Source Generated with Decompyle++
# File: TrackerNode.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ClientBase
import Point3
import LOrientationf
import Mat4
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

def generateClass_TrackerNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class TrackerNode(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, client, deviceName):
            self.this = libpanda._inPOfOPAMDC(client.this, deviceName)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPOfOPUa7p()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def isValid(self):
            returnValue = libpanda._inPOfOP8doZ(self.this)
            return returnValue

        
        def getPos(self):
            returnValue = libpanda._inPOfOPYDcJ(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getOrient(self):
            returnValue = libpanda._inPOfOPVPe9(self.this)
            returnObject = LOrientationf.LOrientationf(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getTransform(self):
            returnValue = libpanda._inPOfOPs1sf(self.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject


    globals()['TrackerNode'] = TrackerNode

