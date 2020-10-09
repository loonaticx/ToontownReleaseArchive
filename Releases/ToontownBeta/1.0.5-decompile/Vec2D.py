# Source Generated with Decompyle++
# File: Vec2D.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase2D
import TypeHandle
import VBase2D
import Ostream
import TypeHandle
classDefined = 0

def generateClass_Vec2D():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Vec2D(VBase2D.VBase2D, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3p2d5()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase2d(self, copy):
            self.this = libpanda._inPVZN3j3IZ(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double(self, fillValue):
            self.this = libpanda._inPVZN3XgDk(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double_double(self, x, y):
            self.this = libpanda._inPVZN35L8S(x, y)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3DCHl:
                libpanda._inPVZN3DCHl(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3tfN9()
            returnObject = Vec2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN3ixVS()
            returnObject = Vec2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN3iVPX()
            returnObject = Vec2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def getClassType():
            returnValue = libpanda._inPVZN3xzsu()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLVector2d_ptrConstLVecBase2d(self, copy):
            returnValue = libpanda._inPVZN3s7OK(self.this, copy.this)
            returnObject = Vec2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLVector2d_double(self, fillValue):
            returnValue = libpanda._inPVZN3vY6n(self.this, fillValue)
            returnObject = Vec2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___sub___ptrConstLVector2d(self):
            returnValue = libpanda._inPVZN3HnJe(self.this)
            returnObject = Vec2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLVector2d_ptrConstLVecBase2d(self, other):
            returnValue = libpanda._inPVZN3ZdY_(self.this, other.this)
            returnObject = VBase2D.VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLVector2d_ptrConstLVector2d(self, other):
            returnValue = libpanda._inPVZN3DGPa(self.this, other.this)
            returnObject = Vec2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVector2d_ptrConstLVecBase2d(self, other):
            returnValue = libpanda._inPVZN35n__(self.this, other.this)
            returnObject = VBase2D.VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVector2d_ptrConstLVector2d(self, other):
            returnValue = libpanda._inPVZN3jC2a(self.this, other.this)
            returnObject = Vec2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def length(self):
            returnValue = libpanda._inPVZN3Tnl6(self.this)
            return returnValue

        
        def lengthSquared(self):
            returnValue = libpanda._inPVZN3jGkV(self.this)
            return returnValue

        
        def normalize(self):
            returnValue = libpanda._inPVZN3Q7QD(self.this)
            return returnValue

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN34z18(self.this, scalar)
            returnObject = Vec2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3oKX_(self.this, scalar)
            returnObject = Vec2D(None)
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
                    return self.overloaded_constructor_double(_args[0])
                elif isinstance(_args[0], VBase2D.VBase2D):
                    return self.overloaded_constructor_ptrConstLVecBase2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D.VBase2D> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor_double_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

        
        def __sub__(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded___sub___ptrConstLVector2d()
            elif numArgs == 1:
                if isinstance(_args[0], VBase2D.VBase2D):
                    return self.overloaded___sub___ptrConstLVector2d_ptrConstLVecBase2d(_args[0])
                elif isinstance(_args[0], Vec2D):
                    return self.overloaded___sub___ptrConstLVector2d_ptrConstLVector2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2D.VBase2D> <Vec2D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def __add__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase2D.VBase2D):
                    return self.overloaded___add___ptrConstLVector2d_ptrConstLVecBase2d(_args[0])
                elif isinstance(_args[0], Vec2D):
                    return self.overloaded___add___ptrConstLVector2d_ptrConstLVector2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2D.VBase2D> <Vec2D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLVector2d_double(_args[0])
                elif isinstance(_args[0], VBase2D.VBase2D):
                    return self.overloaded_assign_ptrLVector2d_ptrConstLVecBase2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D.VBase2D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['Vec2D'] = Vec2D

