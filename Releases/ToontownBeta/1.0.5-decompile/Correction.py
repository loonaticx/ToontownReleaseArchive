# Source Generated with Decompyle++
# File: Correction.pyo (Python 2.0)

import PandaStatic
import types
import libdirect
import libdirectDowncasts
import FFIExternalObject
import Point3
import Vec3
classDefined = 0

def generateClass_Correction():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Correction(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libdirectDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, parameter0, parameter1):
            self.this = libdirect._inPw5Y6m4yN(parameter0.this, parameter1.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libdirect and libdirect._inPw5Y6KQQx:
                libdirect._inPw5Y6KQQx(self.this)
            

        
        def step(self):
            returnValue = libdirect._inPw5Y6SA9X(self.this)
            return returnValue

        
        def newTarget(self, parameter1, parameter2):
            returnValue = libdirect._inPw5Y6um6w(self.this, parameter1.this, parameter2.this)
            return returnValue

        
        def forceTarget(self, parameter1, parameter2):
            returnValue = libdirect._inPw5Y6u7sP(self.this, parameter1.this, parameter2.this)
            return returnValue

        
        def getPos(self):
            returnValue = libdirect._inPw5Y6lEoP(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getVel(self):
            returnValue = libdirect._inPw5Y6cnsh(self.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject


    globals()['Correction'] = Correction

