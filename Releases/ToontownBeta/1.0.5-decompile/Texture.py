# Source Generated with Decompyle++
# File: Texture.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ImageBuffer
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
import Namable
import Ostream
import TypeHandle
import ImageBuffer
import Namable
import TypeHandle
import WritableConfigurable
import DDrawable
import BoundedObject
import Ostream
classDefined = 0

def generateClass_Texture():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Texture(ImageBuffer.ImageBuffer, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        FTLinearMipmapLinear = 5
        FTNearest = 0
        FTNearestMipmapNearest = 2
        FTNearestMipmapLinear = 4
        FTLinear = 1
        FTLinearMipmapNearest = 3
        WMClamp = 0
        WMRepeat = 1
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPMAKPGOoZ()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPMAKP80sL:
                libpanda._inPMAKP80sL(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPMAKPhc2_()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def read(self, name, gray):
            returnValue = libpanda._inPMAKPrm0E(self.this, name, gray)
            return returnValue

        
        def setWrapu(self, wrap):
            returnValue = libpanda._inPMAKPWi99(self.this, wrap)
            return returnValue

        
        def setWrapv(self, wrap):
            returnValue = libpanda._inPMAKPRiLa(self.this, wrap)
            return returnValue

        
        def setMinfilter(self, filter):
            returnValue = libpanda._inPMAKPfeu7(self.this, filter)
            return returnValue

        
        def setMagfilter(self, filter):
            returnValue = libpanda._inPMAKP1kn6(self.this, filter)
            return returnValue

        
        def setAnisotropicDegree(self, anisotropicDegree):
            returnValue = libpanda._inPMAKP_qw3(self.this, anisotropicDegree)
            return returnValue

        
        def getWrapu(self):
            returnValue = libpanda._inPMAKPB4dk(self.this)
            return returnValue

        
        def getWrapv(self):
            returnValue = libpanda._inPMAKPG4rA(self.this)
            return returnValue

        
        def getMinfilter(self):
            returnValue = libpanda._inPMAKPfGfL(self.this)
            return returnValue

        
        def getMagfilter(self):
            returnValue = libpanda._inPMAKP14YK(self.this)
            return returnValue

        
        def getAnisotropicDegree(self):
            returnValue = libpanda._inPMAKPKcMk(self.this)
            return returnValue


    globals()['Texture'] = Texture

