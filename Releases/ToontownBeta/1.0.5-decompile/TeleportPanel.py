# Source Generated with Decompyle++
# File: TeleportPanel.pyo (Python 2.0)

from ShowBaseGlobal import *
import ToontownGlobals
import PandaObject
import FSM
import State
import Button
import DirectNotifyGlobal
import OnscreenPanel

class TeleportPanel(OnscreenPanel.OnscreenPanel):
    notify = DirectNotifyGlobal.directNotify.newCategory('TeleportPanel')
    
    def __init__(self, placeFSM, avId, avName, avDisableName):
        OnscreenPanel.OnscreenPanel.__init__(self, 'TeleportPanel')
        self.placeFSM = placeFSM
        self.avId = avId
        self.avName = avName
        self.avDisableName = avDisableName
        self.fsm = FSM.FSM('TeleportPanel', [
            State.State('off', self.enterOff, self.exitOff, [
                'begin']),
            State.State('begin', self.enterBegin, self.exitBegin, [
                'self',
                'notOnline',
                'checkAvailability',
                'wentAway']),
            State.State('checkAvailability', self.enterCheckAvailability, self.exitCheckAvailability, [
                'notAvailable',
                'wentAway',
                'otherShard',
                'teleport',
                'off']),
            State.State('notAvailable', self.enterNotAvailable, self.exitNotAvailable, [
                'off',
                'wentAway']),
            State.State('notOnline', self.enterNotOnline, self.exitNotOnline, [
                'off']),
            State.State('wentAway', self.enterWentAway, self.exitWentAway, [
                'off']),
            State.State('self', self.enterSelf, self.exitSelf, [
                'off']),
            State.State('unknownHood', self.enterUnknownHood, self.exitUnknownHood, [
                'off']),
            State.State('unavailableHood', self.enterUnavailableHood, self.exitUnavailableHood, [
                'off']),
            State.State('otherShard', self.enterOtherShard, self.exitOtherShard, [
                'teleport',
                'off']),
            State.State('teleport', self.enterTeleport, self.exitTeleport, [
                'unknownHood',
                'unavailableHood',
                'wentAway',
                'off'])], 'off', 'off')
        OnscreenPanel.cleanupPanel('FriendInviter')
        OnscreenPanel.cleanupPanel('AvatarDetailPanel')
        self.makePanel(rect = (-0.19, 0.81, 0.33, 0.99), bg = (1, 0.89, 0.77, 0.85))
        self.infoText = self.makeText(wordwrap = 13.5, scale = 0.06, pos = (0, 0.13), mayChange = 1)
        self.bOk = self.makeButton('Ok', scale = 0.075, pos = (0, -0.2), manage = 0, func = self._TeleportPanel__handleOk, event = 'ok')
        self.bCancel = self.makeButton('Cancel', scale = 0.075, pos = (0, -0.2), manage = 0, func = self._TeleportPanel__handleCancel, event = 'cancel')
        self.bYes = self.makeButton('Yes', scale = 0.075, pos = (-0.2, -0.2), manage = 0, func = self._TeleportPanel__handleYes, event = 'yes')
        self.bNo = self.makeButton('No', scale = 0.075, pos = (0.2, -0.2), manage = 0, func = self._TeleportPanel__handleNo, event = 'no')
        self.accept(self.avDisableName, self._TeleportPanel__handleDisableAvatar)
        self.show()
        self.fsm.enterInitialState()
        self.fsm.request('begin')

    
    def cleanup(self):
        self.fsm.request('off')
        OnscreenPanel.OnscreenPanel.cleanup(self)
        self.ignore(self.avDisableName)
        self.placeFSM = None

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterBegin(self):
        myId = toonbase.localToon.doId
        if self.avId == myId:
            self.fsm.request('self')
        elif toonbase.tcr.doId2do.has_key(self.avId):
            self.fsm.request('checkAvailability')
        elif toonbase.tcr.isFriend(self.avId):
            if toonbase.tcr.isFriendOnline(self.avId):
                self.fsm.request('checkAvailability')
            else:
                self.fsm.request('notOnline')
        else:
            self.fsm.request('wentAway')

    
    def exitBegin(self):
        pass

    
    def enterCheckAvailability(self):
        myId = toonbase.localToon.getDoId()
        toonbase.localToon.d_teleportQuery(myId, sendToId = self.avId)
        self.infoText.setText('Trying to go to %s.' % self.avName)
        self.accept('teleportResponse', self._TeleportPanel__teleportResponse)
        self.bCancel.manage(self)

    
    def exitCheckAvailability(self):
        self.ignore('teleportResponse')
        self.bCancel.unmanage()

    
    def enterNotAvailable(self):
        self.infoText.setText('%s is busy right now; try again later.' % self.avName)
        self.bOk.manage(self)

    
    def exitNotAvailable(self):
        self.bOk.unmanage()

    
    def enterNotOnline(self):
        self.infoText.setText("%s isn't online right now." % self.avName)
        self.bOk.manage(self)

    
    def exitNotOnline(self):
        self.bOk.unmanage()

    
    def enterWentAway(self):
        self.infoText.setText('%s went away.' % self.avName)
        self.bOk.manage(self)

    
    def exitWentAway(self):
        self.bOk.unmanage()

    
    def enterUnknownHood(self, hoodId):
        self.infoText.setText("You don't know how to get to %s!" % toonbase.tcr.hoodMgr.getFullnameFromId(hoodId))
        self.bOk.manage(self)

    
    def exitUnknownHood(self):
        self.bOk.unmanage()

    
    def enterUnavailableHood(self, hoodId):
        self.infoText.setText('%s is not available right now; try again later.' % toonbase.tcr.hoodMgr.getFullnameFromId(hoodId))
        self.bOk.manage(self)

    
    def exitUnavailableHood(self):
        self.bOk.unmanage()

    
    def enterSelf(self):
        self.infoText.setText("You can't go to yourself!")
        self.bOk.manage(self)

    
    def exitSelf(self):
        self.bOk.unmanage()

    
    def enterOtherShard(self, shardId, hoodId, zoneId):
        shardName = toonbase.tcr.getShardName(shardId)
        myShardName = toonbase.tcr.getShardName(toonbase.localToon.defaultShard)
        self.infoText.setText("%s is in district %s, and you're in district %s.  Do you want to switch to %s?" % (self.avName, shardName, myShardName, shardName))
        self.bYes.manage(self)
        self.bNo.manage(self)
        self.shardId = shardId
        self.hoodId = hoodId
        self.zoneId = zoneId

    
    def exitOtherShard(self):
        pass

    
    def enterTeleport(self, shardId, hoodId, zoneId):
        if toonbase.localToon.teleportCheat:
            hoodsVisited = ToontownGlobals.Hoods
        else:
            hoodsVisited = toonbase.localToon.hoodsVisited
        if hoodId not in hoodsVisited:
            self.fsm.request('unknownHood', [
                hoodId])
        elif hoodId not in toonbase.tcr.hoodMgr.getAvailableZones():
            self.fsm.request('unavailableHood', [
                hoodId])
        elif shardId != toonbase.localToon.defaultShard:
            toonbase.tcr.gameFSM.request('waitOnEnterResponses', [
                shardId,
                hoodId,
                zoneId,
                self.avId])
        else:
            toonbase.tcr.playGame.hood.loader.place.requestTeleport(hoodId, zoneId, self.avId)
            self.cleanup()
        return None

    
    def exitTeleport(self):
        pass

    
    def __handleOk(self, okButton, item):
        if okButton == item:
            self.cleanup()
        

    
    def __handleCancel(self, cancelButton, item):
        if cancelButton == item:
            self.cleanup()
        

    
    def __handleYes(self, yesButton, item):
        if yesButton == item:
            self.fsm.request('teleport', [
                self.shardId,
                self.hoodId,
                self.zoneId])
        

    
    def __handleNo(self, noButton, item):
        if noButton == item:
            self.cleanup()
        

    
    def __teleportResponse(self, avId, available, shardId, hoodId, zoneId):
        if avId != self.avId:
            return None
        
        if not available:
            self.fsm.request('notAvailable')
        elif shardId != toonbase.localToon.defaultShard:
            self.fsm.request('otherShard', [
                shardId,
                hoodId,
                zoneId])
        else:
            self.fsm.request('teleport', [
                shardId,
                hoodId,
                zoneId])

    
    def __handleDisableAvatar(self):
        self.fsm.request('wentAway')


