# Source Generated with Decompyle++
# File: GuiLabel.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Vec3
import VBase4
import Ostream
import Texture
import TextFont
import Node
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
classDefined = 0

def generateClass_GuiLabel():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GuiLabel(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        PHIGHER = 3
        PHIGHEST = 4
        PNONE = 0
        PLOWEST = 1
        PLOWER = 2
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPlRE2ynP7()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def makeSimpleTextureLabel(parameter0):
            returnValue = libpanda._inPlRE2XutL(parameter0.this)
            returnObject = GuiLabel(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        makeSimpleTextureLabel = PandaStatic.PandaStatic(makeSimpleTextureLabel)
        
        def overloaded_makeSimpleTextLabel_atomicstring_ptrTextFont_ptrTexture(parameter0, parameter1, parameter2):
            returnValue = libpanda._inPlRE2FQB_(parameter0, parameter1.this, parameter2.this)
            returnObject = GuiLabel(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        overloaded_makeSimpleTextLabel_atomicstring_ptrTextFont_ptrTexture = PandaStatic.PandaStatic(overloaded_makeSimpleTextLabel_atomicstring_ptrTextFont_ptrTexture)
        
        def overloaded_makeSimpleTextLabel_atomicstring_ptrTextFont(parameter0, parameter1):
            returnValue = libpanda._inPlRE29L1r(parameter0, parameter1.this)
            returnObject = GuiLabel(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        overloaded_makeSimpleTextLabel_atomicstring_ptrTextFont = PandaStatic.PandaStatic(overloaded_makeSimpleTextLabel_atomicstring_ptrTextFont)
        
        def makeSimpleCardLabel():
            returnValue = libpanda._inPlRE2Aor7()
            returnObject = GuiLabel(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        makeSimpleCardLabel = PandaStatic.PandaStatic(makeSimpleCardLabel)
        
        def makeNullLabel():
            returnValue = libpanda._inPlRE2gDk9()
            returnObject = GuiLabel(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        makeNullLabel = PandaStatic.PandaStatic(makeNullLabel)
        
        def overloaded_makeModelLabel_ptrNode_float_float(parameter0, parameter1, parameter2):
            returnValue = libpanda._inPlRE2uAjf(parameter0.this, parameter1, parameter2)
            returnObject = GuiLabel(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        overloaded_makeModelLabel_ptrNode_float_float = PandaStatic.PandaStatic(overloaded_makeModelLabel_ptrNode_float_float)
        
        def overloaded_makeModelLabel_ptrNode_float_float_float_float(parameter0, parameter1, parameter2, parameter3, parameter4):
            returnValue = libpanda._inPlRE26lpq(parameter0.this, parameter1, parameter2, parameter3, parameter4)
            returnObject = GuiLabel(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        overloaded_makeModelLabel_ptrNode_float_float_float_float = PandaStatic.PandaStatic(overloaded_makeModelLabel_ptrNode_float_float_float_float)
        
        def getClassType():
            returnValue = libpanda._inPlRE2S1Dn()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def freeze(self):
            returnValue = libpanda._inPlRE2GaGB(self.this)
            return returnValue

        
        def thaw(self):
            returnValue = libpanda._inPlRE2THj_(self.this)
            return returnValue

        
        def getWidth(self):
            returnValue = libpanda._inPlRE2714e(self.this)
            return returnValue

        
        def getHeight(self):
            returnValue = libpanda._inPlRE2eFiI(self.this)
            return returnValue

        
        def setWidth(self, parameter1):
            returnValue = libpanda._inPlRE2gnwy(self.this, parameter1)
            return returnValue

        
        def setHeight(self, parameter1):
            returnValue = libpanda._inPlRE2Vxln(self.this, parameter1)
            return returnValue

        
        def overloaded_setScale_ptrGuiLabel_float(self, parameter1):
            returnValue = libpanda._inPlRE2Dcbs(self.this, parameter1)
            return returnValue

        
        def overloaded_setScale_ptrGuiLabel_float_float_float(self, parameter1, parameter2, parameter3):
            returnValue = libpanda._inPlRE2agZq(self.this, parameter1, parameter2, parameter3)
            return returnValue

        
        def setMirrorX(self, parameter1):
            returnValue = libpanda._inPlRE2Swvl(self.this, parameter1)
            return returnValue

        
        def setMirrorY(self, parameter1):
            returnValue = libpanda._inPlRE2SIhv(self.this, parameter1)
            return returnValue

        
        def overloaded_setPos_ptrGuiLabel_float_float_float(self, parameter1, parameter2, parameter3):
            returnValue = libpanda._inPlRE2B3QQ(self.this, parameter1, parameter2, parameter3)
            return returnValue

        
        def overloaded_setPos_ptrGuiLabel_ptrConstLVector3f(self, parameter1):
            returnValue = libpanda._inPlRE2Ukbw(self.this, parameter1.this)
            return returnValue

        
        def getScale(self):
            returnValue = libpanda._inPlRE2Gb0X(self.this)
            return returnValue

        
        def getMirrorX(self):
            returnValue = libpanda._inPlRE26de9(self.this)
            return returnValue

        
        def getMirrorY(self):
            returnValue = libpanda._inPlRE251PH(self.this)
            return returnValue

        
        def getPos(self):
            returnValue = libpanda._inPlRE2ToLZ(self.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_setForegroundColor_ptrGuiLabel_float_float_float_float(self, parameter1, parameter2, parameter3, parameter4):
            returnValue = libpanda._inPlRE2nFdL(self.this, parameter1, parameter2, parameter3, parameter4)
            return returnValue

        
        def overloaded_setForegroundColor_ptrGuiLabel_ptrConstLVecBase4f(self, parameter1):
            returnValue = libpanda._inPlRE2v60C(self.this, parameter1.this)
            return returnValue

        
        def overloaded_setBackgroundColor_ptrGuiLabel_float_float_float_float(self, parameter1, parameter2, parameter3, parameter4):
            returnValue = libpanda._inPlRE2PeXp(self.this, parameter1, parameter2, parameter3, parameter4)
            return returnValue

        
        def overloaded_setBackgroundColor_ptrGuiLabel_ptrConstLVecBase4f(self, parameter1):
            returnValue = libpanda._inPlRE2L4wg(self.this, parameter1.this)
            return returnValue

        
        def getForegroundColor(self):
            returnValue = libpanda._inPlRE2a_9a(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getBackgroundColor(self):
            returnValue = libpanda._inPlRE24h44(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setText(self, parameter1):
            returnValue = libpanda._inPlRE2DJcz(self.this, parameter1)
            return returnValue

        
        def overloaded_setShadowColor_ptrGuiLabel_float_float_float_float(self, parameter1, parameter2, parameter3, parameter4):
            returnValue = libpanda._inPlRE2XwbW(self.this, parameter1, parameter2, parameter3, parameter4)
            return returnValue

        
        def overloaded_setShadowColor_ptrGuiLabel_ptrConstLVecBase4f(self, parameter1):
            returnValue = libpanda._inPlRE2ja5L(self.this, parameter1.this)
            return returnValue

        
        def setShadow(self, parameter1, parameter2):
            returnValue = libpanda._inPlRE2NpFn(self.this, parameter1, parameter2)
            return returnValue

        
        def setAlign(self, parameter1):
            returnValue = libpanda._inPlRE2i6Dq(self.this, parameter1)
            return returnValue

        
        def recompute(self):
            returnValue = libpanda._inPlRE25R6G(self.this)
            return returnValue

        
        def lessThan(self, parameter1):
            returnValue = libpanda._inPlRE2xUp2(self.this, parameter1.this)
            return returnValue

        
        def setPriority(self, parameter1, parameter2):
            returnValue = libpanda._inPlRE232qH(self.this, parameter1.this, parameter2)
            return returnValue

        
        def softSetDrawOrder(self, parameter1):
            returnValue = libpanda._inPlRE2TZNx(self.this, parameter1)
            return returnValue

        
        def setDrawOrder(self, parameter1):
            returnValue = libpanda._inPlRE2GJDm(self.this, parameter1)
            return returnValue

        
        def hasHardDrawOrder(self):
            returnValue = libpanda._inPlRE2V4NJ(self.this)
            return returnValue

        
        def getDrawOrder(self):
            returnValue = libpanda._inPlRE2AAD3(self.this)
            return returnValue

        
        def write(self, parameter1):
            returnValue = libpanda._inPlRE2y_rX(self.this, parameter1.this)
            return returnValue

        
        def makeModelLabel(*_args):
            numArgs = len(_args)
            if numArgs == 3:
                if isinstance(_args[0], Node.Node):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return GuiLabel.overloaded_makeModelLabel_ptrNode_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Node.Node> '
            elif numArgs == 5:
                if isinstance(_args[0], Node.Node):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                    return GuiLabel.overloaded_makeModelLabel_ptrNode_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4])
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Node.Node> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 5 '

        makeModelLabel = PandaStatic.PandaStatic(makeModelLabel)
        
        def makeSimpleTextLabel(*_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], TextFont.TextFont):
                        return GuiLabel.overloaded_makeSimpleTextLabel_atomicstring_ptrTextFont(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <TextFont.TextFont> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], TextFont.TextFont):
                        if isinstance(_args[2], Texture.Texture):
                            return GuiLabel.overloaded_makeSimpleTextLabel_atomicstring_ptrTextFont_ptrTexture(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Texture.Texture> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <TextFont.TextFont> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

        makeSimpleTextLabel = PandaStatic.PandaStatic(makeSimpleTextLabel)
        
        def setShadowColor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setShadowColor_ptrGuiLabel_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setShadowColor_ptrGuiLabel_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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

        
        def setForegroundColor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setForegroundColor_ptrGuiLabel_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setForegroundColor_ptrGuiLabel_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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

        
        def setBackgroundColor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setBackgroundColor_ptrGuiLabel_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setBackgroundColor_ptrGuiLabel_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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

        
        def setScale(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setScale_ptrGuiLabel_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setScale_ptrGuiLabel_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

        
        def setPos(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Vec3.Vec3):
                    return self.overloaded_setPos_ptrGuiLabel_ptrConstLVector3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Vec3.Vec3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setPos_ptrGuiLabel_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


    globals()['GuiLabel'] = GuiLabel

