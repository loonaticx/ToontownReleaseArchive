# Source Generated with Decompyle++
# File: Point3.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase3
import Vec3
import TypeHandle
import VBase3
import Ostream
import TypeHandle
classDefined = 0

def generateClass_Point3():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Point3(VBase3.VBase3, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3sRRe()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase3f(self, copy):
            self.this = libpanda._inPVZN3UY7E(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float(self, fillValue):
            self.this = libpanda._inPVZN37n2W(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float(self, x, y, z):
            self.this = libpanda._inPVZN3FLv6(x, y, z)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3XgrD:
                libpanda._inPVZN3XgrD(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3jI84()
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN37okF()
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN3T4uF()
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def unitZ():
            returnValue = libpanda._inPVZN3LD4F()
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitZ = PandaStatic.PandaStatic(unitZ)
        
        def overloaded_origin___enum__CoordinateSystem(cs):
            returnValue = libpanda._inPVZN3OryH(cs)
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_origin___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_origin___enum__CoordinateSystem)
        
        def overloaded_origin():
            returnValue = libpanda._inPVZN3FP7_()
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_origin = PandaStatic.PandaStatic(overloaded_origin)
        
        def overloaded_rfu_float_float_float___enum__CoordinateSystem(right, fwd, up, cs):
            returnValue = libpanda._inPVZN3d0Iy(right, fwd, up, cs)
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rfu_float_float_float___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_rfu_float_float_float___enum__CoordinateSystem)
        
        def overloaded_rfu_float_float_float(right, fwd, up):
            returnValue = libpanda._inPVZN3vHkk(right, fwd, up)
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rfu_float_float_float = PandaStatic.PandaStatic(overloaded_rfu_float_float_float)
        
        def getClassType():
            returnValue = libpanda._inPVZN3g_bU()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLPoint3f_ptrConstLVecBase3f(self, copy):
            returnValue = libpanda._inPVZN3CUyP(self.this, copy.this)
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLPoint3f_float(self, fillValue):
            returnValue = libpanda._inPVZN3j_xL(self.this, fillValue)
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___sub___ptrConstLPoint3f(self):
            returnValue = libpanda._inPVZN3tm7V(self.this)
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLPoint3f_ptrConstLVecBase3f(self, other):
            returnValue = libpanda._inPVZN33SYx(self.this, other.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLPoint3f_ptrConstLVector3f(self, other):
            returnValue = libpanda._inPVZN3ZP3J(self.this, other.this)
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLPoint3f_ptrConstLVecBase3f(self, other):
            returnValue = libpanda._inPVZN36kZx(self.this, other.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLPoint3f_ptrConstLPoint3f(self, other):
            returnValue = libpanda._inPVZN3LfwU(self.this, other.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLPoint3f_ptrConstLVector3f(self, other):
            returnValue = libpanda._inPVZN3YB4J(self.this, other.this)
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def cross(self, other):
            returnValue = libpanda._inPVZN3wA30(self.this, other.this)
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN3Ncf8(self.this, scalar)
            returnObject = Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3koic(self.this, scalar)
            returnObject = Point3(None)
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
                elif isinstance(_args[0], VBase3.VBase3):
                    return self.overloaded_constructor_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_constructor_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 '

        
        def rfu(*_args):
            numArgs = len(_args)
            if numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return Point3.overloaded_rfu_float_float_float(_args[0], _args[1], _args[2])
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
                            if isinstance(_args[3], types.IntType):
                                return Point3.overloaded_rfu_float_float_float___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '

        rfu = PandaStatic.PandaStatic(rfu)
        
        def origin(*_args):
            numArgs = len(_args)
            if numArgs == 0:
                return Point3.overloaded_origin()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return Point3.overloaded_origin___enum__CoordinateSystem(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        origin = PandaStatic.PandaStatic(origin)
        
        def __sub__(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded___sub___ptrConstLPoint3f()
            elif numArgs == 1:
                if isinstance(_args[0], VBase3.VBase3):
                    return self.overloaded___sub___ptrConstLPoint3f_ptrConstLVecBase3f(_args[0])
                elif isinstance(_args[0], Vec3.Vec3):
                    return self.overloaded___sub___ptrConstLPoint3f_ptrConstLVector3f(_args[0])
                elif isinstance(_args[0], Point3):
                    return self.overloaded___sub___ptrConstLPoint3f_ptrConstLPoint3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> <Vec3.Vec3> <Point3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def __add__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3.VBase3):
                    return self.overloaded___add___ptrConstLPoint3f_ptrConstLVecBase3f(_args[0])
                elif isinstance(_args[0], Vec3.Vec3):
                    return self.overloaded___add___ptrConstLPoint3f_ptrConstLVector3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLPoint3f_float(_args[0])
                elif isinstance(_args[0], VBase3.VBase3):
                    return self.overloaded_assign_ptrLPoint3f_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['Point3'] = Point3

