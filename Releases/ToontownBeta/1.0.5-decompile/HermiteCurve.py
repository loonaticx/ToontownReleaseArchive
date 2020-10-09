# Source Generated with Decompyle++
# File: HermiteCurve.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ParametricCurve
import VBase3
import Ostream
import TypeHandle
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import BoundedObject
import BoundingVolume
import TypeHandle
import ReferenceCount
import TypeHandle
import Node
import TypeHandle
import NodeRelation
import Ostream
import BoundedObject
import ReferenceCount
import Writable
import TypedWritable
import BoundingVolume
import Namable
import Ostream
import TypeHandle
import NamedNode
import Namable
import TypeHandle
import Node
import NodeRelation
import Ostream
import BoundedObject
import ReferenceCount
import ParametricCurve
import VBase3
import Filename
import Ostream
import TypeHandle
import PiecewiseCurve
import TypeHandle
classDefined = 0

def generateClass_HermiteCurve():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class HermiteCurve(PiecewiseCurve.PiecewiseCurve, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPHc9WsGNE()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstParametricCurve(self, pc):
            self.this = libpanda._inPHc9WsJjK(pc.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPHc9Ww7uh()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getNumCvs(self):
            returnValue = libpanda._inPHc9Wz5OV(self.this)
            return returnValue

        
        def insertCv(self, t):
            returnValue = libpanda._inPHc9WEz8L(self.this, t)
            return returnValue

        
        def overloaded_appendCv_ptrHermiteCurve_int_float_float_float(self, type, x, y, z):
            returnValue = libpanda._inPHc9WFZ7n(self.this, type, x, y, z)
            return returnValue

        
        def overloaded_appendCv_ptrHermiteCurve_int_ptrConstLVecBase3f(self, type, v):
            returnValue = libpanda._inPHc9Wq2eQ(self.this, type, v.this)
            return returnValue

        
        def removeCv(self, n):
            returnValue = libpanda._inPHc9WVglz(self.this, n)
            return returnValue

        
        def removeAllCvs(self):
            returnValue = libpanda._inPHc9WR5OG(self.this)
            return returnValue

        
        def setCvType(self, n, type):
            returnValue = libpanda._inPHc9W93DJ(self.this, n, type)
            return returnValue

        
        def overloaded_setCvPoint_ptrHermiteCurve_int_float_float_float(self, n, x, y, z):
            returnValue = libpanda._inPHc9WvE8R(self.this, n, x, y, z)
            return returnValue

        
        def overloaded_setCvPoint_ptrHermiteCurve_int_ptrConstLVecBase3f(self, n, v):
            returnValue = libpanda._inPHc9Wu8fu(self.this, n, v.this)
            return returnValue

        
        def overloaded_setCvIn_ptrHermiteCurve_int_float_float_float(self, n, x, y, z):
            returnValue = libpanda._inPHc9W_9ya(self.this, n, x, y, z)
            return returnValue

        
        def overloaded_setCvIn_ptrHermiteCurve_int_ptrConstLVecBase3f(self, n, v):
            returnValue = libpanda._inPHc9WP7VD(self.this, n, v.this)
            return returnValue

        
        def overloaded_setCvOut_ptrHermiteCurve_int_float_float_float(self, n, x, y, z):
            returnValue = libpanda._inPHc9WdrXh(self.this, n, x, y, z)
            return returnValue

        
        def overloaded_setCvOut_ptrHermiteCurve_int_ptrConstLVecBase3f(self, n, v):
            returnValue = libpanda._inPHc9WtJ5x(self.this, n, v.this)
            return returnValue

        
        def setCvTstart(self, n, tstart):
            returnValue = libpanda._inPHc9WhREW(self.this, n, tstart)
            return returnValue

        
        def setCvName(self, n, name):
            returnValue = libpanda._inPHc9WRM2_(self.this, n, name)
            return returnValue

        
        def getCvType(self, n):
            returnValue = libpanda._inPHc9WhoER(self.this, n)
            return returnValue

        
        def overloaded_getCvPoint_ptrConstHermiteCurve_int(self, n):
            returnValue = libpanda._inPHc9W5ZkK(self.this, n)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_getCvPoint_ptrConstHermiteCurve_int_ptrLVecBase3f(self, n, v):
            returnValue = libpanda._inPHc9WK1j7(self.this, n, v.this)
            return returnValue

        
        def overloaded_getCvIn_ptrConstHermiteCurve_int(self, n):
            returnValue = libpanda._inPHc9W99Rx(self.this, n)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_getCvIn_ptrConstHermiteCurve_int_ptrLVecBase3f(self, n, v):
            returnValue = libpanda._inPHc9WHxkH(self.this, n, v.this)
            return returnValue

        
        def overloaded_getCvOut_ptrConstHermiteCurve_int(self, n):
            returnValue = libpanda._inPHc9W7jEx(self.this, n)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_getCvOut_ptrConstHermiteCurve_int_ptrLVecBase3f(self, n, v):
            returnValue = libpanda._inPHc9WHF57(self.this, n, v.this)
            return returnValue

        
        def getCvTstart(self, n):
            returnValue = libpanda._inPHc9W60ZE(self.this, n)
            return returnValue

        
        def getCvName(self, n):
            returnValue = libpanda._inPHc9WgPAi(self.this, n)
            return returnValue

        
        def writeCv(self, out, n):
            returnValue = libpanda._inPHc9WXMjA(self.this, out.this, n)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], ParametricCurve.ParametricCurve):
                    return self.overloaded_constructor_ptrConstParametricCurve(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <ParametricCurve.ParametricCurve> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def appendCv(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_appendCv_ptrHermiteCurve_int_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_appendCv_ptrHermiteCurve_int_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

        
        def setCvPoint(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_setCvPoint_ptrHermiteCurve_int_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setCvPoint_ptrHermiteCurve_int_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

        
        def getCvPoint(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_getCvPoint_ptrConstHermiteCurve_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_getCvPoint_ptrConstHermiteCurve_int_ptrLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def setCvOut(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_setCvOut_ptrHermiteCurve_int_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setCvOut_ptrHermiteCurve_int_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

        
        def setCvIn(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_setCvIn_ptrHermiteCurve_int_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setCvIn_ptrHermiteCurve_int_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

        
        def getCvIn(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_getCvIn_ptrConstHermiteCurve_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_getCvIn_ptrConstHermiteCurve_int_ptrLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def getCvOut(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_getCvOut_ptrConstHermiteCurve_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_getCvOut_ptrConstHermiteCurve_int_ptrLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['HermiteCurve'] = HermiteCurve

