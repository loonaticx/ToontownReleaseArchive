# Source Generated with Decompyle++
# File: GeometricBoundingVolume.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Point3
import Mat4
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
classDefined = 0

def generateClass_GeometricBoundingVolume():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GeometricBoundingVolume(BoundingVolume.BoundingVolume, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPSkjPd5dG:
                libpanda._inPSkjPd5dG(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPSkjP6Ogo()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_extendBy_ptrGeometricBoundingVolume_ptrConstGeometricBoundingVolume(self, vol):
            returnValue = libpanda._inPSkjPsza3(self.this, vol.this)
            return returnValue

        
        def overloaded_extendBy_ptrGeometricBoundingVolume_ptrConstLPoint3f(self, point):
            returnValue = libpanda._inPSkjPyztT(self.this, point.this)
            return returnValue

        
        def around(self, first, last):
            returnValue = libpanda._inPSkjPWJ7k(self.this, first.this, last.this)
            return returnValue

        
        def overloaded_contains_ptrConstGeometricBoundingVolume_ptrConstGeometricBoundingVolume(self, vol):
            returnValue = libpanda._inPSkjP6VB3(self.this, vol.this)
            return returnValue

        
        def overloaded_contains_ptrConstGeometricBoundingVolume_ptrConstLPoint3f(self, point):
            returnValue = libpanda._inPSkjP9AdR(self.this, point.this)
            return returnValue

        
        def overloaded_contains_ptrConstGeometricBoundingVolume_ptrConstLPoint3f_ptrConstLPoint3f(self, a, b):
            returnValue = libpanda._inPSkjPtswX(self.this, a.this, b.this)
            return returnValue

        
        def getApproxCenter(self):
            returnValue = libpanda._inPSkjP_67m(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def xform(self, mat):
            returnValue = libpanda._inPSkjPB198(self.this, mat.this)
            return returnValue

        
        def extendBy(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Point3.Point3):
                    return self.overloaded_extendBy_ptrGeometricBoundingVolume_ptrConstLPoint3f(_args[0])
                elif isinstance(_args[0], GeometricBoundingVolume):
                    return self.overloaded_extendBy_ptrGeometricBoundingVolume_ptrConstGeometricBoundingVolume(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <GeometricBoundingVolume> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def contains(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Point3.Point3):
                    return self.overloaded_contains_ptrConstGeometricBoundingVolume_ptrConstLPoint3f(_args[0])
                elif isinstance(_args[0], GeometricBoundingVolume):
                    return self.overloaded_contains_ptrConstGeometricBoundingVolume_ptrConstGeometricBoundingVolume(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <GeometricBoundingVolume> '
            elif numArgs == 2:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], Point3.Point3):
                        return self.overloaded_contains_ptrConstGeometricBoundingVolume_ptrConstLPoint3f_ptrConstLPoint3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['GeometricBoundingVolume'] = GeometricBoundingVolume

