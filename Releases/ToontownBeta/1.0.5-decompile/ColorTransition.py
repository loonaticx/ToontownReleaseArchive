# Source Generated with Decompyle++
# File: ColorTransition.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VBase4
import TypeHandle
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import ReferenceCount
import TypeHandle
import TypedWritableReferenceCount
import ReferenceCount
import TypeHandle
import Writable
import TypedWritable
import NodeTransition
import Ostream
import TypeHandle
import OnOffTransition
import TypeHandle
classDefined = 0

def generateClass_ColorTransition():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ColorTransition(OnOffTransition.OnOffTransition, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPuUZ_go7k()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase4f(self, color):
            self.this = libpanda._inPuUZ_JAy6(color.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float_float(self, r, g, b, a):
            self.this = libpanda._inPuUZ_kCBf(r, g, b, a)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPuUZ_dJCe:
                libpanda._inPuUZ_dJCe(self.this)
            

        
        def uncolor():
            returnValue = libpanda._inPuUZ_srk7()
            returnObject = ColorTransition(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        uncolor = PandaStatic.PandaStatic(uncolor)
        
        def off():
            returnValue = libpanda._inPuUZ_bpEI()
            returnObject = ColorTransition(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        off = PandaStatic.PandaStatic(off)
        
        def getClassType():
            returnValue = libpanda._inPuUZ__bau()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_setOn_ptrColorTransition_ptrConstLVecBase4f(self, color):
            returnValue = libpanda._inPuUZ_HsTO(self.this, color.this)
            return returnValue

        
        def overloaded_setOn_ptrColorTransition_float_float_float_float(self, r, g, b, a):
            returnValue = libpanda._inPuUZ_ITgw(self.this, r, g, b, a)
            return returnValue

        
        def setUncolor(self):
            returnValue = libpanda._inPuUZ_d2_z(self.this)
            return returnValue

        
        def isReal(self):
            returnValue = libpanda._inPuUZ_gT4c(self.this)
            return returnValue

        
        def getColor(self):
            returnValue = libpanda._inPuUZ_zAoM(self.this)
            returnObject = VBase4.VBase4(None)
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
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_constructor_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
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

        
        def setOn(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setOn_ptrColorTransition_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setOn_ptrColorTransition_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '


    globals()['ColorTransition'] = ColorTransition

