# Source Generated with Decompyle++
# File: DCAtomicField.pyo (Python 2.0)

import PandaStatic
import types
import libdirect
import libdirectDowncasts
import FFIExternalObject
import DCField
import DCAtomicField
import DCMolecularField
classDefined = 0

def generateClass_DCAtomicField():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DCAtomicField(DCField.DCField, FFIExternalObject.FFIExternalObject):
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
            if libdirect and libdirect._inP5HfQ6Z_T:
                libdirect._inP5HfQ6Z_T(self.this)
            

        
        def getNumElements(self):
            returnValue = libdirect._inP5HfQsX5I(self.this)
            return returnValue

        
        def getElementType(self, n):
            returnValue = libdirect._inP5HfQpnXT(self.this, n)
            return returnValue

        
        def getElementName(self, n):
            returnValue = libdirect._inP5HfQDm_N(self.this, n)
            return returnValue

        
        def getElementDivisor(self, n):
            returnValue = libdirect._inP5HfQ3hmD(self.this, n)
            return returnValue

        
        def getElementDefault(self, n):
            returnValue = libdirect._inP5HfQddFi(self.this, n)
            return returnValue

        
        def hasElementDefault(self, n):
            returnValue = libdirect._inP5HfQcdfy(self.this, n)
            return returnValue

        
        def isRequired(self):
            returnValue = libdirect._inP5HfQT1zo(self.this)
            return returnValue

        
        def isBroadcast(self):
            returnValue = libdirect._inP5HfQjsGH(self.this)
            return returnValue

        
        def isP2p(self):
            returnValue = libdirect._inP5HfQBN1D(self.this)
            return returnValue

        
        def isRam(self):
            returnValue = libdirect._inP5HfQqQYx(self.this)
            return returnValue

        
        def isDb(self):
            returnValue = libdirect._inP5HfQCUN0(self.this)
            return returnValue

        
        def isClsend(self):
            returnValue = libdirect._inP5HfQV8B2(self.this)
            return returnValue

        
        def isClrecv(self):
            returnValue = libdirect._inP5HfQFJ6E(self.this)
            return returnValue

        
        def isOwnsend(self):
            returnValue = libdirect._inP5HfQWk40(self.this)
            return returnValue


    globals()['DCAtomicField'] = DCAtomicField

