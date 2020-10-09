# Source Generated with Decompyle++
# File: LinearPrediction.pyo (Python 2.0)

import PandaStatic
import types
import libdirect
import libdirectDowncasts
import FFIExternalObject
import Point3
import Prediction
import Prediction
import Point3
import Vec3
classDefined = 0

def generateClass_LinearPrediction():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class LinearPrediction(Prediction.Prediction, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libdirectDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, parameter0):
            self.this = libdirect._inPw5Y6sUtB(parameter0.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libdirect and libdirect._inPw5Y68uSh:
                libdirect._inPw5Y68uSh(self.this)
            


    globals()['LinearPrediction'] = LinearPrediction

