# Source Generated with Decompyle++
# File: SafeZoneLoader.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from ToontownMsgTypes import *
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
import ToonInterior
import DirectObject

class SafeZoneLoader(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('SafeZoneLoader')
    
    def __init__(self, hood, parentFSMState, doneEvent):
        self.hood = hood
        self.parentFSMState = parentFSMState
        self.hoodDoneEvent = doneEvent
        self.fsm = FSM.FSM('SafeZoneLoader', [
            State.State('start', self.enterStart, self.exitStart, [
                'waitForSetZoneResponse',
                'playground']),
            State.State('playground', self.enterPlayground, self.exitPlayground, [
                'waitForQuietZoneResponse']),
            State.State('toonInterior', self.enterToonInterior, self.exitToonInterior, [
                'waitForQuietZoneResponse']),
            State.State('waitForQuietZoneResponse', self.enterWaitForQuietZoneResponse, self.exitWaitForQuietZoneResponse, [
                'waitForSetZoneResponse']),
            State.State('waitForSetZoneResponse', self.enterWaitForSetZoneResponse, self.exitWaitForSetZoneResponse, [
                'waitForSetZoneComplete']),
            State.State('waitForSetZoneComplete', self.enterWaitForSetZoneComplete, self.exitWaitForSetZoneComplete, [
                'playground',
                'toonInterior']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')
        self.safeZoneDoneEvent = 'szDone'
        self.toonInteriorDoneEvent = 'toonInteriorDone'
        self.place = None

    
    def load(self):
        self.music = base.loadMusic(self.musicFile)
        self.activityMusic = base.loadMusic(self.activityMusicFile)
        self.createSafeZone(self.dnaFile)
        self.parentFSMState.addChild(self.fsm)

    
    def unload(self):
        self.parentFSMState.removeChild(self.fsm)
        del self.parentFSMState
        self.geom.removeNode()
        del self.geom
        del self.fsm
        del self.hood
        del self.nodeList
        del self.playgroundClass
        base.unloadMusic(self.music)
        base.unloadMusic(self.activityMusic)
        del self.music
        del self.activityMusic
        self.ignoreAll()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    
    def enter(self, requestStatus):
        self.fsm.enterInitialState()
        messenger.send('enterSafeZone')

    
    def exit(self):
        messenger.send('exitSafeZone')

    
    def setState(self, stateName, requestStatus):
        self.fsm.request(stateName, [
            requestStatus])

    
    def createSafeZone(self, dnaFile):
        loadDNAFile(self.hood.dnaStore, self.safeZoneStorageDNAFile, CSDefault, 0)
        node = loadDNAFile(self.hood.dnaStore, dnaFile, CSDefault, 0)
        if node.getNumParents(RenderRelation.getClassType()) == 1:
            self.geom = NodePath()
            self.geom.extendBy(node.getParent(RenderRelation.getClassType(), 0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(node)
        self.makeDictionaries(self.hood.dnaStore)
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
        self.hood.dnaStore.resetPlaceNodes()
        self.hood.dnaStore.resetDNAGroups()
        self.hood.dnaStore.resetDNAVisGroups()
        self.hood.dnaStore.resetDNAVisGroupsAI()

    
    def removeLandmarkBlockNodes(self):
        npc = self.geom.findAllMatches('**/suit_building_origin')
        for i in range(npc.getNumPaths()):
            npc.getPath(i).removeNode()
        

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def enterPlayground(self, requestStatus):
        self.place = self.playgroundClass(self, self.fsm, self.safeZoneDoneEvent)
        self.place.load()
        self.place.enter(requestStatus)

    
    def exitPlayground(self):
        self.place.exit()
        self.place.unload()
        self.place = None

    
    def enterToonInterior(self, requestStatus):
        self.place = ToonInterior.ToonInterior(self, self.fsm, self.toonInteriorDoneEvent)
        self.place.load()
        requestStatus['mode'] = 'doorIn'
        self.place.enter(requestStatus)

    
    def exitToonInterior(self):
        self.place.exit()
        self.place.unload()
        self.place = None

    
    def enterFinal(self):
        pass

    
    def exitFinal(self):
        pass

    
    def enterWaitForQuietZoneResponse(self, doneStatus):
        toonbase.tcr.handler = self.handleWaitForQuietZoneResponse
        toonbase.tcr.handlerArgs = doneStatus
        toonbase.tcr.sendQuietZoneRequest()

    
    def exitWaitForQuietZoneResponse(self):
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None

    
    def enterWaitForSetZoneResponse(self, requestStatus):
        toonbase.tcr.handler = self.handleWaitForSetZoneResponse
        toonbase.tcr.handlerArgs = requestStatus
        zoneId = requestStatus['zoneId']
        toonbase.tcr.sendSetZoneMsg(zoneId)

    
    def exitWaitForSetZoneResponse(self):
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None

    
    def enterWaitForSetZoneComplete(self, requestStatus):
        toonbase.tcr.handler = self.handleWaitForSetZoneComplete
        toonbase.tcr.handlerArgs = requestStatus

    
    def exitWaitForSetZoneComplete(self):
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None

    
    def handleWaitForQuietZoneResponse(self, msgType, di):
        if msgType == CLIENT_GET_STATE_RESP:
            self.fsm.request('waitForSetZoneResponse', [
                toonbase.tcr.handlerArgs])
        elif msgType in QUIET_ZONE_IGNORED_LIST:
            pass
        else:
            toonbase.tcr.handlePlayGame(msgType, di)

    
    def handleWaitForSetZoneResponse(self, msgType, di):
        if msgType == CLIENT_GET_STATE_RESP:
            self.fsm.request('waitForSetZoneComplete', [
                toonbase.tcr.handlerArgs])
        elif msgType in QUIET_ZONE_IGNORED_LIST:
            pass
        else:
            toonbase.tcr.handlePlayGame(msgType, di)

    
    def handleWaitForSetZoneComplete(self, msgType, di):
        if msgType == CLIENT_DONE_SET_ZONE_RESP:
            toonbase.localToon.startChat()
            mode = toonbase.tcr.handlerArgs['mode']
            self.fsm.request(mode, [
                toonbase.tcr.handlerArgs])
        else:
            toonbase.tcr.handlePlayGame(msgType, di)


