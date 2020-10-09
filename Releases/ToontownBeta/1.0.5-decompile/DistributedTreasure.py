# Source Generated with Decompyle++
# File: DistributedTreasure.pyo (Python 2.0)

from ShowBaseGlobal import *
from PandaObject import *
from ClockDelta import *
from IntervalGlobal import *
from ToontownGlobals import *
import CollisionNode
import CollisionSphere
import DistributedObject
import DirectNotifyGlobal

class DistributedTreasure(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTreasure')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        return None

    
    def disable(self):
        self.ignore(self.uniqueName('entertreasureSphere'))
        self.nodePath.reparentTo(hidden)
        return None

    
    def delete(self):
        self.nodePath.removeNode()
        del self.nodePath
        del self.collSphere
        self.collNodePath.removeNode()
        del self.collNodePath
        del self.collNode

    
    def generateInit(self):
        self.nodePath = self.loadModel()
        self.collSphere = CollisionSphere.CollisionSphere(0, 0, 0, self.getSphereRadius())
        self.collSphere.setTangible(0)
        self.collNode = CollisionNode.CollisionNode()
        self.collNode.setIntoCollideMask(WallBitmask)
        self.collNode.addSolid(self.collSphere)
        self.collNodePath = self.nodePath.attachNewNode(self.collNode)
        self.collNodePath.hide()
        self.collNodePath.setName(self.uniqueName('treasureSphere'))
        self.collNodePath.reparentTo(self.nodePath)
        return None

    
    def generate(self):
        self.nodePath.wrtReparentTo(render)
        self.accept(self.uniqueName('entertreasureSphere'), self.handleEnterSphere)
        return None

    
    def handleEnterSphere(self, collEntry):
        self.d_requestGrab(toonbase.localToon.getDoId())
        return None

    
    def d_requestGrab(self, avId):
        self.sendUpdate('requestGrab', [
            avId])
        return None

    
    def getSphereRadius(self):
        return 1.0

    
    def loadModel(self):
        self.notify.error('This function is pure virtual.')
        return None

    
    def getParentNodePath(self):
        return render

    
    def setPosition(self, x, y, z):
        self.nodePath.setPos(x, y, z)
        return None

    
    def setGrab(self, avId, sec, usec):
        self.ignore(self.uniqueName('entertreasureSphere'))
        return None


