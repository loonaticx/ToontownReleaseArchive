# Source Generated with Decompyle++
# File: PruneTransition.pyo (Python 2.0)

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
import NodeTransition
import Ostream
import TypeHandle
import ImmediateTransition
import TypeHandle
classDefined = 0

def generateClass_PruneTransition():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PruneTransition(ImmediateTransition.ImmediateTransition, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPuUZ_3Yke()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPuUZ_62SJ:
                libpanda._inPuUZ_62SJ(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPuUZ_L3VD()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)

    globals()['PruneTransition'] = PruneTransition

