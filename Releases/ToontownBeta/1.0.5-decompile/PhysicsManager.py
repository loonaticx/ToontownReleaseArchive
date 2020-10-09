# Source Generated with Decompyle++
# File: PhysicsManager.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import FFIExternalObject
import LinearIntegrator
import AngularIntegrator
import Physical
import PhysicalNode
import LinearForce
import AngularForce
classDefined = 0

def generateClass_PhysicsManager():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PhysicsManager(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpandaphysics._inP9fJJIqAe()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inP9fJJct2P:
                libpandaphysics._inP9fJJct2P(self.this)
            

        
        def attachLinearIntegrator(self, i):
            returnValue = libpandaphysics._inP9fJJxQYZ(self.this, i.this)
            return returnValue

        
        def attachAngularIntegrator(self, i):
            returnValue = libpandaphysics._inP9fJJp63X(self.this, i.this)
            return returnValue

        
        def attachPhysical(self, p):
            returnValue = libpandaphysics._inP9fJJPvm7(self.this, p.this)
            return returnValue

        
        def attachPhysicalnode(self, p):
            returnValue = libpandaphysics._inP9fJJ67Jv(self.this, p.this)
            return returnValue

        
        def addLinearForce(self, f):
            returnValue = libpandaphysics._inP9fJJ7pEN(self.this, f.this)
            return returnValue

        
        def addAngularForce(self, f):
            returnValue = libpandaphysics._inP9fJJElwm(self.this, f.this)
            return returnValue

        
        def clearLinearForces(self):
            returnValue = libpandaphysics._inP9fJJifDw(self.this)
            return returnValue

        
        def clearAngularForces(self):
            returnValue = libpandaphysics._inP9fJJUgDA(self.this)
            return returnValue

        
        def clearPhysicals(self):
            returnValue = libpandaphysics._inP9fJJETHU(self.this)
            return returnValue

        
        def removePhysical(self, p):
            returnValue = libpandaphysics._inP9fJJKQ_e(self.this, p.this)
            return returnValue

        
        def removeLinearForce(self, f):
            returnValue = libpandaphysics._inP9fJJ3Opv(self.this, f.this)
            return returnValue

        
        def removeAngularForce(self, f):
            returnValue = libpandaphysics._inP9fJJZzkY(self.this, f.this)
            return returnValue

        
        def doPhysics(self, dt):
            returnValue = libpandaphysics._inP9fJJKCKp(self.this, dt)
            return returnValue


    globals()['PhysicsManager'] = PhysicsManager

