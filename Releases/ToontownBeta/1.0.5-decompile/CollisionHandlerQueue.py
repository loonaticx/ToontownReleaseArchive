# Source Generated with Decompyle++
# File: CollisionHandlerQueue.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CollisionEntry
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import CollisionHandler
import TypeHandle
classDefined = 0

def generateClass_CollisionHandlerQueue():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CollisionHandlerQueue(CollisionHandler.CollisionHandler, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPHwcaJgY4()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPHwca6RSj:
                libpanda._inPHwca6RSj(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPHwcafBhh()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def sortEntries(self):
            returnValue = libpanda._inPHwcaxZPE(self.this)
            return returnValue

        
        def clearEntries(self):
            returnValue = libpanda._inPHwcaSkav(self.this)
            return returnValue

        
        def getNumEntries(self):
            returnValue = libpanda._inPHwcatndh(self.this)
            return returnValue

        
        def getEntry(self, n):
            returnValue = libpanda._inPHwcaUek_(self.this, n)
            returnObject = CollisionEntry.CollisionEntry(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()


    globals()['CollisionHandlerQueue'] = CollisionHandlerQueue

