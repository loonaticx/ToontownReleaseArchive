# Source Generated with Decompyle++
# File: VBase3D.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Ostream
import TypeHandle
classDefined = 0

def generateClass_VBase3D():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class VBase3D(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3c8ry()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase3d(self, copy):
            self.this = libpanda._inPVZN3n0kN(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double(self, fillValue):
            self.this = libpanda._inPVZN335Fc(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double_double_double(self, x, y, z):
            self.this = libpanda._inPVZN3i2cq(x, y, z)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3pKtX:
                libpanda._inPVZN3pKtX(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3mFgB()
            returnObject = VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN39KWl()
            returnObject = VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN3ALkB()
            returnObject = VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def unitZ():
            returnValue = libpanda._inPVZN36Kyd()
            returnObject = VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitZ = PandaStatic.PandaStatic(unitZ)
        
        def getClassType():
            returnValue = libpanda._inPVZN3ra_x()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLVecBase3d_ptrConstLVecBase3d(self, copy):
            returnValue = libpanda._inPVZN3r0vJ(self.this, copy.this)
            returnObject = VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLVecBase3d_double(self, fillValue):
            returnValue = libpanda._inPVZN34nPY(self.this, fillValue)
            returnObject = VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def __getitem__(self, i):
            returnValue = libpanda._inPVZN3Bh7D(self.this, i)
            return returnValue

        
        def isNan(self):
            returnValue = libpanda._inPVZN30IHy(self.this)
            return returnValue

        
        def getCell(self, i):
            returnValue = libpanda._inPVZN3ZEgX(self.this, i)
            return returnValue

        
        def getX(self):
            returnValue = libpanda._inPVZN31HAD(self.this)
            return returnValue

        
        def getY(self):
            returnValue = libpanda._inPVZN31j4H(self.this)
            return returnValue

        
        def getZ(self):
            returnValue = libpanda._inPVZN31_wM(self.this)
            return returnValue

        
        def setCell(self, i, value):
            returnValue = libpanda._inPVZN3cYRe(self.this, i, value)
            return returnValue

        
        def setX(self, value):
            returnValue = libpanda._inPVZN3YzV6(self.this, value)
            return returnValue

        
        def setY(self, value):
            returnValue = libpanda._inPVZN3YXO_(self.this, value)
            return returnValue

        
        def setZ(self, value):
            returnValue = libpanda._inPVZN3XbGE(self.this, value)
            return returnValue

        
        def getNumComponents(self):
            returnValue = libpanda._inPVZN3ELHp(self.this)
            return returnValue

        
        def fill(self, fillValue):
            returnValue = libpanda._inPVZN3q0c_(self.this, fillValue)
            return returnValue

        
        def set(self, x, y, z):
            returnValue = libpanda._inPVZN3EW26(self.this, x, y, z)
            return returnValue

        
        def dot(self, other):
            returnValue = libpanda._inPVZN3xn6j(self.this, other.this)
            return returnValue

        
        def cross(self, other):
            returnValue = libpanda._inPVZN3oAMU(self.this, other.this)
            returnObject = VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def lessThan(self, other):
            returnValue = libpanda._inPVZN3YYd1(self.this, other.this)
            return returnValue

        
        def eq(self, other):
            returnValue = libpanda._inPVZN3ye4P(self.this, other.this)
            return returnValue

        
        def ne(self, other):
            returnValue = libpanda._inPVZN379g_(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLVecBase3d_ptrConstLVecBase3d(self, other):
            returnValue = libpanda._inPVZN35DU1(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLVecBase3d_ptrConstLVecBase3d_double(self, other, threshold):
            returnValue = libpanda._inPVZN38uKA(self.this, other.this, threshold)
            return returnValue

        
        def overloaded___sub___ptrConstLVecBase3d(self):
            returnValue = libpanda._inPVZN39LAg(self.this)
            returnObject = VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __add__(self, other):
            returnValue = libpanda._inPVZN3SQeP(self.this, other.this)
            returnObject = VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVecBase3d_ptrConstLVecBase3d(self, other):
            returnValue = libpanda._inPVZN3Sg_i(self.this, other.this)
            returnObject = VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN3zYn2(self.this, scalar)
            returnObject = VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN30wdn(self.this, scalar)
            returnObject = VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __iadd__(self, other):
            returnValue = libpanda._inPVZN3TNXw(self.this, other.this)
            return self

        
        def __isub__(self, other):
            returnValue = libpanda._inPVZN3Ud4D(self.this, other.this)
            return self

        
        def __imul__(self, scalar):
            returnValue = libpanda._inPVZN3_bn2(self.this, scalar)
            return self

        
        def __idiv__(self, scalar):
            returnValue = libpanda._inPVZN3DUcn(self.this, scalar)
            return self

        
        def crossInto(self, other):
            returnValue = libpanda._inPVZN3fwqm(self.this, other.this)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLVecBase3d_ptrConstLVecBase3d_double(self, other, threshold):
            returnValue = libpanda._inPVZN3zcbn(self.this, other.this, threshold)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLVecBase3d_ptrConstLVecBase3d(self, other):
            returnValue = libpanda._inPVZN3Z_6W(self.this, other.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPVZN3abt4(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_double(_args[0])
                elif isinstance(_args[0], VBase3D):
                    return self.overloaded_constructor_ptrConstLVecBase3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_constructor_double_double_double(_args[0], _args[1], _args[2])
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
                if isinstance(_args[0], VBase3D):
                    return self.overloaded_compareTo_ptrConstLVecBase3d_ptrConstLVecBase3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3D> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase3D):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_compareTo_ptrConstLVecBase3d_ptrConstLVecBase3d_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLVecBase3d_double(_args[0])
                elif isinstance(_args[0], VBase3D):
                    return self.overloaded_assign_ptrLVecBase3d_ptrConstLVecBase3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def __sub__(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded___sub___ptrConstLVecBase3d()
            elif numArgs == 1:
                if isinstance(_args[0], VBase3D):
                    return self.overloaded___sub___ptrConstLVecBase3d_ptrConstLVecBase3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def almostEqual(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3D):
                    return self.overloaded_almostEqual_ptrConstLVecBase3d_ptrConstLVecBase3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3D> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase3D):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_almostEqual_ptrConstLVecBase3d_ptrConstLVecBase3d_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['VBase3D'] = VBase3D

