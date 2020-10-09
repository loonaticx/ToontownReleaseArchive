# Source Generated with Decompyle++
# File: GuiItem.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
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
classDefined = 0

def generateClass_GuiItem():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GuiItem(TypedReferenceCount.TypedReferenceCount, Namable.Namable, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        PNormal = 2
        PHighest = 4
        PLow = 1
        PLowest = 0
        PHigh = 3
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPlRE2Ktya:
                libpanda._inPlRE2Ktya(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPlRE2y2Gc()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_manage_ptrGuiItem_ptrGuiManager_ptrEventHandler(self, parameter1, parameter2):
            returnValue = libpanda._inPlRE2yOp8(self.this, parameter1.this, parameter2.this)
            return returnValue

        
        def overloaded_manage_ptrGuiItem_ptrGuiManager_ptrEventHandler_ptrNode(self, parameter1, parameter2, parameter3):
            returnValue = libpanda._inPlRE2MxXr(self.this, parameter1.this, parameter2.this, parameter3.this)
            return returnValue

        
        def unmanage(self):
            returnValue = libpanda._inPlRE2oNAs(self.this)
            return returnValue

        
        def freeze(self):
            returnValue = libpanda._inPlRE2vF88(self.this)
            return returnValue

        
        def thaw(self):
            returnValue = libpanda._inPlRE20T4S(self.this)
            return returnValue

        
        def overloaded_setScale_ptrGuiItem_float(self, parameter1):
            returnValue = libpanda._inPlRE24VQO(self.this, parameter1)
            return returnValue

        
        def overloaded_setScale_ptrGuiItem_float_float_float(self, parameter1, parameter2, parameter3):
            returnValue = libpanda._inPlRE2owIy(self.this, parameter1, parameter2, parameter3)
            return returnValue

        
        def setPos(self, parameter1):
            returnValue = libpanda._inPlRE2r8Xi(self.this, parameter1.this)
            return returnValue

        
        def overloaded_setPriority_ptrGuiItem_ptrGuiLabel___enum__Priority(self, parameter1, parameter2):
            returnValue = libpanda._inPlRE2Q_6j(self.this, parameter1.this, parameter2)
            return returnValue

        
        def overloaded_setPriority_ptrGuiItem_ptrGuiItem___enum__Priority(self, parameter1, parameter2):
            returnValue = libpanda._inPlRE2W20m(self.this, parameter1.this, parameter2)
            return returnValue

        
        def getScale(self):
            returnValue = libpanda._inPlRE24RlL(self.this)
            return returnValue

        
        def getScaleX(self):
            returnValue = libpanda._inPlRE2lrXc(self.this)
            return returnValue

        
        def getScaleY(self):
            returnValue = libpanda._inPlRE2KTY8(self.this)
            return returnValue

        
        def getScaleZ(self):
            returnValue = libpanda._inPlRE2eBZc(self.this)
            return returnValue

        
        def getPos(self):
            returnValue = libpanda._inPlRE2x3pT(self.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getLeft(self):
            returnValue = libpanda._inPlRE2Df74(self.this)
            return returnValue

        
        def getRight(self):
            returnValue = libpanda._inPlRE2_2z8(self.this)
            return returnValue

        
        def getBottom(self):
            returnValue = libpanda._inPlRE2IUHN(self.this)
            return returnValue

        
        def getTop(self):
            returnValue = libpanda._inPlRE2lnKh(self.this)
            return returnValue

        
        def getFrame(self):
            returnValue = libpanda._inPlRE2yIEz(self.this)
            returnObject = Vec4.Vec4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getWidth(self):
            returnValue = libpanda._inPlRE2O8z1(self.this)
            return returnValue

        
        def getHeight(self):
            returnValue = libpanda._inPlRE2neZs(self.this)
            return returnValue

        
        def getPriority(self):
            returnValue = libpanda._inPlRE24Vel(self.this)
            return returnValue

        
        def recompute(self):
            returnValue = libpanda._inPlRE2E1Hb(self.this)
            return returnValue

        
        def setDrawOrder(self, parameter1):
            returnValue = libpanda._inPlRE2TqDM(self.this, parameter1)
            return returnValue

        
        def output(self, parameter1):
            returnValue = libpanda._inPlRE2PvZV(self.this, parameter1.this)
            return returnValue

        
        def upcastToNamable(self):
            returnValue = libpanda._inPlRE2y4pw(self.this)
            returnObject = Namable.Namable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def upcastToReferenceCount(self):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxtDe8f(upcastSelf.this)
            returnObject = ReferenceCount.ReferenceCount(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getType(self):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxtuIyI(upcastSelf.this)
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getTypeIndex(self):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxtfVBU(upcastSelf.this)
            return returnValue

        
        def isOfType(self, handle):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxtgfKt(upcastSelf.this, handle.this)
            return returnValue

        
        def isExactType(self, handle):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxt0xzz(upcastSelf.this, handle.this)
            return returnValue

        
        def getRefCount(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtIP2_(upcastSelf.this)
            return returnValue

        
        def ref(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtTs5_(upcastSelf.this)
            return returnValue

        
        def unref(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtpMWy(upcastSelf.this)
            return returnValue

        
        def testRefCountIntegrity(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtoDk2(upcastSelf.this)
            return returnValue

        
        def assign(self, other):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtiPcI(upcastSelf.this, other.this)
            returnObject = Namable.Namable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setName(self, name):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtEnBW(upcastSelf.this, name)
            return returnValue

        
        def clearName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtSJVl(upcastSelf.this)
            return returnValue

        
        def hasName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtR9hC(upcastSelf.this)
            return returnValue

        
        def getName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtYaRN(upcastSelf.this)
            return returnValue

        
        def setPriority(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], GuiLabel.GuiLabel):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_setPriority_ptrGuiItem_ptrGuiLabel___enum__Priority(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                elif isinstance(_args[0], GuiItem):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_setPriority_ptrGuiItem_ptrGuiItem___enum__Priority(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GuiLabel.GuiLabel> <GuiItem> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

        
        def setScale(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setScale_ptrGuiItem_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setScale_ptrGuiItem_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

        
        def manage(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], GuiManager.GuiManager):
                    if isinstance(_args[1], EventHandler.EventHandler):
                        return self.overloaded_manage_ptrGuiItem_ptrGuiManager_ptrEventHandler(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <EventHandler.EventHandler> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GuiManager.GuiManager> '
            elif numArgs == 3:
                if isinstance(_args[0], GuiManager.GuiManager):
                    if isinstance(_args[1], EventHandler.EventHandler):
                        if isinstance(_args[2], Node.Node):
                            return self.overloaded_manage_ptrGuiItem_ptrGuiManager_ptrEventHandler_ptrNode(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Node.Node> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <EventHandler.EventHandler> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GuiManager.GuiManager> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


    globals()['GuiItem'] = GuiItem

