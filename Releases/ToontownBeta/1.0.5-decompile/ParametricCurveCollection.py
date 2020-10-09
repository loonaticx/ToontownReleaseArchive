# Source Generated with Decompyle++
# File: ParametricCurveCollection.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ParametricCurve
import Node
import VBase3
import Mat4
import Ostream
import Filename
import ReferenceCount
import TypeHandle
classDefined = 0

def generateClass_ParametricCurveCollection():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ParametricCurveCollection(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPHc9WqFVC()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPHc9WVi4s:
                libpanda._inPHc9WVi4s(self.this)
            

        
        def overloaded_addCurve_ptrParametricCurveCollection_ptrParametricCurve(self, curve):
            returnValue = libpanda._inPHc9WQMiA(self.this, curve.this)
            return returnValue

        
        def overloaded_addCurve_ptrParametricCurveCollection_ptrParametricCurve_int(self, curve, index):
            returnValue = libpanda._inPHc9Wlu26(self.this, curve.this, index)
            return returnValue

        
        def addCurves(self, node):
            returnValue = libpanda._inPHc9WwSd2(self.this, node.this)
            return returnValue

        
        def overloaded_removeCurve_ptrParametricCurveCollection_ptrParametricCurve(self, curve):
            returnValue = libpanda._inPHc9WksBL(self.this, curve.this)
            return returnValue

        
        def overloaded_removeCurve_ptrParametricCurveCollection_int(self, index):
            returnValue = libpanda._inPHc9WHM1q(self.this, index)
            return returnValue

        
        def hasCurve(self, curve):
            returnValue = libpanda._inPHc9WT5PA(self.this, curve.this)
            return returnValue

        
        def clear(self):
            returnValue = libpanda._inPHc9WCG_a(self.this)
            return returnValue

        
        def clearTimewarps(self):
            returnValue = libpanda._inPHc9WNRLR(self.this)
            return returnValue

        
        def getNumCurves(self):
            returnValue = libpanda._inPHc9WS1yN(self.this)
            return returnValue

        
        def getCurve(self, index):
            returnValue = libpanda._inPHc9Wh_s_(self.this, index)
            returnObject = ParametricCurve.ParametricCurve(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getXyzCurve(self):
            returnValue = libpanda._inPHc9WSC9i(self.this)
            returnObject = ParametricCurve.ParametricCurve(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getHprCurve(self):
            returnValue = libpanda._inPHc9WOZUC(self.this)
            returnObject = ParametricCurve.ParametricCurve(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getDefaultCurve(self):
            returnValue = libpanda._inPHc9W4fGT(self.this)
            returnObject = ParametricCurve.ParametricCurve(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getNumTimewarps(self):
            returnValue = libpanda._inPHc9WbD2P(self.this)
            return returnValue

        
        def getTimewarpCurve(self, n):
            returnValue = libpanda._inPHc9WzslK(self.this, n)
            returnObject = ParametricCurve.ParametricCurve(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getMaxT(self):
            returnValue = libpanda._inPHc9WdM36(self.this)
            return returnValue

        
        def makeEven(self, maxT, segmentsPerUnit):
            returnValue = libpanda._inPHc9W_RcH(self.this, maxT, segmentsPerUnit)
            return returnValue

        
        def faceForward(self, segmentsPerUnit):
            returnValue = libpanda._inPHc9Wfoll(self.this, segmentsPerUnit)
            return returnValue

        
        def resetMaxT(self, maxT):
            returnValue = libpanda._inPHc9W0Qq2(self.this, maxT)
            return returnValue

        
        def overloaded_evaluate_ptrConstParametricCurveCollection_float_ptrLVecBase3f_ptrLVecBase3f(self, t, xyz, hpr):
            returnValue = libpanda._inPHc9WoFUO(self.this, t, xyz.this, hpr.this)
            return returnValue

        
        def overloaded_evaluate_ptrConstParametricCurveCollection_float_ptrLMatrix4f___enum__CoordinateSystem(self, t, result, cs):
            returnValue = libpanda._inPHc9W8r8W(self.this, t, result.this, cs)
            return returnValue

        
        def overloaded_evaluate_ptrConstParametricCurveCollection_float_ptrLMatrix4f(self, t, result):
            returnValue = libpanda._inPHc9WYVab(self.this, t, result.this)
            return returnValue

        
        def evaluateT(self, t):
            returnValue = libpanda._inPHc9WdC0F(self.this, t)
            return returnValue

        
        def evaluateXyz(self, t, xyz):
            returnValue = libpanda._inPHc9WD89F(self.this, t, xyz.this)
            return returnValue

        
        def evaluateHpr(self, t, hpr):
            returnValue = libpanda._inPHc9WKyqE(self.this, t, hpr.this)
            return returnValue

        
        def overloaded_adjustXyz_ptrParametricCurveCollection_float_float_float_float(self, t, x, y, z):
            returnValue = libpanda._inPHc9WgQTI(self.this, t, x, y, z)
            return returnValue

        
        def overloaded_adjustXyz_ptrParametricCurveCollection_float_ptrConstLVecBase3f(self, t, xyz):
            returnValue = libpanda._inPHc9WAvjM(self.this, t, xyz.this)
            return returnValue

        
        def overloaded_adjustHpr_ptrParametricCurveCollection_float_float_float_float(self, t, h, p, r):
            returnValue = libpanda._inPHc9WqHPA(self.this, t, h, p, r)
            return returnValue

        
        def overloaded_adjustHpr_ptrParametricCurveCollection_float_ptrConstLVecBase3f(self, t, xyz):
            returnValue = libpanda._inPHc9WGqfE(self.this, t, xyz.this)
            return returnValue

        
        def recompute(self):
            returnValue = libpanda._inPHc9WbQSj(self.this)
            return returnValue

        
        def stitch(self, a, b):
            returnValue = libpanda._inPHc9WPN_C(self.this, a.this, b.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPHc9WVYKm(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstParametricCurveCollection_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPHc9WyVSA(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstParametricCurveCollection_ptrOstream(self, out):
            returnValue = libpanda._inPHc9WXFeh(self.this, out.this)
            return returnValue

        
        def overloaded_writeEgg_ptrParametricCurveCollection_ptrFilename___enum__CoordinateSystem(self, filename, cs):
            returnValue = libpanda._inPHc9WIxGo(self.this, filename.this, cs)
            return returnValue

        
        def overloaded_writeEgg_ptrParametricCurveCollection_ptrFilename(self, filename):
            returnValue = libpanda._inPHc9WbOcC(self.this, filename.this)
            return returnValue

        
        def overloaded_writeEgg_ptrParametricCurveCollection_ptrOstream_ptrConstFilename___enum__CoordinateSystem(self, out, filename, cs):
            returnValue = libpanda._inPHc9WML25(self.this, out.this, filename.this, cs)
            return returnValue

        
        def addCurve(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], ParametricCurve.ParametricCurve):
                    return self.overloaded_addCurve_ptrParametricCurveCollection_ptrParametricCurve(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <ParametricCurve.ParametricCurve> '
            elif numArgs == 2:
                if isinstance(_args[0], ParametricCurve.ParametricCurve):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_addCurve_ptrParametricCurveCollection_ptrParametricCurve_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <ParametricCurve.ParametricCurve> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def removeCurve(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_removeCurve_ptrParametricCurveCollection_int(_args[0])
                elif isinstance(_args[0], ParametricCurve.ParametricCurve):
                    return self.overloaded_removeCurve_ptrParametricCurveCollection_ptrParametricCurve(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <ParametricCurve.ParametricCurve> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def evaluate(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], Mat4.Mat4):
                        return self.overloaded_evaluate_ptrConstParametricCurveCollection_float_ptrLMatrix4f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Mat4.Mat4> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        if isinstance(_args[2], VBase3.VBase3):
                            return self.overloaded_evaluate_ptrConstParametricCurveCollection_float_ptrLVecBase3f_ptrLVecBase3f(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
                    elif isinstance(_args[1], Mat4.Mat4):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_evaluate_ptrConstParametricCurveCollection_float_ptrLMatrix4f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> <Mat4.Mat4> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

        
        def adjustXyz(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_adjustXyz_ptrParametricCurveCollection_float_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_adjustXyz_ptrParametricCurveCollection_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

        
        def adjustHpr(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_adjustHpr_ptrParametricCurveCollection_float_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_adjustHpr_ptrParametricCurveCollection_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

        
        def writeEgg(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Filename.Filename):
                    return self.overloaded_writeEgg_ptrParametricCurveCollection_ptrFilename(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
            elif numArgs == 2:
                if isinstance(_args[0], Filename.Filename):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_writeEgg_ptrParametricCurveCollection_ptrFilename___enum__CoordinateSystem(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
            elif numArgs == 3:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], Filename.Filename):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_writeEgg_ptrParametricCurveCollection_ptrOstream_ptrConstFilename___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Filename.Filename> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstParametricCurveCollection_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstParametricCurveCollection_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['ParametricCurveCollection'] = ParametricCurveCollection

