# Source Generated with Decompyle++
# File: GeomBinGroup.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import GeomBin
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

def generateClass_GeomBinGroup():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GeomBinGroup(GeomBin.GeomBin, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPspg2zd2_:
                libpanda._inPspg2zd2_(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPspg2PsYX()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def addSubBin(self, subBin):
            returnValue = libpanda._inPspg2jTd0(self.this, subBin.this)
            return returnValue

        
        def getNumBins(self):
            returnValue = libpanda._inPspg2T7ZW(self.this)
            return returnValue

        
        def getBin(self, n):
            returnValue = libpanda._inPspg2EB1P(self.this, n)
            returnObject = GeomBin.GeomBin(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def removeBin(self, n):
            returnValue = libpanda._inPspg2IBCq(self.this, n)
            returnObject = GeomBin.GeomBin(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()


    globals()['GeomBinGroup'] = GeomBinGroup

