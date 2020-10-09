# Source Generated with Decompyle++
# File: ParticleSystemManager.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import FFIExternalObject
import ParticleSystem
classDefined = 0

def generateClass_ParticleSystemManager():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ParticleSystemManager(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_int(self, everyNthFrame):
            self.this = libpandaphysics._inPKBUAnofO(everyNthFrame)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inPKBUADLpE()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inPKBUAkEnp:
                libpandaphysics._inPKBUAkEnp(self.this)
            

        
        def setFrameStepping(self, everyNthFrame):
            returnValue = libpandaphysics._inPKBUAaipF(self.this, everyNthFrame)
            return returnValue

        
        def getFrameStepping(self):
            returnValue = libpandaphysics._inPKBUAw3iP(self.this)
            return returnValue

        
        def attachParticlesystem(self, ps):
            returnValue = libpandaphysics._inPKBUAfdR9(self.this, ps.this)
            return returnValue

        
        def removeParticlesystem(self, ps):
            returnValue = libpandaphysics._inPKBUAlHwE(self.this, ps.this)
            return returnValue

        
        def clear(self):
            returnValue = libpandaphysics._inPKBUAMenv(self.this)
            return returnValue

        
        def doParticles(self, dt):
            returnValue = libpandaphysics._inPKBUAga7I(self.this, dt)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['ParticleSystemManager'] = ParticleSystemManager

