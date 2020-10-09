# Source Generated with Decompyle++
# File: DepthWriteTransition.pyo (Python 2.0)

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
import OnOffTransition
import TypeHandle
classDefined = 0

def generateClass_DepthWriteTransition():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DepthWriteTransition(OnOffTransition.OnOffTransition, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPuUZ_WURm()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPuUZ_8JpD:
                libpanda._inPuUZ_8JpD(self.this)
            

        
        def off():
            returnValue = libpanda._inPuUZ_8fx_()
            returnObject = DepthWriteTransition(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        off = PandaStatic.PandaStatic(off)
        
        def getClassType():
            returnValue = libpanda._inPuUZ__seM()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)

    globals()['DepthWriteTransition'] = DepthWriteTransition

