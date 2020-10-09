# Source Generated with Decompyle++
# File: DNASignBaseline.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VBase4
import TextFont
import Vec3
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
import DNAGroup
import NodePath
import DNAStorage
import Ostream
import Namable
import TypeHandle
import ReferenceCount
import TypedReferenceCount
import DNANode
import VBase3
import TypeHandle
classDefined = 0

def generateClass_DNASignBaseline():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNASignBaseline(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, initialName):
            self.this = libtoontown._inPdt4ywzTT(initialName)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libtoontown._inPdt4yjBmX()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstDNASignBaseline(self, sign):
            self.this = libtoontown._inPdt4yt_lq(sign.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4yGyDv:
                libtoontown._inPdt4yGyDv(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPdt4yz_HB()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setCode(self, code):
            returnValue = libtoontown._inPdt4yM_8n(self.this, code)
            return returnValue

        
        def getCode(self):
            returnValue = libtoontown._inPdt4yXxt1(self.this)
            return returnValue

        
        def setColor(self, color):
            returnValue = libtoontown._inPdt4ynDdh(self.this, color.this)
            return returnValue

        
        def getColor(self):
            returnValue = libtoontown._inPdt4y1OWf(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setFont(self, font):
            returnValue = libtoontown._inPdt4yosVm(self.this, font.this)
            return returnValue

        
        def getFont(self):
            returnValue = libtoontown._inPdt4yVETf(self.this)
            returnObject = TextFont.TextFont(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setIndent(self, indent):
            returnValue = libtoontown._inPdt4yRZ_C(self.this, indent)
            return returnValue

        
        def getIndent(self):
            returnValue = libtoontown._inPdt4ybK_D(self.this)
            return returnValue

        
        def setKern(self, kern):
            returnValue = libtoontown._inPdt4y8spR(self.this, kern)
            return returnValue

        
        def getKern(self):
            returnValue = libtoontown._inPdt4yqOoT(self.this)
            return returnValue

        
        def getCurrentKern(self):
            returnValue = libtoontown._inPdt4yL2MV(self.this)
            return returnValue

        
        def setWiggle(self, wiggle):
            returnValue = libtoontown._inPdt4yG1X1(self.this, wiggle)
            return returnValue

        
        def getWiggle(self):
            returnValue = libtoontown._inPdt4y7la2(self.this)
            return returnValue

        
        def getCurrentWiggle(self):
            returnValue = libtoontown._inPdt4ye9iJ(self.this)
            return returnValue

        
        def setStumble(self, stumble):
            returnValue = libtoontown._inPdt4yjJEo(self.this, stumble)
            return returnValue

        
        def getStumble(self):
            returnValue = libtoontown._inPdt4yA98K(self.this)
            return returnValue

        
        def getCurrentStumble(self):
            returnValue = libtoontown._inPdt4y9z4q(self.this)
            return returnValue

        
        def setStomp(self, stomp):
            returnValue = libtoontown._inPdt4yhfe_(self.this, stomp)
            return returnValue

        
        def getStomp(self):
            returnValue = libtoontown._inPdt4yS9f_(self.this)
            return returnValue

        
        def getCurrentStomp(self):
            returnValue = libtoontown._inPdt4yEmE1(self.this)
            return returnValue

        
        def setWidth(self, width):
            returnValue = libtoontown._inPdt4y9Z_Z(self.this, width)
            return returnValue

        
        def getWidth(self):
            returnValue = libtoontown._inPdt4yQ__Z(self.this)
            return returnValue

        
        def setHeight(self, height):
            returnValue = libtoontown._inPdt4yjso_(self.this, height)
            return returnValue

        
        def getHeight(self):
            returnValue = libtoontown._inPdt4yzbrA(self.this)
            return returnValue

        
        def setFlags(self, flags):
            returnValue = libtoontown._inPdt4yTobB(self.this, flags)
            return returnValue

        
        def getFlags(self):
            returnValue = libtoontown._inPdt4ycAy5(self.this)
            return returnValue

        
        def isFirstLetterOfWord(self, letter):
            returnValue = libtoontown._inPdt4yg6Ki(self.this, letter)
            return returnValue

        
        def resetCounter(self):
            returnValue = libtoontown._inPdt4yGwmo(self.this)
            return returnValue

        
        def incCounter(self):
            returnValue = libtoontown._inPdt4ys4oR(self.this)
            return returnValue

        
        def baselineNextPosHprScale(self, pos, hpr, scale, size):
            returnValue = libtoontown._inPdt4yBZVE(self.this, pos.this, hpr.this, scale.this, size.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                elif isinstance(_args[0], DNASignBaseline):
                    return self.overloaded_constructor_ptrConstDNASignBaseline(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNASignBaseline> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['DNASignBaseline'] = DNASignBaseline

