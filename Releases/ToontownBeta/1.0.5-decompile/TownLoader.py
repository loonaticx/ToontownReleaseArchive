# Source Generated with Decompyle++
# File: TownLoader.pyo (Python 2.0)

from ShowBaseGlobal import *
from BattleProps import *
from BattleSounds import *
from ToontownMsgTypes import *
from ToontownGlobals import *
import DirectNotifyGlobal
import Place
import PandaObject
import StateData
import FSM
import State
import Task
import HoodChooser
import DownloadForceAcknowledge
import TownBattle
import OnscreenPanel
import Toon
import BattleParticles
import DirectObject

class TownLoader(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('TownLoader')
    
    def __init__(self, hood, parentFSMState, doneEvent):
        self.hood = hood
        self.parentFSMState = parentFSMState
        self.doneEvent = doneEvent
        self.fsm = FSM.FSM('SafeZoneLoader', [
            State.State('start', self.enterStart, self.exitStart, [
                'waitForSetZoneResponse',
                'street']),
            State.State('street', self.enterStreet, self.exitStreet, [
                'waitForQuietZoneResponse']),
            State.State('toonInterior', self.enterToonInterior, self.exitToonInterior, [
                'waitForQuietZoneResponse']),
            State.State('waitForQuietZoneResponse', self.enterWaitForQuietZoneResponse, self.exitWaitForQuietZoneResponse, [
                'waitForSetZoneResponse']),
            State.State('waitForSetZoneResponse', self.enterWaitForSetZoneResponse, self.exitWaitForSetZoneResponse, [
                'waitForSetZoneComplete']),
            State.State('waitForSetZoneComplete', self.enterWaitForSetZoneComplete, self.exitWaitForSetZoneComplete, [
                'street',
                'toonInterior']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')
        self.branchZone = None
        self.streetDoneEvent = 'streetDone'
        self.townBattleDoneEvent = 'town-battle-done'

    
    def load(self, zoneId):
        self.parentFSMState.addChild(self.fsm)
        Toon.loadBattleAnims()
        self.branchZone = toonbase.tcr.hoodMgr.getBranchZone(zoneId)
        self.music = base.loadMusic(self.musicFile)
        self.battleMusic = base.loadMusic('phase_5/audio/bgm/encntr_general_bg.mid')
        self.townBattle = TownBattle.TownBattle(self.townBattleDoneEvent)
        self.townBattle.load()

    
    def unload(self):
        Toon.unloadBattleAnims()
        globalPropPool.unloadProps()
        globalSoundCache.unloadSounds()
        BattleParticles.unloadParticles()
        del self.branchZone
        self.parentFSMState.removeChild(self.fsm)
        del self.parentFSMState
        del self.fsm
        del self.streetClass
        self.landmarkBlocks.removeNode()
        del self.landmarkBlocks
        self.hood.dnaStore.resetSuitPoints()
        self.hood.dnaStore.resetBattleCells()
        del self.hood
        del self.nodeDict
        del self.zoneDict
        del self.nodeList
        self.geom.removeNode()
        del self.geom
        self.townBattle.unload()
        self.townBattle.cleanup()
        del self.townBattle
        OnscreenPanel.cleanupPanel('globalDialog')
        self.ignoreAll()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    
    def enter(self, requestStatus):
        self.fsm.enterInitialState()

    
    def exit(self):
        pass

    
    def setState(self, stateName, requestStatus):
        self.fsm.request(stateName, [
            requestStatus])

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def enterStreet(self, requestStatus):
        self.acceptOnce(self.streetDoneEvent, self.streetDone)
        self.place = self.streetClass(self, self.fsm, self.streetDoneEvent)
        self.place.load()
        self.place.enter(requestStatus)

    
    def exitStreet(self):
        self.place.exit()
        self.place.unload()
        self.place = None

    
    def streetDone(self):
        self.requestStatus = self.place.doneStatus
        self.doneStatus = self.place.doneStatus
        messenger.send(self.doneEvent)

    
    def enterToonInterior(self, flag = 0):
        pass

    
    def exitToonInterior(self):
        pass

    
    def enterDoor(self):
        pass

    
    def exitDoor(self):
        pass

    
    def handleDoorEntry(self):
        self.fsm.request('door')

    
    def enterWaitForQuietZoneResponse(self, doneStatus):
        toonbase.tcr.handler = self.handleWaitForQuietZoneResponse
        toonbase.tcr.handlerArgs = doneStatus
        toonbase.tcr.sendQuietZoneRequest()
        return None

    
    def handleWaitForQuietZoneResponse(self, msgType, di):
        if msgType == CLIENT_GET_STATE_RESP:
            self.handleQuietZoneResponseMsg(di)
        elif msgType in QUIET_ZONE_IGNORED_LIST:
            self.notify.debug('ignoring unwanted message from previous zone')
        else:
            toonbase.tcr.handlePlayGame(msgType, di)
        return None

    
    def handleQuietZoneResponseMsg(self, di):
        self.fsm.request('waitForSetZoneResponse', [
            toonbase.tcr.handlerArgs])
        return None

    
    def exitWaitForQuietZoneResponse(self):
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None
        return None

    
    def enterWaitForSetZoneResponse(self, requestStatus):
        mode = requestStatus['mode']
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        toonbase.tcr.handler = self.handleWaitForSetZoneResponse
        toonbase.tcr.handlerArgs = requestStatus
        toonbase.tcr.sendSetZoneMsg(zoneId)
        return None

    
    def handleWaitForSetZoneResponse(self, msgType, di):
        if msgType == CLIENT_GET_STATE_RESP:
            self.handleSetZoneResponse(di)
        elif msgType in QUIET_ZONE_IGNORED_LIST:
            self.notify.debug('ignoring unwanted message from previous zone')
        else:
            toonbase.tcr.handlePlayGame(msgType, di)
        return None

    
    def handleSetZoneResponse(self, di):
        self.fsm.request('waitForSetZoneComplete', [
            toonbase.tcr.handlerArgs])
        return None

    
    def exitWaitForSetZoneResponse(self):
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None
        return None

    
    def enterWaitForSetZoneComplete(self, requestStatus):
        toonbase.tcr.handler = self.handleWaitForSetZoneComplete
        toonbase.tcr.handlerArgs = requestStatus
        return None

    
    def handleWaitForSetZoneComplete(self, msgType, di):
        if msgType == CLIENT_DONE_SET_ZONE_RESP:
            self.handleSetZoneComplete(di)
        else:
            toonbase.tcr.handlePlayGame(msgType, di)

    
    def handleSetZoneComplete(self, di):
        self.fsm.request('teleportIn', [
            toonbase.tcr.handlerArgs])
        return None

    
    def exitWaitForSetZoneComplete(self):
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None
        return None

    
    def enterFinal(self):
        pass

    
    def exitFinal(self):
        pass

    
    def createHood(self, dnaFile):
        loadDNAFile(self.hood.dnaStore, 'phase_5/dna/storage_town.dna', CSDefault, 0)
        loadDNAFile(self.hood.dnaStore, self.townStorageDNAFile, CSDefault, 0)
        node = loadDNAFile(self.hood.dnaStore, dnaFile, CSDefault, 0)
        if node.getNumParents(RenderRelation.getClassType()) == 1:
            self.geom = NodePath()
            self.geom.extendBy(node.getParent(RenderRelation.getClassType(), 0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(node)
        self.makeDictionaries(self.hood.dnaStore)
        self.reparentLandmarkBlockNodes()
        self.renameFloorPolys(self.nodeList)
        self.geom.flattenMedium()
        self.geom.prepareScene(base.win.getGsg())
        self.geom.setName('town_top_level')

    
    def reparentLandmarkBlockNodes(self):
        bucket = hidden.attachNewNode('landmarkBlocks')
        self.landmarkBlocks = hidden.attachNewNode('landmarkBlocks')
        npc = self.geom.findAllMatches('**/sb*:*_landmark_*_DNARoot')
        for i in range(npc.getNumPaths()):
            nodePath = npc.getPath(i)
            nodePath.wrtReparentTo(bucket)
        

    
    def makeDictionaries(self, dnaStore):
        self.nodeDict = { }
        self.zoneDict = { }
        self.nodeList = []
        for i in range(dnaStore.getNumDNAVisGroups()):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            groupName = toonbase.tcr.hoodMgr.extractGroupName(groupFullName)
            zoneId = int(groupName)
            self.nodeDict[zoneId] = []
            self.zoneDict[zoneId] = self.geom.find('**/' + groupName)
            groupNode = self.geom.find('**/' + groupFullName)
            if groupNode.isEmpty():
                self.notify.error('Could not find visgroup')
            
            self.nodeList.append(groupNode)
            for j in range(dnaStore.getNumVisiblesInDNAVisGroup(i)):
                visName = dnaStore.getVisibleName(i, j)
                visNode = self.geom.find('**/' + visName)
                self.nodeDict[zoneId].append(visNode)
            
        
        self.hood.dnaStore.resetPlaceNodes()
        self.hood.dnaStore.resetDNAGroups()
        self.hood.dnaStore.resetDNAVisGroups()
        self.hood.dnaStore.resetDNAVisGroupsAI()

    
    def renameFloorPolys(self, nodeList):
        for i in nodeList:
            collNodePaths = i.findAllMatches('**/+CollisionNode')
            numCollNodePaths = collNodePaths.getNumPaths()
            visGroupName = i.node().getName()
            for j in range(numCollNodePaths):
                collNodePath = collNodePaths.getPath(j)
                bitMask = collNodePath.node().getIntoCollideMask()
                if bitMask.getBit(1):
                    collNodePath.node().setName(visGroupName)
                
            
        


