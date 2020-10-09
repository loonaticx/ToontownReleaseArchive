# Source Generated with Decompyle++
# File: BaseParticleRenderer.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import GeomNode
import ReferenceCount
import TypeHandle
classDefined = 0

def generateClass_BaseParticleRenderer():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class BaseParticleRenderer(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        PRALPHANONE = 0
        PRALPHAOUT = 1
        PRALPHAIN = 2
        PRNOTINITIALIZEDYET = 4
        PRALPHAUSER = 3
        PPNOBLEND = 0
        PPBLENDCUBIC = 2
        PPBLENDLINEAR = 1
        
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
            if libpandaphysics and libpandaphysics._inPKBUAVz5b:
                libpandaphysics._inPKBUAVz5b(self.this)
            

        
        def getRenderNode(self):
            returnValue = libpandaphysics._inPKBUAgCUT(self.this)
            returnObject = GeomNode.GeomNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setAlphaMode(self, am):
            returnValue = libpandaphysics._inPKBUAtD6w(self.this, am)
            return returnValue

        
        def getAlphaMode(self):
            returnValue = libpandaphysics._inPKBUAVN27(self.this)
            return returnValue

        
        def setUserAlpha(self, ua):
            returnValue = libpandaphysics._inPKBUAfpHY(self.this, ua)
            return returnValue

        
        def getUserAlpha(self):
            returnValue = libpandaphysics._inPKBUAdQW9(self.this)
            return returnValue


    globals()['BaseParticleRenderer'] = BaseParticleRenderer

