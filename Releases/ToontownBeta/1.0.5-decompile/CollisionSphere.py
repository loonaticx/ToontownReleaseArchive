# Source Generated with Decompyle++
# File: CollisionSphere.pyo (Python 2.0)

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
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import ReferenceCount
import TypeHandle
import TypedWritableReferenceCount
import ReferenceCount
import TypeHandle
import Writable
import TypedWritable
import BoundedObject
import BoundingVolume
import TypeHandle
import CollisionSolid
import Ostream
import BoundedObject
import TypeHandle
import ReferenceCount
import TypedWritableReferenceCount
import BoundingVolume
classDefined = 0

def generateClass_CollisionSphere():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CollisionSphere(CollisionSolid.CollisionSolid, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrConstLPoint3f_float(self, center, radius):
            self.this = libpanda._inPHwcaEnNB(center.this, radius)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float_float(self, cx, cy, cz, radius):
            self.this = libpanda._inPHwcavrzm(cx, cy, cz, radius)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPHwcaJ0y2:
                libpanda._inPHwcaJ0y2(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPHwcaHA89()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_setCenter_ptrCollisionSphere_ptrConstLPoint3f(self, center):
            returnValue = libpanda._inPHwcawcUl(self.this, center.this)
            return returnValue

        
        def overloaded_setCenter_ptrCollisionSphere_float_float_float(self, x, y, z):
            returnValue = libpanda._inPHwcah3aV(self.this, x, y, z)
            return returnValue

        
        def getCenter(self):
            returnValue = libpanda._inPHwcas6Aq(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setRadius(self, radius):
            returnValue = libpanda._inPHwcanewq(self.this, radius)
            return returnValue

        
        def getRadius(self):
            returnValue = libpanda._inPHwcaEszr(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor_ptrConstLPoint3f_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_constructor_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

        
        def setCenter(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Point3.Point3):
                    return self.overloaded_setCenter_ptrCollisionSphere_ptrConstLPoint3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setCenter_ptrCollisionSphere_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


    globals()['CollisionSphere'] = CollisionSphere

