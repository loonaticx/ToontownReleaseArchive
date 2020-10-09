# Source Generated with Decompyle++
# File: DataRelation.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypeHandle
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import ReferenceCount
import TypeHandle
import TypedWritableReferenceCount
import ReferenceCount
import TypeHandle
import Writable
import TypedWritable
import BoundedObject
import BoundingVolume
import TypeHandle
import NodeRelation
import Ostream
import Node
import TypeHandle
import NodeTransition
import NodeTransitions
import UpdateSeq
import BoundedObject
import ReferenceCount
import TypedWritableReferenceCount
import BoundingVolume
classDefined = 0

def generateClass_DataRelation():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DataRelation(NodeRelation.NodeRelation, FFIExternalObject.FFIExternalObject):
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
            

        
        def destructor(self):
            if libpanda and libpanda._inPSLSeIgby:
                libpanda._inPSLSeIgby(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPSLSeCiBP()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)

    globals()['DataRelation'] = DataRelation

