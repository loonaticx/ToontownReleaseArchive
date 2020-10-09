# Source Generated with Decompyle++
# File: Street.pyo (Python 2.0)

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
import OnscreenPanel
import Toon
import BattleParticles
import Elevator
visualizeZones = base.config.GetBool('visualize-zones', 0)

class Street(Place.Place):
    notify = DirectNotifyGlobal.directNotify.newCategory('Street')
    
    def __init__(self, hood, parentFSM, doneEvent):
        Place.Place.__init__(self, hood, doneEvent)
        self.fsm = FSM.FSM('Street', [
            State.State('start', self.enterStart, self.exitStart, [
                'walk',
                'tunnelIn',
                'teleportIn']),
            State.State('walk', self.enterWalk, self.exitWalk, [
                'stickerBook',
                'WaitForBattle',
                'battle',
                'DFA',
                'doorOut',
                'elevator',
                'tunnelIn',
                'tunnelOut',
                'teleportOut']),
            State.State('stickerBook', self.enterStickerBook, self.exitStickerBook, [
                'walk',
                'battle',
                'DFA']),
            State.State('WaitForBattle', self.enterWaitForBattle, self.exitWaitForBattle, [
                'battle',
                'walk']),
            State.State('battle', self.enterBattle, self.exitBattle, [
                'walk',
                'teleportOut']),
            State.State('doorIn', self.enterDoorIn, self.exitDoorIn, [
                'walk']),
            State.State('doorOut', self.enterDoorOut, self.exitDoorOut, [
                'walk']),
            State.State('elevator', self.enterElevator, self.exitElevator, [
                'walk']),
            State.State('DFA', self.enterDFA, self.exitDFA, [
                'DFAReject',
                'teleportOut',
                'tunnelOut']),
            State.State('DFAReject', self.enterDFAReject, self.exitDFAReject, [
                'walk']),
            State.State('teleportIn', self.enterTeleportIn, self.exitTeleportIn, [
                'walk']),
            State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, [
                'teleportIn',
                'waitForQuietZoneResponse']),
            State.State('tunnelIn', self.enterTunnelIn, self.exitTunnelIn, [
                'walk']),
            State.State('tunnelOut', self.enterTunnelOut, self.exitTunnelOut, [
                'final']),
            State.State('waitForQuietZoneResponse', self.enterWaitForQuietZoneResponse, self.exitWaitForQuietZoneResponse, [
                'waitForSetZoneResponse']),
            State.State('waitForSetZoneResponse', self.enterWaitForSetZoneResponse, self.exitWaitForSetZoneResponse, [
                'waitForSetZoneComplete']),
            State.State('waitForSetZoneComplete', self.enterWaitForSetZoneComplete, self.exitWaitForSetZoneComplete, [
                'teleportIn']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')
        self.parentFSM = parentFSM
        self._Street__zoneId = None
        self.tunnelOriginList = []
        self.elevatorDoneEvent = 'elevatorDone'

    
    def enter(self, requestStatus):
        self.fsm.enterInitialState()
        base.playMusic(self.loader.music, looping = 1, volume = 0.8, restart = (self, self._Street__restartMusic))
        toonbase.localToon.b_setParent('render')
        self.loader.geom.reparentTo(render)
        self.visibilityOn()
        toonbase.localToon.setGeom(self.loader.geom)
        toonbase.localToon.setOnLevelGround(1)
        NametagGlobals.setMasterArrowsOn(1)
        toonbase.localToon.startSky(self.loader.hood.sky)
        if requestStatus['mode'] == 'teleportOut':
            self.fsm.request('teleportIn', [
                requestStatus])
        elif requestStatus['mode'] == 'tunnelOut':
            self.fsm.request('tunnelIn', [
                requestStatus])
        

    
    def exit(self):
        toonbase.localToon.b_setParent('hidden')
        self.visibilityOff()
        self.loader.geom.reparentTo(hidden)
        NametagGlobals.setMasterArrowsOn(0)
        toonbase.localToon.stopSky(self.loader.hood.sky)
        base.stopMusic(self.loader.music, restart = (self, self._Street__restartMusic))
        toonbase.localToon.setGeom(render)
        toonbase.localToon.setOnLevelGround(0)

    
    def load(self):
        Place.Place.load(self)
        Toon.loadBattleAnims()
        self.parentFSM.getStateNamed('street').addChild(self.fsm)
        self.tunnelOriginList = toonbase.tcr.hoodMgr.addLinkTunnelHooks(self, self.loader.nodeList)

    
    def unload(self):
        self.parentFSM.getStateNamed('street').removeChild(self.fsm)
        del self.parentFSM
        del self.fsm
        self.enterZone(None)
        for node in self.tunnelOriginList:
            node.removeNode()
        
        del self.tunnelOriginList
        OnscreenPanel.cleanupPanel('globalDialog')
        self.ignoreAll()
        Place.Place.unload(self)

    
    def setState(self, state, battleEvent = None):
        if battleEvent:
            self.fsm.request(state, [
                battleEvent])
        else:
            self.fsm.request(state)

    
    def getZoneId(self):
        return self._Street__zoneId

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def enterWalk(self, flag = 0):
        Place.Place.enterWalk(self, flag)
        self.accept('enterBattle', self.handleBattleEntry)

    
    def exitWalk(self):
        Place.Place.exitWalk(self)
        self.ignore('enterBattle')

    
    def enterWaitForBattle(self):
        self.notify.debug('enterWaitForBattle()')
        toonbase.localToon.loop('neutral')

    
    def exitWaitForBattle(self):
        pass

    
    def enterBattle(self, event):
        base.stopMusic(self.loader.music, restart = (self, self._Street__restartMusic))
        base.playMusic(self.loader.battleMusic, looping = 1, volume = 0.9, restart = (self, self._Street__restartBattleMusic))
        self.loader.townBattle.enter(event, self.fsm.getStateNamed('battle'))
        toonbase.localToon.b_setAnimState('off', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)

    
    def exitBattle(self):
        self.loader.townBattle.exit()
        base.stopMusic(self.loader.battleMusic)
        base.playMusic(self.loader.music, looping = 1, volume = 0.8, restart = (self, self._Street__restartMusic))
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')

    
    def handleBattleEntry(self):
        self.fsm.request('battle')

    
    def enterDoor(self):
        pass

    
    def exitDoor(self):
        pass

    
    def handleDoorEntry(self):
        self.fsm.request('door')

    
    def enterElevator(self):
        self.accept(self.elevatorDoneEvent, self.handleElevatorDone)
        self.elevator = Elevator.Elevator(self.fsm, self.elevatorDoneEvent)
        self.elevator.load()
        self.elevator.enter()
        return None

    
    def exitElevator(self):
        self.ignore(self.elevatorDoneEvent)
        self.elevator.unload()
        self.elevator.exit()
        del self.elevator
        return None

    
    def detectedElevatorCollision(self):
        self.fsm.request('elevator')
        return None

    
    def handleElevatorDone(self, doneStatus):
        self.notify.debug('handling elevator done event')
        mode = doneStatus['mode']
        if mode == 'reject':
            self.fsm.request('walk')
        elif mode == 'exit':
            self.fsm.request('walk')
        else:
            self.notify.error('Unknown mode: ' + mode + ' in handleElevatorDone')

    
    def enterTunnelIn(self, requestStatus):
        self.enterZone(requestStatus['zoneId'])
        Place.Place.enterTunnelIn(self, requestStatus)

    
    def enterTeleportIn(self, requestStatus):
        avId = requestStatus['avId']
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        if avId != -1:
            if not toonbase.tcr.doId2do.has_key(avId):
                self.fsm.request('walk', [
                    1])
                requestStatus = {
                    'mode': 'teleportOut',
                    'hoodId': hoodId,
                    'zoneId': hoodId,
                    'avId': avId }
                self._Street__teleportOutDone(requestStatus)
                return None
            
        
        self.enterZone(zoneId)
        Place.Place.enterTeleportIn(self, requestStatus)
        return None

    
    def enterTeleportOut(self, requestStatus):
        if requestStatus.has_key('battle'):
            self._Street__teleportOutDone(requestStatus)
        else:
            Place.Place.enterTeleportOut(self, requestStatus, self._Street__teleportOutDone)

    
    def __teleportOutDone(self, requestStatus):
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        if hoodId == self.loader.hood.id:
            if zoneId == self._Street__zoneId:
                self.fsm.request('teleportIn', [
                    requestStatus])
            elif toonbase.tcr.hoodMgr.getBranchZone(zoneId) == self.loader.branchZone:
                self.fsm.request('waitForQuietZoneResponse', [
                    requestStatus])
            else:
                self.doneStatus = requestStatus
                messenger.send(self.doneEvent)
        else:
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)

    
    def exitTeleportOut(self):
        pass

    
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
        avId = requestStatus['avId']
        toonbase.tcr.handler = self.handleWaitForSetZoneResponse
        toonbase.tcr.handlerArgs = requestStatus
        toonbase.tcr.sendSetZoneMsg(zoneId)

    
    def handleWaitForSetZoneResponse(self, msgType, di):
        if msgType == CLIENT_GET_STATE_RESP:
            self.handleSetZoneResponse(di)
        elif msgType in QUIET_ZONE_IGNORED_LIST:
            self.notify.debug('ignoring unwanted message from previous zone')
        else:
            toonbase.tcr.handlePlayGame(msgType, di)

    
    def handleSetZoneResponse(self, di):
        self.fsm.request('waitForSetZoneComplete', [
            toonbase.tcr.handlerArgs])

    
    def exitWaitForSetZoneResponse(self):
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None

    
    def enterWaitForSetZoneComplete(self, requestStatus):
        toonbase.tcr.handler = self.handleWaitForSetZoneComplete
        toonbase.tcr.handlerArgs = requestStatus

    
    def handleWaitForSetZoneComplete(self, msgType, di):
        if msgType == CLIENT_DONE_SET_ZONE_RESP:
            self.handleSetZoneComplete(di)
        else:
            toonbase.tcr.handlePlayGame(msgType, di)

    
    def handleSetZoneComplete(self, di):
        self.fsm.request('teleportIn', [
            toonbase.tcr.handlerArgs])

    
    def exitWaitForSetZoneComplete(self):
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None

    
    def enterFinal(self):
        pass

    
    def exitFinal(self):
        pass

    
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
                
            
        

    
    def hideAllVisibles(self):
        for i in self.loader.nodeList:
            i.stash()
        

    
    def showAllVisibles(self):
        for i in self.loader.nodeList:
            i.unstash()
        

    
    def visibilityOn(self):
        self.hideAllVisibles()
        self.accept('on-floor', self.enterZone)

    
    def visibilityOff(self):
        self.ignore('on-floor')
        self.showAllVisibles()

    
    def enterZone(self, newZone):
        if isinstance(newZone, CollisionEntry):
            newZoneId = int(newZone.getIntoNode().getName())
        else:
            newZoneId = newZone
        if self._Street__zoneId != None:
            for i in self.loader.nodeDict[self._Street__zoneId]:
                i.stash()
            
        
        if newZoneId != None:
            for i in self.loader.nodeDict[newZoneId]:
                i.unstash()
            
        
        if newZoneId != self._Street__zoneId:
            if visualizeZones:
                if self._Street__zoneId != None:
                    self.loader.zoneDict[self._Street__zoneId].clearColor()
                
                if newZoneId != None:
                    self.loader.zoneDict[newZoneId].setColor(0, 0, 1, 1, 100)
                
            
            if newZoneId != None:
                toonbase.tcr.sendSetZoneMsg(newZoneId)
                self.notify.debug('Entering Zone %d' % newZoneId)
            
            self._Street__zoneId = newZoneId
        

    
    def __restartMusic(self):
        base.playMusic(self.loader.music, looping = 1, volume = 0.8)

    
    def __restartBattleMusic(self):
        base.playMusic(self.loader.battleMusic, looping = 1, volume = 0.9)

    
    def requestTeleport(self, hoodId, zoneId, avId):
        self.fsm.request('teleportOut', [
            {
                'mode': 'teleportOut',
                'hoodId': hoodId,
                'zoneId': zoneId,
                'avId': avId }])


