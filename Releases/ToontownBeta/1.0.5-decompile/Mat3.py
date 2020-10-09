# Source Generated with Decompyle++
# File: Mat3.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase3
import VBase2
import Ostream
import TypeHandle
classDefined = 0

def generateClass_Mat3():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Mat3(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3eOQU()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLMatrix3f(self, other):
            self.this = libpanda._inPVZN3ln2u(other.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float_float_float_float_float_float_float(self, e00, e01, e02, e10, e11, e12, e20, e21, e22):
            self.this = libpanda._inPVZN3JN9c(e00, e01, e02, e10, e11, e12, e20, e21, e22)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3lQqE:
                libpanda._inPVZN3lQqE(self.this)
            

        
        def identMat():
            returnValue = libpanda._inPVZN3jWwo()
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        identMat = PandaStatic.PandaStatic(identMat)
        
        def overloaded_translateMat_ptrConstLVecBase2f(trans):
            returnValue = libpanda._inPVZN32yv7(trans.this)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_translateMat_ptrConstLVecBase2f = PandaStatic.PandaStatic(overloaded_translateMat_ptrConstLVecBase2f)
        
        def overloaded_translateMat_float_float(tx, ty):
            returnValue = libpanda._inPVZN3u0HR(tx, ty)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_translateMat_float_float = PandaStatic.PandaStatic(overloaded_translateMat_float_float)
        
        def overloaded_rotateMat_float(angle):
            returnValue = libpanda._inPVZN3ps2A(angle)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMat_float = PandaStatic.PandaStatic(overloaded_rotateMat_float)
        
        def overloaded_scaleMat_ptrConstLVecBase2f(scale):
            returnValue = libpanda._inPVZN3Yf2k(scale.this)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_scaleMat_ptrConstLVecBase2f = PandaStatic.PandaStatic(overloaded_scaleMat_ptrConstLVecBase2f)
        
        def overloaded_scaleMat_float_float(sx, sy):
            returnValue = libpanda._inPVZN3Dkk6(sx, sy)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_scaleMat_float_float = PandaStatic.PandaStatic(overloaded_scaleMat_float_float)
        
        def overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem(angle, axis, cs):
            returnValue = libpanda._inPVZN3s6NZ(angle, axis.this, cs)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem)
        
        def overloaded_rotateMat_float_ptrLVecBase3f(angle, axis):
            returnValue = libpanda._inPVZN3rOsv(angle, axis.this)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMat_float_ptrLVecBase3f = PandaStatic.PandaStatic(overloaded_rotateMat_float_ptrLVecBase3f)
        
        def overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem(angle, axis, cs):
            returnValue = libpanda._inPVZN3L_9G(angle, axis.this, cs)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem)
        
        def overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f(angle, axis):
            returnValue = libpanda._inPVZN3b52Z(angle, axis.this)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f = PandaStatic.PandaStatic(overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f)
        
        def overloaded_scaleMat_ptrConstLVecBase3f(scale):
            returnValue = libpanda._inPVZN3GD5k(scale.this)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_scaleMat_ptrConstLVecBase3f = PandaStatic.PandaStatic(overloaded_scaleMat_ptrConstLVecBase3f)
        
        def overloaded_scaleMat_float_float_float(sx, sy, sz):
            returnValue = libpanda._inPVZN3qUog(sx, sy, sz)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_scaleMat_float_float_float = PandaStatic.PandaStatic(overloaded_scaleMat_float_float_float)
        
        def getClassType():
            returnValue = libpanda._inPVZN3BxnT()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLMatrix3f_ptrConstLMatrix3f(self, other):
            returnValue = libpanda._inPVZN3PgVN(self.this, other.this)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLMatrix3f_float(self, fillValue):
            returnValue = libpanda._inPVZN3Hzp_(self.this, fillValue)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def fill(self, fillValue):
            returnValue = libpanda._inPVZN3Zh0z(self.this, fillValue)
            return returnValue

        
        def set(self, e00, e01, e02, e10, e11, e12, e20, e21, e22):
            returnValue = libpanda._inPVZN3sRrU(self.this, e00, e01, e02, e10, e11, e12, e20, e21, e22)
            return returnValue

        
        def overloaded_setRow_ptrLMatrix3f_int_ptrConstLVecBase3f(self, row, v):
            returnValue = libpanda._inPVZN3yThf(self.this, row, v.this)
            return returnValue

        
        def overloaded_setCol_ptrLMatrix3f_int_ptrConstLVecBase3f(self, col, v):
            returnValue = libpanda._inPVZN3T20m(self.this, col, v.this)
            return returnValue

        
        def overloaded_setRow_ptrLMatrix3f_int_ptrConstLVecBase2f(self, row, v):
            returnValue = libpanda._inPVZN3GTx9(self.this, row, v.this)
            return returnValue

        
        def overloaded_setCol_ptrLMatrix3f_int_ptrConstLVecBase2f(self, col, v):
            returnValue = libpanda._inPVZN3odEF(self.this, col, v.this)
            return returnValue

        
        def overloaded_getRow_ptrConstLMatrix3f_int(self, row):
            returnValue = libpanda._inPVZN3prOZ(self.this, row)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getCol(self, col):
            returnValue = libpanda._inPVZN3_Hig(self.this, col)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getRow2(self, row):
            returnValue = libpanda._inPVZN30ETI(self.this, row)
            returnObject = VBase2.VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getCol2(self, col):
            returnValue = libpanda._inPVZN3PjmP(self.this, col)
            returnObject = VBase2.VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_getRow_ptrConstLMatrix3f_ptrLVecBase3f_int(self, resultVec, row):
            returnValue = libpanda._inPVZN3W5DX(self.this, resultVec.this, row)
            return returnValue

        
        def __call__(self, row, col):
            returnValue = libpanda._inPVZN33fgz(self.this, row, col)
            return returnValue

        
        def isNan(self):
            returnValue = libpanda._inPVZN3KRqT(self.this)
            return returnValue

        
        def getCell(self, row, col):
            returnValue = libpanda._inPVZN3ASay(self.this, row, col)
            return returnValue

        
        def setCell(self, row, col, value):
            returnValue = libpanda._inPVZN3eO_H(self.this, row, col, value)
            return returnValue

        
        def getNumComponents(self):
            returnValue = libpanda._inPVZN3UmUR(self.this)
            return returnValue

        
        def lessThan(self, other):
            returnValue = libpanda._inPVZN3o7zu(self.this, other.this)
            return returnValue

        
        def eq(self, other):
            returnValue = libpanda._inPVZN3Cqr_(self.this, other.this)
            return returnValue

        
        def ne(self, other):
            returnValue = libpanda._inPVZN3C7J3(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLMatrix3f_ptrConstLMatrix3f(self, other):
            returnValue = libpanda._inPVZN3Dm0m(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLMatrix3f_ptrConstLMatrix3f_float(self, other, threshold):
            returnValue = libpanda._inPVZN3qcZj(self.this, other.this, threshold)
            return returnValue

        
        def xform(self, v):
            returnValue = libpanda._inPVZN3ANx6(self.this, v.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def xformPoint(self, v):
            returnValue = libpanda._inPVZN39NCQ(self.this, v.this)
            returnObject = VBase2.VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def xformVec(self, v):
            returnValue = libpanda._inPVZN3BRNJ(self.this, v.this)
            returnObject = VBase2.VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def multiply(self, other1, other2):
            returnValue = libpanda._inPVZN3Lr6_(self.this, other1.this, other2.this)
            return returnValue

        
        def overloaded___mul___ptrConstLMatrix3f_ptrConstLMatrix3f(self, other):
            returnValue = libpanda._inPVZN3IbTp(self.this, other.this)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___mul___ptrConstLMatrix3f_float(self, scalar):
            returnValue = libpanda._inPVZN3VfqV(self.this, scalar)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3FENX(self.this, scalar)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def scaleMultiply(self, scaleVector, otherMat):
            returnValue = libpanda._inPVZN3lQ_I(self.this, scaleVector.this, otherMat.this)
            return returnValue

        
        def __iadd__(self, other):
            returnValue = libpanda._inPVZN39NjA(self.this, other.this)
            return self

        
        def __isub__(self, other):
            returnValue = libpanda._inPVZN3diJB(self.this, other.this)
            return self

        
        def overloaded___imul___ptrLMatrix3f_ptrConstLMatrix3f(self, other):
            returnValue = libpanda._inPVZN3txOA(self.this, other.this)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___imul___ptrLMatrix3f_float(self, scalar):
            returnValue = libpanda._inPVZN3Fh5p(self.this, scalar)
            returnObject = Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def __idiv__(self, scalar):
            returnValue = libpanda._inPVZN3VWbr(self.this, scalar)
            return self

        
        def determinant(self):
            returnValue = libpanda._inPVZN3wNmL(self.this)
            return returnValue

        
        def transposeFrom(self, other):
            returnValue = libpanda._inPVZN3es3s(self.this, other.this)
            return returnValue

        
        def transposeInPlace(self):
            returnValue = libpanda._inPVZN31ojo(self.this)
            return returnValue

        
        def invertFrom(self, other):
            returnValue = libpanda._inPVZN3NkZ2(self.this, other.this)
            return returnValue

        
        def invertInPlace(self):
            returnValue = libpanda._inPVZN3aIMY(self.this)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLMatrix3f_ptrConstLMatrix3f_float(self, other, threshold):
            returnValue = libpanda._inPVZN3csL6(self.this, other.this, threshold)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLMatrix3f_ptrConstLMatrix3f(self, other):
            returnValue = libpanda._inPVZN3ylZV(self.this, other.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPVZN3se1n(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstLMatrix3f_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPVZN3q86e(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstLMatrix3f_ptrOstream(self, out):
            returnValue = libpanda._inPVZN3mTWo(self.this, out.this)
            return returnValue

        
        def rotateMat(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return Mat3.overloaded_rotateMat_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        return Mat3.overloaded_rotateMat_float_ptrLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        if isinstance(_args[2], types.IntType):
                            return Mat3.overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

        rotateMat = PandaStatic.PandaStatic(rotateMat)
        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], Mat3):
                    return self.overloaded_constructor_ptrConstLMatrix3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat3> '
            elif numArgs == 9:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                    if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                        if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                            if isinstance(_args[7], types.FloatType) or isinstance(_args[7], types.IntType):
                                                if isinstance(_args[8], types.FloatType) or isinstance(_args[8], types.IntType):
                                                    return self.overloaded_constructor_float_float_float_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8])
                                                else:
                                                    raise TypeError, 'Invalid argument 8, expected one of: <types.FloatType> '
                                            else:
                                                raise TypeError, 'Invalid argument 7, expected one of: <types.FloatType> '
                                        else:
                                            raise TypeError, 'Invalid argument 6, expected one of: <types.FloatType> '
                                    else:
                                        raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 9 '

        
        def translateMat(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase2.VBase2):
                    return Mat3.overloaded_translateMat_ptrConstLVecBase2f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2.VBase2> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return Mat3.overloaded_translateMat_float_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        translateMat = PandaStatic.PandaStatic(translateMat)
        
        def rotateMatNormaxis(*_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        return Mat3.overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        if isinstance(_args[2], types.IntType):
                            return Mat3.overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

        rotateMatNormaxis = PandaStatic.PandaStatic(rotateMatNormaxis)
        
        def scaleMat(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3.VBase3):
                    return Mat3.overloaded_scaleMat_ptrConstLVecBase3f(_args[0])
                elif isinstance(_args[0], VBase2.VBase2):
                    return Mat3.overloaded_scaleMat_ptrConstLVecBase2f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> <VBase2.VBase2> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return Mat3.overloaded_scaleMat_float_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return Mat3.overloaded_scaleMat_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

        scaleMat = PandaStatic.PandaStatic(scaleMat)
        
        def getRow(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_getRow_ptrConstLMatrix3f_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase3.VBase3):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_getRow_ptrConstLMatrix3f_ptrLVecBase3f_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLMatrix3f_float(_args[0])
                elif isinstance(_args[0], Mat3):
                    return self.overloaded_assign_ptrLMatrix3f_ptrConstLMatrix3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def __imul__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded___imul___ptrLMatrix3f_float(_args[0])
                elif isinstance(_args[0], Mat3):
                    return self.overloaded___imul___ptrLMatrix3f_ptrConstLMatrix3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def setRow(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_setRow_ptrLMatrix3f_int_ptrConstLVecBase3f(_args[0], _args[1])
                    elif isinstance(_args[1], VBase2.VBase2):
                        return self.overloaded_setRow_ptrLMatrix3f_int_ptrConstLVecBase2f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> <VBase2.VBase2> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

        
        def setCol(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_setCol_ptrLMatrix3f_int_ptrConstLVecBase3f(_args[0], _args[1])
                    elif isinstance(_args[1], VBase2.VBase2):
                        return self.overloaded_setCol_ptrLMatrix3f_int_ptrConstLVecBase2f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> <VBase2.VBase2> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

        
        def compareTo(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat3):
                    return self.overloaded_compareTo_ptrConstLMatrix3f_ptrConstLMatrix3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat3> '
            elif numArgs == 2:
                if isinstance(_args[0], Mat3):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_compareTo_ptrConstLMatrix3f_ptrConstLMatrix3f_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def __mul__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded___mul___ptrConstLMatrix3f_float(_args[0])
                elif isinstance(_args[0], Mat3):
                    return self.overloaded___mul___ptrConstLMatrix3f_ptrConstLMatrix3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def almostEqual(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat3):
                    return self.overloaded_almostEqual_ptrConstLMatrix3f_ptrConstLMatrix3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat3> '
            elif numArgs == 2:
                if isinstance(_args[0], Mat3):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_almostEqual_ptrConstLMatrix3f_ptrConstLMatrix3f_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstLMatrix3f_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstLMatrix3f_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['Mat3'] = Mat3

