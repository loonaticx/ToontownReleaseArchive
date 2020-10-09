# Source Generated with Decompyle++
# File: DCMolecularField.pyo (Python 2.0)

import PandaStatic
import types
import libdirect
import libdirectDowncasts
import FFIExternalObject
import DCAtomicField
import DCField
import DCAtomicField
import DCMolecularField
classDefined = 0

def generateClass_DCMolecularField():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DCMolecularField(DCField.DCField, FFIExternalObject.FFIExternalObject):
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
            if libdirect and libdirect._inP5HfQSR88:
                libdirect._inP5HfQSR88(self.this)
            

        
        def getNumAtomics(self):
            returnValue = libdirect._inP5HfQ2tYG(self.this)
            return returnValue

        
        def getAtomic(self, n):
            returnValue = libdirect._inP5HfQDLkf(self.this, n)
            returnObject = DCAtomicField.DCAtomicField(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject


    globals()['DCMolecularField'] = DCMolecularField

