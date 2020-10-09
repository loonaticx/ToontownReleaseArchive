# Source Generated with Decompyle++
# File: GuiBackground.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import GuiItem
import Texture
import GuiLabel
import VBase4
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

def generateClass_GuiBackground():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GuiBackground(GuiItem.GuiItem, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring_ptrGuiItem(self, parameter0, parameter1):
            self.this = libpanda._inPlRE2jxUR(parameter0, parameter1.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_atomicstring_ptrGuiItem_ptrTexture(self, parameter0, parameter1, parameter2):
            self.this = libpanda._inPlRE2c3Za(parameter0, parameter1.this, parameter2.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_atomicstring_ptrGuiItem_ptrGuiLabel(self, parameter0, parameter1, parameter2):
            self.this = libpanda._inPlRE2u1Ev(parameter0, parameter1.this, parameter2.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPlRE2Ktya:
                libpanda._inPlRE2Ktya(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPlRE22Y_u()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_setColor_ptrGuiBackground_float_float_float_float(self, parameter1, parameter2, parameter3, parameter4):
            returnValue = libpanda._inPlRE2KoQM(self.this, parameter1, parameter2, parameter3, parameter4)
            return returnValue

        
        def overloaded_setColor_ptrGuiBackground_ptrConstLVecBase4f(self, parameter1):
            returnValue = libpanda._inPlRE2I6KE(self.this, parameter1.this)
            return returnValue

        
        def getColor(self):
            returnValue = libpanda._inPlRE2Krue(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def reassert(self):
            returnValue = libpanda._inPlRE2LpkC(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], GuiItem.GuiItem):
                        return self.overloaded_constructor_atomicstring_ptrGuiItem(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <GuiItem.GuiItem> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], GuiItem.GuiItem):
                        if isinstance(_args[2], Texture.Texture):
                            return self.overloaded_constructor_atomicstring_ptrGuiItem_ptrTexture(_args[0], _args[1], _args[2])
                        elif isinstance(_args[2], GuiLabel.GuiLabel):
                            return self.overloaded_constructor_atomicstring_ptrGuiItem_ptrGuiLabel(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Texture.Texture> <GuiLabel.GuiLabel> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <GuiItem.GuiItem> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

        
        def setColor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setColor_ptrGuiBackground_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setColor_ptrGuiBackground_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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


    globals()['GuiBackground'] = GuiBackground

