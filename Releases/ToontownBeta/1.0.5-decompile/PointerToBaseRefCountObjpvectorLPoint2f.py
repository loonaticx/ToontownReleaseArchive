# Source Generated with Decompyle++
# File: PointerToBaseRefCountObjpvectorLPoint2f.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
classDefined = 0

def generateClass_PointerToBaseRefCountObjpvectorLPoint2f():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PointerToBaseRefCountObjpvectorLPoint2f(FFIExternalObject.FFIExternalObject):
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
            


    globals()['PointerToBaseRefCountObjpvectorLPoint2f'] = PointerToBaseRefCountObjpvectorLPoint2f
