# Source Generated with Decompyle++
# File: VBase2D.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Ostream
import TypeHandle
classDefined = 0

def generateClass_VBase2D():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class VBase2D(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3_2nQ()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase2d(self, copy):
            self.this = libpanda._inPVZN37tdE(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double(self, fillValue):
            self.this = libpanda._inPVZN3bXC6(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double_double(self, x, y):
            self.this = libpanda._inPVZN37x0M(x, y)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3ViLs:
                libpanda._inPVZN3ViLs(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3qFwf()
            returnObject = VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN3yQmD()
            returnObject = VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN30Q0f()
            returnObject = VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def getClassType():
            returnValue = libpanda._inPVZN3oaPQ()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLVecBase2d_ptrConstLVecBase2d(self, copy):
            returnValue = libpanda._inPVZN3_U8A(self.this, copy.this)
            returnObject = VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLVecBase2d_double(self, fillValue):
            returnValue = libpanda._inPVZN3cnf2(self.this, fillValue)
            returnObject = VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def __getitem__(self, i):
            returnValue = libpanda._inPVZN3VhLi(self.this, i)
            return returnValue

        
        def isNan(self):
            returnValue = libpanda._inPVZN3fIXQ(self.this)
            return returnValue

        
        def getCell(self, i):
            returnValue = libpanda._inPVZN3NFw1(self.this, i)
            return returnValue

        
        def getX(self):
            returnValue = libpanda._inPVZN3JGQh(self.this)
            return returnValue

        
        def getY(self):
            returnValue = libpanda._inPVZN3JiIm(self.this)
            return returnValue

        
        def setCell(self, i, value):
            returnValue = libpanda._inPVZN3wYh8(self.this, i, value)
            return returnValue

        
        def setX(self, value):
            returnValue = libpanda._inPVZN3DzlY(self.this, value)
            return returnValue

        
        def setY(self, value):
            returnValue = libpanda._inPVZN3DXed(self.this, value)
            return returnValue

        
        def getNumComponents(self):
            returnValue = libpanda._inPVZN31LXH(self.this)
            return returnValue

        
        def fill(self, fillValue):
            returnValue = libpanda._inPVZN3l0sc(self.this, fillValue)
            return returnValue

        
        def set(self, x, y):
            returnValue = libpanda._inPVZN3Uay_(self.this, x, y)
            return returnValue

        
        def dot(self, other):
            returnValue = libpanda._inPVZN3VcJC(self.this, other.this)
            return returnValue

        
        def lessThan(self, other):
            returnValue = libpanda._inPVZN3E4os(self.this, other.this)
            return returnValue

        
        def eq(self, other):
            returnValue = libpanda._inPVZN3ZlYM(self.this, other.this)
            return returnValue

        
        def ne(self, other):
            returnValue = libpanda._inPVZN3mFB7(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLVecBase2d_ptrConstLVecBase2d(self, other):
            returnValue = libpanda._inPVZN3Vkgs(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLVecBase2d_ptrConstLVecBase2d_double(self, other, threshold):
            returnValue = libpanda._inPVZN3XPX3(self.this, other.this, threshold)
            return returnValue

        
        def overloaded___sub___ptrConstLVecBase2d(self):
            returnValue = libpanda._inPVZN3xMQ_(self.this)
            returnObject = VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __add__(self, other):
            returnValue = libpanda._inPVZN3_vpG(self.this, other.this)
            returnObject = VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVecBase2d_ptrConstLVecBase2d(self, other):
            returnValue = libpanda._inPVZN3__La(self.this, other.this)
            returnObject = VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN3IT3U(self.this, scalar)
            returnObject = VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3BrtF(self.this, scalar)
            returnObject = VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __iadd__(self, other):
            returnValue = libpanda._inPVZN3sN3s(self.this, other.this)
            return self

        
        def __isub__(self, other):
            returnValue = libpanda._inPVZN31dYA(self.this, other.this)
            return self

        
        def __imul__(self, scalar):
            returnValue = libpanda._inPVZN3Pc3U(self.this, scalar)
            return self

        
        def __idiv__(self, scalar):
            returnValue = libpanda._inPVZN3QUsF(self.this, scalar)
            return self

        
        def overloaded_almostEqual_ptrConstLVecBase2d_ptrConstLVecBase2d_double(self, other, threshold):
            returnValue = libpanda._inPVZN34oqN(self.this, other.this, threshold)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLVecBase2d_ptrConstLVecBase2d(self, other):
            returnValue = libpanda._inPVZN3gtK9(self.this, other.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPVZN3Lb9W(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_double(_args[0])
                elif isinstance(_args[0], VBase2D):
                    return self.overloaded_constructor_ptrConstLVecBase2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D> '
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

        
        def compareTo(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase2D):
                    return self.overloaded_compareTo_ptrConstLVecBase2d_ptrConstLVecBase2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2D> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase2D):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_compareTo_ptrConstLVecBase2d_ptrConstLVecBase2d_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLVecBase2d_double(_args[0])
                elif isinstance(_args[0], VBase2D):
                    return self.overloaded_assign_ptrLVecBase2d_ptrConstLVecBase2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def __sub__(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded___sub___ptrConstLVecBase2d()
            elif numArgs == 1:
                if isinstance(_args[0], VBase2D):
                    return self.overloaded___sub___ptrConstLVecBase2d_ptrConstLVecBase2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def almostEqual(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase2D):
                    return self.overloaded_almostEqual_ptrConstLVecBase2d_ptrConstLVecBase2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2D> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase2D):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_almostEqual_ptrConstLVecBase2d_ptrConstLVecBase2d_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['VBase2D'] = VBase2D

