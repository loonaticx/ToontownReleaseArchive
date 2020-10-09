# Source Generated with Decompyle++
# File: OrthoProjection.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Frustum
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import Projection
import Point2
import Point3
import Vec3
import TypeHandle
classDefined = 0

def generateClass_OrthoProjection():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class OrthoProjection(Projection.Projection, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, frustumBase):
            self.this = libpanda._inPMAKPin60(frustumBase.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPMAKPJ_RU:
                libpanda._inPMAKPJ_RU(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPMAKPudqt()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)

    globals()['OrthoProjection'] = OrthoProjection

