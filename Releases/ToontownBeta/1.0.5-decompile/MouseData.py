# Source Generated with Decompyle++
# File: MouseData.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
classDefined = 0

def generateClass_MouseData():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class MouseData(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPflboZwcW()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPflbo5__W:
                libpanda._inPflbo5__W(self.this)
            

        
        def getX(self):
            returnValue = libpanda._inPflboKC6w(self.this)
            return returnValue

        
        def getY(self):
            returnValue = libpanda._inPflboiSEx(self.this)
            return returnValue

        
        def getInWindow(self):
            returnValue = libpanda._inPflbowV1X(self.this)
            return returnValue


    globals()['MouseData'] = MouseData

