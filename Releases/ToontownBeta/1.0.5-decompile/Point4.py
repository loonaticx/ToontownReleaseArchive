# Source Generated with Decompyle++
# File: Point4.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase4
import Vec4
import TypeHandle
import VBase4
import Ostream
import TypeHandle
classDefined = 0

def generateClass_Point4():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Point4(VBase4.VBase4, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3suXk()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase4f(self, copy):
            self.this = libpanda._inPVZN3Ld57(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float(self, fillValue):
            self.this = libpanda._inPVZN3788c(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float_float(self, x, y, z, w):
            self.this = libpanda._inPVZN3sF9M(x, y, z, w)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3JTIh:
                libpanda._inPVZN3JTIh(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3jPK6()
            returnObject = Point4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN37NzG()
            returnObject = Point4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN3Th8G()
            returnObject = Point4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def unitZ():
            returnValue = libpanda._inPVZN3LwGH()
            returnObject = Point4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitZ = PandaStatic.PandaStatic(unitZ)
        
        def unitW():
            returnValue = libpanda._inPVZN3D_oG()
            returnObject = Point4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitW = PandaStatic.PandaStatic(unitW)
        
        def getClassType():
            returnValue = libpanda._inPVZN3g1pV()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLPoint4f_ptrConstLVecBase4f(self, copy):
            returnValue = libpanda._inPVZN3UzBR(self.this, copy.this)
            returnObject = Point4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLPoint4f_float(self, fillValue):
            returnValue = libpanda._inPVZN3j3AN(self.this, fillValue)
            returnObject = Point4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___sub___ptrConstLPoint4f(self):
            returnValue = libpanda._inPVZN3tlJX(self.this)
            returnObject = Point4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLPoint4f_ptrConstLVecBase4f(self, other):
            returnValue = libpanda._inPVZN3B2oy(self.this, other.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLPoint4f_ptrConstLVector4f(self, other):
            returnValue = libpanda._inPVZN3hDFn(self.this, other.this)
            returnObject = Point4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLPoint4f_ptrConstLVecBase4f(self, other):
            returnValue = libpanda._inPVZN3MIqy(self.this, other.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLPoint4f_ptrConstLPoint4f(self, other):
            returnValue = libpanda._inPVZN3Fm2G(self.this, other.this)
            returnObject = Vec4.Vec4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLPoint4f_ptrConstLVector4f(self, other):
            returnValue = libpanda._inPVZN3Q1Fn(self.this, other.this)
            returnObject = Point4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN3N3t9(self.this, scalar)
            returnObject = Point4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3kxwd(self.this, scalar)
            returnObject = Point4(None)
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
                    return self.overloaded_constructor_float(_args[0])
                elif isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_constructor_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4.VBase4> '
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

        
        def __sub__(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded___sub___ptrConstLPoint4f()
            elif numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded___sub___ptrConstLPoint4f_ptrConstLVecBase4f(_args[0])
                elif isinstance(_args[0], Vec4.Vec4):
                    return self.overloaded___sub___ptrConstLPoint4f_ptrConstLVector4f(_args[0])
                elif isinstance(_args[0], Point4):
                    return self.overloaded___sub___ptrConstLPoint4f_ptrConstLPoint4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> <Vec4.Vec4> <Point4> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def __add__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded___add___ptrConstLPoint4f_ptrConstLVecBase4f(_args[0])
                elif isinstance(_args[0], Vec4.Vec4):
                    return self.overloaded___add___ptrConstLPoint4f_ptrConstLVector4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> <Vec4.Vec4> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLPoint4f_float(_args[0])
                elif isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_assign_ptrLPoint4f_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4.VBase4> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['Point4'] = Point4

