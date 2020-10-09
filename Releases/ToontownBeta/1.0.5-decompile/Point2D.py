# Source Generated with Decompyle++
# File: Point2D.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase2D
import Vec2D
import TypeHandle
import VBase2D
import Ostream
import TypeHandle
classDefined = 0

def generateClass_Point2D():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Point2D(VBase2D.VBase2D, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3mknR()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase2d(self, copy):
            self.this = libpanda._inPVZN3dcZP(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double(self, fillValue):
            self.this = libpanda._inPVZN3wWSo(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double_double(self, x, y):
            self.this = libpanda._inPVZN3OlaV(x, y)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN33cIK:
                libpanda._inPVZN33cIK(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3kBnp()
            returnObject = Point2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN35fP2()
            returnObject = Point2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN3RrZ2()
            returnObject = Point2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def getClassType():
            returnValue = libpanda._inPVZN3fHHF()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLPoint2d_ptrConstLVecBase2d(self, copy):
            returnValue = libpanda._inPVZN32m99(self.this, copy.this)
            returnObject = Point2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLPoint2d_double(self, fillValue):
            returnValue = libpanda._inPVZN3Fh4I(self.this, fillValue)
            returnObject = Point2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___sub___ptrConstLPoint2d(self):
            returnValue = libpanda._inPVZN3uPmG(self.this)
            returnObject = Point2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLPoint2d_ptrConstLVecBase2d(self, other):
            returnValue = libpanda._inPVZN3olkf(self.this, other.this)
            returnObject = VBase2D.VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLPoint2d_ptrConstLVector2d(self, other):
            returnValue = libpanda._inPVZN37_ce(self.this, other.this)
            returnObject = Point2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLPoint2d_ptrConstLVecBase2d(self, other):
            returnValue = libpanda._inPVZN3tvlf(self.this, other.this)
            returnObject = VBase2D.VBase2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLPoint2d_ptrConstLPoint2d(self, other):
            returnValue = libpanda._inPVZN3Ggic(self.this, other.this)
            returnObject = Vec2D.Vec2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLPoint2d_ptrConstLVector2d(self, other):
            returnValue = libpanda._inPVZN3_Bee(self.this, other.this)
            returnObject = Point2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN3kaiF(self.this, scalar)
            returnObject = Point2D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3zvkl(self.this, scalar)
            returnObject = Point2D(None)
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
                elif isinstance(_args[0], VBase2D.VBase2D):
                    return self.overloaded_constructor_ptrConstLVecBase2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D.VBase2D> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor_double_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

        
        def __sub__(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded___sub___ptrConstLPoint2d()
            elif numArgs == 1:
                if isinstance(_args[0], VBase2D.VBase2D):
                    return self.overloaded___sub___ptrConstLPoint2d_ptrConstLVecBase2d(_args[0])
                elif isinstance(_args[0], Vec2D.Vec2D):
                    return self.overloaded___sub___ptrConstLPoint2d_ptrConstLVector2d(_args[0])
                elif isinstance(_args[0], Point2D):
                    return self.overloaded___sub___ptrConstLPoint2d_ptrConstLPoint2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2D.VBase2D> <Vec2D.Vec2D> <Point2D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def __add__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase2D.VBase2D):
                    return self.overloaded___add___ptrConstLPoint2d_ptrConstLVecBase2d(_args[0])
                elif isinstance(_args[0], Vec2D.Vec2D):
                    return self.overloaded___add___ptrConstLPoint2d_ptrConstLVector2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2D.VBase2D> <Vec2D.Vec2D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLPoint2d_double(_args[0])
                elif isinstance(_args[0], VBase2D.VBase2D):
                    return self.overloaded_assign_ptrLPoint2d_ptrConstLVecBase2d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D.VBase2D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['Point2D'] = Point2D

