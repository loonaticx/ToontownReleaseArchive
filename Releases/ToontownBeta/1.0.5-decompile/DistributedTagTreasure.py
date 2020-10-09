# Source Generated with Decompyle++
# File: DistributedTagTreasure.pyo (Python 2.0)

from ShowBaseGlobal import *
from PandaObject import *
from ClockDelta import *
from IntervalGlobal import *
import DirectNotifyGlobal
import DistributedTreasure

class DistributedTagTreasure(DistributedTreasure.DistributedTreasure):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTagTreasure')
    
    def __init__(self, cr):
        DistributedTreasure.DistributedTreasure.__init__(self, cr)
        self.av = None
        return None

    
    def disable(self):
        DistributedTreasure.DistributedTreasure.disable(self)
        if self.av == None:
            pass
        1
        self.ignore(self.av.uniqueName('disable'))
        return None

    
    def generate(self):
        DistributedTreasure.DistributedTreasure.generate(self)
        return None

    
    def getSphereRadius(self):
        return 2.0

    
    def loadModel(self):
        self.grabSound = base.loadSfx('phase_4/audio/sfx/SZ_DD_treasure.mp3')
        nodePath = self.getParentNodePath().attachNewNode(self.uniqueName('treasure'))
        self.chest = loader.loadModelOnce('phase_4/models/props/coffin')
        self.chest.reparentTo(nodePath)
        self.dropShadow = loader.loadModelOnce('phase_3/models/props/drop_shadow')
        self.dropShadow.setColor(0, 0, 0, 0.5)
        self.dropShadow.reparentTo(nodePath)
        nodePath.setScale(0.5)
        return nodePath

    
    def setGrab(self, avId, sec, usec):
        DistributedTreasure.DistributedTreasure.setGrab(self, avId, sec, usec)
        self.avId = avId
        self.dropShadow.hide()
        if self.cr.doId2do.has_key(avId):
            av = self.cr.doId2do[avId]
            self.av = av
            base.playSfx(self.grabSound)
            self.nodePath.wrtReparentTo(av)
            flytime = 1.0
            self.treasureStartPos = self.nodePath.getPos()
            self.treasureStartHpr = self.nodePath.getHpr()
            self.treasureEndPos = Point3(0, 0, 3)
            self.treasureEndHpr = Point3(0, 0, 0)
            self.treasureFlyPosHprInterval = LerpPosHprInterval(self.nodePath, flytime, pos = self.treasureEndPos, hpr = self.treasureEndHpr, startPos = self.treasureStartPos, startHpr = self.treasureStartHpr, blendType = 'easeInOut', name = self.uniqueName('flyingTreasure'))
            self.treasureFlyTrack = Track([
                self.treasureFlyPosHprInterval], self.uniqueName('treasureFly'))
            self.treasureParentIntervalAv = WrtParentInterval(self.nodePath, av, self.uniqueName('parentAv'))
            self.treasureParentIntervalHidden = ParentInterval(self.nodePath, hidden, self.uniqueName('parentHidden'))
            self.treasureParentTrack = Track([
                self.treasureParentIntervalAv,
                self.treasureParentIntervalHidden], self.uniqueName('treasureParent'))
            self.treasureParentTrack.setIntervalStartTime(self.uniqueName('parentAv'), 0)
            self.treasureParentTrack.setIntervalStartTime(self.uniqueName('parentHidden'), flytime)
            self.treasureFlyMultiTrack = MultiTrack([
                self.treasureFlyTrack,
                self.treasureParentTrack])
            self.treasureFlyMultiTrack.play()
            self.accept(self.av.uniqueName('disable'), self.handleUnexpectedExit)
        else:
            self.nodePath.reparentTo(hidden)
        return None

    
    def handleUnexpectedExit(self):
        self.notify.warning('While getting treasure, ' + str(self.avId) + ' disconnected.')
        self.treasureFlyMultiTrack.stop()
        self.nodePath.reparentTo(hidden)

    
    def handleEnterSphere(self, collEntry):
        if not (toonbase.localToon.isIt):
            self.d_requestGrab(toonbase.localToon.getDoId())
        
        return None


