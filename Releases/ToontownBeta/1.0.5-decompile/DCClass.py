# Source Generated with Decompyle++
# File: DCClass.pyo (Python 2.0)

import PandaStatic
import types
import libdirect
import libdirectDowncasts
import FFIExternalObject
import DCField
classDefined = 0

def generateClass_DCClass():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DCClass(FFIExternalObject.FFIExternalObject):
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
            if libdirect and libdirect._inP5HfQrPDw:
                libdirect._inP5HfQrPDw(self.this)
            

        
        def getNumber(self):
            returnValue = libdirect._inP5HfQxF3k(self.this)
            return returnValue

        
        def getName(self):
            returnValue = libdirect._inP5HfQ64kV(self.this)
            return returnValue

        
        def hasParent(self):
            returnValue = libdirect._inP5HfQ_db8(self.this)
            return returnValue

        
        def getParent(self):
            returnValue = libdirect._inP5HfQtDJH(self.this)
            returnObject = DCClass(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getNumFields(self):
            returnValue = libdirect._inP5HfQzDsE(self.this)
            return returnValue

        
        def getField(self, n):
            returnValue = libdirect._inP5HfQL5GD(self.this, n)
            returnObject = DCField.DCField(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getFieldByName(self, name):
            returnValue = libdirect._inP5HfQCWLR(self.this, name)
            returnObject = DCField.DCField(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getNumInheritedFields(self):
            returnValue = libdirect._inP5HfQJq1_(self.this)
            return returnValue

        
        def getInheritedField(self, n):
            returnValue = libdirect._inP5HfQxJUD(self.this, n)
            returnObject = DCField.DCField(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject


    globals()['DCClass'] = DCClass

