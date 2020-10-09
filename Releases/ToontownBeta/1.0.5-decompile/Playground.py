# Source Generated with Decompyle++
# File: Playground.pyo (Python 2.0)

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

class Playground(Place.Place):
    notify = DirectNotifyGlobal.directNotify.newCategory('Playground')
    
    def __init__(self, loader, parentFSM, doneEvent):
        Place.Place.__init__(self, loader, doneEvent)
        self.tfaDoneEvent = 'tfaDoneEvent'
        self.fsm = FSM.FSM('Playground', [
            State.State('start', self.enterStart, self.exitStart, [
                'walk',
                'deathAck',
                'tunnelIn']),
            State.State('walk', self.enterWalk, self.exitWalk, [
                'stickerBook',
                'TFA',
                'DFA',
                'trolley',
                'final',
                'doorOut',
                'options']),
            State.State('stickerBook', self.enterStickerBook, self.exitStickerBook, [
                'walk',
                'DFA']),
            State.State('trolley', self.enterTrolley, self.exitTrolley, [
                'walk']),
            State.State('doorIn', self.enterDoorIn, self.exitDoorIn, [
                'walk']),
            State.State('doorOut', self.enterDoorOut, self.exitDoorOut, [
                'walk']),
            State.State('TFA', self.enterTFA, self.exitTFA, [
                'TFAReject',
                'DFA']),
            State.State('TFAReject', self.enterTFAReject, self.exitTFAReject, [
                'walk']),
            State.State('HFA', self.enterHFA, self.exitHFA, [
                'HFAReject',
                'teleportOut',
                'tunnelOut']),
            State.State('HFAReject', self.enterHFAReject, self.exitHFAReject, [
                'walk']),
            State.State('DFA', self.enterDFA, self.exitDFA, [
                'DFAReject',
                'teleportOut',
                'HFA']),
            State.State('DFAReject', self.enterDFAReject, self.exitDFAReject, [
                'walk']),
            State.State('deathAck', self.enterDeathAck, self.exitDeathAck, [
                'teleportIn']),
            State.State('teleportIn', self.enterTeleportIn, self.exitTeleportIn, [
                'walk']),
            State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, [
                'deathAck']),
            State.State('tunnelIn', self.enterTunnelIn, self.exitTunnelIn, [
                'walk']),
            State.State('tunnelOut', self.enterTunnelOut, self.exitTunnelOut, [
                'final']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')
        self.parentFSM = parentFSM
        self.tunnelOriginList = []
        self.trolleyDoneEvent = 'trolleyDone'
        self.hfaDoneEvent = 'hfaDoneEvent'

    
    def enter(self, requestStatus):
        self.fsm.enterInitialState()
        messenger.send('enterPlayground')
        base.playMusic(self.loader.music, looping = 1, volume = 0.8, restart = (self, self._Playground__restartMusic))
        self.loader.geom.reparentTo(render)
        toonbase.localToon.b_setParent('render')
        toonbase.localToon.startSky(self.loader.hood.sky)
        NametagGlobals.setMasterArrowsOn(1)
        if requestStatus['mode'] == 'teleportOut':
            self.fsm.request('deathAck', [
                requestStatus])
        elif requestStatus['mode'] == 'tunnelOut':
            self.fsm.request('tunnelIn', [
                requestStatus])
        

    
    def exit(self):
        self.ignoreAll()
        messenger.send('exitPlayground')
        toonbase.localToon.b_setParent('hidden')
        self.loader.geom.reparentTo(hidden)
        NametagGlobals.setMasterArrowsOn(0)
        toonbase.localToon.stopSky(self.loader.hood.sky)
        base.stopMusic(self.loader.music, restart = (self, self._Playground__restartMusic))

    
    def load(self):
        Place.Place.load(self)
        self.parentFSM.getStateNamed('playground').addChild(self.fsm)
        self.tunnelOriginList = toonbase.tcr.hoodMgr.addLinkTunnelHooks(self, self.loader.nodeList)

    
    def unload(self):
        self.parentFSM.getStateNamed('playground').removeChild(self.fsm)
        del self.parentFSM
        del self.fsm
        OnscreenPanel.cleanupPanel('globalDialog')
        self.ignoreAll()
        for node in self.tunnelOriginList:
            node.removeNode()
        
        del self.tunnelOriginList
        Place.Place.unload(self)

    
    def getZoneId(self):
        return self.loader.hood.id

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def enterTrolley(self):
        toonbase.localToon.laffMeter.start()
        self.accept(self.trolleyDoneEvent, self.handleTrolleyDone)
        self.trolley = Trolley.Trolley(self, self.fsm, self.trolleyDoneEvent)
        self.trolley.load()
        self.trolley.enter()
        return None

    
    def exitTrolley(self):
        toonbase.localToon.laffMeter.stop()
        self.ignore(self.trolleyDoneEvent)
        self.trolley.unload()
        self.trolley.exit()
        del self.trolley
        return None

    
    def detectedTrolleyCollision(self):
        self.fsm.request('trolley')
        return None

    
    def handleTrolleyDone(self, doneStatus):
        self.notify.debug('handling trolley done event')
        mode = doneStatus['mode']
        if mode == 'reject':
            self.fsm.request('walk')
        elif mode == 'exit':
            self.fsm.request('walk')
        elif mode == 'minigame':
            self.doneStatus = {
                'mode': 'minigame',
                'hoodId': self.loader.hood.id,
                'zoneId': doneStatus['zoneId'],
                'minigameId': doneStatus['minigameId'] }
            messenger.send(self.doneEvent)
        else:
            self.notify.error('Unknown mode: ' + mode + ' in handleTrolleyDone')

    
    def debugStartMinigame(self, zoneId, minigameId):
        self.doneStatus = {
            'mode': 'minigame',
            'hoodId': self.loader.hood.id,
            'zoneId': zoneId,
            'minigameId': minigameId }
        messenger.send(self.doneEvent)

    
    def enterTFACallback(self, requestStatus, doneStatus):
        self.tfa.exit()
        del self.tfa
        doneStatusMode = doneStatus['mode']
        if doneStatusMode == 'complete':
            self.fsm.request('DFA', [
                requestStatus])
        elif doneStatusMode == 'incomplete':
            self.fsm.request('TFAReject')
        else:
            self.notify.error('Unknown mode: %s' % doneStatusMode)
        return None

    
    def enterDFACallback(self, requestStatus, doneStatus):
        self.dfa.exit()
        del self.dfa
        ds = doneStatus['mode']
        if ds == 'complete':
            mode = requestStatus['mode']
            hoodId = requestStatus['hoodId']
            zoneId = requestStatus['zoneId']
            if mode == 'teleportOut' and hoodId == self.loader.hood.id and zoneId == self.loader.hood.id:
                self.fsm.request('teleportOut', [
                    requestStatus])
            else:
                self.fsm.request('HFA', [
                    requestStatus])
        elif ds == 'incomplete':
            self.fsm.request('DFAReject')
        else:
            self.notify.error('Unknown done status for DownloadForceAcknowledge: ' + `doneStatus`)
        return None

    
    def enterHFA(self, requestStatus):
        self.acceptOnce(self.hfaDoneEvent, self.enterHFACallback, [
            requestStatus])
        self.hfa = HealthForceAcknowledge.HealthForceAcknowledge(self.hfaDoneEvent)
        self.hfa.enter(1)

    
    def exitHFA(self):
        self.ignore(self.hfaDoneEvent)

    
    def enterHFACallback(self, requestStatus, doneStatus):
        self.hfa.exit()
        del self.hfa
        if doneStatus['mode'] == 'complete':
            self.fsm.request(requestStatus['mode'], [
                requestStatus])
        elif doneStatus['mode'] == 'incomplete':
            self.fsm.request('HFAReject')
        else:
            self.notify.error('Unknown done status for HealthForceAcknowledge: ' + `doneStatus`)
        return None

    
    def enterHFAReject(self):
        self.fsm.request('walk')

    
    def exitHFAReject(self):
        pass

    
    def enterDeathAck(self, requestStatus):
        self.deathAckBox = None
        if toonbase.localToon.hp < 1:
            self.deathAckBox = DialogBox.DialogBox(message = 'The Cogs took all your gags!\n\nYou are sad. You may not leave the playground until you are happy.', doneEvent = 'deathAck', style = DialogBox.Acknowledge)
            self.deathAckBox.show()
            self.accept('deathAck', self._Playground__handleDeathAck, extraArgs = [
                requestStatus])
        else:
            self.fsm.request('teleportIn', [
                requestStatus])
        return None

    
    def __handleDeathAck(self, requestStatus):
        doneStatus = self.deathAckBox.doneStatus
        if doneStatus == 'ok':
            self.fsm.request('teleportIn', [
                requestStatus])
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))
        return None

    
    def exitDeathAck(self):
        if self.deathAckBox:
            self.ignore('deathAck')
            self.deathAckBox.cleanup()
            del self.deathAckBox
        
        return None

    
    def enterTeleportIn(self, requestStatus):
        (x, y, z, h, p, r) = toonbase.tcr.hoodMgr.getPlaygroundCenterFromId(self.loader.hood.id)
        toonbase.localToon.setPosHpr(render, x, y, z, h, p, r)
        Place.Place.enterTeleportIn(self, requestStatus)

    
    def enterTeleportOut(self, requestStatus):
        Place.Place.enterTeleportOut(self, requestStatus, self._Playground__teleportOutDone)

    
    def __teleportOutDone(self, requestStatus):
        if hasattr(self, 'activityFsm'):
            self.activityFsm.requestFinalState()
        
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

    
    def createPlayground(self, dnaFile):
        loadDNAFile(self.loader.dnaStore, self.safeZoneStorageDNAFile, CSDefault, 0)
        node = loadDNAFile(self.loader.dnaStore, dnaFile, CSDefault, 0)
        if node.getNumParents(RenderRelation.getClassType()) == 1:
            self.geom = NodePath()
            self.geom.extendBy(node.getParent(RenderRelation.getClassType(), 0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(node)
        self.makeDictionaries(self.loader.dnaStore)
        self.tunnelOriginList = toonbase.tcr.hoodMgr.addLinkTunnelHooks(self, self.nodeList)
        self.geom.flattenMedium()
        self.geom.prepareScene(base.win.getGsg())

    
    def makeDictionaries(self, dnaStore):
        self.nodeList = []
        for i in range(dnaStore.getNumDNAVisGroups()):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            groupName = toonbase.tcr.hoodMgr.extractGroupName(groupFullName)
            groupNode = self.geom.find('**/' + groupFullName)
            if groupNode.isEmpty():
                self.notify.error('Could not find visgroup')
            
            self.nodeList.append(groupNode)
        
        self.removeLandmarkBlockNodes()
        self.loader.dnaStore.resetPlaceNodes()
        self.loader.dnaStore.resetDNAGroups()
        self.loader.dnaStore.resetDNAVisGroups()
        self.loader.dnaStore.resetDNAVisGroupsAI()

    
    def removeLandmarkBlockNodes(self):
        npc = self.geom.findAllMatches('**/suit_building_origin')
        for i in range(npc.getNumPaths()):
            npc.getPath(i).removeNode()
        

    
    def __restartMusic(self):
        base.playMusic(self.music, looping = 1, volume = 0.8)

    
    def enterTFA(self, requestStatus):
        self.acceptOnce(self.tfaDoneEvent, self.enterTFACallback, [
            requestStatus])
        self.tfa = TutorialForceAcknowledge.TutorialForceAcknowledge(self.tfaDoneEvent)
        self.tfa.enter()

    
    def exitTFA(self):
        self.ignore(self.tfaDoneEvent)

    
    def enterTFAReject(self):
        self.fsm.request('walk')

    
    def exitTFAReject(self):
        pass

    
    def requestTeleport(self, hoodId, zoneId, avId):
        self.fsm.request('DFA', [
            {
                'mode': 'teleportOut',
                'hoodId': hoodId,
                'zoneId': zoneId,
                'avId': avId }])


