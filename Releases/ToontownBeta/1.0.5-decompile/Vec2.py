# Source Generated with Decompyle++
# File: Vec2.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase2
import TypeHandle
import VBase2
import Ostream
import TypeHandle
classDefined = 0

def generateClass_Vec2():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Vec2(VBase2.VBase2, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3JJA9()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase2f(self, copy):
            self.this = libpanda._inPVZN33KGf(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float(self, fillValue):
            self.this = libpanda._inPVZN3mJJb(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float(self, x, y):
            self.this = libpanda._inPVZN3HG10(x, y)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN38UQp:
                libpanda._inPVZN38UQp(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3FctA()
            returnObject = Vec2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN3ri1V()
            returnObject = Vec2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN3r_ua()
            returnObject = Vec2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def getClassType():
            returnValue = libpanda._inPVZN3ayMy()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLVector2f_ptrConstLVecBase2f(self, copy):
            returnValue = libpanda._inPVZN3k61b(self.this, copy.this)
            returnObject = Vec2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLVector2f_float(self, fillValue):
            returnValue = libpanda._inPVZN3H5Pd(self.this, fillValue)
            returnObject = Vec2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___sub___ptrConstLVector2f(self):
            returnValue = libpanda._inPVZN3Omph(self.this)
            returnObject = Vec2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLVector2f_ptrConstLVecBase2f(self, other):
            returnValue = libpanda._inPVZN3Cc_P(self.this, other.this)
            returnObject = VBase2.VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLVector2f_ptrConstLVector2f(self, other):
            returnValue = libpanda._inPVZN3c5Kg(self.this, other.this)
            returnObject = Vec2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVector2f_ptrConstLVecBase2f(self, other):
            returnValue = libpanda._inPVZN3ipmQ(self.this, other.this)
            returnObject = VBase2.VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVector2f_ptrConstLVector2f(self, other):
            returnValue = libpanda._inPVZN380xg(self.this, other.this)
            returnObject = Vec2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def length(self):
            returnValue = libpanda._inPVZN3acF_(self.this)
            return returnValue

        
        def lengthSquared(self):
            returnValue = libpanda._inPVZN38FEZ(self.this)
            return returnValue

        
        def normalize(self):
            returnValue = libpanda._inPVZN3n6wG(self.this)
            return returnValue

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN3WpP0(self.this, scalar)
            returnObject = Vec2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3mBy1(self.this, scalar)
            returnObject = Vec2(None)
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
                elif isinstance(_args[0], VBase2.VBase2):
                    return self.overloaded_constructor_ptrConstLVecBase2f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2.VBase2> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor_float_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

        
        def __sub__(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded___sub___ptrConstLVector2f()
            elif numArgs == 1:
                if isinstance(_args[0], VBase2.VBase2):
                    return self.overloaded___sub___ptrConstLVector2f_ptrConstLVecBase2f(_args[0])
                elif isinstance(_args[0], Vec2):
                    return self.overloaded___sub___ptrConstLVector2f_ptrConstLVector2f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2.VBase2> <Vec2> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def __add__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase2.VBase2):
                    return self.overloaded___add___ptrConstLVector2f_ptrConstLVecBase2f(_args[0])
                elif isinstance(_args[0], Vec2):
                    return self.overloaded___add___ptrConstLVector2f_ptrConstLVector2f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2.VBase2> <Vec2> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLVector2f_float(_args[0])
                elif isinstance(_args[0], VBase2.VBase2):
                    return self.overloaded_assign_ptrLVector2f_ptrConstLVecBase2f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2.VBase2> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['Vec2'] = Vec2

