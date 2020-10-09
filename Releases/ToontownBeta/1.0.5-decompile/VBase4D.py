# Source Generated with Decompyle++
# File: VBase4D.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Ostream
import TypeHandle
classDefined = 0

def generateClass_VBase4D():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class VBase4D(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3YauU()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase4d(self, copy):
            self.this = libpanda._inPVZN3D5rW(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double(self, fillValue):
            self.this = libpanda._inPVZN3ybJ_(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double_double_double_double(self, x, y, z, w):
            self.this = libpanda._inPVZN3_dNf(x, y, z, w)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN39YOD:
                libpanda._inPVZN39YOD(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3RFQj()
            returnObject = VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN3JLGH()
            returnObject = VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN3LLUj()
            returnObject = VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def unitZ():
            returnValue = libpanda._inPVZN3lLi_()
            returnObject = VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitZ = PandaStatic.PandaStatic(unitZ)
        
        def unitW():
            returnValue = libpanda._inPVZN3OL4q()
            returnObject = VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitW = PandaStatic.PandaStatic(unitW)
        
        def getClassType():
            returnValue = libpanda._inPVZN3_ZvT()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLVecBase4d_ptrConstLVecBase4d(self, copy):
            returnValue = libpanda._inPVZN3XUjS(self.this, copy.this)
            returnObject = VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLVecBase4d_double(self, fillValue):
            returnValue = libpanda._inPVZN3Bm_5(self.this, fillValue)
            returnObject = VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def __getitem__(self, i):
            returnValue = libpanda._inPVZN3uhrl(self.this, i)
            return returnValue

        
        def isNan(self):
            returnValue = libpanda._inPVZN3II3T(self.this)
            return returnValue

        
        def getCell(self, i):
            returnValue = libpanda._inPVZN34EQ5(self.this, i)
            return returnValue

        
        def getX(self):
            returnValue = libpanda._inPVZN3kHwk(self.this)
            return returnValue

        
        def getY(self):
            returnValue = libpanda._inPVZN3kjop(self.this)
            return returnValue

        
        def getZ(self):
            returnValue = libpanda._inPVZN3k_gu(self.this)
            return returnValue

        
        def getW(self):
            returnValue = libpanda._inPVZN3kL4f(self.this)
            return returnValue

        
        def setCell(self, i, value):
            returnValue = libpanda._inPVZN3YZBA(self.this, i, value)
            return returnValue

        
        def setX(self, value):
            returnValue = libpanda._inPVZN3cgFc(self.this, value)
            return returnValue

        
        def setY(self, value):
            returnValue = libpanda._inPVZN3c89g(self.this, value)
            return returnValue

        
        def setZ(self, value):
            returnValue = libpanda._inPVZN3c42l(self.this, value)
            return returnValue

        
        def setW(self, value):
            returnValue = libpanda._inPVZN3cENX(self.this, value)
            return returnValue

        
        def getNumComponents(self):
            returnValue = libpanda._inPVZN3QL3K(self.this)
            return returnValue

        
        def fill(self, fillValue):
            returnValue = libpanda._inPVZN3_0Mg(self.this, fillValue)
            return returnValue

        
        def set(self, x, y, z, w):
            returnValue = libpanda._inPVZN3Wt7O(self.this, x, y, z, w)
            return returnValue

        
        def dot(self, other):
            returnValue = libpanda._inPVZN3O5rF(self.this, other.this)
            return returnValue

        
        def lessThan(self, other):
            returnValue = libpanda._inPVZN3s5P_(self.this, other.this)
            return returnValue

        
        def eq(self, other):
            returnValue = libpanda._inPVZN3XfYT(self.this, other.this)
            return returnValue

        
        def ne(self, other):
            returnValue = libpanda._inPVZN3T_AC(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLVecBase4d_ptrConstLVecBase4d(self, other):
            returnValue = libpanda._inPVZN3tlH_(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLVecBase4d_ptrConstLVecBase4d_double(self, other, threshold):
            returnValue = libpanda._inPVZN3wP_I(self.this, other.this, threshold)
            return returnValue

        
        def overloaded___sub___ptrConstLVecBase4d(self):
            returnValue = libpanda._inPVZN3JMwB(self.this)
            returnObject = VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __add__(self, other):
            returnValue = libpanda._inPVZN3mxQY(self.this, other.this)
            returnObject = VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVecBase4d_ptrConstLVecBase4d(self, other):
            returnValue = libpanda._inPVZN3mBzr(self.this, other.this)
            returnObject = VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN3PYXY(self.this, scalar)
            returnObject = VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3QwNJ(self.this, scalar)
            returnObject = VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __iadd__(self, other):
            returnValue = libpanda._inPVZN3aK3z(self.this, other.this)
            return self

        
        def __isub__(self, other):
            returnValue = libpanda._inPVZN3baYH(self.this, other.this)
            return self

        
        def __imul__(self, scalar):
            returnValue = libpanda._inPVZN3ydXY(self.this, scalar)
            return self

        
        def __idiv__(self, scalar):
            returnValue = libpanda._inPVZN33VMJ(self.this, scalar)
            return self

        
        def overloaded_almostEqual_ptrConstLVecBase4d_ptrConstLVecBase4d_double(self, other, threshold):
            returnValue = libpanda._inPVZN32iLB(self.this, other.this, threshold)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLVecBase4d_ptrConstLVecBase4d(self, other):
            returnValue = libpanda._inPVZN3VCrw(self.this, other.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPVZN3ubda(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_double(_args[0])
                elif isinstance(_args[0], VBase4D):
                    return self.overloaded_constructor_ptrConstLVecBase4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4D> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_constructor_double_double_double_double(_args[0], _args[1], _args[2], _args[3])
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
                if isinstance(_args[0], VBase4D):
                    return self.overloaded_compareTo_ptrConstLVecBase4d_ptrConstLVecBase4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4D> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase4D):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_compareTo_ptrConstLVecBase4d_ptrConstLVecBase4d_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLVecBase4d_double(_args[0])
                elif isinstance(_args[0], VBase4D):
                    return self.overloaded_assign_ptrLVecBase4d_ptrConstLVecBase4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def __sub__(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded___sub___ptrConstLVecBase4d()
            elif numArgs == 1:
                if isinstance(_args[0], VBase4D):
                    return self.overloaded___sub___ptrConstLVecBase4d_ptrConstLVecBase4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def almostEqual(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4D):
                    return self.overloaded_almostEqual_ptrConstLVecBase4d_ptrConstLVecBase4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4D> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase4D):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_almostEqual_ptrConstLVecBase4d_ptrConstLVecBase4d_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['VBase4D'] = VBase4D

