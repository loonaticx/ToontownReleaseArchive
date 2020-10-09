# Source Generated with Decompyle++
# File: DepthTestProperty.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
classDefined = 0

def generateClass_DepthTestProperty():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DepthTestProperty(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        MGreaterEqual = 7
        MLess = 2
        MNotEqual = 6
        MGreater = 5
        MNever = 1
        MNone = 0
        MAlways = 8
        MEqual = 3
        MLessEqual = 4
        
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
            if libpanda and libpanda._inPuUZ_ROux:
                libpanda._inPuUZ_ROux(self.this)
            


    globals()['DepthTestProperty'] = DepthTestProperty

