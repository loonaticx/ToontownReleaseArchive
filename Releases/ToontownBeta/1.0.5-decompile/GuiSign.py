# Source Generated with Decompyle++
# File: GuiSign.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import GuiLabel
import GuiItem
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import Namable
import Ostream
import TypeHandle
import GuiItem
import GuiManager
import EventHandler
import Node
import Vec3
import GuiLabel
import Vec4
import Ostream
import Namable
import TypeHandle
import ReferenceCount
import TypedReferenceCount
classDefined = 0

def generateClass_GuiSign():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GuiSign(GuiItem.GuiItem, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, parameter0, parameter1):
            self.this = libpanda._inPlRE2F8Rk(parameter0, parameter1.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPlRE2Ktya:
                libpanda._inPlRE2Ktya(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPlRE25GJS()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)

    globals()['GuiSign'] = GuiSign
