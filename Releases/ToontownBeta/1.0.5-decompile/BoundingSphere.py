# Source Generated with Decompyle++
# File: BoundingSphere.pyo (Python 2.0)

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
import FiniteBoundingVolume
import Point3
import TypeHandle
classDefined = 0

def generateClass_BoundingSphere():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class BoundingSphere(FiniteBoundingVolume.FiniteBoundingVolume, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPSkjPj4oF()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLPoint3f_float(self, center, radius):
            self.this = libpanda._inPSkjPQRaH(center.this, radius)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPSkjPmo8B:
                libpanda._inPSkjPmo8B(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPSkjPpMTa()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getCenter(self):
            returnValue = libpanda._inPSkjPskph(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getRadius(self):
            returnValue = libpanda._inPSkjPrysx(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 2:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor_ptrConstLPoint3f_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 '


    globals()['BoundingSphere'] = BoundingSphere

