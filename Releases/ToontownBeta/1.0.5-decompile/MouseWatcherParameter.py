# Source Generated with Decompyle++
# File: MouseWatcherParameter.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import ButtonHandle
import ModifierButtons
import Point2
import Ostream
classDefined = 0

def generateClass_MouseWatcherParameter():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class MouseWatcherParameter(FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPyiw5PEor:
                libpanda._inPyiw5PEor(self.this)
            

        
        def hasButton(self):
            returnValue = libpanda._inPyiw5A3BJ(self.this)
            return returnValue

        
        def getButton(self):
            returnValue = libpanda._inPyiw5P1t7(self.this)
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getModifierButtons(self):
            returnValue = libpanda._inPyiw58Pbu(self.this)
            returnObject = ModifierButtons.ModifierButtons(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def hasMouse(self):
            returnValue = libpanda._inPyiw5wy9y(self.this)
            return returnValue

        
        def getMouse(self):
            returnValue = libpanda._inPyiw5gfpl(self.this)
            returnObject = Point2.Point2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def isOutside(self):
            returnValue = libpanda._inPyiw57Had(self.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPyiw5IPCE(self.this, out.this)
            return returnValue


    globals()['MouseWatcherParameter'] = MouseWatcherParameter

