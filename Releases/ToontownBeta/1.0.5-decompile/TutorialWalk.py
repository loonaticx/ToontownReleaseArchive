# Source Generated with Decompyle++
# File: TutorialWalk.pyo (Python 2.0)

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

class TutorialWalk(Walk.Walk):
    notify = DirectNotifyGlobal.directNotify.newCategory('TutorialWalk')
    
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

    
    def shtickerBookOn(self):
        toonbase.localToon.book.showButton()
        self.accept(StickerBookHotkey, self._TutorialWalk__handleStickerBookEntry)
        self.accept('enterStickerBook', self._TutorialWalk__handleStickerBookEntry)
        self.accept(OptionsPageHotkey, self._TutorialWalk__handleOptionsEntry)

    
    def laffMeterOn(self):
        toonbase.localToon.laffMeter.start()

    
    def enter(self):
        Walk.Walk.enter(self)
        self.accept('tutorialLaffMeterOn', self.laffMeterOn)
        self.accept('tutorialShtickerBookOn', self.shtickerBookOn)
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
        return None

    
    def __handleFriendsList(self, item):
        self._TutorialWalk__openFriendsList()
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


