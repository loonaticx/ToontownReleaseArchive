# Source Generated with Decompyle++
# File: SpriteParticleRenderer.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Texture
import BaseParticleRenderer
import NodePath
import Point2
import VBase4
import ReferenceCount
import TypeHandle
import BaseParticleRenderer
import GeomNode
classDefined = 0

def generateClass_SpriteParticleRenderer():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class SpriteParticleRenderer(BaseParticleRenderer.BaseParticleRenderer, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        STTexture = 0
        STFromNode = 1
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrTexture(self, tex):
            self.this = libpandaphysics._inPKBUAWONb(tex.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inPKBUA7DaT()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstSpriteParticleRenderer(self, copy):
            self.this = libpandaphysics._inPKBUAMl04(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inPKBUAVz5b:
                libpandaphysics._inPKBUAVz5b(self.this)
            

        
        def getSourceType(self):
            returnValue = libpandaphysics._inPKBUAKJ9R(self.this)
            return returnValue

        
        def setFromNode(self, nodePath):
            returnValue = libpandaphysics._inPKBUA41AP(self.this, nodePath.this)
            return returnValue

        
        def setTexture(self, tex):
            returnValue = libpandaphysics._inPKBUAl1bZ(self.this, tex.this)
            return returnValue

        
        def setLlUv(self, llUv):
            returnValue = libpandaphysics._inPKBUAZQRj(self.this, llUv.this)
            return returnValue

        
        def setUrUv(self, urUv):
            returnValue = libpandaphysics._inPKBUADGgf(self.this, urUv.this)
            return returnValue

        
        def setColor(self, color):
            returnValue = libpandaphysics._inPKBUAJj7q(self.this, color.this)
            return returnValue

        
        def setXScaleFlag(self, animateXRatio):
            returnValue = libpandaphysics._inPKBUAtIPC(self.this, animateXRatio)
            return returnValue

        
        def setYScaleFlag(self, animateYRatio):
            returnValue = libpandaphysics._inPKBUAFDPe(self.this, animateYRatio)
            return returnValue

        
        def setAnimAngleFlag(self, animateTheta):
            returnValue = libpandaphysics._inPKBUA8Cte(self.this, animateTheta)
            return returnValue

        
        def setInitialXScale(self, initialXScale):
            returnValue = libpandaphysics._inPKBUA_I74(self.this, initialXScale)
            return returnValue

        
        def setFinalXScale(self, finalXScale):
            returnValue = libpandaphysics._inPKBUAzpRG(self.this, finalXScale)
            return returnValue

        
        def setInitialYScale(self, initialYScale):
            returnValue = libpandaphysics._inPKBUAEJEH(self.this, initialYScale)
            return returnValue

        
        def setFinalYScale(self, finalYScale):
            returnValue = libpandaphysics._inPKBUAXRWG(self.this, finalYScale)
            return returnValue

        
        def setNonanimatedTheta(self, theta):
            returnValue = libpandaphysics._inPKBUAKA_e(self.this, theta)
            return returnValue

        
        def setAlphaBlendMethod(self, bm):
            returnValue = libpandaphysics._inPKBUAo_sQ(self.this, bm)
            return returnValue

        
        def setAlphaDisable(self, ad):
            returnValue = libpandaphysics._inPKBUAxebD(self.this, ad)
            return returnValue

        
        def getTexture(self):
            returnValue = libpandaphysics._inPKBUAVwud(self.this)
            returnObject = Texture.Texture(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getLlUv(self):
            returnValue = libpandaphysics._inPKBUAgen7(self.this)
            returnObject = Point2.Point2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getUrUv(self):
            returnValue = libpandaphysics._inPKBUAVr23(self.this)
            returnObject = Point2.Point2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getColor(self):
            returnValue = libpandaphysics._inPKBUAMsQe(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getXScaleFlag(self):
            returnValue = libpandaphysics._inPKBUA_FZl(self.this)
            return returnValue

        
        def getYScaleFlag(self):
            returnValue = libpandaphysics._inPKBUA76YB(self.this)
            return returnValue

        
        def getAnimAngleFlag(self):
            returnValue = libpandaphysics._inPKBUALRLv(self.this)
            return returnValue

        
        def getInitialXScale(self):
            returnValue = libpandaphysics._inPKBUA23Bl(self.this)
            return returnValue

        
        def getFinalXScale(self):
            returnValue = libpandaphysics._inPKBUArh8a(self.this)
            return returnValue

        
        def getInitialYScale(self):
            returnValue = libpandaphysics._inPKBUA33Iz(self.this)
            return returnValue

        
        def getFinalYScale(self):
            returnValue = libpandaphysics._inPKBUAXpBb(self.this)
            return returnValue

        
        def getNonanimatedTheta(self):
            returnValue = libpandaphysics._inPKBUAjDGo(self.this)
            return returnValue

        
        def getAlphaBlendMethod(self):
            returnValue = libpandaphysics._inPKBUAicjT(self.this)
            return returnValue

        
        def getAlphaDisable(self):
            returnValue = libpandaphysics._inPKBUAUOiv(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], Texture.Texture):
                    return self.overloaded_constructor_ptrTexture(_args[0])
                elif isinstance(_args[0], SpriteParticleRenderer):
                    return self.overloaded_constructor_ptrConstSpriteParticleRenderer(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Texture.Texture> <SpriteParticleRenderer> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        sourceFileName = 'phase_5/models/props/suit-particles'
        sourceNodeName = '**/fire'
        
        def getSourceFileName(self):
            return self.sourceFileName

        
        def setSourceFileName(self, name):
            self.sourceFileName = name

        
        def getSourceNodeName(self):
            return self.sourceNodeName

        
        def setSourceNodeName(self, name):
            self.sourceNodeName = name

        
        def setTextureFromNode(self, modelName = None, nodeName = None):
            if modelName == None:
                modelName = self.getSourceFileName()
            else:
                self.setSourceFileName(modelName)
            if nodeName == None:
                nodeName = self.getSourceNodeName()
            else:
                self.setSourceNodeName(nodeName)
            m = loader.loadModelOnce(modelName)
            if m == None:
                print "SpriteParticleRenderer: Couldn't find model: %s!" % modelName
                return None
            
            nodeName = self.getSourceNodeName()
            np = m.find(nodeName)
            if np.isEmpty():
                print "SpriteParticleRenderer: Couldn't find node: %s!" % nodeName
                m.removeNode()
                return None
            
            self.setFromNode(np)
            m.removeNode()


    globals()['SpriteParticleRenderer'] = SpriteParticleRenderer

