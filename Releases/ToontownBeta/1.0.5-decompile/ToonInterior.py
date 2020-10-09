# Source Generated with Decompyle++
# File: ToonInterior.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
import DirectNotifyGlobal
import Place
import PandaObject
import StateData
import FSM
import State
import Task
import HoodChooser
import DownloadForceAcknowledge
import HealthForceAcknowledge
import TutorialForceAcknowledge
import Trolley
import OnscreenPanel
from ToontownGlobals import *

class ToonInterior(Place.Place):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonInterior')
    
    def __init__(self, loader, parentFSM, doneEvent):
        Place.Place.__init__(self, loader, doneEvent)
        self.tfaDoneEvent = 'tfaDoneEvent'
        self.fsm = FSM.FSM('ToonInterior', [
            State.State('start', self.enterStart, self.exitStart, [
                'doorIn',
                'teleportIn']),
            State.State('walk', self.enterWalk, self.exitWalk, [
                'stickerBook',
                'doorOut',
                'teleportOut']),
            State.State('stickerBook', self.enterStickerBook, self.exitStickerBook, [
                'walk']),
            State.State('doorIn', self.enterDoorIn, self.exitDoorIn, [
                'walk']),
            State.State('doorOut', self.enterDoorOut, self.exitDoorOut, [
                'walk']),
            State.State('teleportIn', self.enterTeleportIn, self.exitTeleportIn, [
                'walk']),
            State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, []),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')
        self.parentFSM = parentFSM
        self.dnaFile = 'phase_7/models/modules/toon_interior'

    
    def enter(self, requestStatus):
        self.fsm.enterInitialState()
        messenger.send('enterToonInterior')
        toonbase.localToon.b_setParent('render')
        NametagGlobals.setMasterArrowsOn(1)
        if requestStatus['mode'] == 'teleportOut':
            self.fsm.request('teleportOut', [
                requestStatus])
        
        self.fsm.request(requestStatus['mode'], [
            requestStatus])

    
    def exit(self):
        self.ignoreAll()
        messenger.send('exitToonInterior')
        toonbase.localToon.b_setParent('hidden')
        NametagGlobals.setMasterArrowsOn(0)

    
    def load(self):
        Place.Place.load(self)
        self.parentFSM.getStateNamed('toonInterior').addChild(self.fsm)

    
    def unload(self):
        Place.Place.unload(self)
        self.parentFSM.getStateNamed('toonInterior').removeChild(self.fsm)
        del self.parentFSM
        del self.fsm
        self.ignoreAll()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    
    def setState(self, state):
        self.fsm.request(state)

    
    def getZoneId(self):
        return self.zoneID

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def enterTeleportIn(self, requestStatus):
        avId = requestStatus['avId']
        if avId == -1:
            (x, y, z, h, p, r) = toonbase.tcr.hoodMgr.getToonInteriorCenterFromId(self.loader.hood.id)
            toonbase.localToon.setPosHpr(render, x, y, z, h, p, r)
        
        Place.Place.enterTeleportIn(self, requestStatus)

    
    def enterTeleportOut(self, requestStatus):
        Place.Place.enterTeleportOut(self, requestStatus, self._ToonInterior__teleportOutDone)

    
    def __teleportOutDone(self, requestStatus):
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        if hoodId == self.loader.hood.id and zoneId == self.loader.hood.id:
            self.fsm.request('deathAck', [
                requestStatus])
        else:
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)

    
    def exitTeleportOut(self):
        pass

    
    def enterFinal(self):
        pass

    
    def exitFinal(self):
        pass

    
    def createToonInterior(self, dnaFile):
        loadDNAFile(self.loader.dnaStore, self.safeZoneStorageDNAFile, CSDefault, 0)
        node = loadDNAFile(self.loader.dnaStore, dnaFile, CSDefault, 0)
        if node.getNumParents(RenderRelation.getClassType()) == 1:
            self.geom = NodePath()
            self.geom.extendBy(node.getParent(RenderRelation.getClassType(), 0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(node)
        self.geom.flattenMedium()
        self.geom.prepareScene(base.win.getGsg())

    
    def __restartMusic(self):
        base.playMusic(self.music, looping = 1, volume = 0.8)


