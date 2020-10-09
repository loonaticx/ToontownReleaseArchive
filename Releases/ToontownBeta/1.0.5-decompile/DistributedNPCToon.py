# Source Generated with Decompyle++
# File: DistributedNPCToon.pyo (Python 2.0)

from ShowBaseGlobal import *
import DirectNotifyGlobal
import FSM
import State
import ToontownGlobals
import DistributedToon

class DistributedNPCToon(DistributedToon.DistributedToon):
    
    def __init__(self, cr):
        
        try:
            self.DistributedNPCToon_initialized
        except:
            self.DistributedNPCToon_initialized = 1
            DistributedToon.DistributedToon.__init__(self, cr)
            self._DistributedNPCToon__initCollisions()


    
    def disable(self):
        self.ignore('enter' + self.cSphereNode.getName())
        DistributedToon.DistributedToon.disable(self)

    
    def delete(self):
        
        try:
            self.DistributedNPCToon_deleted
        except:
            self.DistributedNPCToon_deleted = 1
            DistributedToon.DistributedToon.delete(self)


    
    def generate(self):
        DistributedToon.DistributedToon.generate(self)
        self.cSphereNode.setName(self.uniqueName('NPCToon'))
        self.accept('enter' + self.cSphereNode.getName(), self._DistributedNPCToon__handleCollisionSphereEnter)

    
    def __initCollisions(self):
        self.cSphere = CollisionSphere(0.0, 0.0, 0.0, 4.0)
        self.cSphere.setTangible(0)
        self.cSphereNode = CollisionNode()
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.attachNewNode(self.cSphereNode)
        self.cSphereNodePath.hide()
        self.cSphereNode.setCollideMask(ToontownGlobals.WallBitmask)

    
    def __deleteCollisions(self):
        del self.cSphere
        del self.cSphereNode
        self.cSphereNodePath.removeNode()
        del self.cSphereNodePath

    
    def __handleCollisionSphereEnter(self, collEntry):
        self.notify.info('Entering collision sphere...')
        self.sendUpdate('avatarEnter', [
            toonbase.localToon.getDoId()])


