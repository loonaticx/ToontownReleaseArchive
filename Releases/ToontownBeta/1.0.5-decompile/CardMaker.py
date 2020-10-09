# Source Generated with Decompyle++
# File: CardMaker.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Point2
import VBase4
import Node
classDefined = 0

def generateClass_CardMaker():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CardMaker(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPXs2xIh_5()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPXs2x7ekv:
                libpanda._inPXs2x7ekv(self.this)
            

        
        def reset(self):
            returnValue = libpanda._inPXs2xVISh(self.this)
            return returnValue

        
        def setUvRange(self, ll, ur):
            returnValue = libpanda._inPXs2x3Tgw(self.this, ll.this, ur.this)
            return returnValue

        
        def setHasUvs(self, flag):
            returnValue = libpanda._inPXs2x36_I(self.this, flag)
            return returnValue

        
        def overloaded_setFrame_ptrCardMaker_float_float_float_float(self, left, right, bottom, top):
            returnValue = libpanda._inPXs2xwLU3(self.this, left, right, bottom, top)
            return returnValue

        
        def overloaded_setFrame_ptrCardMaker_ptrConstLVecBase4f(self, frame):
            returnValue = libpanda._inPXs2xDoM1(self.this, frame.this)
            return returnValue

        
        def overloaded_setColor_ptrCardMaker_float_float_float_float(self, r, g, b, a):
            returnValue = libpanda._inPXs2xtrvM(self.this, r, g, b, a)
            return returnValue

        
        def overloaded_setColor_ptrCardMaker_ptrConstLVecBase4f(self, color):
            returnValue = libpanda._inPXs2xh_pK(self.this, color.this)
            return returnValue

        
        def setSourceGeometry(self, node, frame):
            returnValue = libpanda._inPXs2xoFtu(self.this, node.this, frame.this)
            return returnValue

        
        def clearSourceGeometry(self):
            returnValue = libpanda._inPXs2xAPZC(self.this)
            return returnValue

        
        def generate(self):
            returnValue = libpanda._inPXs2xl2Lf(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setFrame(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setFrame_ptrCardMaker_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setFrame_ptrCardMaker_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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

        
        def setColor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setColor_ptrCardMaker_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setColor_ptrCardMaker_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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


    globals()['CardMaker'] = CardMaker

