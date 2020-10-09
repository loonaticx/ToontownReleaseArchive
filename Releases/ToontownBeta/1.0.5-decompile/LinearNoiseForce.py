# Source Generated with Decompyle++
# File: LinearNoiseForce.pyo (Python 2.0)

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
import LinearRandomForce
import TypeHandle
classDefined = 0

def generateClass_LinearNoiseForce():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class LinearNoiseForce(LinearRandomForce.LinearRandomForce, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_float_bool(self, a, m):
            self.this = libpandaphysics._inP9fJJZFF1(a, m)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float(self, a):
            self.this = libpandaphysics._inP9fJJGZFG(a)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inP9fJJiaku()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLinearNoiseForce(self, copy):
            self.this = libpandaphysics._inP9fJJb5_B(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpandaphysics._inP9fJJYDNh()
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
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_float(_args[0])
                elif isinstance(_args[0], LinearNoiseForce):
                    return self.overloaded_constructor_ptrConstLinearNoiseForce(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <LinearNoiseForce> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor_float_bool(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


    globals()['LinearNoiseForce'] = LinearNoiseForce

