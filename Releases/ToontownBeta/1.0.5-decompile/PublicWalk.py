# Source Generated with Decompyle++
# File: PublicWalk.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
import DirectNotifyGlobal
import Walk
import AvatarPanel
import AvatarDetailPanel
import FriendsListPanel
import FriendInviter
import FriendInvitee
import TeleportPanel

class PublicWalk(Walk.Walk):
    notify = DirectNotifyGlobal.directNotify.newCategory('PublicWalk')
    
    def __init__(self, parentFSM, doneEvent):
        Walk.Walk.__init__(self, doneEvent)
        self.parentFSM = parentFSM
        self.avatarPanel = None
        self.friendInviter = None
        return None

    
    def load(self):
        Walk.Walk.load(self)
        return None

    
    def unload(self):
        Walk.Walk.unload(self)
        del self.parentFSM
        del self.avatarPanel
        del self.friendInviter
        return None

    
    def enter(self, slowWalk = 0):
        Walk.Walk.enter(self, slowWalk)
        toonbase.localToon.book.showButton()
        self.accept(StickerBookHotkey, self._PublicWalk__handleStickerBookEntry)
        self.accept('enterStickerBook', self._PublicWalk__handleStickerBookEntry)
        self.accept(OptionsPageHotkey, self._PublicWalk__handleOptionsEntry)
        self.accept(FriendsListHotkey, self._PublicWalk__openFriendsList)
        self.accept('openFriendsList', self._PublicWalk__openFriendsList)
        self.accept('clickedNametag', self._PublicWalk__handleClickedNametag)
        toonbase.localToon.setFriendsListButtonActive(1)
        self.accept('friendsList', self._PublicWalk__handleFriendsList)
        NametagGlobals.setMasterNametagsActive(1)
        self.accept('gotoAvatar', self._PublicWalk__handleGotoAvatar)
        self.accept('friendAvatar', self._PublicWalk__handleFriendAvatar)
        self.accept('avatarDetails', self._PublicWalk__handleAvatarDetails)
        toonbase.localToon.laffMeter.start()
        self.accept('friendInvitation', self._PublicWalk__handleFriendInvitation)
        if toonbase.tcr.friendManager:
            toonbase.tcr.friendManager.setAvailable(1)
        
        return None

    
    def exit(self):
        Walk.Walk.exit(self)
        toonbase.localToon.book.hideButton()
        self.ignore(StickerBookHotkey)
        self.ignore('enterStickerBook')
        self.ignore(OptionsPageHotkey)
        self.ignore(FriendsListHotkey)
        self.ignore('openFriendsList')
        self.ignore('clickedNametag')
        toonbase.localToon.setFriendsListButtonActive(0)
        self.ignore('friendsList')
        NametagGlobals.setMasterNametagsActive(0)
        toonbase.localToon.laffMeter.stop()
        if self.avatarPanel:
            self.avatarPanel.cleanup()
            self.avatarPanel = None
        
        self.ignore('gotoAvatar')
        self.ignore('friendAvatar')
        self.ignore('avatarDetails')
        if toonbase.tcr.friendManager:
            toonbase.tcr.friendManager.setAvailable(0)
        
        self.ignore('friendInvitation')
        if self.friendInviter:
            self.friendInviter.cleanup()
            self.friendInviter = None
        
        return None

    
    def __handleFriendsList(self):
        self._PublicWalk__openFriendsList()
        return None

    
    def __openFriendsList(self):
        self.avatarPanel = FriendsListPanel.FriendsListPanel(FriendsListPanel.FLPOnline)
        return None

    
    def __handleStickerBookEntry(self):
        doneStatus = { }
        doneStatus['mode'] = 'StickerBook'
        messenger.send(self.doneEvent, [
            doneStatus])
        return None

    
    def __handleOptionsEntry(self):
        doneStatus = { }
        doneStatus['mode'] = 'Options'
        messenger.send(self.doneEvent, [
            doneStatus])
        return None

    
    def __handleClickedNametag(self, avatar):
        self.avatarPanel = AvatarPanel.AvatarPanel(avatar)

    
    def __handleGotoAvatar(self, avId, avName, avDisableName):
        self.friendInviter = TeleportPanel.TeleportPanel(self.parentFSM, avId, avName, avDisableName)
        return None

    
    def __handleFriendAvatar(self, avId, avName, avDisableName):
        self.friendInviter = FriendInviter.FriendInviter(avId, avName, avDisableName)
        return None

    
    def __handleFriendInvitation(self, avId, avName, dna, context):
        FriendInvitee.FriendInvitee(avId, avName, dna, context)
        return None

    
    def __handleAvatarDetails(self, avId, avName):
        self.friendInviter = AvatarDetailPanel.AvatarDetailPanel(avId, avName)
        return None


