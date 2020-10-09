# Source Generated with Decompyle++
# File: LinearFrictionForce.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
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
import BaseForce
import ForceNode
import Vec3
import PhysicsObject
import TypeHandle
import LinearForce
import TypeHandle
classDefined = 0

def generateClass_LinearFrictionForce():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class LinearFrictionForce(LinearForce.LinearForce, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_float_float_bool(self, coef, a, m):
            self.this = libpandaphysics._inP9fJJuaho(coef, a, m)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float(self, coef, a):
            self.this = libpandaphysics._inP9fJJY6K3(coef, a)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float(self, coef):
            self.this = libpandaphysics._inP9fJJS_3b(coef)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inP9fJJoFV5()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLinearFrictionForce(self, copy):
            self.this = libpandaphysics._inP9fJJmYW5(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpandaphysics._inP9fJJqIo1()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setCoef(self, coef):
            returnValue = libpandaphysics._inP9fJJz8ox(self.this, coef)
            return returnValue

        
        def getCoef(self):
            returnValue = libpandaphysics._inP9fJJHtwt(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_float(_args[0])
                elif isinstance(_args[0], LinearFrictionForce):
                    return self.overloaded_constructor_ptrConstLinearFrictionForce(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <LinearFrictionForce> '
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
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_constructor_float_float_bool(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 '


    globals()['LinearFrictionForce'] = LinearFrictionForce

