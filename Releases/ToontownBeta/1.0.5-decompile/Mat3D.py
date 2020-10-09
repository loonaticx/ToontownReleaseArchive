# Source Generated with Decompyle++
# File: Mat3D.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase3D
import VBase2D
import Ostream
import TypeHandle
classDefined = 0

def generateClass_Mat3D():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Mat3D(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3AktQ()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLMatrix3d(self, other):
            self.this = libpanda._inPVZN3ZKQr(other.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double_double_double_double_double_double_double_double_double(self, e00, e01, e02, e10, e11, e12, e20, e21, e22):
            self.this = libpanda._inPVZN3uCQv(e00, e01, e02, e10, e11, e12, e20, e21, e22)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3ONjA:
                libpanda._inPVZN3ONjA(self.this)
            

        
        def identMat():
            returnValue = libpanda._inPVZN38YQl()
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        identMat = PandaStatic.PandaStatic(identMat)
        
        def overloaded_translateMat_ptrConstLVecBase2d(trans):
            returnValue = libpanda._inPVZN3VDH4(trans.this)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_translateMat_ptrConstLVecBase2d = PandaStatic.PandaStatic(overloaded_translateMat_ptrConstLVecBase2d)
        
        def overloaded_translateMat_double_double(tx, ty):
            returnValue = libpanda._inPVZN3S8s7(tx, ty)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_translateMat_double_double = PandaStatic.PandaStatic(overloaded_translateMat_double_double)
        
        def overloaded_rotateMat_double(angle):
            returnValue = libpanda._inPVZN36TiL(angle)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMat_double = PandaStatic.PandaStatic(overloaded_rotateMat_double)
        
        def overloaded_scaleMat_ptrConstLVecBase2d(scale):
            returnValue = libpanda._inPVZN3dK6e(scale.this)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_scaleMat_ptrConstLVecBase2d = PandaStatic.PandaStatic(overloaded_scaleMat_ptrConstLVecBase2d)
        
        def overloaded_scaleMat_double_double(sx, sy):
            returnValue = libpanda._inPVZN3DytY(sx, sy)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_scaleMat_double_double = PandaStatic.PandaStatic(overloaded_scaleMat_double_double)
        
        def overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem(angle, axis, cs):
            returnValue = libpanda._inPVZN3TfgZ(angle, axis.this, cs)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem)
        
        def overloaded_rotateMat_double_ptrLVecBase3d(angle, axis):
            returnValue = libpanda._inPVZN3sUtm(angle, axis.this)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMat_double_ptrLVecBase3d = PandaStatic.PandaStatic(overloaded_rotateMat_double_ptrLVecBase3d)
        
        def overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem(angle, axis, cs):
            returnValue = libpanda._inPVZN3r76r(angle, axis.this, cs)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem)
        
        def overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d(angle, axis):
            returnValue = libpanda._inPVZN3R_qF(angle, axis.this)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d = PandaStatic.PandaStatic(overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d)
        
        def overloaded_scaleMat_ptrConstLVecBase3d(scale):
            returnValue = libpanda._inPVZN3v28e(scale.this)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_scaleMat_ptrConstLVecBase3d = PandaStatic.PandaStatic(overloaded_scaleMat_ptrConstLVecBase3d)
        
        def overloaded_scaleMat_double_double_double(sx, sy, sz):
            returnValue = libpanda._inPVZN3QtVN(sx, sy, sz)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_scaleMat_double_double_double = PandaStatic.PandaStatic(overloaded_scaleMat_double_double_double)
        
        def getClassType():
            returnValue = libpanda._inPVZN3gxHQ()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLMatrix3d_ptrConstLMatrix3d(self, other):
            returnValue = libpanda._inPVZN32qZH(self.this, other.this)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLMatrix3d_double(self, fillValue):
            returnValue = libpanda._inPVZN36LVJ(self.this, fillValue)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def fill(self, fillValue):
            returnValue = libpanda._inPVZN3mmiW(self.this, fillValue)
            return returnValue

        
        def set(self, e00, e01, e02, e10, e11, e12, e20, e21, e22):
            returnValue = libpanda._inPVZN3RsjO(self.this, e00, e01, e02, e10, e11, e12, e20, e21, e22)
            return returnValue

        
        def overloaded_setRow_ptrLMatrix3d_int_ptrConstLVecBase3d(self, row, v):
            returnValue = libpanda._inPVZN309Bs(self.this, row, v.this)
            return returnValue

        
        def overloaded_setCol_ptrLMatrix3d_int_ptrConstLVecBase3d(self, col, v):
            returnValue = libpanda._inPVZN3VgVz(self.this, col, v.this)
            return returnValue

        
        def overloaded_setRow_ptrLMatrix3d_int_ptrConstLVecBase2d(self, row, v):
            returnValue = libpanda._inPVZN3F9RK(self.this, row, v.this)
            return returnValue

        
        def overloaded_setCol_ptrLMatrix3d_int_ptrConstLVecBase2d(self, col, v):
            returnValue = libpanda._inPVZN3aflR(self.this, col, v.this)
            return returnValue

        
        def overloaded_getRow_ptrConstLMatrix3d_int(self, row):
            returnValue = libpanda._inPVZN3iquV(self.this, row)
            returnObject = VBase3D.VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getCol(self, col):
            returnValue = libpanda._inPVZN3jJCd(self.this, col)
            returnObject = VBase3D.VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getRow2(self, row):
            returnValue = libpanda._inPVZN37DzE(self.this, row)
            returnObject = VBase2D.VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getCol2(self, col):
            returnValue = libpanda._inPVZN3qkGM(self.this, col)
            returnObject = VBase2D.VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_getRow_ptrConstLMatrix3d_ptrLVecBase3d_int(self, resultVec, row):
            returnValue = libpanda._inPVZN3_qjb(self.this, resultVec.this, row)
            return returnValue

        
        def __call__(self, row, col):
            returnValue = libpanda._inPVZN3geAw(self.this, row, col)
            return returnValue

        
        def isNan(self):
            returnValue = libpanda._inPVZN3nRKQ(self.this)
            return returnValue

        
        def getCell(self, row, col):
            returnValue = libpanda._inPVZN3nV6u(self.this, row, col)
            return returnValue

        
        def setCell(self, row, col, value):
            returnValue = libpanda._inPVZN3RwBO(self.this, row, col, value)
            return returnValue

        
        def getNumComponents(self):
            returnValue = libpanda._inPVZN3pp0N(self.this)
            return returnValue

        
        def lessThan(self, other):
            returnValue = libpanda._inPVZN3_I4o(self.this, other.this)
            return returnValue

        
        def eq(self, other):
            returnValue = libpanda._inPVZN3KrEu(self.this, other.this)
            return returnValue

        
        def ne(self, other):
            returnValue = libpanda._inPVZN3K6il(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLMatrix3d_ptrConstLMatrix3d(self, other):
            returnValue = libpanda._inPVZN3mY4g(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLMatrix3d_ptrConstLMatrix3d_double(self, other, threshold):
            returnValue = libpanda._inPVZN3L1np(self.this, other.this, threshold)
            return returnValue

        
        def xform(self, v):
            returnValue = libpanda._inPVZN3nqNQ(self.this, v.this)
            returnObject = VBase3D.VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def xformPoint(self, v):
            returnValue = libpanda._inPVZN3LPCJ(self.this, v.this)
            returnObject = VBase2D.VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def xformVec(self, v):
            returnValue = libpanda._inPVZN3KgPD(self.this, v.this)
            returnObject = VBase2D.VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def multiply(self, other1, other2):
            returnValue = libpanda._inPVZN3STHD(self.this, other1.this, other2.this)
            return returnValue

        
        def overloaded___mul___ptrConstLMatrix3d_ptrConstLMatrix3d(self, other):
            returnValue = libpanda._inPVZN3fpXj(self.this, other.this)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___mul___ptrConstLMatrix3d_double(self, scalar):
            returnValue = libpanda._inPVZN335Qe(self.this, scalar)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3HCyf(self.this, scalar)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def scaleMultiply(self, scaleVector, otherMat):
            returnValue = libpanda._inPVZN3WftP(self.this, scaleVector.this, otherMat.this)
            return returnValue

        
        def __iadd__(self, other):
            returnValue = libpanda._inPVZN34O8u(self.this, other.this)
            return self

        
        def __isub__(self, other):
            returnValue = libpanda._inPVZN3Yiiv(self.this, other.this)
            return self

        
        def overloaded___imul___ptrLMatrix3d_ptrConstLMatrix3d(self, other):
            returnValue = libpanda._inPVZN3Ixnu(self.this, other.this)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___imul___ptrLMatrix3d_double(self, scalar):
            returnValue = libpanda._inPVZN3QORs(self.this, scalar)
            returnObject = Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def __idiv__(self, scalar):
            returnValue = libpanda._inPVZN3g3yt(self.this, scalar)
            return self

        
        def determinant(self):
            returnValue = libpanda._inPVZN3lMGI(self.this)
            return returnValue

        
        def transposeFrom(self, other):
            returnValue = libpanda._inPVZN3ToNp(self.this, other.this)
            return returnValue

        
        def transposeInPlace(self):
            returnValue = libpanda._inPVZN3epDl(self.this)
            return returnValue

        
        def invertFrom(self, other):
            returnValue = libpanda._inPVZN3Fjyk(self.this, other.this)
            return returnValue

        
        def invertInPlace(self):
            returnValue = libpanda._inPVZN3BIsU(self.this)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLMatrix3d_ptrConstLMatrix3d_double(self, other, threshold):
            returnValue = libpanda._inPVZN3ioQZ(self.this, other.this, threshold)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLMatrix3d_ptrConstLMatrix3d(self, other):
            returnValue = libpanda._inPVZN3kiZO(self.this, other.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPVZN3VeVk(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstLMatrix3d_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPVZN3B7ab(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstLMatrix3d_ptrOstream(self, out):
            returnValue = libpanda._inPVZN3NS2k(self.this, out.this)
            return returnValue

        
        def rotateMat(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return Mat3D.overloaded_rotateMat_double(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3D.VBase3D):
                        return Mat3D.overloaded_rotateMat_double_ptrLVecBase3d(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3D.VBase3D):
                        if isinstance(_args[2], types.IntType):
                            return Mat3D.overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
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
                if isinstance(_args[0], Mat3D):
                    return self.overloaded_constructor_ptrConstLMatrix3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat3D> '
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
                                                    return self.overloaded_constructor_double_double_double_double_double_double_double_double_double(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8])
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
                if isinstance(_args[0], VBase2D.VBase2D):
                    return Mat3D.overloaded_translateMat_ptrConstLVecBase2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2D.VBase2D> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return Mat3D.overloaded_translateMat_double_double(_args[0], _args[1])
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
                    if isinstance(_args[1], VBase3D.VBase3D):
                        return Mat3D.overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3D.VBase3D):
                        if isinstance(_args[2], types.IntType):
                            return Mat3D.overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

        rotateMatNormaxis = PandaStatic.PandaStatic(rotateMatNormaxis)
        
        def scaleMat(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3D.VBase3D):
                    return Mat3D.overloaded_scaleMat_ptrConstLVecBase3d(_args[0])
                elif isinstance(_args[0], VBase2D.VBase2D):
                    return Mat3D.overloaded_scaleMat_ptrConstLVecBase2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> <VBase2D.VBase2D> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return Mat3D.overloaded_scaleMat_double_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return Mat3D.overloaded_scaleMat_double_double_double(_args[0], _args[1], _args[2])
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
                    return self.overloaded_getRow_ptrConstLMatrix3d_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase3D.VBase3D):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_getRow_ptrConstLMatrix3d_ptrLVecBase3d_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLMatrix3d_double(_args[0])
                elif isinstance(_args[0], Mat3D):
                    return self.overloaded_assign_ptrLMatrix3d_ptrConstLMatrix3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def __imul__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded___imul___ptrLMatrix3d_double(_args[0])
                elif isinstance(_args[0], Mat3D):
                    return self.overloaded___imul___ptrLMatrix3d_ptrConstLMatrix3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def setRow(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3D.VBase3D):
                        return self.overloaded_setRow_ptrLMatrix3d_int_ptrConstLVecBase3d(_args[0], _args[1])
                    elif isinstance(_args[1], VBase2D.VBase2D):
                        return self.overloaded_setRow_ptrLMatrix3d_int_ptrConstLVecBase2d(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> <VBase2D.VBase2D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

        
        def setCol(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3D.VBase3D):
                        return self.overloaded_setCol_ptrLMatrix3d_int_ptrConstLVecBase3d(_args[0], _args[1])
                    elif isinstance(_args[1], VBase2D.VBase2D):
                        return self.overloaded_setCol_ptrLMatrix3d_int_ptrConstLVecBase2d(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> <VBase2D.VBase2D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

        
        def compareTo(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat3D):
                    return self.overloaded_compareTo_ptrConstLMatrix3d_ptrConstLMatrix3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat3D> '
            elif numArgs == 2:
                if isinstance(_args[0], Mat3D):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_compareTo_ptrConstLMatrix3d_ptrConstLMatrix3d_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def __mul__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded___mul___ptrConstLMatrix3d_double(_args[0])
                elif isinstance(_args[0], Mat3D):
                    return self.overloaded___mul___ptrConstLMatrix3d_ptrConstLMatrix3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def almostEqual(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat3D):
                    return self.overloaded_almostEqual_ptrConstLMatrix3d_ptrConstLMatrix3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat3D> '
            elif numArgs == 2:
                if isinstance(_args[0], Mat3D):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_almostEqual_ptrConstLMatrix3d_ptrConstLMatrix3d_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstLMatrix3d_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstLMatrix3d_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['Mat3D'] = Mat3D

