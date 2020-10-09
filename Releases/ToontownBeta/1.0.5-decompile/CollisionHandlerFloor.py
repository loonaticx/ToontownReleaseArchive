# Source Generated with Decompyle++
# File: CollisionHandlerFloor.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CollisionHandlerEvent
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
import CollisionHandlerEvent
import TypeHandle
import CollisionHandlerPhysical
import CollisionHandlerEvent
import CollisionNode
import DriveInterface
import NodeRelation
import TypeHandle
classDefined = 0

def generateClass_CollisionHandlerFloor():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CollisionHandlerFloor(CollisionHandlerPhysical.CollisionHandlerPhysical, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPHwcaweUx()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPHwcaVSmv:
                libpanda._inPHwcaVSmv(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPHwcaAyw3()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setOffset(self, offset):
            returnValue = libpanda._inPHwcawnQk(self.this, offset)
            return returnValue

        
        def getOffset(self):
            returnValue = libpanda._inPHwca_WVn(self.this)
            return returnValue

        
        def setMaxVelocity(self, maxVel):
            returnValue = libpanda._inPHwcaxlRc(self.this, maxVel)
            return returnValue

        
        def getMaxVelocity(self):
            returnValue = libpanda._inPHwcaLUa5(self.this)
            return returnValue


    globals()['CollisionHandlerFloor'] = CollisionHandlerFloor

