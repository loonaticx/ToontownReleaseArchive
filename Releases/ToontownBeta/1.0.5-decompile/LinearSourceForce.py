# Source Generated with Decompyle++
# File: LinearSourceForce.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
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
import BaseForce
import ForceNode
import Vec3
import PhysicsObject
import TypeHandle
import LinearForce
import TypeHandle
import LinearDistanceForce
import Point3
import TypeHandle
classDefined = 0

def generateClass_LinearSourceForce():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class LinearSourceForce(LinearDistanceForce.LinearDistanceForce, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrConstLPoint3f___enum__FalloffType_float_float_bool(self, p, f, r, a, mass):
            self.this = libpandaphysics._inP9fJJL9wD(p.this, f, r, a, mass)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLPoint3f___enum__FalloffType_float_float(self, p, f, r, a):
            self.this = libpandaphysics._inP9fJJFeul(p.this, f, r, a)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLPoint3f___enum__FalloffType_float(self, p, f, r):
            self.this = libpandaphysics._inP9fJJfknZ(p.this, f, r)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inP9fJJ0UoW()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLinearSourceForce(self, copy):
            self.this = libpandaphysics._inP9fJJfbjF(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpandaphysics._inP9fJJJPNb()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], LinearSourceForce):
                    return self.overloaded_constructor_ptrConstLinearSourceForce(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <LinearSourceForce> '
            elif numArgs == 3:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_constructor_ptrConstLPoint3f___enum__FalloffType_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            elif numArgs == 4:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_constructor_ptrConstLPoint3f___enum__FalloffType_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            elif numArgs == 5:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.IntType):
                                    return self.overloaded_constructor_ptrConstLPoint3f___enum__FalloffType_float_float_bool(_args[0], _args[1], _args[2], _args[3], _args[4])
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 4 5 '


    globals()['LinearSourceForce'] = LinearSourceForce

