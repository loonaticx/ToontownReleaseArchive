# Source Generated with Decompyle++
# File: Vec3.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase3
import TypeHandle
import VBase3
import Ostream
import TypeHandle
classDefined = 0

def generateClass_Vec3():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Vec3(VBase3.VBase3, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3aaCr()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase3f(self, copy):
            self.this = libpanda._inPVZN3SWMN(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float(self, fillValue):
            self.this = libpanda._inPVZN3zoMJ(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float(self, x, y, z):
            self.this = libpanda._inPVZN3aD7I(x, y, z)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3_LTw:
                libpanda._inPVZN3_LTw(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3F8xn()
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN3rC68()
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN3qexB()
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def unitZ():
            returnValue = libpanda._inPVZN3q6qG()
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitZ = PandaStatic.PandaStatic(unitZ)
        
        def overloaded_up___enum__CoordinateSystem(cs):
            returnValue = libpanda._inPVZN3eoZo(cs)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_up___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_up___enum__CoordinateSystem)
        
        def overloaded_up():
            returnValue = libpanda._inPVZN3sZNF()
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_up = PandaStatic.PandaStatic(overloaded_up)
        
        def overloaded_right___enum__CoordinateSystem(cs):
            returnValue = libpanda._inPVZN3wGvp(cs)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_right___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_right___enum__CoordinateSystem)
        
        def overloaded_right():
            returnValue = libpanda._inPVZN3Rm3h()
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_right = PandaStatic.PandaStatic(overloaded_right)
        
        def overloaded_forward___enum__CoordinateSystem(cs):
            returnValue = libpanda._inPVZN3gU31(cs)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_forward___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_forward___enum__CoordinateSystem)
        
        def overloaded_forward():
            returnValue = libpanda._inPVZN3hqbv()
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_forward = PandaStatic.PandaStatic(overloaded_forward)
        
        def overloaded_down___enum__CoordinateSystem(cs):
            returnValue = libpanda._inPVZN3yG5e(cs)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_down___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_down___enum__CoordinateSystem)
        
        def overloaded_down():
            returnValue = libpanda._inPVZN3cbqg()
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_down = PandaStatic.PandaStatic(overloaded_down)
        
        def overloaded_left___enum__CoordinateSystem(cs):
            returnValue = libpanda._inPVZN3ot2J(cs)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_left___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_left___enum__CoordinateSystem)
        
        def overloaded_left():
            returnValue = libpanda._inPVZN3uYqL()
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_left = PandaStatic.PandaStatic(overloaded_left)
        
        def overloaded_back___enum__CoordinateSystem(cs):
            returnValue = libpanda._inPVZN3qpd_(cs)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_back___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_back___enum__CoordinateSystem)
        
        def overloaded_back():
            returnValue = libpanda._inPVZN3NNQA()
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_back = PandaStatic.PandaStatic(overloaded_back)
        
        def overloaded_rfu_float_float_float___enum__CoordinateSystem(right, fwd, up, cs):
            returnValue = libpanda._inPVZN3asqR(right, fwd, up, cs)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rfu_float_float_float___enum__CoordinateSystem = PandaStatic.PandaStatic(overloaded_rfu_float_float_float___enum__CoordinateSystem)
        
        def overloaded_rfu_float_float_float(right, fwd, up):
            returnValue = libpanda._inPVZN3Nw9c(right, fwd, up)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        overloaded_rfu_float_float_float = PandaStatic.PandaStatic(overloaded_rfu_float_float_float)
        
        def getClassType():
            returnValue = libpanda._inPVZN3ZSRZ()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLVector3f_ptrConstLVecBase3f(self, copy):
            returnValue = libpanda._inPVZN3jzGE(self.this, copy.this)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLVector3f_float(self, fillValue):
            returnValue = libpanda._inPVZN3KZRE(self.this, fillValue)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___sub___ptrConstLVector3f(self):
            returnValue = libpanda._inPVZN3PGuI(self.this)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLVector3f_ptrConstLVecBase3f(self, other):
            returnValue = libpanda._inPVZN3CFS4(self.this, other.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLVector3f_ptrConstLVector3f(self, other):
            returnValue = libpanda._inPVZN3V8QH(self.this, other.this)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVector3f_ptrConstLVecBase3f(self, other):
            returnValue = libpanda._inPVZN3iC54(self.this, other.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVector3f_ptrConstLVector3f(self, other):
            returnValue = libpanda._inPVZN3153H(self.this, other.this)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def length(self):
            returnValue = libpanda._inPVZN3b8Il(self.this)
            return returnValue

        
        def lengthSquared(self):
            returnValue = libpanda._inPVZN37lHA(self.this)
            return returnValue

        
        def normalize(self):
            returnValue = libpanda._inPVZN3nazt(self.this)
            return returnValue

        
        def cross(self, other):
            returnValue = libpanda._inPVZN3QsXn(self.this, other.this)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN3VJUb(self.this, scalar)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3lh0c(self.this, scalar)
            returnObject = Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def left(*_args):
            numArgs = len(_args)
            if numArgs == 0:
                return Vec3.overloaded_left()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return Vec3.overloaded_left___enum__CoordinateSystem(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        left = PandaStatic.PandaStatic(left)
        
        def up(*_args):
            numArgs = len(_args)
            if numArgs == 0:
                return Vec3.overloaded_up()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return Vec3.overloaded_up___enum__CoordinateSystem(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        up = PandaStatic.PandaStatic(up)
        
        def back(*_args):
            numArgs = len(_args)
            if numArgs == 0:
                return Vec3.overloaded_back()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return Vec3.overloaded_back___enum__CoordinateSystem(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        back = PandaStatic.PandaStatic(back)
        
        def forward(*_args):
            numArgs = len(_args)
            if numArgs == 0:
                return Vec3.overloaded_forward()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return Vec3.overloaded_forward___enum__CoordinateSystem(_args[0])
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
                            return Vec3.overloaded_rfu_float_float_float(_args[0], _args[1], _args[2])
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
                                return Vec3.overloaded_rfu_float_float_float___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
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
                return Vec3.overloaded_right()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return Vec3.overloaded_right___enum__CoordinateSystem(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        right = PandaStatic.PandaStatic(right)
        
        def down(*_args):
            numArgs = len(_args)
            if numArgs == 0:
                return Vec3.overloaded_down()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return Vec3.overloaded_down___enum__CoordinateSystem(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        down = PandaStatic.PandaStatic(down)
        
        def __sub__(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded___sub___ptrConstLVector3f()
            elif numArgs == 1:
                if isinstance(_args[0], VBase3.VBase3):
                    return self.overloaded___sub___ptrConstLVector3f_ptrConstLVecBase3f(_args[0])
                elif isinstance(_args[0], Vec3):
                    return self.overloaded___sub___ptrConstLVector3f_ptrConstLVector3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> <Vec3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def __add__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3.VBase3):
                    return self.overloaded___add___ptrConstLVector3f_ptrConstLVecBase3f(_args[0])
                elif isinstance(_args[0], Vec3):
                    return self.overloaded___add___ptrConstLVector3f_ptrConstLVector3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> <Vec3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLVector3f_float(_args[0])
                elif isinstance(_args[0], VBase3.VBase3):
                    return self.overloaded_assign_ptrLVector3f_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['Vec3'] = Vec3

