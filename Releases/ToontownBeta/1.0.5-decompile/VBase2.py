# Source Generated with Decompyle++
# File: VBase2.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Ostream
import TypeHandle
classDefined = 0

def generateClass_VBase2():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class VBase2(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3Z0IU()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase2f(self, copy):
            self.this = libpanda._inPVZN3OqfL(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float(self, fillValue):
            self.this = libpanda._inPVZN3erq3(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float(self, x, y):
            self.this = libpanda._inPVZN3hqsK(x, y)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3B2DN:
                libpanda._inPVZN3B2DN(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3YgvP()
            returnObject = VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN3Tclz()
            returnObject = VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN3OczP()
            returnObject = VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def getClassType():
            returnValue = libpanda._inPVZN3DnOA()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLVecBase2f_ptrConstLVecBase2f(self, copy):
            returnValue = libpanda._inPVZN33Ic0(self.this, copy.this)
            returnObject = VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLVecBase2f_float(self, fillValue):
            returnValue = libpanda._inPVZN345ng(self.this, fillValue)
            returnObject = VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def __getitem__(self, i):
            returnValue = libpanda._inPVZN3zEMS(self.this, i)
            return returnValue

        
        def isNan(self):
            returnValue = libpanda._inPVZN3BTXA(self.this)
            return returnValue

        
        def getCell(self, i):
            returnValue = libpanda._inPVZN3rZwl(self.this, i)
            return returnValue

        
        def getX(self):
            returnValue = libpanda._inPVZN3nyPR(self.this)
            return returnValue

        
        def getY(self):
            returnValue = libpanda._inPVZN3nWJW(self.this)
            return returnValue

        
        def setCell(self, i, value):
            returnValue = libpanda._inPVZN3gqnT(self.this, i, value)
            return returnValue

        
        def setX(self, value):
            returnValue = libpanda._inPVZN3ZJql(self.this, value)
            return returnValue

        
        def setY(self, value):
            returnValue = libpanda._inPVZN3Zliq(self.this, value)
            return returnValue

        
        def getNumComponents(self):
            returnValue = libpanda._inPVZN3WeX3(self.this)
            return returnValue

        
        def fill(self, fillValue):
            returnValue = libpanda._inPVZN32PoF(self.this, fillValue)
            return returnValue

        
        def set(self, x, y):
            returnValue = libpanda._inPVZN3ft_9(self.this, x, y)
            return returnValue

        
        def dot(self, other):
            returnValue = libpanda._inPVZN32rXz(self.this, other.this)
            return returnValue

        
        def lessThan(self, other):
            returnValue = libpanda._inPVZN3C_Ig(self.this, other.this)
            return returnValue

        
        def eq(self, other):
            returnValue = libpanda._inPVZN3lGZs(self.this, other.this)
            return returnValue

        
        def ne(self, other):
            returnValue = libpanda._inPVZN3hmAb(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLVecBase2f_ptrConstLVecBase2f(self, other):
            returnValue = libpanda._inPVZN3OwAg(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLVecBase2f_ptrConstLVecBase2f_float(self, other, threshold):
            returnValue = libpanda._inPVZN3ZAyE(self.this, other.this, threshold)
            return returnValue

        
        def overloaded___sub___ptrConstLVecBase2f(self):
            returnValue = libpanda._inPVZN3PpOu(self.this)
            returnObject = VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __add__(self, other):
            returnValue = libpanda._inPVZN3DGK6(self.this, other.this)
            returnObject = VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVecBase2f_ptrConstLVecBase2f(self, other):
            returnValue = libpanda._inPVZN3E2rN(self.this, other.this)
            returnObject = VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN3t31B(self.this, scalar)
            returnObject = VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3tPqy(self.this, scalar)
            returnObject = VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __iadd__(self, other):
            returnValue = libpanda._inPVZN34E4M(self.this, other.this)
            return self

        
        def __isub__(self, other):
            returnValue = libpanda._inPVZN340Zg(self.this, other.this)
            return self

        
        def __imul__(self, scalar):
            returnValue = libpanda._inPVZN3byvI(self.this, scalar)
            return self

        
        def __idiv__(self, scalar):
            returnValue = libpanda._inPVZN3b6j5(self.this, scalar)
            return self

        
        def overloaded_almostEqual_ptrConstLVecBase2f_ptrConstLVecBase2f_float(self, other, threshold):
            returnValue = libpanda._inPVZN3gtFd(self.this, other.this, threshold)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLVecBase2f_ptrConstLVecBase2f(self, other):
            returnValue = libpanda._inPVZN3G4Tt(self.this, other.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPVZN3io8G(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_float(_args[0])
                elif isinstance(_args[0], VBase2):
                    return self.overloaded_constructor_ptrConstLVecBase2f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2> '
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

        
        def compareTo(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase2):
                    return self.overloaded_compareTo_ptrConstLVecBase2f_ptrConstLVecBase2f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase2):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_compareTo_ptrConstLVecBase2f_ptrConstLVecBase2f_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLVecBase2f_float(_args[0])
                elif isinstance(_args[0], VBase2):
                    return self.overloaded_assign_ptrLVecBase2f_ptrConstLVecBase2f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def __sub__(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded___sub___ptrConstLVecBase2f()
            elif numArgs == 1:
                if isinstance(_args[0], VBase2):
                    return self.overloaded___sub___ptrConstLVecBase2f_ptrConstLVecBase2f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def almostEqual(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase2):
                    return self.overloaded_almostEqual_ptrConstLVecBase2f_ptrConstLVecBase2f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase2):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_almostEqual_ptrConstLVecBase2f_ptrConstLVecBase2f_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['VBase2'] = VBase2

