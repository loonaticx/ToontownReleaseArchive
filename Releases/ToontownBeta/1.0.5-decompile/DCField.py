# Source Generated with Decompyle++
# File: DCField.pyo (Python 2.0)

import PandaStatic
import types
import libdirect
import libdirectDowncasts
import FFIExternalObject
import DCAtomicField
import DCMolecularField
classDefined = 0

def generateClass_DCField():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DCField(FFIExternalObject.FFIExternalObject):
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
            

        
        def destructor(self):
            if libdirect and libdirect._inP5HfQBZ_K:
                libdirect._inP5HfQBZ_K(self.this)
            

        
        def getNumber(self):
            returnValue = libdirect._inP5HfQRiQq(self.this)
            return returnValue

        
        def getName(self):
            returnValue = libdirect._inP5HfQaL_a(self.this)
            return returnValue

        
        def asAtomicField(self):
            returnValue = libdirect._inP5HfQ97Du(self.this)
            returnObject = DCAtomicField.DCAtomicField(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def asMolecularField(self):
            returnValue = libdirect._inP5HfQn7mz(self.this)
            returnObject = DCMolecularField.DCMolecularField(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject


    globals()['DCField'] = DCField

