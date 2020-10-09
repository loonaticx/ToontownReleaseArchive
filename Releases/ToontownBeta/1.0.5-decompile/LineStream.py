# Source Generated with Decompyle++
# File: LineStream.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Ostream
classDefined = 0

def generateClass_LineStream():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class LineStream(Ostream.Ostream, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPflboQNuw()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPflbobB31:
                libpanda._inPflbobB31(self.this)
            

        
        def isTextAvailable(self):
            returnValue = libpanda._inPflbokGyw(self.this)
            return returnValue

        
        def getLine(self):
            returnValue = libpanda._inPflbouMmt(self.this)
            return returnValue

        
        def hasNewline(self):
            returnValue = libpanda._inPflboMjFM(self.this)
            return returnValue


    globals()['LineStream'] = LineStream

