# Source Generated with Decompyle++
# File: FriendManager.pyo (Python 2.0)

from ShowBaseGlobal import *
import DistributedObject
import AvatarDNA
import DirectNotifyGlobal

class FriendManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendManager')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self._FriendManager__available = 0
        self.setNeverDisable(1)

    
    def setAvailable(self, available):
        self._FriendManager__available = available

    
    def getAvailable(self):
        return self._FriendManager__available

    
    def generate(self):
        toonbase.tcr.friendManager = self
        DistributedObject.DistributedObject.generate(self)

    
    def disable(self):
        toonbase.tcr.friendManager = None
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        toonbase.tcr.friendManager = None
        DistributedObject.DistributedObject.delete(self)

    
    def up_friendQuery(self, inviterId, inviteeId):
        self.sendUpdate('friendQuery', [
            inviterId,
            inviteeId])

    
    def up_cancelFriendQuery(self, context):
        self.sendUpdate('cancelFriendQuery', [
            context])

    
    def up_inviteeFriendConsidering(self, yesNo, context):
        self.sendUpdate('inviteeFriendConsidering', [
            yesNo,
            context])

    
    def up_inviteeFriendResponse(self, yesNoMaybe, context):
        self.sendUpdate('inviteeFriendResponse', [
            yesNoMaybe,
            context])

    
    def up_inviteeAcknowledgeCancel(self, context):
        self.sendUpdate('inviteeAcknowledgeCancel', [
            context])

    
    def friendConsidering(self, yesNoAlready, context):
        messenger.send('friendConsidering', [
            yesNoAlready,
            context])

    
    def friendResponse(self, yesNoMaybe, context):
        messenger.send('friendResponse', [
            yesNoMaybe,
            context])

    
    def inviteeFriendQuery(self, inviterId, inviterName, inviterDna, context):
        dna = AvatarDNA.AvatarDNA()
        dna.makeFromNetString(inviterDna)
        self.up_inviteeFriendConsidering(self._FriendManager__available, context)
        if self._FriendManager__available:
            messenger.send('friendInvitation', [
                inviterId,
                inviterName,
                dna,
                context])
        

    
    def inviteeCancelFriendQuery(self, context):
        messenger.send('cancelFriendInvitation', [
            context])
        self.up_inviteeAcknowledgeCancel(context)


