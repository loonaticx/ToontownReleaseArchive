# Source Generated with Decompyle++
# File: ParticleSystem.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Node
import BaseParticleRenderer
import BaseParticleEmitter
import BaseParticleFactory
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import Physical
import PhysicsManager
import PhysicalNode
import PhysicsObject
import LinearForce
import AngularForce
import TypeHandle
classDefined = 0

def generateClass_ParticleSystem():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ParticleSystem(Physical.Physical, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_int(self, poolSize):
            self.this = libpandaphysics._inPKBUA3K04(poolSize)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inPKBUAehaR()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstParticleSystem(self, copy):
            self.this = libpandaphysics._inPKBUAtVFu(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def setPoolSize(self, size):
            returnValue = libpandaphysics._inPKBUAiJrS(self.this, size)
            return returnValue

        
        def setBirthRate(self, newBr):
            returnValue = libpandaphysics._inPKBUA6GvQ(self.this, newBr)
            return returnValue

        
        def setLitterSize(self, newLs):
            returnValue = libpandaphysics._inPKBUANrZZ(self.this, newLs)
            return returnValue

        
        def setLitterSpread(self, newLs):
            returnValue = libpandaphysics._inPKBUAA_Gy(self.this, newLs)
            return returnValue

        
        def setLocalVelocityFlag(self, lv):
            returnValue = libpandaphysics._inPKBUALaZN(self.this, lv)
            return returnValue

        
        def setSystemGrowsOlderFlag(self, sgo):
            returnValue = libpandaphysics._inPKBUA6nU3(self.this, sgo)
            return returnValue

        
        def setSystemLifespan(self, sl):
            returnValue = libpandaphysics._inPKBUA4iib(self.this, sl)
            return returnValue

        
        def setSystemAge(self, age):
            returnValue = libpandaphysics._inPKBUAxgAU(self.this, age)
            return returnValue

        
        def setActiveSystemFlag(self, a):
            returnValue = libpandaphysics._inPKBUAetf6(self.this, a)
            return returnValue

        
        def setSpawnOnDeathFlag(self, sod):
            returnValue = libpandaphysics._inPKBUAw_Kx(self.this, sod)
            return returnValue

        
        def setSpawnRenderNode(self, node):
            returnValue = libpandaphysics._inPKBUADSzt(self.this, node.this)
            return returnValue

        
        def setTemplateSystemFlag(self, tsf):
            returnValue = libpandaphysics._inPKBUA80aK(self.this, tsf)
            return returnValue

        
        def setRenderParent(self, node):
            returnValue = libpandaphysics._inPKBUA_zq6(self.this, node.this)
            return returnValue

        
        def setRenderer(self, r):
            returnValue = libpandaphysics._inPKBUA41Ac(self.this, r.this)
            return returnValue

        
        def setEmitter(self, e):
            returnValue = libpandaphysics._inPKBUAIU06(self.this, e.this)
            return returnValue

        
        def setFactory(self, f):
            returnValue = libpandaphysics._inPKBUATYjU(self.this, f.this)
            return returnValue

        
        def getPoolSize(self):
            returnValue = libpandaphysics._inPKBUAQt57(self.this)
            return returnValue

        
        def getBirthRate(self):
            returnValue = libpandaphysics._inPKBUAjYU_(self.this)
            return returnValue

        
        def getLitterSize(self):
            returnValue = libpandaphysics._inPKBUARQUr(self.this)
            return returnValue

        
        def getLitterSpread(self):
            returnValue = libpandaphysics._inPKBUAwPwh(self.this)
            return returnValue

        
        def getLocalVelocityFlag(self):
            returnValue = libpandaphysics._inPKBUAo36d(self.this)
            return returnValue

        
        def getSystemGrowsOlderFlag(self):
            returnValue = libpandaphysics._inPKBUAf1bN(self.this)
            return returnValue

        
        def getSystemLifespan(self):
            returnValue = libpandaphysics._inPKBUAIfTz(self.this)
            return returnValue

        
        def getSystemAge(self):
            returnValue = libpandaphysics._inPKBUALllC(self.this)
            return returnValue

        
        def getActiveSystemFlag(self):
            returnValue = libpandaphysics._inPKBUA0DSo(self.this)
            return returnValue

        
        def getSpawnOnDeathFlag(self):
            returnValue = libpandaphysics._inPKBUArGsB(self.this)
            return returnValue

        
        def getSpawnRenderNode(self):
            returnValue = libpandaphysics._inPKBUAwd5l(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getIWasSpawnedFlag(self):
            returnValue = libpandaphysics._inPKBUAxrPW(self.this)
            return returnValue

        
        def getLivingParticles(self):
            returnValue = libpandaphysics._inPKBUA5GSp(self.this)
            return returnValue

        
        def getRenderParent(self):
            returnValue = libpandaphysics._inPKBUAJx9q(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getRenderer(self):
            returnValue = libpandaphysics._inPKBUAPwmZ(self.this)
            returnObject = BaseParticleRenderer.BaseParticleRenderer(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getEmitter(self):
            returnValue = libpandaphysics._inPKBUAZKTc(self.this)
            returnObject = BaseParticleEmitter.BaseParticleEmitter(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getFactory(self):
            returnValue = libpandaphysics._inPKBUAPQWl(self.this)
            returnObject = BaseParticleFactory.BaseParticleFactory(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def addSpawnTemplate(self, ps):
            returnValue = libpandaphysics._inPKBUAEY47(self.this, ps.this)
            return returnValue

        
        def clearSpawnTemplates(self):
            returnValue = libpandaphysics._inPKBUAYUYZ(self.this)
            return returnValue

        
        def render(self):
            returnValue = libpandaphysics._inPKBUAs1qe(self.this)
            return returnValue

        
        def update(self, dt):
            returnValue = libpandaphysics._inPKBUAv82m(self.this, dt)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_int(_args[0])
                elif isinstance(_args[0], ParticleSystem):
                    return self.overloaded_constructor_ptrConstParticleSystem(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <ParticleSystem> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['ParticleSystem'] = ParticleSystem

