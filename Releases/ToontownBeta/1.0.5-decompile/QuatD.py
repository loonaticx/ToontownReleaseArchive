# Source Generated with Decompyle++
# File: QuatD.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Mat3D
import Mat4D
import Ostream
import VBase3D
import Vec3D
import TypeHandle
import VBase4D
import Ostream
import TypeHandle
classDefined = 0

def generateClass_QuatD():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class QuatD(VBase4D.VBase4D, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3koX4()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLQuaterniond(self, parameter0):
            self.this = libpanda._inPVZN3AJ4f(parameter0.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double_double_double_double(self, parameter0, parameter1, parameter2, parameter3):
            self.this = libpanda._inPVZN3zz6w(parameter0, parameter1, parameter2, parameter3)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3cq0F:
                libpanda._inPVZN3cq0F(self.this)
            

        
        def pureImaginary(parameter0):
            returnValue = libpanda._inPVZN3HpmP(parameter0.this)
            returnObject = QuatD(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        pureImaginary = PandaStatic.PandaStatic(pureImaginary)
        
        def identQuat():
            returnValue = libpanda._inPVZN3f0TM()
            returnObject = QuatD(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        identQuat = PandaStatic.PandaStatic(identQuat)
        
        def getClassType():
            returnValue = libpanda._inPVZN3gLSY()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded___mul___ptrLQuaterniond_ptrConstLQuaterniond(self, parameter1):
            returnValue = libpanda._inPVZN36zg1(self.this, parameter1.this)
            returnObject = QuatD(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __imul__(self, parameter1):
            returnValue = libpanda._inPVZN3zJeR(self.this, parameter1.this)
            return self

        
        def overloaded___mul___ptrLQuaterniond_ptrConstLMatrix3d(self, parameter1):
            returnValue = libpanda._inPVZN36mgV(self.this, parameter1.this)
            returnObject = Mat3D.Mat3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___mul___ptrLQuaterniond_ptrConstLMatrix4d(self, parameter1):
            returnValue = libpanda._inPVZN31nQ3(self.this, parameter1.this)
            returnObject = Mat4D.Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_almostEqual_ptrConstLQuaterniond_ptrConstLQuaterniond_double(self, parameter1, parameter2):
            returnValue = libpanda._inPVZN3DrVo(self.this, parameter1.this, parameter2)
            return returnValue

        
        def overloaded_almostEqual_ptrConstLQuaterniond_ptrConstLQuaterniond(self, parameter1):
            returnValue = libpanda._inPVZN3laTv(self.this, parameter1.this)
            return returnValue

        
        def output(self, parameter1):
            returnValue = libpanda._inPVZN3Vz7K(self.this, parameter1.this)
            return returnValue

        
        def overloaded_extractToMatrix_ptrConstLQuaterniond_ptrLMatrix3d(self, m):
            returnValue = libpanda._inPVZN3Jlcn(self.this, m.this)
            return returnValue

        
        def overloaded_extractToMatrix_ptrConstLQuaterniond_ptrLMatrix4d(self, m):
            returnValue = libpanda._inPVZN3BUon(self.this, m.this)
            return returnValue

        
        def overloaded_setFromMatrix_ptrLQuaterniond_ptrConstLMatrix3d(self, m):
            returnValue = libpanda._inPVZN3X04e(self.this, m.this)
            return returnValue

        
        def overloaded_setFromMatrix_ptrLQuaterniond_ptrConstLMatrix4d(self, m):
            returnValue = libpanda._inPVZN3y1Yi(self.this, m.this)
            return returnValue

        
        def setHpr(self, hpr):
            returnValue = libpanda._inPVZN3afnX(self.this, hpr.this)
            return returnValue

        
        def getHpr(self):
            returnValue = libpanda._inPVZN3HrIv(self.this)
            returnObject = VBase3D.VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getR(self):
            returnValue = libpanda._inPVZN3eyi_(self.this)
            return returnValue

        
        def getI(self):
            returnValue = libpanda._inPVZN3dvi_(self.this)
            return returnValue

        
        def getJ(self):
            returnValue = libpanda._inPVZN3uwiG(self.this)
            return returnValue

        
        def getK(self):
            returnValue = libpanda._inPVZN3AqiN(self.this)
            return returnValue

        
        def setR(self, r):
            returnValue = libpanda._inPVZN3vGsU(self.this, r)
            return returnValue

        
        def setI(self, i):
            returnValue = libpanda._inPVZN3w7rV(self.this, i)
            return returnValue

        
        def setJ(self, j):
            returnValue = libpanda._inPVZN3y8rc(self.this, j)
            return returnValue

        
        def setK(self, k):
            returnValue = libpanda._inPVZN3E9rj(self.this, k)
            return returnValue

        
        def normalize(self):
            returnValue = libpanda._inPVZN3T_eL(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], QuatD):
                    return self.overloaded_constructor_ptrConstLQuaterniond(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <QuatD> '
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

        
        def setFromMatrix(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat4D.Mat4D):
                    return self.overloaded_setFromMatrix_ptrLQuaterniond_ptrConstLMatrix4d(_args[0])
                elif isinstance(_args[0], Mat3D.Mat3D):
                    return self.overloaded_setFromMatrix_ptrLQuaterniond_ptrConstLMatrix3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat3D.Mat3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def __mul__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], QuatD):
                    return self.overloaded___mul___ptrLQuaterniond_ptrConstLQuaterniond(_args[0])
                elif isinstance(_args[0], Mat4D.Mat4D):
                    return self.overloaded___mul___ptrLQuaterniond_ptrConstLMatrix4d(_args[0])
                elif isinstance(_args[0], Mat3D.Mat3D):
                    return self.overloaded___mul___ptrLQuaterniond_ptrConstLMatrix3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <QuatD> <Mat4D.Mat4D> <Mat3D.Mat3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def extractToMatrix(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat4D.Mat4D):
                    return self.overloaded_extractToMatrix_ptrConstLQuaterniond_ptrLMatrix4d(_args[0])
                elif isinstance(_args[0], Mat3D.Mat3D):
                    return self.overloaded_extractToMatrix_ptrConstLQuaterniond_ptrLMatrix3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat3D.Mat3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def almostEqual(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], QuatD):
                    return self.overloaded_almostEqual_ptrConstLQuaterniond_ptrConstLQuaterniond(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <QuatD> '
            elif numArgs == 2:
                if isinstance(_args[0], QuatD):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_almostEqual_ptrConstLQuaterniond_ptrConstLQuaterniond_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <QuatD> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['QuatD'] = QuatD

