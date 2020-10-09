# Source Generated with Decompyle++
# File: Istream.pyo (Python 2.0)

import PandaStatic
import types
import libdirect
import libdirectDowncasts
import FFIExternalObject
classDefined = 0

def generateClass_Istream():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Istream(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libdirectDowncasts]
        
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
            


    globals()['Istream'] = Istream

