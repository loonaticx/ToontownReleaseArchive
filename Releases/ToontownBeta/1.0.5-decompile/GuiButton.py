# Source Generated with Decompyle++
# File: GuiButton.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import GuiLabel
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
import GuiBehavior
import GuiItem
import TypeHandle
classDefined = 0

def generateClass_GuiButton():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GuiButton(GuiBehavior.GuiBehavior, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring_ptrGuiLabel_ptrGuiLabel(self, parameter0, parameter1, parameter2):
            self.this = libpanda._inPlRE2y3LW(parameter0, parameter1.this, parameter2.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_atomicstring_ptrGuiLabel_ptrGuiLabel_ptrGuiLabel(self, parameter0, parameter1, parameter2, parameter3):
            self.this = libpanda._inPlRE2_PwR(parameter0, parameter1.this, parameter2.this, parameter3.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_atomicstring_ptrGuiLabel_ptrGuiLabel_ptrGuiLabel_ptrGuiLabel_ptrGuiLabel(self, parameter0, parameter1, parameter2, parameter3, parameter4, parameter5):
            self.this = libpanda._inPlRE2kXkA(parameter0, parameter1.this, parameter2.this, parameter3.this, parameter4.this, parameter5.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPlRE2Ktya:
                libpanda._inPlRE2Ktya(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPlRE2jUPB()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def enter(self):
            returnValue = libpanda._inPlRE26S0N(self.this)
            return returnValue

        
        def exit(self):
            returnValue = libpanda._inPlRE2FyH5(self.this)
            return returnValue

        
        def up(self):
            returnValue = libpanda._inPlRE2dNLt(self.this)
            return returnValue

        
        def down(self):
            returnValue = libpanda._inPlRE2QfoI(self.this)
            return returnValue

        
        def inactive(self):
            returnValue = libpanda._inPlRE2Dbb_(self.this)
            return returnValue

        
        def click(self):
            returnValue = libpanda._inPlRE2e0Hl(self.this)
            return returnValue

        
        def isUp(self):
            returnValue = libpanda._inPlRE2filb(self.this)
            return returnValue

        
        def isOver(self):
            returnValue = libpanda._inPlRE29BY5(self.this)
            return returnValue

        
        def isActive(self):
            returnValue = libpanda._inPlRE287Rz(self.this)
            return returnValue

        
        def setUpEvent(self, parameter1):
            returnValue = libpanda._inPlRE2xFfb(self.this, parameter1)
            return returnValue

        
        def setUpRolloverEvent(self, parameter1):
            returnValue = libpanda._inPlRE2nRN9(self.this, parameter1)
            return returnValue

        
        def setDownEvent(self, parameter1):
            returnValue = libpanda._inPlRE2pLW4(self.this, parameter1)
            return returnValue

        
        def setDownRolloverEvent(self, parameter1):
            returnValue = libpanda._inPlRE2Z5yL(self.this, parameter1)
            return returnValue

        
        def setInactiveEvent(self, parameter1):
            returnValue = libpanda._inPlRE2pgKT(self.this, parameter1)
            return returnValue

        
        def setBehaviorEvent(self, parameter1):
            returnValue = libpanda._inPlRE2A1D3(self.this, parameter1)
            return returnValue

        
        def getUpEvent(self):
            returnValue = libpanda._inPlRE2Qf5L(self.this)
            return returnValue

        
        def getUpRolloverEvent(self):
            returnValue = libpanda._inPlRE2wNqZ(self.this)
            return returnValue

        
        def getDownEvent(self):
            returnValue = libpanda._inPlRE2p7a7(self.this)
            return returnValue

        
        def getDownRolloverEvent(self):
            returnValue = libpanda._inPlRE20UlC(self.this)
            return returnValue

        
        def getInactiveEvent(self):
            returnValue = libpanda._inPlRE2WO9f(self.this)
            return returnValue

        
        def getBehaviorEvent(self):
            returnValue = libpanda._inPlRE2kg1D(self.this)
            return returnValue

        
        def setUpRollover(self, parameter1):
            returnValue = libpanda._inPlRE2BB7l(self.this, parameter1.this)
            return returnValue

        
        def setDownRollover(self, parameter1):
            returnValue = libpanda._inPlRE2ZKM5(self.this, parameter1.this)
            return returnValue

        
        def setBehaviorFunctor(self, parameter1):
            returnValue = libpanda._inPlRE2ipdU(self.this, parameter1.this)
            return returnValue

        
        def getBehaviorFunctor(self):
            returnValue = libpanda._inPlRE2jxuz(self.this)
            returnObject = GuiBehavior.GuiBehavior.BehaviorFunctor(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setRolloverFunctor(self, parameter1):
            returnValue = libpanda._inPlRE23k0H(self.this, parameter1.this)
            return returnValue

        
        def getRolloverFunctor(self):
            returnValue = libpanda._inPlRE2nYIn(self.this)
            returnObject = GuiBehavior.GuiBehavior.BehaviorFunctor(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setBehaviorEventParameter(self, parameter1):
            returnValue = libpanda._inPlRE2aPnh(self.this, parameter1)
            return returnValue

        
        def getBehaviorEventParameter(self):
            returnValue = libpanda._inPlRE2ornT(self.this)
            return returnValue

        
        def setUpLabel(self, parameter1):
            returnValue = libpanda._inPlRE2gF1_(self.this, parameter1.this)
            return returnValue

        
        def setUpRolloverLabel(self, parameter1):
            returnValue = libpanda._inPlRE2awnx(self.this, parameter1.this)
            return returnValue

        
        def setDownLabel(self, parameter1):
            returnValue = libpanda._inPlRE2vA36(self.this, parameter1.this)
            return returnValue

        
        def setDownRolloverLabel(self, parameter1):
            returnValue = libpanda._inPlRE2PPJ0(self.this, parameter1.this)
            return returnValue

        
        def setInactiveLabel(self, parameter1):
            returnValue = libpanda._inPlRE2ZLXn(self.this, parameter1.this)
            return returnValue

        
        def getUpLabel(self):
            returnValue = libpanda._inPlRE2y7YA(self.this)
            returnObject = GuiLabel.GuiLabel(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getUpRolloverLabel(self):
            returnValue = libpanda._inPlRE20UOg(self.this)
            returnObject = GuiLabel.GuiLabel(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getDownLabel(self):
            returnValue = libpanda._inPlRE20AEJ(self.this)
            returnObject = GuiLabel.GuiLabel(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getDownRolloverLabel(self):
            returnValue = libpanda._inPlRE2T8RE(self.this)
            returnObject = GuiLabel.GuiLabel(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getInactiveLabel(self):
            returnValue = libpanda._inPlRE2_7yA(self.this)
            returnObject = GuiLabel.GuiLabel(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 3:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], GuiLabel.GuiLabel):
                        if isinstance(_args[2], GuiLabel.GuiLabel):
                            return self.overloaded_constructor_atomicstring_ptrGuiLabel_ptrGuiLabel(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <GuiLabel.GuiLabel> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <GuiLabel.GuiLabel> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], GuiLabel.GuiLabel):
                        if isinstance(_args[2], GuiLabel.GuiLabel):
                            if isinstance(_args[3], GuiLabel.GuiLabel):
                                return self.overloaded_constructor_atomicstring_ptrGuiLabel_ptrGuiLabel_ptrGuiLabel(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <GuiLabel.GuiLabel> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <GuiLabel.GuiLabel> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <GuiLabel.GuiLabel> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 6:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], GuiLabel.GuiLabel):
                        if isinstance(_args[2], GuiLabel.GuiLabel):
                            if isinstance(_args[3], GuiLabel.GuiLabel):
                                if isinstance(_args[4], GuiLabel.GuiLabel):
                                    if isinstance(_args[5], GuiLabel.GuiLabel):
                                        return self.overloaded_constructor_atomicstring_ptrGuiLabel_ptrGuiLabel_ptrGuiLabel_ptrGuiLabel_ptrGuiLabel(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                                    else:
                                        raise TypeError, 'Invalid argument 5, expected one of: <GuiLabel.GuiLabel> '
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <GuiLabel.GuiLabel> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <GuiLabel.GuiLabel> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <GuiLabel.GuiLabel> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <GuiLabel.GuiLabel> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 6 '


    globals()['GuiButton'] = GuiButton

