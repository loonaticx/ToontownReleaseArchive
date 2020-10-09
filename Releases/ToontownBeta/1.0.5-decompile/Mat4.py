# Source Generated with Decompyle++
# File: Mat4.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Mat3
import VBase3
import VBase4
import Ostream
import TypeHandle
classDefined = 0

def generateClass_Mat4():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Mat4(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3tvSC()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLMatrix4f(self, other):
            self.this = libpanda._inPVZN3QR64(other.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float(self, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33):
            self.this = libpanda._inPVZN3d5iq(e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLMatrix3f(self, upper3):
            self.this = libpanda._inPVZN3YG6c(upper3.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLMatrix3f_ptrConstLVecBase3f(self, upper3, trans):
            self.this = libpanda._inPVZN3zZ09(upper3.this, trans.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN30zvL:
                libpanda._inPVZN30zvL(self.this)
            

        
        def identMat():
            returnValue = libpanda._inPVZN3k2zP()
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        identMat = PandaStatic.PandaStatic(identMat)
        
        def overloaded_translateMat_ptrConstLVecBase3f(trans):
            returnValue = libpanda._inPVZN3cM0a(trans.this)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_translateMat_ptrConstLVecBase3f = PandaStatic.PandaStatic(overloaded_translateMat_ptrConstLVecBase3f)
        
        def overloaded_translateMat_float_float_float(tx, ty, tz):
            returnValue = libpanda._inPVZN3JXiS(tx, ty, tz)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_translateMat_float_float_float = PandaStatic.PandaStatic(overloaded_translateMat_float_float_float)
        
        def overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem(angle, axis, cs):
            returnValue = libpanda._inPVZN31aQA(angle, axis.this, cs)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem)
        
        def overloaded_rotateMat_float_ptrLVecBase3f(angle, axis):
            returnValue = libpanda._inPVZN3suuW(angle, axis.this)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMat_float_ptrLVecBase3f = PandaStatic.PandaStatic(overloaded_rotateMat_float_ptrLVecBase3f)
        
        def overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem(angle, axis, cs):
            returnValue = libpanda._inPVZN3LfBu(angle, axis.this, cs)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem)
        
        def overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f(angle, axis):
            returnValue = libpanda._inPVZN3eZ6A(angle, axis.this)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f = PandaStatic.PandaStatic(overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f)
        
        def overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f___enum__CoordinateSystem(angle, axis, resultMat, cs):
            returnValue = libpanda._inPVZN3KV2s(angle, axis.this, resultMat.this, cs)
            return returnValue

        overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f___enum__CoordinateSystem)
        
        def overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f(angle, axis, resultMat):
            returnValue = libpanda._inPVZN3JmA0(angle, axis.this, resultMat.this)
            return returnValue

        overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f = PandaStatic.PandaStatic(overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f)
        
        def overloaded_scaleMat_ptrConstLVecBase3f(scale):
            returnValue = libpanda._inPVZN3Hj8L(scale.this)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_scaleMat_ptrConstLVecBase3f = PandaStatic.PandaStatic(overloaded_scaleMat_ptrConstLVecBase3f)
        
        def overloaded_scaleMat_float_float_float(sx, sy, sz):
            returnValue = libpanda._inPVZN3p0qH(sx, sy, sz)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_scaleMat_float_float_float = PandaStatic.PandaStatic(overloaded_scaleMat_float_float_float)
        
        def overloaded_scaleMat_float(scale):
            returnValue = libpanda._inPVZN3Z99H(scale)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_scaleMat_float = PandaStatic.PandaStatic(overloaded_scaleMat_float)
        
        def yToZUpMat():
            returnValue = libpanda._inPVZN3eiST()
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        yToZUpMat = PandaStatic.PandaStatic(yToZUpMat)
        
        def zToYUpMat():
            returnValue = libpanda._inPVZN3eg2Q()
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zToYUpMat = PandaStatic.PandaStatic(zToYUpMat)
        
        def convertMat(_from, to):
            returnValue = libpanda._inPVZN3Zp4Q(_from, to)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        convertMat = PandaStatic.PandaStatic(convertMat)
        
        def getClassType():
            returnValue = libpanda._inPVZN3BRs6()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLMatrix4f_ptrConstLMatrix4f(self, other):
            returnValue = libpanda._inPVZN3dlb0(self.this, other.this)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLMatrix4f_float(self, fillValue):
            returnValue = libpanda._inPVZN3CTul(self.this, fillValue)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def fill(self, fillValue):
            returnValue = libpanda._inPVZN3aB4a(self.this, fillValue)
            return returnValue

        
        def set(self, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33):
            returnValue = libpanda._inPVZN3UYHk(self.this, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33)
            return returnValue

        
        def setUpper3(self, upper3):
            returnValue = libpanda._inPVZN3JiTa(self.this, upper3.this)
            return returnValue

        
        def getUpper3(self):
            returnValue = libpanda._inPVZN3uzhQ(self.this)
            returnObject = Mat3.Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_setRow_ptrLMatrix4f_int_ptrConstLVecBase4f(self, row, v):
            returnValue = libpanda._inPVZN3ezUo(self.this, row, v.this)
            return returnValue

        
        def overloaded_setCol_ptrLMatrix4f_int_ptrConstLVecBase4f(self, col, v):
            returnValue = libpanda._inPVZN3vWov(self.this, col, v.this)
            return returnValue

        
        def overloaded_setRow_ptrLMatrix4f_int_ptrConstLVecBase3f(self, row, v):
            returnValue = libpanda._inPVZN3vzkG(self.this, row, v.this)
            return returnValue

        
        def overloaded_setCol_ptrLMatrix4f_int_ptrConstLVecBase3f(self, col, v):
            returnValue = libpanda._inPVZN3UW4N(self.this, col, v.this)
            return returnValue

        
        def overloaded_getRow_ptrConstLMatrix4f_int(self, row):
            returnValue = libpanda._inPVZN3qLSA(self.this, row)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getCol(self, col):
            returnValue = libpanda._inPVZN37nlH(self.this, col)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_getRow3_ptrConstLMatrix4f_int(self, row):
            returnValue = libpanda._inPVZN3CmW2(self.this, row)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_getRow_ptrConstLMatrix4f_ptrLVecBase4f_int(self, resultVec, row):
            returnValue = libpanda._inPVZN3gZ_u(self.this, resultVec.this, row)
            return returnValue

        
        def overloaded_getRow3_ptrConstLMatrix4f_ptrLVecBase3f_int(self, resultVec, row):
            returnValue = libpanda._inPVZN3Wf7x(self.this, resultVec.this, row)
            return returnValue

        
        def getCol3(self, col):
            returnValue = libpanda._inPVZN3dCq9(self.this, col)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __call__(self, row, col):
            returnValue = libpanda._inPVZN34_ka(self.this, row, col)
            return returnValue

        
        def isNan(self):
            returnValue = libpanda._inPVZN3Kxs6(self.this)
            return returnValue

        
        def getCell(self, row, col):
            returnValue = libpanda._inPVZN3_xcZ(self.this, row, col)
            return returnValue

        
        def setCell(self, row, col, value):
            returnValue = libpanda._inPVZN3euBv(self.this, row, col, value)
            return returnValue

        
        def getNumComponents(self):
            returnValue = libpanda._inPVZN3UGY4(self.this)
            return returnValue

        
        def lessThan(self, other):
            returnValue = libpanda._inPVZN31_5V(self.this, other.this)
            return returnValue

        
        def eq(self, other):
            returnValue = libpanda._inPVZN3BT_n(self.this, other.this)
            return returnValue

        
        def ne(self, other):
            returnValue = libpanda._inPVZN3Boaf(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLMatrix4f_ptrConstLMatrix4f(self, other):
            returnValue = libpanda._inPVZN3sb6N(self.this, other.this)
            return returnValue

        
        def overloaded_compareTo_ptrConstLMatrix4f_ptrConstLMatrix4f_float(self, other, threshold):
            returnValue = libpanda._inPVZN3fofK(self.this, other.this, threshold)
            return returnValue

        
        def xform(self, v):
            returnValue = libpanda._inPVZN3fwbi(self.this, v.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def xformPoint(self, v):
            returnValue = libpanda._inPVZN3_NJe(self.this, v.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def xformVec(self, v):
            returnValue = libpanda._inPVZN3TVTw(self.this, v.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def multiply(self, other1, other2):
            returnValue = libpanda._inPVZN3VJ4G(self.this, other1.this, other2.this)
            return returnValue

        
        def scaleMultiply(self, scaleVector, otherMat):
            returnValue = libpanda._inPVZN3l4y5(self.this, scaleVector.this, otherMat.this)
            return returnValue

        
        def overloaded___mul___ptrConstLMatrix4f_ptrConstLMatrix4f(self, other):
            returnValue = libpanda._inPVZN3VfZQ(self.this, other.this)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___mul___ptrConstLMatrix4f_float(self, scalar):
            returnValue = libpanda._inPVZN3V_u8(self.this, scalar)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3FkP_(self.this, scalar)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __iadd__(self, other):
            returnValue = libpanda._inPVZN39I1o(self.this, other.this)
            return self

        
        def __isub__(self, other):
            returnValue = libpanda._inPVZN3d9bp(self.this, other.this)
            return self

        
        def overloaded___imul___ptrLMatrix4f_ptrConstLMatrix4f(self, other):
            returnValue = libpanda._inPVZN3togo(self.this, other.this)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___imul___ptrLMatrix4f_float(self, scalar):
            returnValue = libpanda._inPVZN3GB9Q(self.this, scalar)
            returnObject = Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def __idiv__(self, scalar):
            returnValue = libpanda._inPVZN3W2eS(self.this, scalar)
            return self

        
        def transposeFrom(self, other):
            returnValue = libpanda._inPVZN3ki6L(self.this, other.this)
            return returnValue

        
        def transposeInPlace(self):
            returnValue = libpanda._inPVZN32InP(self.this)
            return returnValue

        
        def invertFrom(self, other):
            returnValue = libpanda._inPVZN3OHre(self.this, other.this)
            return returnValue

        
        def invertAffineFrom(self, other):
            returnValue = libpanda._inPVZN3DJIn(self.this, other.this)
            return returnValue

        
        def invertInPlace(self):
            returnValue = libpanda._inPVZN3aoP_(self.this)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLMatrix4f_ptrConstLMatrix4f_float(self, other, threshold):
            returnValue = libpanda._inPVZN32sSI(self.this, other.this, threshold)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLMatrix4f_ptrConstLMatrix4f(self, other):
            returnValue = libpanda._inPVZN3xlgj(self.this, other.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPVZN3t_4O(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstLMatrix4f_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPVZN3pc_F(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstLMatrix4f_ptrOstream(self, out):
            returnValue = libpanda._inPVZN3lzZP(self.this, out.this)
            return returnValue

        
        def rotateMat(*_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        return Mat4.overloaded_rotateMat_float_ptrLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        if isinstance(_args[2], types.IntType):
                            return Mat4.overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
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
                if isinstance(_args[0], Mat4):
                    return self.overloaded_constructor_ptrConstLMatrix4f(_args[0])
                elif isinstance(_args[0], Mat3.Mat3):
                    return self.overloaded_constructor_ptrConstLMatrix3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4> <Mat3.Mat3> '
            elif numArgs == 2:
                if isinstance(_args[0], Mat3.Mat3):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_constructor_ptrConstLMatrix3f_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat3.Mat3> '
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
                                                                                return self.overloaded_constructor_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8], _args[9], _args[10], _args[11], _args[12], _args[13], _args[14], _args[15])
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
                if isinstance(_args[0], VBase3.VBase3):
                    return Mat4.overloaded_translateMat_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return Mat4.overloaded_translateMat_float_float_float(_args[0], _args[1], _args[2])
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
                    if isinstance(_args[1], VBase3.VBase3):
                        return Mat4.overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        if isinstance(_args[2], types.IntType):
                            return Mat4.overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                        elif isinstance(_args[2], Mat4):
                            return Mat4.overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Mat4> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        if isinstance(_args[2], Mat4):
                            if isinstance(_args[3], types.IntType):
                                return Mat4.overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Mat4> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '

        rotateMatNormaxis = PandaStatic.PandaStatic(rotateMatNormaxis)
        
        def scaleMat(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return Mat4.overloaded_scaleMat_float(_args[0])
                elif isinstance(_args[0], VBase3.VBase3):
                    return Mat4.overloaded_scaleMat_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return Mat4.overloaded_scaleMat_float_float_float(_args[0], _args[1], _args[2])
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
                    return self.overloaded_getRow_ptrConstLMatrix4f_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase4.VBase4):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_getRow_ptrConstLMatrix4f_ptrLVecBase4f_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLMatrix4f_float(_args[0])
                elif isinstance(_args[0], Mat4):
                    return self.overloaded_assign_ptrLMatrix4f_ptrConstLMatrix4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def __imul__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded___imul___ptrLMatrix4f_float(_args[0])
                elif isinstance(_args[0], Mat4):
                    return self.overloaded___imul___ptrLMatrix4f_ptrConstLMatrix4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def setRow(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase4.VBase4):
                        return self.overloaded_setRow_ptrLMatrix4f_int_ptrConstLVecBase4f(_args[0], _args[1])
                    elif isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_setRow_ptrLMatrix4f_int_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

        
        def setCol(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase4.VBase4):
                        return self.overloaded_setCol_ptrLMatrix4f_int_ptrConstLVecBase4f(_args[0], _args[1])
                    elif isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_setCol_ptrLMatrix4f_int_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

        
        def compareTo(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat4):
                    return self.overloaded_compareTo_ptrConstLMatrix4f_ptrConstLMatrix4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4> '
            elif numArgs == 2:
                if isinstance(_args[0], Mat4):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_compareTo_ptrConstLMatrix4f_ptrConstLMatrix4f_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def __mul__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded___mul___ptrConstLMatrix4f_float(_args[0])
                elif isinstance(_args[0], Mat4):
                    return self.overloaded___mul___ptrConstLMatrix4f_ptrConstLMatrix4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def getRow3(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_getRow3_ptrConstLMatrix4f_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase3.VBase3):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_getRow3_ptrConstLMatrix4f_ptrLVecBase3f_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def almostEqual(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat4):
                    return self.overloaded_almostEqual_ptrConstLMatrix4f_ptrConstLMatrix4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4> '
            elif numArgs == 2:
                if isinstance(_args[0], Mat4):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_almostEqual_ptrConstLMatrix4f_ptrConstLMatrix4f_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstLMatrix4f_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstLMatrix4f_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['Mat4'] = Mat4

