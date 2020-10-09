# Source Generated with Decompyle++
# File: SparkleParticleRenderer.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VBase4
import BaseParticleRenderer
import ReferenceCount
import TypeHandle
import BaseParticleRenderer
import GeomNode
classDefined = 0

def generateClass_SparkleParticleRenderer():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class SparkleParticleRenderer(BaseParticleRenderer.BaseParticleRenderer, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        SPNOSCALE = 0
        SPSCALE = 1
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inPKBUA4qFL()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstSparkleParticleRenderer(self, copy):
            self.this = libpandaphysics._inPKBUAH8dn(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVecBase4f_ptrConstLVecBase4f_float_float___enum__SparkleParticleLifeScale___enum__ParticleRendererAlphaMode(self, center, edge, birthRadius, deathRadius, lifeScale, alphaMode):
            self.this = libpandaphysics._inPKBUAAozb(center.this, edge.this, birthRadius, deathRadius, lifeScale, alphaMode)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inPKBUAVz5b:
                libpandaphysics._inPKBUAVz5b(self.this)
            

        
        def setCenterColor(self, c):
            returnValue = libpandaphysics._inPKBUAGCa9(self.this, c.this)
            return returnValue

        
        def setEdgeColor(self, c):
            returnValue = libpandaphysics._inPKBUAYZ6c(self.this, c.this)
            return returnValue

        
        def setBirthRadius(self, radius):
            returnValue = libpandaphysics._inPKBUAZDgV(self.this, radius)
            return returnValue

        
        def setDeathRadius(self, radius):
            returnValue = libpandaphysics._inPKBUAC_w4(self.this, radius)
            return returnValue

        
        def setLifeScale(self, parameter1):
            returnValue = libpandaphysics._inPKBUA4a96(self.this, parameter1)
            return returnValue

        
        def getCenterColor(self):
            returnValue = libpandaphysics._inPKBUA_kA6(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getEdgeColor(self):
            returnValue = libpandaphysics._inPKBUALrs4(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getBirthRadius(self):
            returnValue = libpandaphysics._inPKBUAZiEj(self.this)
            return returnValue

        
        def getDeathRadius(self):
            returnValue = libpandaphysics._inPKBUAXmVG(self.this)
            return returnValue

        
        def getLifeScale(self):
            returnValue = libpandaphysics._inPKBUAZmLm(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], SparkleParticleRenderer):
                    return self.overloaded_constructor_ptrConstSparkleParticleRenderer(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <SparkleParticleRenderer> '
            elif numArgs == 6:
                if isinstance(_args[0], VBase4.VBase4):
                    if isinstance(_args[1], VBase4.VBase4):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.IntType):
                                    if isinstance(_args[5], types.IntType):
                                        return self.overloaded_constructor_ptrConstLVecBase4f_ptrConstLVecBase4f_float_float___enum__SparkleParticleLifeScale___enum__ParticleRendererAlphaMode(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                                    else:
                                        raise TypeError, 'Invalid argument 5, expected one of: <types.IntType> '
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 6 '


    globals()['SparkleParticleRenderer'] = SparkleParticleRenderer

