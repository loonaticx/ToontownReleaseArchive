# Source Generated with Decompyle++
# File: ButtonRegistry.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import ButtonHandle
classDefined = 0

def generateClass_ButtonRegistry():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ButtonRegistry(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
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
            if libpanda and libpanda._inPflbowDnE:
                libpanda._inPflbowDnE(self.this)
            

        
        def ptr():
            returnValue = libpanda._inPflboW6yc()
            returnObject = ButtonRegistry(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        ptr = PandaStatic.PandaStatic(ptr)
        
        def getButton(self, name):
            returnValue = libpanda._inPflboDzsi(self.this, name)
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def findAsciiButton(self, asciiEquivalent):
            returnValue = libpanda._inPflbon28u(self.this, asciiEquivalent)
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject


    globals()['ButtonRegistry'] = ButtonRegistry

