# Source Generated with Decompyle++
# File: Prediction.pyo (Python 2.0)

import PandaStatic
import types
import libdirect
import libdirectDowncasts
import FFIExternalObject
import Point3
import Vec3
classDefined = 0

def generateClass_Prediction():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Prediction(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libdirectDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, parameter0):
            self.this = libdirect._inPw5Y6ppf4(parameter0.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libdirect and libdirect._inPw5Y68uSh:
                libdirect._inPw5Y68uSh(self.this)
            

        
        def step(self):
            returnValue = libdirect._inPw5Y6fm8f(self.this)
            return returnValue

        
        def newTelemetry(self, parameter1):
            returnValue = libdirect._inPw5Y6dpWq(self.this, parameter1.this)
            return returnValue

        
        def forceTelemetry(self, parameter1):
            returnValue = libdirect._inPw5Y6cZwT(self.this, parameter1.this)
            return returnValue

        
        def getPos(self):
            returnValue = libdirect._inPw5Y6wRlX(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getVel(self):
            returnValue = libdirect._inPw5Y61Asp(self.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject


    globals()['Prediction'] = Prediction

