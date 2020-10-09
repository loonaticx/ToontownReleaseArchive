# Source Generated with Decompyle++
# File: TextNode.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TextFont
import VBase4
import Texture
import VBase2
import Mat4
import Point3
import Node
import TypeHandle
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import BoundedObject
import BoundingVolume
import TypeHandle
import ReferenceCount
import TypeHandle
import Node
import TypeHandle
import NodeRelation
import Ostream
import BoundedObject
import ReferenceCount
import Writable
import TypedWritable
import BoundingVolume
import Namable
import Ostream
import TypeHandle
import NamedNode
import Namable
import TypeHandle
import Node
import NodeRelation
import Ostream
import BoundedObject
import ReferenceCount
classDefined = 0

def generateClass_TextNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class TextNode(NamedNode.NamedNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPpUk_qtrj(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPpUk_Byj0()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPpUk_qIT_()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def freeze(self):
            returnValue = libpanda._inPpUk_fQVZ(self.this)
            return returnValue

        
        def getFreezeLevel(self):
            returnValue = libpanda._inPpUk_4Hct(self.this)
            return returnValue

        
        def thaw(self):
            returnValue = libpanda._inPpUk_sMzW(self.this)
            return returnValue

        
        def setFont(self, font):
            returnValue = libpanda._inPpUk__e3a(self.this, font.this)
            return returnValue

        
        def getFont(self):
            returnValue = libpanda._inPpUk_HNQi(self.this)
            returnObject = TextFont.TextFont(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getLineHeight(self):
            returnValue = libpanda._inPpUk_zS_2(self.this)
            return returnValue

        
        def setSlant(self, slant):
            returnValue = libpanda._inPpUk_UZfn(self.this, slant)
            return returnValue

        
        def getSlant(self):
            returnValue = libpanda._inPpUk_RS5S(self.this)
            return returnValue

        
        def setAlign(self, alignType):
            returnValue = libpanda._inPpUk_N2SC(self.this, alignType)
            return returnValue

        
        def getAlign(self):
            returnValue = libpanda._inPpUk_7JWq(self.this)
            return returnValue

        
        def setWordwrap(self, width):
            returnValue = libpanda._inPpUk_2hMt(self.this, width)
            return returnValue

        
        def clearWordwrap(self):
            returnValue = libpanda._inPpUk_YzHt(self.this)
            return returnValue

        
        def hasWordwrap(self):
            returnValue = libpanda._inPpUk_w9U_(self.this)
            return returnValue

        
        def getWordwrap(self):
            returnValue = libpanda._inPpUk_WGIW(self.this)
            return returnValue

        
        def overloaded_setTextColor_ptrTextNode_float_float_float_float(self, r, g, b, a):
            returnValue = libpanda._inPpUk_BIHX(self.this, r, g, b, a)
            return returnValue

        
        def overloaded_setTextColor_ptrTextNode_ptrConstLVecBase4f(self, textColor):
            returnValue = libpanda._inPpUk_3l_O(self.this, textColor.this)
            return returnValue

        
        def clearTextColor(self):
            returnValue = libpanda._inPpUk_kipB(self.this)
            return returnValue

        
        def hasTextColor(self):
            returnValue = libpanda._inPpUk_eGrS(self.this)
            return returnValue

        
        def getTextColor(self):
            returnValue = libpanda._inPpUk_BGeq(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_setFrameColor_ptrTextNode_float_float_float_float(self, r, g, b, a):
            returnValue = libpanda._inPpUk_N1Tz(self.this, r, g, b, a)
            return returnValue

        
        def overloaded_setFrameColor_ptrTextNode_ptrConstLVecBase4f(self, frameColor):
            returnValue = libpanda._inPpUk__VCv(self.this, frameColor.this)
            return returnValue

        
        def getFrameColor(self):
            returnValue = libpanda._inPpUk_Z0p6(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setCardBorder(self, size, uvPortion):
            returnValue = libpanda._inPpUk_5BQk(self.this, size, uvPortion)
            return returnValue

        
        def clearCardBorder(self):
            returnValue = libpanda._inPpUk_wg6F(self.this)
            return returnValue

        
        def getCardBorderSize(self):
            returnValue = libpanda._inPpUk_ki81(self.this)
            return returnValue

        
        def getCardBorderUvPortion(self):
            returnValue = libpanda._inPpUk_tyDM(self.this)
            return returnValue

        
        def hasCardBorder(self):
            returnValue = libpanda._inPpUk_4hvs(self.this)
            return returnValue

        
        def overloaded_setCardColor_ptrTextNode_float_float_float_float(self, r, g, b, a):
            returnValue = libpanda._inPpUk_3jmF(self.this, r, g, b, a)
            return returnValue

        
        def overloaded_setCardColor_ptrTextNode_ptrConstLVecBase4f(self, cardColor):
            returnValue = libpanda._inPpUk_sDg9(self.this, cardColor.this)
            return returnValue

        
        def getCardColor(self):
            returnValue = libpanda._inPpUk_Ca_Y(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setCardTexture(self, cardTexture):
            returnValue = libpanda._inPpUk_aDUx(self.this, cardTexture.this)
            return returnValue

        
        def clearCardTexture(self):
            returnValue = libpanda._inPpUk_shSq(self.this)
            return returnValue

        
        def hasCardTexture(self):
            returnValue = libpanda._inPpUk_0588(self.this)
            return returnValue

        
        def getCardTexture(self):
            returnValue = libpanda._inPpUk_i5vU(self.this)
            returnObject = Texture.Texture(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_setShadowColor_ptrTextNode_float_float_float_float(self, r, g, b, a):
            returnValue = libpanda._inPpUk_pkru(self.this, r, g, b, a)
            return returnValue

        
        def overloaded_setShadowColor_ptrTextNode_ptrConstLVecBase4f(self, shadowColor):
            returnValue = libpanda._inPpUk_FfJk(self.this, shadowColor.this)
            return returnValue

        
        def getShadowColor(self):
            returnValue = libpanda._inPpUk_usuz(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setFrameAsMargin(self, left, right, bottom, top):
            returnValue = libpanda._inPpUk_Yw_a(self.this, left, right, bottom, top)
            return returnValue

        
        def setFrameActual(self, left, right, bottom, top):
            returnValue = libpanda._inPpUk_0ZxM(self.this, left, right, bottom, top)
            return returnValue

        
        def clearFrame(self):
            returnValue = libpanda._inPpUk_nHit(self.this)
            return returnValue

        
        def hasFrame(self):
            returnValue = libpanda._inPpUk_xkuG(self.this)
            return returnValue

        
        def isFrameAsMargin(self):
            returnValue = libpanda._inPpUk_13oH(self.this)
            return returnValue

        
        def getFrameAsSet(self):
            returnValue = libpanda._inPpUk_Exz1(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getFrameActual(self):
            returnValue = libpanda._inPpUk_F01R(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setFrameLineWidth(self, lineWidth):
            returnValue = libpanda._inPpUk_eilf(self.this, lineWidth)
            return returnValue

        
        def getFrameLineWidth(self):
            returnValue = libpanda._inPpUk_FQ1H(self.this)
            return returnValue

        
        def setFrameCorners(self, corners):
            returnValue = libpanda._inPpUk_dmsJ(self.this, corners)
            return returnValue

        
        def getFrameCorners(self):
            returnValue = libpanda._inPpUk_lwF6(self.this)
            return returnValue

        
        def setCardAsMargin(self, left, right, bottom, top):
            returnValue = libpanda._inPpUk_kP0s(self.this, left, right, bottom, top)
            return returnValue

        
        def setCardActual(self, left, right, bottom, top):
            returnValue = libpanda._inPpUk_JvW0(self.this, left, right, bottom, top)
            return returnValue

        
        def clearCard(self):
            returnValue = libpanda._inPpUk_2QTD(self.this)
            return returnValue

        
        def hasCard(self):
            returnValue = libpanda._inPpUk_mtVI(self.this)
            return returnValue

        
        def isCardAsMargin(self):
            returnValue = libpanda._inPpUk_4Pl2(self.this)
            return returnValue

        
        def getCardAsSet(self):
            returnValue = libpanda._inPpUk_BC26(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getCardActual(self):
            returnValue = libpanda._inPpUk_lJu7(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getCardTransformed(self):
            returnValue = libpanda._inPpUk_4Y42(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setShadow(self, xoffset, yoffset):
            returnValue = libpanda._inPpUk__aV_(self.this, xoffset, yoffset)
            return returnValue

        
        def clearShadow(self):
            returnValue = libpanda._inPpUk_0hq_(self.this)
            return returnValue

        
        def hasShadow(self):
            returnValue = libpanda._inPpUk_W8OX(self.this)
            return returnValue

        
        def getShadow(self):
            returnValue = libpanda._inPpUk_x8Bv(self.this)
            returnObject = VBase2.VBase2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setBin(self, bin):
            returnValue = libpanda._inPpUk__5ph(self.this, bin)
            return returnValue

        
        def clearBin(self):
            returnValue = libpanda._inPpUk_oukz(self.this)
            return returnValue

        
        def hasBin(self):
            returnValue = libpanda._inPpUk_QmNg(self.this)
            return returnValue

        
        def getBin(self):
            returnValue = libpanda._inPpUk_lpA4(self.this)
            return returnValue

        
        def setDrawOrder(self, drawOrder):
            returnValue = libpanda._inPpUk_K1S_(self.this, drawOrder)
            return returnValue

        
        def getDrawOrder(self):
            returnValue = libpanda._inPpUk_vATP(self.this)
            return returnValue

        
        def setTransform(self, transform):
            returnValue = libpanda._inPpUk_I1TJ(self.this, transform.this)
            return returnValue

        
        def getTransform(self):
            returnValue = libpanda._inPpUk_hHAR(self.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setCoordinateSystem(self, cs):
            returnValue = libpanda._inPpUk_jXkN(self.this, cs)
            return returnValue

        
        def getCoordinateSystem(self):
            returnValue = libpanda._inPpUk_11zG(self.this)
            return returnValue

        
        def setText(self, str):
            returnValue = libpanda._inPpUk_arrL(self.this, str)
            return returnValue

        
        def clearText(self):
            returnValue = libpanda._inPpUk_9KUx(self.this)
            return returnValue

        
        def hasText(self):
            returnValue = libpanda._inPpUk_jd0Z(self.this)
            return returnValue

        
        def getText(self):
            returnValue = libpanda._inPpUk_Aenx(self.this)
            return returnValue

        
        def overloaded_calcWidth_ptrConstTextNode_char(self, ch):
            returnValue = libpanda._inPpUk_xsTR(self.this, ch)
            return returnValue

        
        def overloaded_calcWidth_ptrConstTextNode_atomicstring(self, line):
            returnValue = libpanda._inPpUk_tRJl(self.this, line)
            return returnValue

        
        def wordwrapTo(self, text, wordwrapWidth, preserveEndWhitespace):
            returnValue = libpanda._inPpUk__Ixk(self.this, text, wordwrapWidth, preserveEndWhitespace)
            return returnValue

        
        def rebuild(self, needsMeasure):
            returnValue = libpanda._inPpUk_FRQ7(self.this, needsMeasure)
            return returnValue

        
        def measure(self):
            returnValue = libpanda._inPpUk__mPx(self.this)
            return returnValue

        
        def getLeft(self):
            returnValue = libpanda._inPpUk_NCtZ(self.this)
            return returnValue

        
        def getRight(self):
            returnValue = libpanda._inPpUk_5KaW(self.this)
            return returnValue

        
        def getBottom(self):
            returnValue = libpanda._inPpUk_jGMg(self.this)
            return returnValue

        
        def getTop(self):
            returnValue = libpanda._inPpUk_8Rzi(self.this)
            return returnValue

        
        def getHeight(self):
            returnValue = libpanda._inPpUk_i9NJ(self.this)
            return returnValue

        
        def getWidth(self):
            returnValue = libpanda._inPpUk_PYa2(self.this)
            return returnValue

        
        def getUpperLeft3d(self):
            returnValue = libpanda._inPpUk_H1uQ(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getLowerRight3d(self):
            returnValue = libpanda._inPpUk_sOpx(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getNumRows(self):
            returnValue = libpanda._inPpUk_xpci(self.this)
            return returnValue

        
        def generate(self):
            returnValue = libpanda._inPpUk_YmjA(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setShadowColor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setShadowColor_ptrTextNode_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setShadowColor_ptrTextNode_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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

        
        def setTextColor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setTextColor_ptrTextNode_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setTextColor_ptrTextNode_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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

        
        def setFrameColor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setFrameColor_ptrTextNode_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setFrameColor_ptrTextNode_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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

        
        def calcWidth(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_calcWidth_ptrConstTextNode_char(_args[0])
                elif isinstance(_args[0], types.StringType):
                    return self.overloaded_calcWidth_ptrConstTextNode_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def setCardColor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setCardColor_ptrTextNode_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setCardColor_ptrTextNode_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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


    globals()['TextNode'] = TextNode

