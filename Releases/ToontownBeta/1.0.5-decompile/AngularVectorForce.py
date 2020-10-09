# Source Generated with Decompyle++
# File: AngularVectorForce.pyo (Python 2.0)

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
import AngularForce
import TypeHandle
classDefined = 0

def generateClass_AngularVectorForce():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class AngularVectorForce(AngularForce.AngularForce, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrConstLVector3f(self, vec):
            self.this = libpandaphysics._inP9fJJXGjq(vec.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float(self, x, y, z):
            self.this = libpandaphysics._inP9fJJPXgj(x, y, z)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float(self, x, y):
            self.this = libpandaphysics._inP9fJJhl6s(x, y)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float(self, x):
            self.this = libpandaphysics._inP9fJJ67gk(x)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inP9fJJ4sEb()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstAngularVectorForce(self, copy):
            self.this = libpandaphysics._inP9fJJTkTX(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpandaphysics._inP9fJJnWC7()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_setVector_ptrAngularVectorForce_ptrConstLVector3f(self, v):
            returnValue = libpandaphysics._inP9fJJCpXM(self.this, v.this)
            return returnValue

        
        def overloaded_setVector_ptrAngularVectorForce_float_float_float(self, x, y, z):
            returnValue = libpandaphysics._inP9fJJHckG(self.this, x, y, z)
            return returnValue

        
        def getLocalVector(self):
            returnValue = libpandaphysics._inP9fJJeSwl(self.this)
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
                elif isinstance(_args[0], AngularVectorForce):
                    return self.overloaded_constructor_ptrConstAngularVectorForce(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Vec3.Vec3> <AngularVectorForce> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor_float_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_constructor_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 '

        
        def setVector(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Vec3.Vec3):
                    return self.overloaded_setVector_ptrAngularVectorForce_ptrConstLVector3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Vec3.Vec3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setVector_ptrAngularVectorForce_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


    globals()['AngularVectorForce'] = AngularVectorForce

