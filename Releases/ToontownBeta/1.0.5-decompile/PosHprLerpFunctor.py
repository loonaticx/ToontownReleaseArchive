# Source Generated with Decompyle++
# File: PosHprLerpFunctor.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import NodePath
import Point3
import VBase3
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import LerpFunctor
import TypeHandle
classDefined = 0

def generateClass_PosHprLerpFunctor():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PosHprLerpFunctor(LerpFunctor.LerpFunctor, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f(self, np, pstart, pend, hstart, hend):
            self.this = libpanda._inPbPIP3UvU(np.this, pstart.this, pend.this, hstart.this, hend.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float(self, np, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez):
            self.this = libpanda._inPbPIP6O5f(np.this, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f_ptrNodePath(self, np, pstart, pend, hstart, hend, wrt):
            self.this = libpanda._inPbPIPEU7r(np.this, pstart.this, pend.this, hstart.this, hend.this, wrt.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float_ptrNodePath(self, np, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez, wrt):
            self.this = libpanda._inPbPIP_r2c(np.this, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez, wrt.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPbPIP82ZH()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def takeShortest(self):
            returnValue = libpanda._inPbPIPXk94(self.this)
            return returnValue

        
        def takeLongest(self):
            returnValue = libpanda._inPbPIP7ZL_(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 5:
                if isinstance(_args[0], NodePath.NodePath):
                    if isinstance(_args[1], Point3.Point3):
                        if isinstance(_args[2], Point3.Point3):
                            if isinstance(_args[3], VBase3.VBase3):
                                if isinstance(_args[4], VBase3.VBase3):
                                    return self.overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f(_args[0], _args[1], _args[2], _args[3], _args[4])
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <VBase3.VBase3> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Point3.Point3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
            elif numArgs == 6:
                if isinstance(_args[0], NodePath.NodePath):
                    if isinstance(_args[1], Point3.Point3):
                        if isinstance(_args[2], Point3.Point3):
                            if isinstance(_args[3], VBase3.VBase3):
                                if isinstance(_args[4], VBase3.VBase3):
                                    if isinstance(_args[5], NodePath.NodePath):
                                        return self.overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f_ptrNodePath(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                                    else:
                                        raise TypeError, 'Invalid argument 5, expected one of: <NodePath.NodePath> '
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <VBase3.VBase3> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Point3.Point3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
            elif numArgs == 13:
                if isinstance(_args[0], NodePath.NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                    if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                        if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                            if isinstance(_args[7], types.FloatType) or isinstance(_args[7], types.IntType):
                                                if isinstance(_args[8], types.FloatType) or isinstance(_args[8], types.IntType):
                                                    if isinstance(_args[9], types.FloatType) or isinstance(_args[9], types.IntType):
                                                        if isinstance(_args[10], types.FloatType) or isinstance(_args[10], types.IntType):
                                                            if isinstance(_args[11], types.FloatType) or isinstance(_args[11], types.IntType):
                                                                if isinstance(_args[12], types.FloatType) or isinstance(_args[12], types.IntType):
                                                                    return self.overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8], _args[9], _args[10], _args[11], _args[12])
                                                                else:
                                                                    raise TypeError, 'Invalid argument 12, expected one of: <types.FloatType> '
                                                            else:
                                                                raise TypeError, 'Invalid argument 11, expected one of: <types.FloatType> '
                                                        else:
                                                            raise TypeError, 'Invalid argument 10, expected one of: <types.FloatType> '
                                                    else:
                                                        raise TypeError, 'Invalid argument 9, expected one of: <types.FloatType> '
                                                else:
                                                    raise TypeError, 'Invalid argument 8, expected one of: <types.FloatType> '
                                            else:
                                                raise TypeError, 'Invalid argument 7, expected one of: <types.FloatType> '
                                        else:
                                            raise TypeError, 'Invalid argument 6, expected one of: <types.FloatType> '
                                    else:
                                        raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
            elif numArgs == 14:
                if isinstance(_args[0], NodePath.NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                    if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                        if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                            if isinstance(_args[7], types.FloatType) or isinstance(_args[7], types.IntType):
                                                if isinstance(_args[8], types.FloatType) or isinstance(_args[8], types.IntType):
                                                    if isinstance(_args[9], types.FloatType) or isinstance(_args[9], types.IntType):
                                                        if isinstance(_args[10], types.FloatType) or isinstance(_args[10], types.IntType):
                                                            if isinstance(_args[11], types.FloatType) or isinstance(_args[11], types.IntType):
                                                                if isinstance(_args[12], types.FloatType) or isinstance(_args[12], types.IntType):
                                                                    if isinstance(_args[13], NodePath.NodePath):
                                                                        return self.overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float_ptrNodePath(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8], _args[9], _args[10], _args[11], _args[12], _args[13])
                                                                    else:
                                                                        raise TypeError, 'Invalid argument 13, expected one of: <NodePath.NodePath> '
                                                                else:
                                                                    raise TypeError, 'Invalid argument 12, expected one of: <types.FloatType> '
                                                            else:
                                                                raise TypeError, 'Invalid argument 11, expected one of: <types.FloatType> '
                                                        else:
                                                            raise TypeError, 'Invalid argument 10, expected one of: <types.FloatType> '
                                                    else:
                                                        raise TypeError, 'Invalid argument 9, expected one of: <types.FloatType> '
                                                else:
                                                    raise TypeError, 'Invalid argument 8, expected one of: <types.FloatType> '
                                            else:
                                                raise TypeError, 'Invalid argument 7, expected one of: <types.FloatType> '
                                        else:
                                            raise TypeError, 'Invalid argument 6, expected one of: <types.FloatType> '
                                    else:
                                        raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 5 6 13 14 '


    globals()['PosHprLerpFunctor'] = PosHprLerpFunctor

