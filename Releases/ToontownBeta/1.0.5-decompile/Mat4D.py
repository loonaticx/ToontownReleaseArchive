# Source Generated with Decompyle++
# File: Mat4D.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Mat3D
import VBase3D
import VBase4D
import Ostream
import TypeHandle
classDefined = 0

def generateClass_Mat4D():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Mat4D(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3OFy_()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLMatrix4d(self, other):
            self.this = libpanda._inPVZN3ioT1(other.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double_double_double_double_double_double_double_double_double_double_double_double_double_double_double_double(self, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33):
            self.this = libpanda._inPVZN3E5ZS(e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLMatrix3d(self, upper3):
            self.this = libpanda._inPVZN3KsTZ(upper3.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLMatrix3d_ptrConstLVecBase3d(self, upper3, trans):
            self.this = libpanda._inPVZN3rQyB(upper3.this, trans.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3rvmH:
                libpanda._inPVZN3rvmH(self.this)
            

        
        def identMat():
            returnValue = libpanda._inPVZN354TM()
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        identMat = PandaStatic.PandaStatic(identMat)
        
        def overloaded_translateMat_ptrConstLVecBase3d(trans):
            returnValue = libpanda._inPVZN3LdJX(trans.this)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_translateMat_ptrConstLVecBase3d = PandaStatic.PandaStatic(overloaded_translateMat_ptrConstLVecBase3d)
        
        def overloaded_translateMat_double_double_double(tx, ty, tz):
            returnValue = libpanda._inPVZN3m5Au(tx, ty, tz)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_translateMat_double_double_double = PandaStatic.PandaStatic(overloaded_translateMat_double_double_double)
        
        def overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem(angle, axis, cs):
            returnValue = libpanda._inPVZN3U_kA(angle, axis.this, cs)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem)
        
        def overloaded_rotateMat_double_ptrLVecBase3d(angle, axis):
            returnValue = libpanda._inPVZN3r0wN(angle, axis.this)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMat_double_ptrLVecBase3d = PandaStatic.PandaStatic(overloaded_rotateMat_double_ptrLVecBase3d)
        
        def overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem(angle, axis, cs):
            returnValue = libpanda._inPVZN32b_S(angle, axis.this, cs)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem)
        
        def overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d(angle, axis):
            returnValue = libpanda._inPVZN3Rfts(angle, axis.this)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d = PandaStatic.PandaStatic(overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d)
        
        def overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d___enum__CoordinateSystem(angle, axis, resultMat, cs):
            returnValue = libpanda._inPVZN30Tln(angle, axis.this, resultMat.this, cs)
            return returnValue

        overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d___enum__CoordinateSystem)
        
        def overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d(angle, axis, resultMat):
            returnValue = libpanda._inPVZN3nUTM(angle, axis.this, resultMat.this)
            return returnValue

        overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d = PandaStatic.PandaStatic(overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d)
        
        def overloaded_scaleMat_ptrConstLVecBase3d(scale):
            returnValue = libpanda._inPVZN3wWAG(scale.this)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_scaleMat_ptrConstLVecBase3d = PandaStatic.PandaStatic(overloaded_scaleMat_ptrConstLVecBase3d)
        
        def overloaded_scaleMat_double_double_double(sx, sy, sz):
            returnValue = libpanda._inPVZN3QNa0(sx, sy, sz)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_scaleMat_double_double_double = PandaStatic.PandaStatic(overloaded_scaleMat_double_double_double)
        
        def overloaded_scaleMat_double(scale):
            returnValue = libpanda._inPVZN3AW5Q(scale)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_scaleMat_double = PandaStatic.PandaStatic(overloaded_scaleMat_double)
        
        def yToZUpMat():
            returnValue = libpanda._inPVZN3FiyP()
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        yToZUpMat = PandaStatic.PandaStatic(yToZUpMat)
        
        def zToYUpMat():
            returnValue = libpanda._inPVZN3FgWN()
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zToYUpMat = PandaStatic.PandaStatic(zToYUpMat)
        
        def convertMat(_from, to):
            returnValue = libpanda._inPVZN3yoYN(_from, to)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        convertMat = PandaStatic.PandaStatic(convertMat)
        
        def getClassType():
            returnValue = libpanda._inPVZN3gRM3()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLMatrix4d_ptrConstLMatrix4d(self, other):
            returnValue = libpanda._inPVZN3Ivfu(self.this, other.this)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLMatrix4d_double(self, fillValue):
            returnValue = libpanda._inPVZN36rXw(self.this, fillValue)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def fill(self, fillValue):
            returnValue = libpanda._inPVZN3mGn9(self.this, fillValue)
            return returnValue

        
        def set(self, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33):
            returnValue = libpanda._inPVZN39SVz(self.this, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33)
            return returnValue

        
        def setUpper3(self, upper3):
            returnValue = libpanda._inPVZN3xjsI(self.this, upper3.this)
            return returnValue

        
        def getUpper3(self):
            returnValue = libpanda._inPVZN3VzBN(self.this)
            returnObject = Mat3D.Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_setRow_ptrLMatrix4d_int_ptrConstLVecBase4d(self, row, v):
            returnValue = libpanda._inPVZN3gd10(self.this, row, v.this)
            return returnValue

        
        def overloaded_setCol_ptrLMatrix4d_int_ptrConstLVecBase4d(self, col, v):
            returnValue = libpanda._inPVZN3BAH8(self.this, col, v.this)
            return returnValue

        
        def overloaded_setRow_ptrLMatrix4d_int_ptrConstLVecBase3d(self, row, v):
            returnValue = libpanda._inPVZN3xdFT(self.this, row, v.this)
            return returnValue

        
        def overloaded_setCol_ptrLMatrix4d_int_ptrConstLVecBase3d(self, col, v):
            returnValue = libpanda._inPVZN3WAXa(self.this, col, v.this)
            return returnValue

        
        def overloaded_getRow_ptrConstLMatrix4d_int(self, row):
            returnValue = libpanda._inPVZN3iKy8(self.this, row)
            returnObject = VBase4D.VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getCol(self, col):
            returnValue = libpanda._inPVZN3kpFE(self.this, col)
            returnObject = VBase4D.VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_getRow3_ptrConstLMatrix4d_int(self, row):
            returnValue = libpanda._inPVZN3Jl2y(self.this, row)
            returnObject = VBase3D.VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_getRow_ptrConstLMatrix4d_ptrLVecBase4d_int(self, resultVec, row):
            returnValue = libpanda._inPVZN3ILfz(self.this, resultVec.this, row)
            return returnValue

        
        def overloaded_getRow3_ptrConstLMatrix4d_ptrLVecBase3d_int(self, resultVec, row):
            returnValue = libpanda._inPVZN3XtWu(self.this, resultVec.this, row)
            return returnValue

        
        def getCol3(self, col):
            returnValue = libpanda._inPVZN34DK6(self.this, col)
            returnObject = VBase3D.VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __call__(self, row, col):
            returnValue = libpanda._inPVZN3Z_EX(self.this, row, col)
            return returnValue

        
        def isNan(self):
            returnValue = libpanda._inPVZN3nxM3(self.this)
            return returnValue

        
        def getCell(self, row, col):
            returnValue = libpanda._inPVZN3m18V(self.this, row, col)
            return returnValue

        
        def setCell(self, row, col, value):
            returnValue = libpanda._inPVZN3RQG1(self.this, row, col, value)
            return returnValue

        
        def getNumComponents(self):
            returnValue = libpanda._inPVZN3pJ40(self.this)
            return returnValue

        
        def lessThan(self, other):
            returnValue = libpanda._inPVZN3QN_P(self.this, other.this)
            return returnValue

        
        def eq(self, other):
            returnValue = libpanda._inPVZN3JSXW(self.this, other.this)
            return returnValue

        
        def ne(self, other):
            returnValue = libpanda._inPVZN3JpzN(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLMatrix4d_ptrConstLMatrix4d(self, other):
            returnValue = libpanda._inPVZN3TN_H(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLMatrix4d_ptrConstLMatrix4d_double(self, other, threshold):
            returnValue = libpanda._inPVZN3egtQ(self.this, other.this, threshold)
            return returnValue

        
        def xform(self, v):
            returnValue = libpanda._inPVZN3HP43(self.this, v.this)
            returnObject = VBase4D.VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def xformPoint(self, v):
            returnValue = libpanda._inPVZN3MPJX(self.this, v.this)
            returnObject = VBase3D.VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def xformVec(self, v):
            returnValue = libpanda._inPVZN38bVq(self.this, v.this)
            returnObject = VBase3D.VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def multiply(self, other1, other2):
            returnValue = libpanda._inPVZN3NWEL(self.this, other1.this, other2.this)
            return returnValue

        
        def scaleMultiply(self, scaleVector, otherMat):
            returnValue = libpanda._inPVZN3VXjA(self.this, scaleVector.this, otherMat.this)
            return returnValue

        
        def overloaded___mul___ptrConstLMatrix4d_ptrConstLMatrix4d(self, other):
            returnValue = libpanda._inPVZN3wtdK(self.this, other.this)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___mul___ptrConstLMatrix4d_double(self, scalar):
            returnValue = libpanda._inPVZN32ZUF(self.this, scalar)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3Gi1G(self.this, scalar)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __iadd__(self, other):
            returnValue = libpanda._inPVZN31JOX(self.this, other.this)
            return self

        
        def __isub__(self, other):
            returnValue = libpanda._inPVZN3V90X(self.this, other.this)
            return self

        
        def overloaded___imul___ptrLMatrix4d_ptrConstLMatrix4d(self, other):
            returnValue = libpanda._inPVZN3Fo5W(self.this, other.this)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___imul___ptrLMatrix4d_double(self, scalar):
            returnValue = libpanda._inPVZN3PuUT(self.this, scalar)
            returnObject = Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def __idiv__(self, scalar):
            returnValue = libpanda._inPVZN3fX4U(self.this, scalar)
            return self

        
        def transposeFrom(self, other):
            returnValue = libpanda._inPVZN3hyQI(self.this, other.this)
            return returnValue

        
        def transposeInPlace(self):
            returnValue = libpanda._inPVZN3bJHM(self.this)
            return returnValue

        
        def invertFrom(self, other):
            returnValue = libpanda._inPVZN3GIEN(self.this, other.this)
            return returnValue

        
        def invertAffineFrom(self, other):
            returnValue = libpanda._inPVZN3ZQnD(self.this, other.this)
            return returnValue

        
        def invertInPlace(self):
            returnValue = libpanda._inPVZN3Bov7(self.this)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLMatrix4d_ptrConstLMatrix4d_double(self, other, threshold):
            returnValue = libpanda._inPVZN3hoXn(self.this, other.this, threshold)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLMatrix4d_ptrConstLMatrix4d(self, other):
            returnValue = libpanda._inPVZN3jigc(self.this, other.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPVZN3W_YL(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstLMatrix4d_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPVZN3QbeC(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstLMatrix4d_ptrOstream(self, out):
            returnValue = libpanda._inPVZN3Qy5L(self.this, out.this)
            return returnValue

        
        def rotateMat(*_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3D.VBase3D):
                        return Mat4D.overloaded_rotateMat_double_ptrLVecBase3d(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3D.VBase3D):
                        if isinstance(_args[2], types.IntType):
                            return Mat4D.overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

        rotateMat = PandaStatic.PandaStatic(rotateMat)
        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], Mat4D):
                    return self.overloaded_constructor_ptrConstLMatrix4d(_args[0])
                elif isinstance(_args[0], Mat3D.Mat3D):
                    return self.overloaded_constructor_ptrConstLMatrix3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4D> <Mat3D.Mat3D> '
            elif numArgs == 2:
                if isinstance(_args[0], Mat3D.Mat3D):
                    if isinstance(_args[1], VBase3D.VBase3D):
                        return self.overloaded_constructor_ptrConstLMatrix3d_ptrConstLVecBase3d(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat3D.Mat3D> '
            elif numArgs == 16:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                    if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                        if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                            if isinstance(_args[7], types.FloatType) or isinstance(_args[7], types.IntType):
                                                if isinstance(_args[8], types.FloatType) or isinstance(_args[8], types.IntType):
                                                    if isinstance(_args[9], types.FloatType) or isinstance(_args[9], types.IntType):
                                                        if isinstance(_args[10], types.FloatType) or isinstance(_args[10], types.IntType):
                                                            if isinstance(_args[11], types.FloatType) or isinstance(_args[11], types.IntType):
                                                                if isinstance(_args[12], types.FloatType) or isinstance(_args[12], types.IntType):
                                                                    if isinstance(_args[13], types.FloatType) or isinstance(_args[13], types.IntType):
                                                                        if isinstance(_args[14], types.FloatType) or isinstance(_args[14], types.IntType):
                                                                            if isinstance(_args[15], types.FloatType) or isinstance(_args[15], types.IntType):
                                                                                return self.overloaded_constructor_double_double_double_double_double_double_double_double_double_double_double_double_double_double_double_double(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8], _args[9], _args[10], _args[11], _args[12], _args[13], _args[14], _args[15])
                                                                            else:
                                                                                raise TypeError, 'Invalid argument 15, expected one of: <types.FloatType> '
                                                                        else:
                                                                            raise TypeError, 'Invalid argument 14, expected one of: <types.FloatType> '
                                                                    else:
                                                                        raise TypeError, 'Invalid argument 13, expected one of: <types.FloatType> '
                                                                else:
                                                                    raise TypeError, 'Invalid argument 12, expected one of: <types.FloatType> '
                                                            else:
                                                                raise TypeError, 'Invalid argument 11, expected one of: <types.FloatType> '
                                                        else:
                                                            raise TypeError, 'Invalid argument 10, expected one of: <types.FloatType> '
                                                    else:
                                                        raise TypeError, 'Invalid argument 9, expected one of: <types.FloatType> '
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
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 16 '

        
        def translateMat(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3D.VBase3D):
                    return Mat4D.overloaded_translateMat_ptrConstLVecBase3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return Mat4D.overloaded_translateMat_double_double_double(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

        translateMat = PandaStatic.PandaStatic(translateMat)
        
        def rotateMatNormaxis(*_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3D.VBase3D):
                        return Mat4D.overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3D.VBase3D):
                        if isinstance(_args[2], types.IntType):
                            return Mat4D.overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                        elif isinstance(_args[2], Mat4D):
                            return Mat4D.overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Mat4D> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3D.VBase3D):
                        if isinstance(_args[2], Mat4D):
                            if isinstance(_args[3], types.IntType):
                                return Mat4D.overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Mat4D> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '

        rotateMatNormaxis = PandaStatic.PandaStatic(rotateMatNormaxis)
        
        def scaleMat(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return Mat4D.overloaded_scaleMat_double(_args[0])
                elif isinstance(_args[0], VBase3D.VBase3D):
                    return Mat4D.overloaded_scaleMat_ptrConstLVecBase3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D.VBase3D> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return Mat4D.overloaded_scaleMat_double_double_double(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

        scaleMat = PandaStatic.PandaStatic(scaleMat)
        
        def getRow(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_getRow_ptrConstLMatrix4d_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase4D.VBase4D):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_getRow_ptrConstLMatrix4d_ptrLVecBase4d_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4D.VBase4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLMatrix4d_double(_args[0])
                elif isinstance(_args[0], Mat4D):
                    return self.overloaded_assign_ptrLMatrix4d_ptrConstLMatrix4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def __imul__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded___imul___ptrLMatrix4d_double(_args[0])
                elif isinstance(_args[0], Mat4D):
                    return self.overloaded___imul___ptrLMatrix4d_ptrConstLMatrix4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def setRow(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase4D.VBase4D):
                        return self.overloaded_setRow_ptrLMatrix4d_int_ptrConstLVecBase4d(_args[0], _args[1])
                    elif isinstance(_args[1], VBase3D.VBase3D):
                        return self.overloaded_setRow_ptrLMatrix4d_int_ptrConstLVecBase3d(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase4D.VBase4D> <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

        
        def setCol(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase4D.VBase4D):
                        return self.overloaded_setCol_ptrLMatrix4d_int_ptrConstLVecBase4d(_args[0], _args[1])
                    elif isinstance(_args[1], VBase3D.VBase3D):
                        return self.overloaded_setCol_ptrLMatrix4d_int_ptrConstLVecBase3d(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase4D.VBase4D> <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

        
        def compareTo(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat4D):
                    return self.overloaded_compareTo_ptrConstLMatrix4d_ptrConstLMatrix4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4D> '
            elif numArgs == 2:
                if isinstance(_args[0], Mat4D):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_compareTo_ptrConstLMatrix4d_ptrConstLMatrix4d_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def __mul__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded___mul___ptrConstLMatrix4d_double(_args[0])
                elif isinstance(_args[0], Mat4D):
                    return self.overloaded___mul___ptrConstLMatrix4d_ptrConstLMatrix4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def getRow3(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_getRow3_ptrConstLMatrix4d_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase3D.VBase3D):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_getRow3_ptrConstLMatrix4d_ptrLVecBase3d_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def almostEqual(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat4D):
                    return self.overloaded_almostEqual_ptrConstLMatrix4d_ptrConstLMatrix4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4D> '
            elif numArgs == 2:
                if isinstance(_args[0], Mat4D):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_almostEqual_ptrConstLMatrix4d_ptrConstLMatrix4d_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstLMatrix4d_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstLMatrix4d_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['Mat4D'] = Mat4D

