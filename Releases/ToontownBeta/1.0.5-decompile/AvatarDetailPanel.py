# Source Generated with Decompyle++
# File: AvatarDetailPanel.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
import PandaObject
import FSM
import State
import Button
import DirectNotifyGlobal
import OnscreenPanel
import DistributedToon
import LaffMeter

class AvatarDetailPanel(OnscreenPanel.OnscreenPanel):
    notify = DirectNotifyGlobal.directNotify.newCategory('AvatarDetailPanel')
    
    def __init__(self, avId, avName):
        OnscreenPanel.OnscreenPanel.__init__(self, 'AvatarDetailPanel')
        self.avId = avId
        self.avName = avName
        self.avatar = None
        self.createdAvatar = None
        self.laffMeter = None
        self.fsm = FSM.FSM('AvatarDetailPanel', [
            State.State('off', self.enterOff, self.exitOff, [
                'begin']),
            State.State('begin', self.enterBegin, self.exitBegin, [
                'query',
                'data',
                'off']),
            State.State('query', self.enterQuery, self.exitQuery, [
                'data',
                'invalid',
                'off']),
            State.State('data', self.enterData, self.exitData, [
                'off']),
            State.State('invalid', self.enterInvalid, self.exitInvalid, [
                'off'])], 'off', 'off')
        OnscreenPanel.cleanupPanel('TeleportPanel')
        OnscreenPanel.cleanupPanel('FriendInviter')
        self.makePanel(rect = (0.0, 0.91, 0.33, 0.99), bg = (1, 0.89, 0.77, 0.85))
        self.infoText = self.makeText(wordwrap = 13.5, scale = 0.06, pos = (0, 0.13), mayChange = 1)
        self.bOk = self.makeButton('Ok', scale = 0.075, pos = (0, -0.2), manage = 0, func = self._AvatarDetailPanel__handleOk, event = 'ok')
        self.bCancel = self.makeButton('Cancel', scale = 0.075, pos = (0, -0.2), manage = 0, func = self._AvatarDetailPanel__handleCancel, event = 'cancel')
        self.show()
        self.fsm.request('begin')

    
    def cleanup(self):
        if self.fsm:
            self.fsm.request('off')
            self.fsm = None
        
        if self.laffMeter:
            self.laffMeter.stop()
            self.laffMeter.destroy()
            self.laffMeter = None
        
        if self.createdAvatar:
            self.avatar.delete()
            self.createdAvatar = None
        
        OnscreenPanel.OnscreenPanel.cleanup(self)

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterBegin(self):
        myId = toonbase.localToon.doId
        if self.avId == myId:
            self.avatar = toonbase.localToon
            self.createdAvatar = 0
            self.fsm.request('data')
        else:
            self.fsm.request('query')

    
    def exitBegin(self):
        pass

    
    def enterQuery(self):
        self.infoText.setText('Looking up details for %s.' % self.avName)
        self.bCancel.manage(self)
        if toonbase.tcr.doId2do.has_key(self.avId):
            self.avatar = toonbase.tcr.doId2do[self.avId]
            self.createdAvatar = 0
        else:
            self.avatar = DistributedToon.DistributedToon(toonbase.tcr)
            self.createdAvatar = 1
            self.avatar.doId = self.avId
        toonbase.tcr.getAvatarDetails(self.avatar, self._AvatarDetailPanel__handleAvatarDetails)

    
    def exitQuery(self):
        self.bCancel.unmanage()

    
    def enterData(self):
        self.infoText.setText('')
        self._AvatarDetailPanel__showData()
        self.bOk.manage(self)

    
    def exitData(self):
        self.bOk.unmanage()

    
    def enterInvalid(self):
        self.infoText.setText('Unable to get details for %s.' % self.avName)
        self.bOk.manage(self)

    
    def exitInvalid(self):
        self.bOk.unmanage()

    
    def __handleOk(self, okButton, item):
        if item == okButton:
            self.cleanup()
        

    
    def __handleCancel(self, cancelButton, item):
        if item == cancelButton:
            self.cleanup()
        

    
    def __handleAvatarDetails(self, gotData, avatar):
        if gotData:
            self.fsm.request('data')
        else:
            self.fsm.request('invalid')

    
    def __showData(self):
        av = self.avatar
        online = 1
        if toonbase.tcr.isFriend(self.avId):
            online = toonbase.tcr.isFriendOnline(self.avId)
        
        self.makeText(av.getName(), scale = 0.066, pos = (0, 0.25))
        if online:
            text = 'Blast login: %s\nDistrict: %s\nLocation: %s\nStars: %s' % (av.accountName, toonbase.tcr.getShardName(av.defaultShard), toonbase.tcr.hoodMgr.getFullnameFromId(av.lastHood), av.getStarLevel())
        else:
            text = 'Blast login: %s\nDistrict: offline\nLocation: offline\nStars: %s' % (av.accountName, av.getStarLevel())
        self.makeText(text, scale = 0.045, pos = (-0.45, 0.18), align = TMALIGNLEFT)
        if online:
            self.laffMeter = LaffMeter.LaffMeter(av.style, av.hp, av.maxHp)
            self.laffMeter.reparentTo(self)
            self.laffMeter.setPos(0.32, 0, 0.15)
            self.laffMeter.setScale(0.065)
            self.laffMeter.start()
        


