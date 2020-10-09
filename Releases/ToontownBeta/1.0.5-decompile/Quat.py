# Source Generated with Decompyle++
# File: Quat.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Mat3
import Mat4
import Ostream
import VBase3
import Vec3
import TypeHandle
import VBase4
import Ostream
import TypeHandle
classDefined = 0

def generateClass_Quat():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Quat(VBase4.VBase4, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3kHe_()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLQuaternionf(self, parameter0):
            self.this = libpanda._inPVZN37E_F(parameter0.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float_float(self, parameter0, parameter1, parameter2, parameter3):
            self.this = libpanda._inPVZN3snTV(parameter0, parameter1, parameter2, parameter3)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3c2wx:
                libpanda._inPVZN3c2wx(self.this)
            

        
        def pureImaginary(parameter0):
            returnValue = libpanda._inPVZN3JCfb(parameter0.this)
            returnObject = Quat(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        pureImaginary = PandaStatic.PandaStatic(pureImaginary)
        
        def identQuat():
            returnValue = libpanda._inPVZN3fANR()
            returnObject = Quat(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        identQuat = PandaStatic.PandaStatic(identQuat)
        
        def getClassType():
            returnValue = libpanda._inPVZN3g3Kd()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded___mul___ptrLQuaternionf_ptrConstLQuaternionf(self, parameter1):
            returnValue = libpanda._inPVZN39XnW(self.this, parameter1.this)
            returnObject = Quat(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __imul__(self, parameter1):
            returnValue = libpanda._inPVZN3FjVd(self.this, parameter1.this)
            return self

        
        def overloaded___mul___ptrLQuaternionf_ptrConstLMatrix3f(self, parameter1):
            returnValue = libpanda._inPVZN3cWZK(self.this, parameter1.this)
            returnObject = Mat3.Mat3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___mul___ptrLQuaternionf_ptrConstLMatrix4f(self, parameter1):
            returnValue = libpanda._inPVZN3XXJs(self.this, parameter1.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_almostEqual_ptrConstLQuaternionf_ptrConstLQuaternionf_float(self, parameter1, parameter2):
            returnValue = libpanda._inPVZN3edKH(self.this, parameter1.this, parameter2)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLQuaternionf_ptrConstLQuaternionf(self, parameter1):
            returnValue = libpanda._inPVZN3khMU(self.this, parameter1.this)
            return returnValue

        
        def output(self, parameter1):
            returnValue = libpanda._inPVZN3V_zP(self.this, parameter1.this)
            return returnValue

        
        def overloaded_extractToMatrix_ptrConstLQuaternionf_ptrLMatrix3f(self, m):
            returnValue = libpanda._inPVZN3JBI2(self.this, m.this)
            return returnValue

        
        def overloaded_extractToMatrix_ptrConstLQuaternionf_ptrLMatrix4f(self, m):
            returnValue = libpanda._inPVZN3BwR2(self.this, m.this)
            return returnValue

        
        def overloaded_setFromMatrix_ptrLQuaternionf_ptrConstLMatrix3f(self, m):
            returnValue = libpanda._inPVZN3T3wD(self.this, m.this)
            return returnValue

        
        def overloaded_setFromMatrix_ptrLQuaternionf_ptrConstLMatrix4f(self, m):
            returnValue = libpanda._inPVZN3u4QH(self.this, m.this)
            return returnValue

        
        def setHpr(self, hpr):
            returnValue = libpanda._inPVZN3Z7kq(self.this, hpr.this)
            return returnValue

        
        def getHpr(self):
            returnValue = libpanda._inPVZN3HPB0(self.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getR(self):
            returnValue = libpanda._inPVZN3dWbD(self.this)
            return returnValue

        
        def getI(self):
            returnValue = libpanda._inPVZN3cLbE(self.this)
            return returnValue

        
        def getJ(self):
            returnValue = libpanda._inPVZN3uMbL(self.this)
            return returnValue

        
        def getK(self):
            returnValue = libpanda._inPVZN3AObS(self.this)
            return returnValue

        
        def setR(self, r):
            returnValue = libpanda._inPVZN3wpLX(self.this, r)
            return returnValue

        
        def setI(self, i):
            returnValue = libpanda._inPVZN3tSLY(self.this, i)
            return returnValue

        
        def setJ(self, j):
            returnValue = libpanda._inPVZN3fTLf(self.this, j)
            return returnValue

        
        def setK(self, k):
            returnValue = libpanda._inPVZN3RgLm(self.this, k)
            return returnValue

        
        def normalize(self):
            returnValue = libpanda._inPVZN3TbWQ(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], Quat):
                    return self.overloaded_constructor_ptrConstLQuaternionf(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Quat> '
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

        
        def setFromMatrix(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat4.Mat4):
                    return self.overloaded_setFromMatrix_ptrLQuaternionf_ptrConstLMatrix4f(_args[0])
                elif isinstance(_args[0], Mat3.Mat3):
                    return self.overloaded_setFromMatrix_ptrLQuaternionf_ptrConstLMatrix3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4.Mat4> <Mat3.Mat3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def __mul__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Quat):
                    return self.overloaded___mul___ptrLQuaternionf_ptrConstLQuaternionf(_args[0])
                elif isinstance(_args[0], Mat4.Mat4):
                    return self.overloaded___mul___ptrLQuaternionf_ptrConstLMatrix4f(_args[0])
                elif isinstance(_args[0], Mat3.Mat3):
                    return self.overloaded___mul___ptrLQuaternionf_ptrConstLMatrix3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Quat> <Mat4.Mat4> <Mat3.Mat3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def extractToMatrix(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat4.Mat4):
                    return self.overloaded_extractToMatrix_ptrConstLQuaternionf_ptrLMatrix4f(_args[0])
                elif isinstance(_args[0], Mat3.Mat3):
                    return self.overloaded_extractToMatrix_ptrConstLQuaternionf_ptrLMatrix3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4.Mat4> <Mat3.Mat3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def almostEqual(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Quat):
                    return self.overloaded_almostEqual_ptrConstLQuaternionf_ptrConstLQuaternionf(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Quat> '
            elif numArgs == 2:
                if isinstance(_args[0], Quat):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_almostEqual_ptrConstLQuaternionf_ptrConstLQuaternionf_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Quat> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['Quat'] = Quat

