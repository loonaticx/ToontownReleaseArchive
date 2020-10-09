# Source Generated with Decompyle++
# File: ButtonHandle.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
classDefined = 0

def generateClass_ButtonHandle():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ButtonHandle(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPflboxOcO()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPflbop2FL:
                libpanda._inPflbop2FL(self.this)
            

        
        def none():
            returnValue = libpanda._inPflboQmlV()
            returnObject = ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        none = PandaStatic.PandaStatic(none)
        
        def getName(self):
            returnValue = libpanda._inPflbohE16(self.this)
            return returnValue

        
        def hasAsciiEquivalent(self):
            returnValue = libpanda._inPflbovZND(self.this)
            return returnValue

        
        def getAsciiEquivalent(self):
            returnValue = libpanda._inPflboo7sY(self.this)
            return returnValue

        
        def getIndex(self):
            returnValue = libpanda._inPflbob0jp(self.this)
            return returnValue


    globals()['ButtonHandle'] = ButtonHandle

