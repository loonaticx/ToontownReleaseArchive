# Source Generated with Decompyle++
# File: PlayGame.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
import DirectNotifyGlobal
import PandaObject
import StateData
import FSM
import State
from ToontownMsgTypes import *
from ToontownGlobals import *
import DDHood
import MMHood
import BRHood
import DGHood
import DLHood
import TaskManagerGlobal

class PlayGame(PandaObject.PandaObject, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('PlayGame')
    notify.setDebug(1)
    
    def __init__(self, parentFSM, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.fsm = FSM.FSM('PlayGame', [
            State.State('start', self.enterStart, self.exitStart, [
                'TTHood',
                'DDHood',
                'BRHood',
                'MMHood',
                'DGHood',
                'DLHood',
                'TutorialHood']),
            State.State('waitForQuietZoneResponse', self.enterWaitForQuietZoneResponse, self.exitWaitForQuietZoneResponse, [
                'TTHood',
                'DDHood',
                'BRHood',
                'MMHood',
                'DGHood',
                'DLHood',
                'TutorialHood']),
            State.State('TTHood', self.enterTTHood, self.exitTTHood, [
                'waitForQuietZoneResponse']),
            State.State('DDHood', self.enterDDHood, self.exitDDHood, [
                'waitForQuietZoneResponse']),
            State.State('BRHood', self.enterBRHood, self.exitBRHood, [
                'waitForQuietZoneResponse']),
            State.State('MMHood', self.enterMMHood, self.exitMMHood, [
                'waitForQuietZoneResponse']),
            State.State('DGHood', self.enterDGHood, self.exitDGHood, [
                'waitForQuietZoneResponse']),
            State.State('DLHood', self.enterDLHood, self.exitDLHood, [
                'waitForQuietZoneResponse']),
            State.State('TutorialHood', self.enterTutorialHood, self.exitTutorialHood, [
                'waitForQuietZoneResponse'])], 'start', 'start')
        self.fsm.enterInitialState()
        self.parentFSM = parentFSM
        self.parentFSM.getStateNamed('playGame').addChild(self.fsm)
        self.hoodDoneEvent = 'hoodDone'

    
    def enter(self, hoodId, zoneId, avId):
        if hoodId == zoneId or hoodId == Tutorial:
            loader.beginBulkLoad('hood', hoodCountMap[hoodId] + safeZoneCountMap[hoodId])
        else:
            loader.beginBulkLoad('hood', hoodCountMap[hoodId] + townCountMap[hoodId])
        self.hoodState = self.getHoodStateByNumber(hoodId)
        self.fsm.request(self.hoodState, [
            {
                'mode': 'teleportOut',
                'hoodId': hoodId,
                'zoneId': zoneId,
                'avId': avId }])

    
    def exit(self):
        pass

    
    def load(self):
        self.dnaStore = DNAStorage()
        loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna', CSDefault, 0)

    
    def unload(self):
        self.dnaStore.resetNodes()
        self.dnaStore.resetTextures()
        del self.dnaStore
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def handleHoodDone(self):
        doneStatus = self.hood.getDoneStatus()
        mode = doneStatus['mode']
        if mode == 'tunnelOut' or mode == 'teleportOut':
            self.fsm.request('waitForQuietZoneResponse', [
                doneStatus])
        else:
            self.notify.error('Exited hood with unknown mode')

    
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
        mode = toonbase.tcr.handlerArgs['mode']
        hoodId = toonbase.tcr.handlerArgs['hoodId']
        zoneId = toonbase.tcr.handlerArgs['zoneId']
        if hoodId == zoneId:
            loader.beginBulkLoad('hood', hoodCountMap[hoodId] + safeZoneCountMap[hoodId])
        else:
            loader.beginBulkLoad('hood', hoodCountMap[hoodId] + townCountMap[hoodId])
        self.fsm.request(self.getHoodStateByNumber(hoodId), [
            toonbase.tcr.handlerArgs])
        return None

    
    def exitWaitForQuietZoneResponse(self):
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None
        return None

    
    def enterTTHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        import TTHood
        self.TTHood = TTHood.TTHood(self.fsm, self.hoodDoneEvent, self.dnaStore)
        self.hood = self.TTHood
        self.TTHood.load()
        self.TTHood.enter(requestStatus)

    
    def exitTTHood(self):
        self.ignore(self.hoodDoneEvent)
        self.TTHood.exit()
        self.TTHood.unload()
        del self.TTHood
        self.hood = None
        self.hoodState = None
        toonbase.tcr.cache.flush()

    
    def enterDDHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        import DDHood
        self.DDHood = DDHood.DDHood(self.fsm, self.hoodDoneEvent, self.dnaStore)
        self.hood = self.DDHood
        self.DDHood.load()
        self.DDHood.enter(requestStatus)

    
    def exitDDHood(self):
        self.ignore(self.hoodDoneEvent)
        self.DDHood.exit()
        self.DDHood.unload()
        del self.DDHood
        self.hood = None
        self.hoodState = None
        toonbase.tcr.cache.flush()

    
    def enterMMHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        import MMHood
        self.MMHood = MMHood.MMHood(self.fsm, self.hoodDoneEvent, self.dnaStore)
        self.hood = self.MMHood
        self.MMHood.load()
        self.MMHood.enter(requestStatus)

    
    def exitMMHood(self):
        self.ignore(self.hoodDoneEvent)
        self.MMHood.exit()
        self.MMHood.unload()
        del self.MMHood
        self.hood = None
        self.hoodState = None
        toonbase.tcr.cache.flush()

    
    def enterBRHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        import BRHood
        self.BRHood = BRHood.BRHood(self.fsm, self.hoodDoneEvent, self.dnaStore)
        self.hood = self.BRHood
        self.BRHood.load()
        self.BRHood.enter(requestStatus)

    
    def exitBRHood(self):
        self.ignore(self.hoodDoneEvent)
        self.BRHood.exit()
        self.BRHood.unload()
        del self.BRHood
        self.hood = None
        self.hoodState = None
        toonbase.tcr.cache.flush()

    
    def enterDGHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        import DGHood
        self.DGHood = DGHood.DGHood(self.fsm, self.hoodDoneEvent, self.dnaStore)
        self.hood = self.DGHood
        self.DGHood.load()
        self.DGHood.enter(requestStatus)

    
    def exitDGHood(self):
        self.ignore(self.hoodDoneEvent)
        self.DGHood.exit()
        self.DGHood.unload()
        del self.DGHood
        self.hood = None
        self.hoodState = None
        toonbase.tcr.cache.flush()

    
    def enterDLHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        import DLHood
        self.DLHood = DLHood.DLHood(self.fsm, self.hoodDoneEvent, self.dnaStore)
        self.hood = self.DLHood
        self.DLHood.load()
        self.DLHood.enter(requestStatus)

    
    def exitDLHood(self):
        self.ignore(self.hoodDoneEvent)
        self.DLHood.exit()
        self.DLHood.unload()
        del self.DLHood
        self.hood = None
        self.hoodState = None
        toonbase.tcr.cache.flush()

    
    def enterTutorialHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        import TutorialHood
        self.TutorialHood = TutorialHood.TutorialHood(self.fsm, self.hoodDoneEvent, self.dnaStore)
        self.hood = self.TutorialHood
        self.TutorialHood.load()
        self.TutorialHood.enter(requestStatus)

    
    def exitTutorialHood(self):
        self.ignore(self.hoodDoneEvent)
        self.TutorialHood.exit()
        self.TutorialHood.unload()
        del self.TutorialHood
        self.hood = None
        self.hoodState = None
        toonbase.tcr.cache.flush()

    
    def getCatalogCodes(self, category):
        numCodes = self.dnaStore.getNumCatalogCodes(category)
        codes = []
        for i in range(numCodes):
            codes.append(self.dnaStore.getCatalogCode(category, i))
        
        return codes

    
    def getNodePathList(self, catalogGroup):
        result = []
        codes = self.getCatalogCodes(catalogGroup)
        for code in codes:
            np = self.dnaStore.findNode(code)
            result.append(np)
        
        return result

    
    def getNodePathDict(self, catalogGroup):
        result = { }
        codes = self.getCatalogCodes(catalogGroup)
        for code in codes:
            np = self.dnaStore.findNode(code)
            result[code] = np
        
        return result

    
    def getHoodByNumber(self, hoodNumber):
        if hoodNumber == ToontownCentral:
            return self.TTHood
        elif hoodNumber == DonaldsDock:
            return self.DDHood
        elif hoodNumber == TheBrrrgh:
            return self.BRHood
        elif hoodNumber == MinniesMelodyland:
            return self.MMHood
        elif hoodNumber == DaisyGardens:
            return self.DGHood
        elif hoodNumber == DonaldsDreamland:
            return self.DLHood
        elif hoodNumber == Tutorial:
            return self.TutorialHood
        else:
            self.notify.error('Unknown hoodNumber: ' + `hoodNumber`)

    
    def getHoodStateByNumber(self, hoodNumber):
        if hoodNumber == ToontownCentral:
            return 'TTHood'
        elif hoodNumber == DonaldsDock:
            return 'DDHood'
        elif hoodNumber == TheBrrrgh:
            return 'BRHood'
        elif hoodNumber == MinniesMelodyland:
            return 'MMHood'
        elif hoodNumber == DaisyGardens:
            return 'DGHood'
        elif hoodNumber == DonaldsDreamland:
            return 'DLHood'
        elif hoodNumber == Tutorial:
            return 'TutorialHood'
        else:
            self.notify.error('Unknown hoodNumber: ' + `hoodNumber`)


