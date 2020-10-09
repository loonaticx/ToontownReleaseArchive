# Source Generated with Decompyle++
# File: LRotationd.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import QuatD
import Vec3D
import Mat3D
import Mat4D
import TypeHandle
import VBase4D
import Ostream
import TypeHandle
import QuatD
import Mat3D
import Mat4D
import Ostream
import VBase3D
import Vec3D
import TypeHandle
classDefined = 0

def generateClass_LRotationd():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class LRotationd(QuatD.QuatD, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3Qt9o()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLQuaterniond(self, parameter0):
            self.this = libpanda._inPVZN30PPh(parameter0.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double_double_double_double(self, parameter0, parameter1, parameter2, parameter3):
            self.this = libpanda._inPVZN35Wdz(parameter0, parameter1, parameter2, parameter3)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVector3d_double(self, parameter0, parameter1):
            self.this = libpanda._inPVZN3E3py(parameter0.this, parameter1)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLMatrix3d(self, parameter0):
            self.this = libpanda._inPVZN3u9tU(parameter0.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLMatrix4d(self, parameter0):
            self.this = libpanda._inPVZN3uC8V(parameter0.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double_double_double(self, parameter0, parameter1, parameter2):
            self.this = libpanda._inPVZN3xiug(parameter0, parameter1, parameter2)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN31cDF:
                libpanda._inPVZN31cDF(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPVZN3DpCY()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded___mul___ptrConstLRotationd_ptrConstLRotationd(self, other):
            returnValue = libpanda._inPVZN3uz8I(self.this, other.this)
            returnObject = LRotationd(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___mul___ptrConstLRotationd_ptrConstLQuaterniond(self, other):
            returnValue = libpanda._inPVZN3n_uN(self.this, other.this)
            returnObject = QuatD.QuatD(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], QuatD.QuatD):
                    return self.overloaded_constructor_ptrConstLQuaterniond(_args[0])
                elif isinstance(_args[0], Mat4D.Mat4D):
                    return self.overloaded_constructor_ptrConstLMatrix4d(_args[0])
                elif isinstance(_args[0], Mat3D.Mat3D):
                    return self.overloaded_constructor_ptrConstLMatrix3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Mat4D.Mat4D> <Mat3D.Mat3D> '
            elif numArgs == 2:
                if isinstance(_args[0], Vec3D.Vec3D):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor_ptrConstLVector3d_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Vec3D.Vec3D> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_constructor_double_double_double(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
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
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 4 '

        
        def __mul__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], QuatD.QuatD):
                    return self.overloaded___mul___ptrConstLRotationd_ptrConstLQuaterniond(_args[0])
                elif isinstance(_args[0], LRotationd):
                    return self.overloaded___mul___ptrConstLRotationd_ptrConstLRotationd(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <LRotationd> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['LRotationd'] = LRotationd

