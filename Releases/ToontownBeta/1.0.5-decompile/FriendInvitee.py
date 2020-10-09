# Source Generated with Decompyle++
# File: FriendInvitee.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
import PandaObject
import ToonHead
import Button
import DirectNotifyGlobal
import OnscreenPanel

class FriendInvitee(OnscreenPanel.OnscreenPanel):
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendInvitee')
    
    def __init__(self, avId, avName, dna, context):
        OnscreenPanel.OnscreenPanel.__init__(self, 'FriendInvitee')
        self.avId = avId
        self.avName = avName
        self.dna = dna
        self.context = context
        self.makePanel(rect = (-0.5, 0.5, -0.3, 0.3), bg = (1, 0.89, 0.77, 0.85), support3d = 1)
        tooMany = len(toonbase.localToon.friendsList) >= MaxFriends
        if tooMany:
            self.makeText('%s would like to be your friend, but you already have too many friends on your list!' % self.avName, wordwrap = 9, scale = 0.06, pos = (0.13, 0.15))
        else:
            self.makeText('%s would like to be your friend.' % self.avName, wordwrap = 9, scale = 0.06, pos = (0.13, 0.13))
        self.head = self.attachNewNode('head')
        self.head.setPosHprScale(-0.3, 5, 0.05, 180, 0, 0, 0.13, 0.13, 0.13)
        self.headModel = ToonHead.ToonHead()
        dw = DepthWriteTransition()
        dt = DepthTestTransition(DepthTestProperty.MLess)
        self.headModel.setupHead(self.dna)
        self.headModel.arc().setTransition(dw, 1)
        self.headModel.arc().setTransition(dt, 1)
        self.headModel.setBin('fixed', 10)
        self.headModel.reparentTo(self.head)
        self.headModel.startBlink()
        if tooMany:
            toonbase.tcr.friendManager.up_inviteeFriendResponse(3, self.context)
            self.context = None
            self.makeButton('Ok', scale = 0.075, pos = (0.0, -0.2), func = self._FriendInvitee__handleOhWell, event = 'ok')
        else:
            self.makeButton('Ok', scale = 0.075, pos = (-0.15, -0.2), func = self._FriendInvitee__handleOk, event = 'ok')
            self.makeButton('No', scale = 0.075, pos = (0.15, -0.2), func = self._FriendInvitee__handleNo, event = 'no')
        self.accept('cancelFriendInvitation', self._FriendInvitee__handleCancelFromAbove)
        self.show()

    
    def cleanup(self):
        if OnscreenPanel.OnscreenPanel.cleanup(self):
            self.ignore('cancelFriendInvitation')
            self.headModel.stopBlink()
            self.headModel.stopLookAroundNow()
            if self.context != None:
                toonbase.tcr.friendManager.up_inviteeFriendResponse(2, self.context)
                self.context = None
            
        

    
    def __handleOk(self, okButton, item):
        if okButton == item:
            toonbase.tcr.friendManager.up_inviteeFriendResponse(1, self.context)
            self.context = None
            self.cleanup()
        

    
    def __handleNo(self, noButton, item):
        if noButton == item:
            toonbase.tcr.friendManager.up_inviteeFriendResponse(0, self.context)
            self.context = None
            self.cleanup()
        

    
    def __handleOhWell(self, noButton, item):
        if noButton == item:
            self.cleanup()
        

    
    def __handleCancelFromAbove(self, context):
        if context == self.context:
            self.context = None
            self.cleanup()
        


