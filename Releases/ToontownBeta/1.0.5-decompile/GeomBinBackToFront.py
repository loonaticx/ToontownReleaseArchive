# Source Generated with Decompyle++
# File: GeomBinBackToFront.pyo (Python 2.0)

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
import Namable
import Ostream
import TypeHandle
import GeomBin
import CullTraverser
import Ostream
import Namable
import TypeHandle
import ReferenceCount
import TypedReferenceCount
classDefined = 0

def generateClass_GeomBinBackToFront():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GeomBinBackToFront(GeomBin.GeomBin, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, name):
            self.this = libpanda._inPspg2Yr_X(name)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPspg2qtsp:
                libpanda._inPspg2qtsp(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPspg282xZ()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)

    globals()['GeomBinBackToFront'] = GeomBinBackToFront

