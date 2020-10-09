# Source Generated with Decompyle++
# File: SplineCorrection.pyo (Python 2.0)

import PandaStatic
import types
import libdirect
import libdirectDowncasts
import FFIExternalObject
import Point3
import Vec3
import Correction
import Correction
import Point3
import Vec3
classDefined = 0

def generateClass_SplineCorrection():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class SplineCorrection(Correction.Correction, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libdirectDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, parameter0, parameter1):
            self.this = libdirect._inPw5Y6iBjt(parameter0.this, parameter1.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libdirect and libdirect._inPw5Y6KQQx:
                libdirect._inPw5Y6KQQx(self.this)
            

        
        def setDuration(self, parameter1):
            returnValue = libdirect._inPw5Y6EXHy(self.this, parameter1)
            return returnValue

        
        def getDuration(self):
            returnValue = libdirect._inPw5Y60pTH(self.this)
            return returnValue


    globals()['SplineCorrection'] = SplineCorrection

