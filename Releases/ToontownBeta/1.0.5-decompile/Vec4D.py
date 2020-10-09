# Source Generated with Decompyle++
# File: Vec4D.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase4D
import TypeHandle
import VBase4D
import Ostream
import TypeHandle
classDefined = 0

def generateClass_Vec4D():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Vec4D(VBase4D.VBase4D, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3LtkV()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase4d(self, copy):
            self.this = libpanda._inPVZN3k2U1(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double(self, fillValue):
            self.this = libpanda._inPVZN31aKA(fillValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_double_double_double_double(self, x, y, z, w):
            self.this = libpanda._inPVZN30QYI(x, y, z, w)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3VUPz:
                libpanda._inPVZN3VUPz(self.this)
            

        
        def zero():
            returnValue = libpanda._inPVZN3vfUL()
            returnObject = Vec4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        zero = PandaStatic.PandaStatic(zero)
        
        def unitX():
            returnValue = libpanda._inPVZN3hxcg()
            returnObject = Vec4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitX = PandaStatic.PandaStatic(unitX)
        
        def unitY():
            returnValue = libpanda._inPVZN3hVWl()
            returnObject = Vec4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitY = PandaStatic.PandaStatic(unitY)
        
        def unitZ():
            returnValue = libpanda._inPVZN3h5Nq()
            returnObject = Vec4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitZ = PandaStatic.PandaStatic(unitZ)
        
        def unitW():
            returnValue = libpanda._inPVZN3hNlb()
            returnObject = Vec4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        unitW = PandaStatic.PandaStatic(unitW)
        
        def getClassType():
            returnValue = libpanda._inPVZN3Azz8()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrLVector4d_ptrConstLVecBase4d(self, copy):
            returnValue = libpanda._inPVZN3rRya(self.this, copy.this)
            returnObject = Vec4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrLVector4d_double(self, fillValue):
            returnValue = libpanda._inPVZN3iYB2(self.this, fillValue)
            returnObject = Vec4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___sub___ptrConstLVector4d(self):
            returnValue = libpanda._inPVZN3InQs(self.this)
            returnObject = Vec4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLVector4d_ptrConstLVecBase4d(self, other):
            returnValue = libpanda._inPVZN3nv7O(self.this, other.this)
            returnObject = VBase4D.VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___add___ptrConstLVector4d_ptrConstLVector4d(self, other):
            returnValue = libpanda._inPVZN3aPbo(self.this, other.this)
            returnObject = Vec4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVector4d_ptrConstLVecBase4d(self, other):
            returnValue = libpanda._inPVZN3HqiP(self.this, other.this)
            returnObject = VBase4D.VBase4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___sub___ptrConstLVector4d_ptrConstLVector4d(self, other):
            returnValue = libpanda._inPVZN36JCp(self.this, other.this)
            returnObject = Vec4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def length(self):
            returnValue = libpanda._inPVZN3VnsI(self.this)
            return returnValue

        
        def lengthSquared(self):
            returnValue = libpanda._inPVZN3iGrj(self.this)
            return returnValue

        
        def normalize(self):
            returnValue = libpanda._inPVZN3N7XR(self.this)
            return returnValue

        
        def __mul__(self, scalar):
            returnValue = libpanda._inPVZN32z8K(self.this, scalar)
            returnObject = Vec4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __div__(self, scalar):
            returnValue = libpanda._inPVZN3mKeM(self.this, scalar)
            returnObject = Vec4D(None)
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
                return self.overloaded___sub___ptrConstLVector4d()
            elif numArgs == 1:
                if isinstance(_args[0], VBase4D.VBase4D):
                    return self.overloaded___sub___ptrConstLVector4d_ptrConstLVecBase4d(_args[0])
                elif isinstance(_args[0], Vec4D):
                    return self.overloaded___sub___ptrConstLVector4d_ptrConstLVector4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4D.VBase4D> <Vec4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def __add__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4D.VBase4D):
                    return self.overloaded___add___ptrConstLVector4d_ptrConstLVecBase4d(_args[0])
                elif isinstance(_args[0], Vec4D):
                    return self.overloaded___add___ptrConstLVector4d_ptrConstLVector4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4D.VBase4D> <Vec4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_assign_ptrLVector4d_double(_args[0])
                elif isinstance(_args[0], VBase4D.VBase4D):
                    return self.overloaded_assign_ptrLVector4d_ptrConstLVecBase4d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4D.VBase4D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['Vec4D'] = Vec4D

