# Source Generated with Decompyle++
# File: OmniBoundingVolume.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import BoundingVolume
import Ostream
import TypeHandle
import GeometricBoundingVolume
import Point3
import Mat4
import TypeHandle
classDefined = 0

def generateClass_OmniBoundingVolume():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class OmniBoundingVolume(GeometricBoundingVolume.GeometricBoundingVolume, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPSkjPK3Bj()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPSkjP6Vf4:
                libpanda._inPSkjP6Vf4(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPSkjPUpVO()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)

    globals()['OmniBoundingVolume'] = OmniBoundingVolume

