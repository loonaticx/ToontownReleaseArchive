# Source Generated with Decompyle++
# File: Vec3D.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase3D
import TypeHandle
import VBase3D
import Ostream
import TypeHandle
classDefined = 0

def generateClass_Vec3D():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Vec3D(VBase3D.VBase3D, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN38Lin()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase3d(self, copy):
            self.this = libpanda._inPVZN3o5OH(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double(self, fillValue):
            self.this = libpanda._inPVZN3o7GS(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double_double_double(self, x, y, z):
            self.this = libpanda._inPVZN34wm1(x, y, z)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3CJMs:
                libpanda._inPVZN3CJMs(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3w_Rk()
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN3iRa5()
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN3i1R_()
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def unitZ():
            returnValue = libpanda._inPVZN3hZLD()
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitZ = PandaStatic.PandaStatic(unitZ)
        
        def overloaded_up___enum__CoordinateSystem(cs):
            returnValue = libpanda._inPVZN31n5k(cs)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_up___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_up___enum__CoordinateSystem)
        
        def overloaded_up():
            returnValue = libpanda._inPVZN3BWtB()
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_up = PandaStatic.PandaStatic(overloaded_up)
        
        def overloaded_right___enum__CoordinateSystem(cs):
            returnValue = libpanda._inPVZN3JHPm(cs)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_right___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_right___enum__CoordinateSystem)
        
        def overloaded_right():
            returnValue = libpanda._inPVZN3qmXe()
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_right = PandaStatic.PandaStatic(overloaded_right)
        
        def overloaded_forward___enum__CoordinateSystem(cs):
            returnValue = libpanda._inPVZN31fXy(cs)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_forward___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_forward___enum__CoordinateSystem)
        
        def overloaded_forward():
            returnValue = libpanda._inPVZN3It7r()
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_forward = PandaStatic.PandaStatic(overloaded_forward)
        
        def overloaded_down___enum__CoordinateSystem(cs):
            returnValue = libpanda._inPVZN3ZHZb(cs)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_down___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_down___enum__CoordinateSystem)
        
        def overloaded_down():
            returnValue = libpanda._inPVZN3DbKd()
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_down = PandaStatic.PandaStatic(overloaded_down)
        
        def overloaded_left___enum__CoordinateSystem(cs):
            returnValue = libpanda._inPVZN3vuWG(cs)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_left___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_left___enum__CoordinateSystem)
        
        def overloaded_left():
            returnValue = libpanda._inPVZN3VLKI()
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_left = PandaStatic.PandaStatic(overloaded_left)
        
        def overloaded_back___enum__CoordinateSystem(cs):
            returnValue = libpanda._inPVZN3Pp96(cs)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_back___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_back___enum__CoordinateSystem)
        
        def overloaded_back():
            returnValue = libpanda._inPVZN3FMw8()
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_back = PandaStatic.PandaStatic(overloaded_back)
        
        def overloaded_rfu_double_double_double___enum__CoordinateSystem(right, fwd, up, cs):
            returnValue = libpanda._inPVZN3npAa(right, fwd, up, cs)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rfu_double_double_double___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_rfu_double_double_double___enum__CoordinateSystem)
        
        def overloaded_rfu_double_double_double(right, fwd, up):
            returnValue = libpanda._inPVZN3gvMh(right, fwd, up)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rfu_double_double_double = PandaStatic.PandaStatic(overloaded_rfu_double_double_double)
        
        def getClassType():
            returnValue = libpanda._inPVZN3ATxV()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLVector3d_ptrConstLVecBase3d(self, copy):
            returnValue = libpanda._inPVZN3syfy(self.this, copy.this)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLVector3d_double(self, fillValue):
            returnValue = libpanda._inPVZN3i48O(self.this, fillValue)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___sub___ptrConstLVector3d(self):
            returnValue = libpanda._inPVZN3IHOF(self.this)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLVector3d_ptrConstLVecBase3d(self, other):
            returnValue = libpanda._inPVZN3aErm(self.this, other.this)
            returnObject = VBase3D.VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLVector3d_ptrConstLVector3d(self, other):
            returnValue = libpanda._inPVZN3sLVB(self.this, other.this)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVector3d_ptrConstLVecBase3d(self, other):
            returnValue = libpanda._inPVZN36CSn(self.this, other.this)
            returnObject = VBase3D.VBase3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVector3d_ptrConstLVector3d(self, other):
            returnValue = libpanda._inPVZN3MG8B(self.this, other.this)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def length(self):
            returnValue = libpanda._inPVZN3UHph(self.this)
            return returnValue

        
        def lengthSquared(self):
            returnValue = libpanda._inPVZN3jmn8(self.this)
            return returnValue

        
        def normalize(self):
            returnValue = libpanda._inPVZN3QbTq(self.this)
            return returnValue

        
        def cross(self, other):
            returnValue = libpanda._inPVZN3IN08(self.this, other.this)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN33T5j(self.this, scalar)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3nqal(self.this, scalar)
            returnObject = Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def left(*_args):
            numArgs = len(_args)
            if numArgs == 0:
                return Vec3D.overloaded_left()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return Vec3D.overloaded_left___enum__CoordinateSystem(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        left = PandaStatic.PandaStatic(left)
        
        def up(*_args):
            numArgs = len(_args)
            if numArgs == 0:
                return Vec3D.overloaded_up()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return Vec3D.overloaded_up___enum__CoordinateSystem(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        up = PandaStatic.PandaStatic(up)
        
        def back(*_args):
            numArgs = len(_args)
            if numArgs == 0:
                return Vec3D.overloaded_back()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return Vec3D.overloaded_back___enum__CoordinateSystem(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        back = PandaStatic.PandaStatic(back)
        
        def forward(*_args):
            numArgs = len(_args)
            if numArgs == 0:
                return Vec3D.overloaded_forward()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return Vec3D.overloaded_forward___enum__CoordinateSystem(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        forward = PandaStatic.PandaStatic(forward)
        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_double(_args[0])
                elif isinstance(_args[0], VBase3D.VBase3D):
                    return self.overloaded_constructor_ptrConstLVecBase3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D.VBase3D> '
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
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 '

        
        def rfu(*_args):
            numArgs = len(_args)
            if numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return Vec3D.overloaded_rfu_double_double_double(_args[0], _args[1], _args[2])
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
                                return Vec3D.overloaded_rfu_double_double_double___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
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
        
        def right(*_args):
            numArgs = len(_args)
            if numArgs == 0:
                return Vec3D.overloaded_right()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return Vec3D.overloaded_right___enum__CoordinateSystem(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        right = PandaStatic.PandaStatic(right)
        
        def down(*_args):
            numArgs = len(_args)
            if numArgs == 0:
                return Vec3D.overloaded_down()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return Vec3D.overloaded_down___enum__CoordinateSystem(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        down = PandaStatic.PandaStatic(down)
        
        def __sub__(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded___sub___ptrConstLVector3d()
            elif numArgs == 1:
                if isinstance(_args[0], VBase3D.VBase3D):
                    return self.overloaded___sub___ptrConstLVector3d_ptrConstLVecBase3d(_args[0])
                elif isinstance(_args[0], Vec3D):
                    return self.overloaded___sub___ptrConstLVector3d_ptrConstLVector3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> <Vec3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def __add__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3D.VBase3D):
                    return self.overloaded___add___ptrConstLVector3d_ptrConstLVecBase3d(_args[0])
                elif isinstance(_args[0], Vec3D):
                    return self.overloaded___add___ptrConstLVector3d_ptrConstLVector3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> <Vec3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLVector3d_double(_args[0])
                elif isinstance(_args[0], VBase3D.VBase3D):
                    return self.overloaded_assign_ptrLVector3d_ptrConstLVecBase3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['Vec3D'] = Vec3D

