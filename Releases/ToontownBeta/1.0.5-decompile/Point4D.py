# Source Generated with Decompyle++
# File: Point4D.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase4D
import Vec4D
import TypeHandle
import VBase4D
import Ostream
import TypeHandle
classDefined = 0

def generateClass_Point4D():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Point4D(VBase4D.VBase4D, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3mu0d()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase4d(self, copy):
            self.this = libpanda._inPVZN3CzW9(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double(self, fillValue):
            self.this = libpanda._inPVZN3wUf0(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double_double_double_double(self, x, y, z, w):
            self.this = libpanda._inPVZN37CfG(x, y, z, w)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3sOBF:
                libpanda._inPVZN3sOBF(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3kPDs()
            returnObject = Point4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN35Ns4()
            returnObject = Point4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN3Rh14()
            returnObject = Point4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def unitZ():
            returnValue = libpanda._inPVZN3Jw_4()
            returnObject = Point4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitZ = PandaStatic.PandaStatic(unitZ)
        
        def unitW():
            returnValue = libpanda._inPVZN3B_h4()
            returnObject = Point4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitW = PandaStatic.PandaStatic(unitW)
        
        def getClassType():
            returnValue = libpanda._inPVZN3f1iH()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLPoint4d_ptrConstLVecBase4d(self, copy):
            returnValue = libpanda._inPVZN3RheA(self.this, copy.this)
            returnObject = Point4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLPoint4d_double(self, fillValue):
            returnValue = libpanda._inPVZN3FLWL(self.this, fillValue)
            returnObject = Point4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___sub___ptrConstLPoint4d(self):
            returnValue = libpanda._inPVZN3ulCJ(self.this)
            returnObject = Point4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLPoint4d_ptrConstLVecBase4d(self, other):
            returnValue = libpanda._inPVZN3EsFi(self.this, other.this)
            returnObject = VBase4D.VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLPoint4d_ptrConstLVector4d(self, other):
            returnValue = libpanda._inPVZN3s74Y(self.this, other.this)
            returnObject = Point4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLPoint4d_ptrConstLVecBase4d(self, other):
            returnValue = libpanda._inPVZN3J2Gi(self.this, other.this)
            returnObject = VBase4D.VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLPoint4d_ptrConstLPoint4d(self, other):
            returnValue = libpanda._inPVZN3qiuA(self.this, other.this)
            returnObject = Vec4D.Vec4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLPoint4d_ptrConstLVector4d(self, other):
            returnValue = libpanda._inPVZN3tt5Y(self.this, other.this)
            returnObject = Point4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN3k4_H(self.this, scalar)
            returnObject = Point4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3zdAo(self.this, scalar)
            returnObject = Point4D(None)
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
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_double(_args[0])
                elif isinstance(_args[0], VBase4D.VBase4D):
                    return self.overloaded_constructor_ptrConstLVecBase4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4D.VBase4D> '
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

        
        def __sub__(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded___sub___ptrConstLPoint4d()
            elif numArgs == 1:
                if isinstance(_args[0], VBase4D.VBase4D):
                    return self.overloaded___sub___ptrConstLPoint4d_ptrConstLVecBase4d(_args[0])
                elif isinstance(_args[0], Vec4D.Vec4D):
                    return self.overloaded___sub___ptrConstLPoint4d_ptrConstLVector4d(_args[0])
                elif isinstance(_args[0], Point4D):
                    return self.overloaded___sub___ptrConstLPoint4d_ptrConstLPoint4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4D.VBase4D> <Vec4D.Vec4D> <Point4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def __add__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4D.VBase4D):
                    return self.overloaded___add___ptrConstLPoint4d_ptrConstLVecBase4d(_args[0])
                elif isinstance(_args[0], Vec4D.Vec4D):
                    return self.overloaded___add___ptrConstLPoint4d_ptrConstLVector4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4D.VBase4D> <Vec4D.Vec4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLPoint4d_double(_args[0])
                elif isinstance(_args[0], VBase4D.VBase4D):
                    return self.overloaded_assign_ptrLPoint4d_ptrConstLVecBase4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4D.VBase4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['Point4D'] = Point4D

