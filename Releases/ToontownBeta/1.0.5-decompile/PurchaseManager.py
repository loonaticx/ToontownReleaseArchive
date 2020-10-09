# Source Generated with Decompyle++
# File: PurchaseManager.pyo (Python 2.0)

from ShowBaseGlobal import *
from PurchaseManagerConstants import *
from ClockDelta import *
import DistributedObject
import DirectNotifyGlobal

class PurchaseManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('PurchaseManager')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.playAgain = 0
        self.displayed = 0
        return None

    
    def disable(self):
        self.ignoreAll()

    
    def setPlayerIds(self, *playerIds):
        self.playerIds = playerIds
        return None

    
    def setMinigamePoints(self, *mpArray):
        self.mpArray = mpArray
        return None

    
    def setPlayerStates(self, *stateArray):
        self.playerStates = stateArray
        if self.displayed:
            messenger.send('purchaseStateChange', [
                self.playerStates])
        
        return None

    
    def setCountdown(self, sec, usec):
        self.displayed = 1
        et = localElapsedTime(sec, usec)
        remain = PURCHASE_COUNTDOWN_TIME - et
        self.acceptOnce('purchasePlayAgain', self.playAgainHandler)
        self.acceptOnce('purchaseBackToToontown', self.backToToontownHandler)
        self.acceptOnce('purchaseTimeout', self.setPurchaseExit)
        toonbase.tcr.playGame.hood.fsm.request('purchase', [
            self.getOurPoints(),
            self.playerIds,
            self.playerStates,
            remain])
        return None

    
    def playAgainHandler(self):
        self.d_requestPlayAgain()
        return None

    
    def backToToontownHandler(self):
        self.d_requestExit()
        print 'requesting exit to toontown...'
        self.playAgain = 0
        self.setPurchaseExit()
        return None

    
    def d_requestExit(self):
        self.sendUpdate('requestExit', [])
        return None

    
    def d_requestPlayAgain(self):
        self.sendUpdate('requestPlayAgain', [])
        self.playAgain = 1
        print 'requesting play again...'
        return None

    
    def d_setInventory(self, invString):
        self.sendUpdate('setInventory', [
            invString])
        return None

    
    def setPurchaseExit(self):
        self.d_setInventory(toonbase.localToon.inventory.makeNetString())
        messenger.send('purchaseOver', [
            self.playAgain])
        return None

    
    def findAvIndex(self, avId):
        for i in range(len(self.playerIds)):
            if avId == self.playerIds[i]:
                return i
            
        
        return None

    
    def getOurPoints(self):
        avIndex = self.findAvIndex(toonbase.localToon.getDoId())
        return self.mpArray[avIndex]


