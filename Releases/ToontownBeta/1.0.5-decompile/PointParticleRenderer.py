# Source Generated with Decompyle++
# File: PointParticleRenderer.pyo (Python 2.0)

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

def generateClass_PointParticleRenderer():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PointParticleRenderer(BaseParticleRenderer.BaseParticleRenderer, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        PPONECOLOR = 0
        PPBLENDVEL = 2
        PPBLENDLIFE = 1
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrConstPointParticleRenderer(self, copy):
            self.this = libpandaphysics._inPKBUA7NI3(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType___enum__ParticleRendererBlendMethod_ptrConstLVecBase4f_ptrConstLVecBase4f(self, ad, pointSize, bt, bm, sc, ec):
            self.this = libpandaphysics._inPKBUACWy3(ad, pointSize, bt, bm, sc.this, ec.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType___enum__ParticleRendererBlendMethod_ptrConstLVecBase4f(self, ad, pointSize, bt, bm, sc):
            self.this = libpandaphysics._inPKBUAHANL(ad, pointSize, bt, bm, sc.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType___enum__ParticleRendererBlendMethod(self, ad, pointSize, bt, bm):
            self.this = libpandaphysics._inPKBUAt_Ea(ad, pointSize, bt, bm)
            self.userManagesMemory = 1

        
        def overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType(self, ad, pointSize, bt):
            self.this = libpandaphysics._inPKBUAPZwy(ad, pointSize, bt)
            self.userManagesMemory = 1

        
        def overloaded_constructor___enum__ParticleRendererAlphaMode_float(self, ad, pointSize):
            self.this = libpandaphysics._inPKBUAEwut(ad, pointSize)
            self.userManagesMemory = 1

        
        def overloaded_constructor___enum__ParticleRendererAlphaMode(self, ad):
            self.this = libpandaphysics._inPKBUAZRVl(ad)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inPKBUABKwl()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inPKBUAVz5b:
                libpandaphysics._inPKBUAVz5b(self.this)
            

        
        def setPointSize(self, pointSize):
            returnValue = libpandaphysics._inPKBUAgRhj(self.this, pointSize)
            return returnValue

        
        def setStartColor(self, sc):
            returnValue = libpandaphysics._inPKBUAWfkn(self.this, sc.this)
            return returnValue

        
        def setEndColor(self, ec):
            returnValue = libpandaphysics._inPKBUA9MFQ(self.this, ec.this)
            return returnValue

        
        def setBlendType(self, bt):
            returnValue = libpandaphysics._inPKBUAluyU(self.this, bt)
            return returnValue

        
        def setBlendMethod(self, bm):
            returnValue = libpandaphysics._inPKBUAAtEJ(self.this, bm)
            return returnValue

        
        def getPointSize(self):
            returnValue = libpandaphysics._inPKBUAWXOK(self.this)
            return returnValue

        
        def getStartColor(self):
            returnValue = libpandaphysics._inPKBUA6irm(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getEndColor(self):
            returnValue = libpandaphysics._inPKBUAT4Eq(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getBlendType(self):
            returnValue = libpandaphysics._inPKBUAKWw5(self.this)
            return returnValue

        
        def getBlendMethod(self):
            returnValue = libpandaphysics._inPKBUAG5kE(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor___enum__ParticleRendererAlphaMode(_args[0])
                elif isinstance(_args[0], PointParticleRenderer):
                    return self.overloaded_constructor_ptrConstPointParticleRenderer(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PointParticleRenderer> '
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor___enum__ParticleRendererAlphaMode_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.IntType):
                                return self.overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType___enum__ParticleRendererBlendMethod(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 5:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], VBase4.VBase4):
                                    return self.overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType___enum__ParticleRendererBlendMethod_ptrConstLVecBase4f(_args[0], _args[1], _args[2], _args[3], _args[4])
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <VBase4.VBase4> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 6:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], VBase4.VBase4):
                                    if isinstance(_args[5], VBase4.VBase4):
                                        return self.overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType___enum__ParticleRendererBlendMethod_ptrConstLVecBase4f_ptrConstLVecBase4f(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                                    else:
                                        raise TypeError, 'Invalid argument 5, expected one of: <VBase4.VBase4> '
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <VBase4.VBase4> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 4 5 6 '


    globals()['PointParticleRenderer'] = PointParticleRenderer

