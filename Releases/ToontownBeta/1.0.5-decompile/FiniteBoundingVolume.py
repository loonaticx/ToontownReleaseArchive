# Source Generated with Decompyle++
# File: FiniteBoundingVolume.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Point3
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

def generateClass_FiniteBoundingVolume():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class FiniteBoundingVolume(GeometricBoundingVolume.GeometricBoundingVolume, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
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
            if libpanda and libpanda._inPSkjPl5kj:
                libpanda._inPSkjPl5kj(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPSkjPBtxA()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getMin(self):
            returnValue = libpanda._inPSkjPaq34(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getMax(self):
            returnValue = libpanda._inPSkjPTm3J(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject


    globals()['FiniteBoundingVolume'] = FiniteBoundingVolume

