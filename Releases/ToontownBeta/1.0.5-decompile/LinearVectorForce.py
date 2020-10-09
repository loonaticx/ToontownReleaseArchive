# Source Generated with Decompyle++
# File: LinearVectorForce.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Vec3
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
classDefined = 0

def generateClass_LinearVectorForce():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class LinearVectorForce(LinearForce.LinearForce, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrConstLVector3f_float_bool(self, vec, a, mass):
            self.this = libpandaphysics._inP9fJJgZIH(vec.this, a, mass)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVector3f_float(self, vec, a):
            self.this = libpandaphysics._inP9fJJyDyV(vec.this, a)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVector3f(self, vec):
            self.this = libpandaphysics._inP9fJJyPg6(vec.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLinearVectorForce(self, copy):
            self.this = libpandaphysics._inP9fJJvtTR(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float_float_bool(self, x, y, z, a, mass):
            self.this = libpandaphysics._inP9fJJ4XC9(x, y, z, a, mass)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float_float(self, x, y, z, a):
            self.this = libpandaphysics._inP9fJJsLl3(x, y, z, a)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float(self, x, y, z):
            self.this = libpandaphysics._inP9fJJipZK(x, y, z)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float(self, x, y):
            self.this = libpandaphysics._inP9fJJYWo5(x, y)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float(self, x):
            self.this = libpandaphysics._inP9fJJuz3E(x)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inP9fJJgfAc()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpandaphysics._inP9fJJeNeJ()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_setVector_ptrLinearVectorForce_ptrConstLVector3f(self, v):
            returnValue = libpandaphysics._inP9fJJe__l(self.this, v.this)
            return returnValue

        
        def overloaded_setVector_ptrLinearVectorForce_float_float_float(self, x, y, z):
            returnValue = libpandaphysics._inP9fJJOgyt(self.this, x, y, z)
            return returnValue

        
        def getLocalVector(self):
            returnValue = libpandaphysics._inP9fJJFSwu(self.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_float(_args[0])
                elif isinstance(_args[0], Vec3.Vec3):
                    return self.overloaded_constructor_ptrConstLVector3f(_args[0])
                elif isinstance(_args[0], LinearVectorForce):
                    return self.overloaded_constructor_ptrConstLinearVectorForce(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Vec3.Vec3> <LinearVectorForce> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor_float_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                elif isinstance(_args[0], Vec3.Vec3):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor_ptrConstLVector3f_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Vec3.Vec3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_constructor_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                elif isinstance(_args[0], Vec3.Vec3):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_constructor_ptrConstLVector3f_float_bool(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Vec3.Vec3> '
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
            elif numArgs == 5:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.IntType):
                                    return self.overloaded_constructor_float_float_float_float_bool(_args[0], _args[1], _args[2], _args[3], _args[4])
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 4 5 '

        
        def setVector(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Vec3.Vec3):
                    return self.overloaded_setVector_ptrLinearVectorForce_ptrConstLVector3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Vec3.Vec3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setVector_ptrLinearVectorForce_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


    globals()['LinearVectorForce'] = LinearVectorForce

