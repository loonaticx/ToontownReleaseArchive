# Source Generated with Decompyle++
# File: GuiFrame.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import GuiItem
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import Namable
import Ostream
import TypeHandle
import GuiItem
import GuiManager
import EventHandler
import Node
import Vec3
import GuiLabel
import Vec4
import Ostream
import Namable
import TypeHandle
import ReferenceCount
import TypedReferenceCount
classDefined = 0

def generateClass_GuiFrame():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GuiFrame(GuiItem.GuiItem, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        LEFT = 3
        ALIGNUNDER = 6
        ALIGNABOVE = 5
        UNDER = 2
        ABOVE = 1
        ALIGNRIGHT = 8
        RIGHT = 4
        NONE = 0
        ALIGNLEFT = 7
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, parameter0):
            self.this = libpanda._inPlRE26c6V(parameter0)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPlRE2Ktya:
                libpanda._inPlRE2Ktya(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPlRE2B_IW()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def addItem(self, parameter1):
            returnValue = libpanda._inPlRE24KFp(self.this, parameter1.this)
            return returnValue

        
        def removeItem(self, parameter1):
            returnValue = libpanda._inPlRE2U7kz(self.this, parameter1.this)
            return returnValue

        
        def overloaded_packItem_ptrGuiFrame_ptrGuiItem___enum__Packing_ptrGuiItem_float(self, parameter1, parameter2, parameter3, parameter4):
            returnValue = libpanda._inPlRE2S5XK(self.this, parameter1.this, parameter2, parameter3.this, parameter4)
            return returnValue

        
        def overloaded_packItem_ptrGuiFrame_ptrGuiItem___enum__Packing_ptrGuiItem(self, parameter1, parameter2, parameter3):
            returnValue = libpanda._inPlRE2LcLH(self.this, parameter1.this, parameter2, parameter3.this)
            return returnValue

        
        def clearPacking(self, parameter1):
            returnValue = libpanda._inPlRE2kzoC(self.this, parameter1.this)
            return returnValue

        
        def clearAllPacking(self):
            returnValue = libpanda._inPlRE2yrUi(self.this)
            return returnValue

        
        def isAlignedLeft(self):
            returnValue = libpanda._inPlRE2uVPj(self.this)
            return returnValue

        
        def isAlignedRight(self):
            returnValue = libpanda._inPlRE2pXAI(self.this)
            return returnValue

        
        def isAlignedTop(self):
            returnValue = libpanda._inPlRE2QR39(self.this)
            return returnValue

        
        def isAlignedBottom(self):
            returnValue = libpanda._inPlRE22gC_(self.this)
            return returnValue

        
        def getLeftGap(self):
            returnValue = libpanda._inPlRE2uEOc(self.this)
            return returnValue

        
        def getRightGap(self):
            returnValue = libpanda._inPlRE2EiRi(self.this)
            return returnValue

        
        def getTopGap(self):
            returnValue = libpanda._inPlRE2j1A3(self.this)
            return returnValue

        
        def getBottomGap(self):
            returnValue = libpanda._inPlRE2KxgX(self.this)
            return returnValue

        
        def clearLeftAlignment(self):
            returnValue = libpanda._inPlRE2ixgA(self.this)
            return returnValue

        
        def clearRightAlignment(self):
            returnValue = libpanda._inPlRE2_fI9(self.this)
            return returnValue

        
        def clearTopAlignment(self):
            returnValue = libpanda._inPlRE2rOhO(self.this)
            return returnValue

        
        def clearBottomAlignment(self):
            returnValue = libpanda._inPlRE2m8Cg(self.this)
            return returnValue

        
        def clearAllAlignment(self):
            returnValue = libpanda._inPlRE2sHHB(self.this)
            return returnValue

        
        def overloaded_alignToLeft_ptrGuiFrame_float(self, parameter1):
            returnValue = libpanda._inPlRE2qfdb(self.this, parameter1)
            return returnValue

        
        def overloaded_alignToLeft_ptrGuiFrame(self):
            returnValue = libpanda._inPlRE2BvTq(self.this)
            return returnValue

        
        def overloaded_alignToRight_ptrGuiFrame_float(self, parameter1):
            returnValue = libpanda._inPlRE2Ha_2(self.this, parameter1)
            return returnValue

        
        def overloaded_alignToRight_ptrGuiFrame(self):
            returnValue = libpanda._inPlRE2vdHR(self.this)
            return returnValue

        
        def overloaded_alignToTop_ptrGuiFrame_float(self, parameter1):
            returnValue = libpanda._inPlRE26bi_(self.this, parameter1)
            return returnValue

        
        def overloaded_alignToTop_ptrGuiFrame(self):
            returnValue = libpanda._inPlRE2D0Ab(self.this)
            return returnValue

        
        def overloaded_alignToBottom_ptrGuiFrame_float(self, parameter1):
            returnValue = libpanda._inPlRE2EqmO(self.this, parameter1)
            return returnValue

        
        def overloaded_alignToBottom_ptrGuiFrame(self):
            returnValue = libpanda._inPlRE2Y1TS(self.this)
            return returnValue

        
        def alignToTop(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_alignToTop_ptrGuiFrame()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_alignToTop_ptrGuiFrame_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def packItem(self, *_args):
            numArgs = len(_args)
            if numArgs == 3:
                if isinstance(_args[0], GuiItem.GuiItem):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], GuiItem.GuiItem):
                            return self.overloaded_packItem_ptrGuiFrame_ptrGuiItem___enum__Packing_ptrGuiItem(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <GuiItem.GuiItem> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GuiItem.GuiItem> '
            elif numArgs == 4:
                if isinstance(_args[0], GuiItem.GuiItem):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], GuiItem.GuiItem):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_packItem_ptrGuiFrame_ptrGuiItem___enum__Packing_ptrGuiItem_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <GuiItem.GuiItem> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GuiItem.GuiItem> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '

        
        def alignToLeft(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_alignToLeft_ptrGuiFrame()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_alignToLeft_ptrGuiFrame_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def alignToRight(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_alignToRight_ptrGuiFrame()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_alignToRight_ptrGuiFrame_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def alignToBottom(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_alignToBottom_ptrGuiFrame()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_alignToBottom_ptrGuiFrame_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['GuiFrame'] = GuiFrame

