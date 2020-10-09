# Source Generated with Decompyle++
# File: CollisionHandlerEvent.pyo (Python 2.0)

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
import CollisionHandler
import TypeHandle
classDefined = 0

def generateClass_CollisionHandlerEvent():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CollisionHandlerEvent(CollisionHandler.CollisionHandler, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPHwca9svw()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPHwcaVSmv:
                libpanda._inPHwcaVSmv(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPHwcaR2qn()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setInPattern(self, pattern):
            returnValue = libpanda._inPHwcadszo(self.this, pattern)
            return returnValue

        
        def getInPattern(self):
            returnValue = libpanda._inPHwcaELQ0(self.this)
            return returnValue

        
        def setAgainPattern(self, pattern):
            returnValue = libpanda._inPHwca_xTx(self.this, pattern)
            return returnValue

        
        def getAgainPattern(self):
            returnValue = libpanda._inPHwcadeDM(self.this)
            return returnValue

        
        def setOutPattern(self, pattern):
            returnValue = libpanda._inPHwcagknm(self.this, pattern)
            return returnValue

        
        def getOutPattern(self):
            returnValue = libpanda._inPHwca1Y6r(self.this)
            return returnValue

        
        def clear(self):
            returnValue = libpanda._inPHwcaoHoS(self.this)
            return returnValue


    globals()['CollisionHandlerEvent'] = CollisionHandlerEvent

