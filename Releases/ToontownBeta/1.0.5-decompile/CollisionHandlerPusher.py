# Source Generated with Decompyle++
# File: CollisionHandlerPusher.pyo (Python 2.0)

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

def generateClass_CollisionHandlerPusher():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CollisionHandlerPusher(CollisionHandlerPhysical.CollisionHandlerPhysical, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPHwcaHyFg()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPHwcaVSmv:
                libpanda._inPHwcaVSmv(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPHwcaJvou()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setHorizontal(self, flag):
            returnValue = libpanda._inPHwcaEM8k(self.this, flag)
            return returnValue

        
        def getHorizontal(self):
            returnValue = libpanda._inPHwca2vDN(self.this)
            return returnValue


    globals()['CollisionHandlerPusher'] = CollisionHandlerPusher

