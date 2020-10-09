# Source Generated with Decompyle++
# File: Hood.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from ToontownGlobals import *
from ToontownMsgTypes import *
import DirectNotifyGlobal
import StateData
import FSM
import State
import Task
import Purchase
import OnscreenText
import DistributedAvatar

class Hood(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('Hood')
    
    def __init__(self, parentFSM, doneEvent, dnaStore):
        StateData.StateData.__init__(self, doneEvent)
        self.fsm = FSM.FSM('Hood', [
            State.State('start', self.enterStart, self.exitStart, [
                'waitForSetZoneResponse']),
            State.State('town', self.enterTown, self.exitTown, [
                'waitForQuietZoneResponse',
                'safeZone',
                'suitInterior']),
            State.State('shop', self.enterShop, self.exitShop, [
                'safeZone']),
            State.State('safeZone', self.enterSafeZone, self.exitSafeZone, [
                'waitForQuietZoneResponse',
                'suitInterior',
                'town',
                'shop',
                'minigame',
                'tutorial']),
            State.State('purchase', self.enterPurchase, self.exitPurchase, [
                'waitForQuietZoneResponse',
                'minigame',
                'safeZone']),
            State.State('suitInterior', self.enterSuitInterior, self.exitSuitInterior, [
                'waitForQuietZoneResponse',
                'town',
                'safeZone']),
            State.State('minigame', self.enterMinigame, self.exitMinigame, [
                'purchase']),
            State.State('tutorial', self.enterTutorial, self.exitTutorial, [
                'safeZone']),
            State.State('waitForQuietZoneResponse', self.enterWaitForQuietZoneResponse, self.exitWaitForQuietZoneResponse, [
                'waitForSetZoneResponse']),
            State.State('waitForSetZoneResponse', self.enterWaitForSetZoneResponse, self.exitWaitForSetZoneResponse, [
                'waitForSetZoneComplete']),
            State.State('waitForSetZoneComplete', self.enterWaitForSetZoneComplete, self.exitWaitForSetZoneComplete, [
                'safeZone',
                'town',
                'suitInterior',
                'minigame']),
            State.State('final', self.enterFinal, self.exitFinal, [])], 'start', 'final')
        self.parentFSM = parentFSM
        self.dnaStore = dnaStore
        self.townDoneEvent = 'townDone'
        self.loaderDoneEvent = 'szDone'
        self.suitInteriorDoneEvent = 'suitInteriorDone'
        self.minigameDoneEvent = 'minigameDone'
        self.id = None
        self.titleText = None
        self.titleColor = (1, 1, 1, 1)

    
    def enter(self, requestStatus):
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        if zoneId == self.id and self.id != Tutorial:
            hoodText = toonbase.tcr.hoodMgr.getFullnameFromId(self.id) + '\nPlayground'
        else:
            hoodText = toonbase.tcr.hoodMgr.getFullnameFromId(self.id)
        self.titleText = OnscreenText.OnscreenText(hoodText, fg = self.titleColor, font = getSignFont(), pos = (0, -0.5), scale = 0.16, drawOrder = 0)
        self.fsm.enterInitialState()
        self.fsm.request('waitForSetZoneResponse', [
            requestStatus])

    
    def hideTitleTextTask(self, task):
        self.titleText.hide()
        return Task.done

    
    def hideTitleText(self):
        if self.titleText:
            self.titleText.hide()
        

    
    def exit(self):
        taskMgr.removeTasksNamed('titleText')
        if self.titleText:
            self.titleText.cleanup()
            self.titleText = None
        
        toonbase.localToon.stopChat()

    
    def load(self):
        loadDNAFile(self.dnaStore, self.storageDNAFile, CSDefault, 0)
        self.sky = loader.loadModel(self.skyFile)
        self.sky.setScale(1.0)

    
    def unload(self):
        toonbase.tcr.disableAll()
        del self.fsm
        del self.parentFSM
        del self.safeZoneLoaderClass
        del self.townLoaderClass
        self.dnaStore.resetHood()
        del self.dnaStore
        self.sky.removeNode()
        del self.sky
        self.ignoreAll()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def enterTown(self, requestStatus):
        self.accept(self.townDoneEvent, self.handleTownDone)
        mode = requestStatus['mode']
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        self.loader.enter(requestStatus)
        seq = Task.sequence(Task.pause(8.0), self.titleText.lerpColor(Vec4(self.titleColor[0], self.titleColor[1], self.titleColor[2], self.titleColor[3]), Vec4(self.titleColor[0], self.titleColor[1], self.titleColor[2], 0.0), 0.5), Task.Task(self.hideTitleTextTask))
        taskMgr.spawnTaskNamed(seq, 'titleText')
        self.loader.setState('street', requestStatus)

    
    def exitTown(self):
        taskMgr.removeTasksNamed('titleText')
        self.hideTitleText()
        self.ignore(self.townDoneEvent)
        self.loader.exit()
        self.loader.unload()
        del self.loader

    
    def handleTownEntry(self):
        self.fsm.request('town')

    
    def enterShop(self):
        pass

    
    def exitShop(self):
        pass

    
    def handleShopEntry(self):
        self.fsm.request('shop')

    
    def enterSafeZone(self, requestStatus):
        self.accept(self.loaderDoneEvent, self.handleSafeZoneLoaderDone)
        seq = Task.sequence(Task.pause(8.0), self.titleText.lerpColor(Vec4(self.titleColor[0], self.titleColor[1], self.titleColor[2], self.titleColor[3]), Vec4(self.titleColor[0], self.titleColor[1], self.titleColor[2], 0.0), 0.5), Task.Task(self.hideTitleTextTask))
        taskMgr.spawnTaskNamed(seq, 'titleText')
        self.loader.enter(requestStatus)
        self.loader.setState('playground', requestStatus)

    
    def exitSafeZone(self):
        taskMgr.removeTasksNamed('titleText')
        self.hideTitleText()
        self.ignore(self.loaderDoneEvent)
        self.loader.exit()
        self.loader.unload()
        del self.loader

    
    def enterPurchase(self, pointsAwarded, playerIds, playerStates, remain):
        messenger.send('enterSafeZone')
        DistributedAvatar.DistributedAvatar.LaffNumbersEnabled = 0
        toonbase.localToon.laffMeter.start()
        self.purchaseDoneEvent = 'purchaseDone'
        self.accept(self.purchaseDoneEvent, self.handlePurchaseDone)
        self.purchase = Purchase.Purchase(toonbase.localToon, pointsAwarded, playerIds, playerStates, remain, self.purchaseDoneEvent)
        self.purchase.load()
        self.purchase.enter()

    
    def exitPurchase(self):
        messenger.send('exitSafeZone')
        DistributedAvatar.DistributedAvatar.LaffNumbersEnabled = 1
        toonbase.localToon.laffMeter.stop()
        self.ignore(self.purchaseDoneEvent)
        self.purchase.exit()
        self.purchase.unload()
        del self.purchase

    
    def handlePurchaseDone(self):
        doneStatus = self.purchase.getDoneStatus()
        if doneStatus['mode'] == 'safeZone':
            if self.id == Tutorial:
                newDoneStatus = { }
                newDoneStatus['mode'] = 'teleportOut'
                newDoneStatus['hoodId'] = ToontownCentral
                newDoneStatus['zoneId'] = ToontownCentral
                newDoneStatus['avId'] = -1
                self.doneStatus = newDoneStatus
                messenger.send(self.doneEvent)
            else:
                self.fsm.request('waitForQuietZoneResponse', [
                    {
                        'mode': 'teleportOut',
                        'hoodId': self.id,
                        'zoneId': self.id,
                        'avId': -1 }])
        elif doneStatus['mode'] == 'minigame':
            self.fsm.request('minigame')
        else:
            self.notify.error('handlePurchaseDone: unknown mode')

    
    def enterSuitInterior(self, requestStatus = None):
        return None
        self.acceptOnce(self.suitInteriorDoneEvent, self.handleSuitInteriorDone)
        if requestStatus:
            self.suitInterior_doneStatus = requestStatus
        else:
            self.suitInterior_doneStatus = { }
            self.suitInterior_doneStatus['hoodId'] = self.id
            self.suitInterior_doneStatus['zoneId'] = self.id
        self.suitInterior_doneStatus['mode'] = 'doorOut'

    
    def exitSuitInterior(self):
        return None
        self.ignore(self.suitInteriorDoneEvent)
        del self.suitInterior_doneStatus

    
    def handleSuitInteriorDone(self):
        return None
        doneStatus = self.suitInterior_doneStatus
        mode = doneStatus['mode']
        hoodId = doneStatus['hoodId']
        if mode == 'teleportOut' or mode == 'doorOut':
            if hoodId == self.id:
                self.fsm.request('waitForQuietZoneResponse', [
                    doneStatus])
            else:
                self.doneStatus = doneStatus
                messenger.send(self.doneEvent)
        else:
            self.notify.error('Unknown done mode from suitInterior')

    
    def enterMinigame(self):
        messenger.send('enterSafeZone')
        DistributedAvatar.DistributedAvatar.LaffNumbersEnabled = 0
        toonbase.localToon.laffMeter.start()
        self.acceptOnce(self.minigameDoneEvent, self.handleMinigameDone)
        return None

    
    def exitMinigame(self):
        messenger.send('exitSafeZone')
        DistributedAvatar.DistributedAvatar.LaffNumbersEnabled = 1
        toonbase.localToon.laffMeter.stop()
        self.ignore(self.minigameDoneEvent)
        minigameState = self.fsm.getStateNamed('minigame')
        for childFSM in minigameState.getChildren():
            minigameState.removeChild(childFSM)
        

    
    def handleMinigameDone(self):
        return None

    
    def enterTutorial(self):
        pass

    
    def exitTutorial(self):
        pass

    
    def enterFinal(self):
        pass

    
    def exitFinal(self):
        pass

    
    def handleSafeZoneLoaderDone(self):
        doneStatus = self.loader.place.getDoneStatus()
        mode = doneStatus['mode']
        hoodId = doneStatus['hoodId']
        zoneId = doneStatus['zoneId']
        if mode == 'teleportOut' or mode == 'doorOut':
            if hoodId == self.id:
                self.fsm.request('waitForQuietZoneResponse', [
                    doneStatus])
            else:
                self.doneStatus = doneStatus
                messenger.send(self.doneEvent)
        elif mode == 'tunnelOut':
            self.fsm.request('waitForQuietZoneResponse', [
                doneStatus])
        elif mode == 'minigame':
            self.fsm.request('waitForQuietZoneResponse', [
                doneStatus])
        else:
            self.notify.error('Unknown done mode from safe zone')

    
    def handleTownDone(self):
        doneStatus = self.loader.place.getDoneStatus()
        mode = doneStatus['mode']
        hoodId = doneStatus['hoodId']
        zoneId = doneStatus['zoneId']
        if mode == 'teleportOut' or mode == 'doorOut':
            if hoodId == self.id:
                self.fsm.request('waitForQuietZoneResponse', [
                    doneStatus])
            else:
                self.doneStatus = doneStatus
                messenger.send(self.doneEvent)
        elif mode == 'tunnelOut':
            if hoodId == self.id:
                self.fsm.request('waitForQuietZoneResponse', [
                    doneStatus])
            else:
                self.doneStatus = doneStatus
                messenger.send(self.doneEvent)
        else:
            self.notify.error('Unknown done mode from safe zone')

    
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
        if mode == 'minigame':
            pass
        1
        if mode == 'teleportOut' or mode == 'tunnelOut':
            if zoneId == self.id or self.id == Tutorial:
                self.loader = self.safeZoneLoaderClass(self, self.fsm.getStateNamed('safeZone'), self.loaderDoneEvent)
                if not (loader.inBulkBlock):
                    loader.beginBulkLoad('hood', safeZoneCountMap[self.id])
                
                loader.notify.info('******** current count is %s' % loader.count)
                self.loader.load()
                loader.endBulkLoad('hood')
            elif zoneId % 1000 >= 500:
                self.suitInterior = self.suitInteriorClass(self, self.fsm, self.suitInteriorDoneEvent)
                self.suitInterior.load(zoneId)
            else:
                self.loader = self.townLoaderClass(self, self.fsm.getStateNamed('town'), self.townDoneEvent)
                if not (loader.inBulkBlock):
                    loader.beginBulkLoad('hood', townCountMap[self.id])
                
                loader.notify.info('******** current count is %s' % loader.count)
                self.loader.load(zoneId)
                loader.endBulkLoad('hood')
        
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
        mode = toonbase.tcr.handlerArgs['mode']
        hoodId = toonbase.tcr.handlerArgs['hoodId']
        zoneId = toonbase.tcr.handlerArgs['zoneId']
        toonbase.localToon.startChat()
        if mode == 'minigame':
            self.fsm.request('minigame')
        elif mode == 'teleportOut' and mode == 'tunnelOut' or mode == 'doorOut':
            if zoneId == self.id or self.id == Tutorial:
                self.fsm.request('safeZone', [
                    toonbase.tcr.handlerArgs])
            elif zoneId % 1000 >= 500:
                self.fsm.request('suitInterior', [
                    toonbase.tcr.handlerArgs])
            else:
                self.fsm.request('town', [
                    toonbase.tcr.handlerArgs])
        

    
    def exitWaitForSetZoneComplete(self):
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None


