# Source Generated with Decompyle++
# File: MouseButton.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import ButtonHandle
classDefined = 0

def generateClass_MouseButton():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class MouseButton(FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPflbolmWo:
                libpanda._inPflbolmWo(self.this)
            

        
        def button(buttonNumber):
            returnValue = libpanda._inPflboTQ5C(buttonNumber)
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        button = PandaStatic.PandaStatic(button)
        
        def one():
            returnValue = libpanda._inPflboK5hO()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        one = PandaStatic.PandaStatic(one)
        
        def two():
            returnValue = libpanda._inPflboz9lR()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        two = PandaStatic.PandaStatic(two)
        
        def three():
            returnValue = libpanda._inPflboaLRB()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        three = PandaStatic.PandaStatic(three)
        
        def isMouseButton(button):
            returnValue = libpanda._inPflboEEqQ(button.this)
            return returnValue

        isMouseButton = PandaStatic.PandaStatic(isMouseButton)

    globals()['MouseButton'] = MouseButton

