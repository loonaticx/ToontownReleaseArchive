# Source Generated with Decompyle++
# File: PGFrameStyle.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase4
import VBase2
import Ostream
classDefined = 0

def generateClass_PGFrameStyle():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PGFrameStyle(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        TNone = 0
        TRidge = 5
        TBevelOut = 2
        TFlat = 1
        TBevelIn = 3
        TGroove = 4
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVvimYDmg()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstPGFrameStyle(self, copy):
            self.this = libpanda._inPVvimg7Ul(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVvimRc6A:
                libpanda._inPVvimRc6A(self.this)
            

        
        def assign(self, copy):
            returnValue = libpanda._inPVvimgtPY(self.this, copy.this)
            returnObject = PGFrameStyle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setType(self, type):
            returnValue = libpanda._inPVvimBW_1(self.this, type)
            return returnValue

        
        def getType(self):
            returnValue = libpanda._inPVvimXrTB(self.this)
            return returnValue

        
        def overloaded_setColor_ptrPGFrameStyle_float_float_float_float(self, r, g, b, a):
            returnValue = libpanda._inPVvimDEvx(self.this, r, g, b, a)
            return returnValue

        
        def overloaded_setColor_ptrPGFrameStyle_ptrConstLVecBase4f(self, color):
            returnValue = libpanda._inPVvimkdgP(self.this, color.this)
            return returnValue

        
        def getColor(self):
            returnValue = libpanda._inPVvimTFXM(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_setWidth_ptrPGFrameStyle_float_float(self, x, y):
            returnValue = libpanda._inPVvimazn4(self.this, x, y)
            return returnValue

        
        def overloaded_setWidth_ptrPGFrameStyle_ptrConstLVecBase2f(self, width):
            returnValue = libpanda._inPVvimBE_R(self.this, width.this)
            return returnValue

        
        def getWidth(self):
            returnValue = libpanda._inPVvimIXUS(self.this)
            returnObject = VBase2.VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def output(self, out):
            returnValue = libpanda._inPVvimiUhR(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], PGFrameStyle):
                    return self.overloaded_constructor_ptrConstPGFrameStyle(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <PGFrameStyle> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setColor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setColor_ptrPGFrameStyle_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setColor_ptrPGFrameStyle_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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

        
        def setWidth(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase2.VBase2):
                    return self.overloaded_setWidth_ptrPGFrameStyle_ptrConstLVecBase2f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase2.VBase2> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_setWidth_ptrPGFrameStyle_float_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['PGFrameStyle'] = PGFrameStyle

