# Source Generated with Decompyle++
# File: GeomPoint.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import WritableConfigurable
import TypeHandle
import BoundedObject
import BoundingVolume
import TypeHandle
import DDrawable
import WritableConfigurable
import BoundedObject
import TypeHandle
import ReferenceCount
import BoundingVolume
import Geom
import DDrawable
import Ostream
import PTAVertexf
import PTANormalf
import PTAColorf
import PTATexCoordf
import PTAUshort
import TypeHandle
classDefined = 0

def generateClass_GeomPoint():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GeomPoint(Geom.Geom, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPMAKPjCsI:
                libpanda._inPMAKPjCsI(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPMAKPiVDs()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)

    globals()['GeomPoint'] = GeomPoint

