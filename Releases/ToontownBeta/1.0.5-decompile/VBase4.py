# Source Generated with Decompyle++
# File: VBase4.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Ostream
import TypeHandle
classDefined = 0

def generateClass_VBase4():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class VBase4(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3y_RY()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase4f(self, copy):
            self.this = libpanda._inPVZN3Wttd(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float(self, fillValue):
            self.this = libpanda._inPVZN3bHz7(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float_float(self, x, y, z, w):
            self.this = libpanda._inPVZN38qvG(x, y, z, w)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3qGGk:
                libpanda._inPVZN3qGGk(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3fhPT()
            returnObject = VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN3qcF3()
            returnObject = VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN3F3TT()
            returnObject = VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def unitZ():
            returnValue = libpanda._inPVZN3H3hv()
            returnObject = VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitZ = PandaStatic.PandaStatic(unitZ)
        
        def unitW():
            returnValue = libpanda._inPVZN3wc3a()
            returnObject = VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitW = PandaStatic.PandaStatic(unitW)
        
        def getClassType():
            returnValue = libpanda._inPVZN3akuD()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLVecBase4f_ptrConstLVecBase4f(self, copy):
            returnValue = libpanda._inPVZN3QIDG(self.this, copy.this)
            returnObject = VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLVecBase4f_float(self, fillValue):
            returnValue = libpanda._inPVZN3_xHk(self.this, fillValue)
            returnObject = VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def __getitem__(self, i):
            returnValue = libpanda._inPVZN3MFsV(self.this, i)
            return returnValue

        
        def isNan(self):
            returnValue = libpanda._inPVZN3qU3D(self.this)
            return returnValue

        
        def getCell(self, i):
            returnValue = libpanda._inPVZN3WZQp(self.this, i)
            return returnValue

        
        def getX(self):
            returnValue = libpanda._inPVZN3CyvU(self.this)
            return returnValue

        
        def getY(self):
            returnValue = libpanda._inPVZN3CWpZ(self.this)
            return returnValue

        
        def getZ(self):
            returnValue = libpanda._inPVZN3Cqge(self.this)
            return returnValue

        
        def getW(self):
            returnValue = libpanda._inPVZN3Ce3P(self.this)
            return returnValue

        
        def setCell(self, i, value):
            returnValue = libpanda._inPVZN35pHX(self.this, i, value)
            return returnValue

        
        def setX(self, value):
            returnValue = libpanda._inPVZN3CIKp(self.this, value)
            return returnValue

        
        def setY(self, value):
            returnValue = libpanda._inPVZN3CkCu(self.this, value)
            return returnValue

        
        def setZ(self, value):
            returnValue = libpanda._inPVZN3Cw6y(self.this, value)
            return returnValue

        
        def setW(self, value):
            returnValue = libpanda._inPVZN3CcRk(self.this, value)
            return returnValue

        
        def getNumComponents(self):
            returnValue = libpanda._inPVZN3tf36(self.this)
            return returnValue

        
        def fill(self, fillValue):
            returnValue = libpanda._inPVZN3PPIJ(self.this, fillValue)
            return returnValue

        
        def set(self, x, y, z, w):
            returnValue = libpanda._inPVZN33ZsX(self.this, x, y, z, w)
            return returnValue

        
        def dot(self, other):
            returnValue = libpanda._inPVZN3vO62(self.this, other.this)
            return returnValue

        
        def lessThan(self, other):
            returnValue = libpanda._inPVZN3q_vx(self.this, other.this)
            return returnValue

        
        def eq(self, other):
            returnValue = libpanda._inPVZN3TIZz(self.this, other.this)
            return returnValue

        
        def ne(self, other):
            returnValue = libpanda._inPVZN3fnAi(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLVecBase4f_ptrConstLVecBase4f(self, other):
            returnValue = libpanda._inPVZN3mxnx(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLVecBase4f_ptrConstLVecBase4f_float(self, other, threshold):
            returnValue = libpanda._inPVZN3BzYW(self.this, other.this, threshold)
            return returnValue

        
        def overloaded___sub___ptrConstLVecBase4f(self):
            returnValue = libpanda._inPVZN3Ioux(self.this)
            returnObject = VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __add__(self, other):
            returnValue = libpanda._inPVZN3sHxL(self.this, other.this)
            returnObject = VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVecBase4f_ptrConstLVecBase4f(self, other):
            returnValue = libpanda._inPVZN3s3Sf(self.this, other.this)
            returnObject = VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN3k4VF(self.this, scalar)
            returnObject = VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3kQK2(self.this, scalar)
            returnObject = VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __iadd__(self, other):
            returnValue = libpanda._inPVZN3mF4T(self.this, other.this)
            return self

        
        def __isub__(self, other):
            returnValue = libpanda._inPVZN3m1Zn(self.this, other.this)
            return self

        
        def __imul__(self, scalar):
            returnValue = libpanda._inPVZN30zPM(self.this, scalar)
            return self

        
        def __idiv__(self, scalar):
            returnValue = libpanda._inPVZN307D9(self.this, scalar)
            return self

        
        def overloaded_almostEqual_ptrConstLVecBase4f_ptrConstLVecBase4f_float(self, other, threshold):
            returnValue = libpanda._inPVZN33ZmQ(self.this, other.this, threshold)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLVecBase4f_ptrConstLVecBase4f(self, other):
            returnValue = libpanda._inPVZN3rkzg(self.this, other.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPVZN3JpcK(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_float(_args[0])
                elif isinstance(_args[0], VBase4):
                    return self.overloaded_constructor_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4> '
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
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 4 '

        
        def compareTo(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4):
                    return self.overloaded_compareTo_ptrConstLVecBase4f_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase4):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_compareTo_ptrConstLVecBase4f_ptrConstLVecBase4f_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLVecBase4f_float(_args[0])
                elif isinstance(_args[0], VBase4):
                    return self.overloaded_assign_ptrLVecBase4f_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def __sub__(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded___sub___ptrConstLVecBase4f()
            elif numArgs == 1:
                if isinstance(_args[0], VBase4):
                    return self.overloaded___sub___ptrConstLVecBase4f_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def almostEqual(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4):
                    return self.overloaded_almostEqual_ptrConstLVecBase4f_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase4):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_almostEqual_ptrConstLVecBase4f_ptrConstLVecBase4f_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['VBase4'] = VBase4

