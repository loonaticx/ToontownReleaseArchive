# Source Generated with Decompyle++
# File: VBase3.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Ostream
import TypeHandle
classDefined = 0

def generateClass_VBase3():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class VBase3(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN32gM2()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase3f(self, copy):
            self.this = libpanda._inPVZN3KrmU(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float(self, fillValue):
            self.this = libpanda._inPVZN36ouZ(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float(self, x, y, z):
            self.this = libpanda._inPVZN3g96v(x, y, z)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3W_k4:
                libpanda._inPVZN3W_k4(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3Dgfx()
            returnObject = VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN3fcVV()
            returnObject = VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN3Zcjx()
            returnObject = VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def unitZ():
            returnValue = libpanda._inPVZN3ccxN()
            returnObject = VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitZ = PandaStatic.PandaStatic(unitZ)
        
        def getClassType():
            returnValue = libpanda._inPVZN3Wn_h()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLVecBase3f_ptrConstLVecBase3f(self, copy):
            returnValue = libpanda._inPVZN3joP9(self.this, copy.this)
            returnObject = VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLVecBase3f_float(self, fillValue):
            returnValue = libpanda._inPVZN3k5XC(self.this, fillValue)
            returnObject = VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def __getitem__(self, i):
            returnValue = libpanda._inPVZN3gE8z(self.this, i)
            return returnValue

        
        def isNan(self):
            returnValue = libpanda._inPVZN3WTHi(self.this)
            return returnValue

        
        def getCell(self, i):
            returnValue = libpanda._inPVZN3HZgH(self.this, i)
            return returnValue

        
        def getX(self):
            returnValue = libpanda._inPVZN3Wy_y(self.this)
            return returnValue

        
        def getY(self):
            returnValue = libpanda._inPVZN3WW53(self.this)
            return returnValue

        
        def getZ(self):
            returnValue = libpanda._inPVZN3Wqw8(self.this)
            return returnValue

        
        def setCell(self, i, value):
            returnValue = libpanda._inPVZN3NqX1(self.this, i, value)
            return returnValue

        
        def setX(self, value):
            returnValue = libpanda._inPVZN3VIaH(self.this, value)
            return returnValue

        
        def setY(self, value):
            returnValue = libpanda._inPVZN3VkSM(self.this, value)
            return returnValue

        
        def setZ(self, value):
            returnValue = libpanda._inPVZN3VwKR(self.this, value)
            return returnValue

        
        def getNumComponents(self):
            returnValue = libpanda._inPVZN3ifHZ(self.this)
            return returnValue

        
        def fill(self, fillValue):
            returnValue = libpanda._inPVZN3jPYn(self.this, fillValue)
            return returnValue

        
        def set(self, x, y, z):
            returnValue = libpanda._inPVZN3H0vy(self.this, x, y, z)
            return returnValue

        
        def dot(self, other):
            returnValue = libpanda._inPVZN3TdIV(self.this, other.this)
            return returnValue

        
        def cross(self, other):
            returnValue = libpanda._inPVZN3Tj6l(self.this, other.this)
            returnObject = VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def lessThan(self, other):
            returnValue = libpanda._inPVZN3We8o(self.this, other.this)
            return returnValue

        
        def eq(self, other):
            returnValue = libpanda._inPVZN3_G5v(self.this, other.this)
            return returnValue

        
        def ne(self, other):
            returnValue = libpanda._inPVZN36mge(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other):
            returnValue = libpanda._inPVZN3yR0o(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLVecBase3f_ptrConstLVecBase3f_float(self, other, threshold):
            returnValue = libpanda._inPVZN31glN(self.this, other.this, threshold)
            return returnValue

        
        def overloaded___sub___ptrConstLVecBase3f(self):
            returnValue = libpanda._inPVZN3bo_P(self.this)
            returnObject = VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __add__(self, other):
            returnValue = libpanda._inPVZN3Ym9C(self.this, other.this)
            returnObject = VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVecBase3f_ptrConstLVecBase3f(self, other):
            returnValue = libpanda._inPVZN3YWfW(self.this, other.this)
            returnObject = VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN3A3lj(self.this, scalar)
            returnObject = VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3RPaU(self.this, scalar)
            returnObject = VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __iadd__(self, other):
            returnValue = libpanda._inPVZN3_DYQ(self.this, other.this)
            return self

        
        def __isub__(self, other):
            returnValue = libpanda._inPVZN3_z5j(self.this, other.this)
            return self

        
        def __imul__(self, scalar):
            returnValue = libpanda._inPVZN3Izfq(self.this, scalar)
            return self

        
        def __idiv__(self, scalar):
            returnValue = libpanda._inPVZN3H7Tb(self.this, scalar)
            return self

        
        def crossInto(self, other):
            returnValue = libpanda._inPVZN3ocKa(self.this, other.this)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLVecBase3f_ptrConstLVecBase3f_float(self, other, threshold):
            returnValue = libpanda._inPVZN3cj12(self.this, other.this, threshold)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other):
            returnValue = libpanda._inPVZN3vaDH(self.this, other.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPVZN31oso(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_float(_args[0])
                elif isinstance(_args[0], VBase3):
                    return self.overloaded_constructor_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3> '
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
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 '

        
        def compareTo(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3):
                    return self.overloaded_compareTo_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase3):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_compareTo_ptrConstLVecBase3f_ptrConstLVecBase3f_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLVecBase3f_float(_args[0])
                elif isinstance(_args[0], VBase3):
                    return self.overloaded_assign_ptrLVecBase3f_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def __sub__(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded___sub___ptrConstLVecBase3f()
            elif numArgs == 1:
                if isinstance(_args[0], VBase3):
                    return self.overloaded___sub___ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def almostEqual(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3):
                    return self.overloaded_almostEqual_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase3):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_almostEqual_ptrConstLVecBase3f_ptrConstLVecBase3f_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['VBase3'] = VBase3

