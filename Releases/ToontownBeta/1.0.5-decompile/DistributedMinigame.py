# Source Generated with Decompyle++
# File: DistributedMinigame.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
import DistributedObject
import DirectNotifyGlobal
import FSM
import State
import Suit
import AvatarDNA
import MinigameRulesPanel
import Sign
import Toon

class DistributedMinigame(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMinigame')
    SuitsCreated = 0
    SuitsModelCount = 22
    SuitTypeList = [
        'pp',
        'b',
        'cc']
    SuitList = []
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.waitingStartSign = Sign.Sign('waitingStartSign', 'Waiting for other players to join...')
        self.waitingStartSign.setPos(-0.3, -0.9)
        self.waitingStartSign.label.setForegroundColor(1, 1, 1, 1)
        self.avIdList = []
        self.remoteAvIdList = []
        self.localAvId = toonbase.localToon.doId
        self.frameworkFSM = FSM.FSM('DistributedMinigame', [
            State.State('frameworkInit', self.enterFrameworkInit, self.exitFrameworkInit, [
                'rules',
                'cleanup']),
            State.State('frameworkOff', self.enterFrameworkOff, self.exitFrameworkOff, []),
            State.State('rules', self.enterRules, self.exitRules, [
                'waitServerStart',
                'cleanup']),
            State.State('waitServerStart', self.enterWaitServerStart, self.exitWaitServerStart, [
                'game',
                'cleanup']),
            State.State('game', self.enterGame, self.exitGame, [
                'score',
                'cleanup']),
            State.State('score', self.enterScore, self.exitScore, [
                'cleanup']),
            State.State('cleanup', self.enterCleanup, self.exitCleanup, [
                'frameworkOff'])], 'frameworkInit', 'frameworkOff')
        hoodMinigameState = self.cr.playGame.hood.fsm.getStateNamed('minigame')
        hoodMinigameState.addChild(self.frameworkFSM)
        self.rulesDoneEvent = 'rulesDone'
        self.acceptOnce('minigameAbort', self.d_requestExit)
        toonbase.currentMinigame = self
        self.modelCount = 500
        self.frameworkFSM.enterInitialState()
        return None

    
    def d_requestExit(self):
        self.sendUpdate('requestExit', [])
        return None

    
    def getTitle(self):
        return 'Minigame Title'

    
    def getInstructions(self):
        return 'Minigame Instructions'

    
    def generate(self):
        self.notify.debug('generate DistributedMinigame')
        count = 0
        if not (DistributedMinigame.SuitsCreated):
            count = self.SuitsModelCount + self.modelCount
        else:
            count = self.modelCount
        loader.beginBulkLoad('minigame', count)
        self.createSuits()
        self.load()
        loader.endBulkLoad('minigame')
        self.announceGenerateName = self.uniqueName('generate')
        self.accept(self.announceGenerateName, self.handleAnnounceGenerate)

    
    def handleAnnounceGenerate(self, obj):
        self.ignore(self.announceGenerateName)
        self.notify.debug('joining DistributedMinigame')
        self.sendUpdate('setAvatarJoined', [
            toonbase.localToon.doId])
        self.onstage()
        self.frameworkFSM.request('rules')

    
    def createSuits(self):
        if not (DistributedMinigame.SuitsCreated):
            for suitType in self.SuitTypeList:
                suit = Suit.Suit()
                suitDNA = AvatarDNA.AvatarDNA()
                suitDNA.newSuit(suitType)
                suit.setDNA(suitDNA)
                self.SuitList.append(suit)
            
            DistributedMinigame.SuitsCreated = 1
        

    
    def disable(self):
        self.notify.debug('disable DistributedMinigame')
        self.frameworkFSM.request(self.frameworkFSM.getFinalState())
        for avId in self.avIdList:
            av = self.getAvatar(avId)
            if av:
                av.stop()
                av.reparentTo(hidden)
            
        
        self.remoteAvIdList = []
        self.offstage()
        hoodMinigameState = self.cr.playGame.hood.fsm.getStateNamed('minigame')
        hoodMinigameState.removeChild(self.frameworkFSM)
        self.ignoreAll()
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        self.notify.debug('delete DistributedMinigame')
        self.unload()
        self.ignore('minigameAbort')
        hoodMinigameState = self.cr.playGame.hood.fsm.getStateNamed('minigame')
        hoodMinigameState.removeChild(self.frameworkFSM)
        del self.frameworkFSM
        DistributedObject.DistributedObject.delete(self)

    
    def load(self):
        Toon.loadMinigameAnims()

    
    def onstage(self):
        pass

    
    def offstage(self):
        pass

    
    def unload(self):
        del toonbase.currentMinigame
        Toon.unloadMinigameAnims()

    
    def setParticipants(self, avIds):
        self.avIdList = avIds
        for avId in self.avIdList:
            if avId != self.localAvId:
                self.remoteAvIdList.append(avId)
            
        
        self.notify.debug('setParticipants: game will be played by these avatars: %s' % self.avIdList)
        for avId in self.avIdList:
            if self.cr.doId2do.has_key(avId):
                avatar = self.cr.doId2do[avId]
                self.acceptOnce(avatar.uniqueName('disable'), self.handleDisabledAvatar, [
                    avId])
            
        

    
    def setAvatarJoined(self, avId):
        pass

    
    def setAvatarReady(self, avId):
        pass

    
    def setAvatarExited(self, avId):
        pass

    
    def setGameReady(self):
        self.notify.debug('Starting game with avatars: %s' % self.avIdList)

    
    def setGameStart(self):
        self.notify.debug('Starting game')
        self.frameworkFSM.request('game')

    
    def setGameExit(self):
        self.notify.debug('Exiting game')
        self.frameworkFSM.request('cleanup')

    
    def setGameAbort(self):
        self.notify.debug('Aborting game')
        self.frameworkFSM.request('cleanup', [
            1])
        return None

    
    def getAvatar(self, avId):
        if self.cr.doId2do.has_key(avId):
            return self.cr.doId2do[avId]
        elif avId in [
            1,
            2,
            3]:
            return self.SuitList[avId - 1]
        else:
            self.notify.warning('getAvatar: No avatar in doId2do with id: ' + str(avId))
            return None

    
    def getAvatarName(self, avId):
        avatar = self.getAvatar(avId)
        if avatar:
            return avatar.getName()
        else:
            return 'Unknown'

    
    def isSuit(self, avId):
        if avId in [
            1,
            2,
            3]:
            return 1
        else:
            return 0

    
    def isSinglePlayer(self):
        if len(self.avIdList) == 1:
            return 1
        else:
            return 0

    
    def handleDisabledAvatar(self, avId):
        self.notify.warning('handleDisabledAvatar: disabled avId: ' + str(avId))

    
    def gameOver(self):
        self.frameworkFSM.request('cleanup')

    
    def enterFrameworkInit(self):
        pass

    
    def exitFrameworkInit(self):
        pass

    
    def enterFrameworkOff(self):
        pass

    
    def exitFrameworkOff(self):
        pass

    
    def enterRules(self):
        self.accept(self.rulesDoneEvent, self.handleRulesDone)
        self.rulesPanel = MinigameRulesPanel.MinigameRulesPanel('MinigameRulesPanel', self.getTitle(), self.getInstructions(), self.rulesDoneEvent)
        self.rulesPanel.load()
        self.rulesPanel.enter()

    
    def exitRules(self):
        self.ignore(self.rulesDoneEvent)
        self.rulesPanel.exit()
        self.rulesPanel.unload()
        del self.rulesPanel

    
    def handleRulesDone(self):
        self.sendUpdate('setAvatarReady', [
            toonbase.localToon.doId])
        self.frameworkFSM.request('waitServerStart')

    
    def enterWaitServerStart(self):
        self.waitingStartSign.manage()

    
    def exitWaitServerStart(self):
        self.waitingStartSign.unmanage()

    
    def enterGame(self):
        pass

    
    def exitGame(self):
        pass

    
    def enterScore(self):
        pass

    
    def exitScore(self):
        pass

    
    def enterCleanup(self, abortFlag = 0):
        if not abortFlag:
            self.sendUpdate('setAvatarExited', [
                toonbase.localToon.doId])
        
        messenger.send(self.cr.playGame.hood.minigameDoneEvent)

    
    def exitCleanup(self):
        pass


