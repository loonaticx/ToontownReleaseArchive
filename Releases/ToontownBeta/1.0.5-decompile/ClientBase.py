# Source Generated with Decompyle++
# File: ClientBase.pyo (Python 2.0)

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
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
classDefined = 0

def generateClass_ClientBase():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ClientBase(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
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
            returnValue = libpanda._inPOfOPQK1P()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def forkAsynchronousThread(self, pollTime):
            returnValue = libpanda._inPOfOP4UyH(self.this, pollTime)
            return returnValue

        
        def isForked(self):
            returnValue = libpanda._inPOfOPi4_A(self.this)
            return returnValue

        
        def poll(self):
            returnValue = libpanda._inPOfOPthyU(self.this)
            return returnValue

        
        def getLastPollTime(self):
            returnValue = libpanda._inPOfOPd_N3(self.this)
            return returnValue


    globals()['ClientBase'] = ClientBase

