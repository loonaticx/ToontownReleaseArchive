# Source Generated with Decompyle++
# File: FriendInviter.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
import PandaObject
import FSM
import State
import Button
import DirectNotifyGlobal
import OnscreenPanel

class FriendInviter(OnscreenPanel.OnscreenPanel):
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendInviter')
    
    def __init__(self, avId, avName, avDisableName):
        OnscreenPanel.OnscreenPanel.__init__(self, 'FriendInviter')
        self.avId = avId
        self.avName = avName
        self.avDisableName = avDisableName
        self.fsm = FSM.FSM('FriendInviter', [
            State.State('off', self.enterOff, self.exitOff, [
                'begin']),
            State.State('begin', self.enterBegin, self.exitBegin, [
                'self',
                'already',
                'tooMany',
                'notYet',
                'wentAway']),
            State.State('tooMany', self.enterTooMany, self.exitTooMany, [
                'off']),
            State.State('notYet', self.enterNotYet, self.exitNotYet, [
                'checkAvailability',
                'off',
                'wentAway']),
            State.State('checkAvailability', self.enterCheckAvailability, self.exitCheckAvailability, [
                'notAvailable',
                'already',
                'self',
                'asking',
                'cancel',
                'down',
                'wentAway']),
            State.State('notAvailable', self.enterNotAvailable, self.exitNotAvailable, [
                'off',
                'wentAway']),
            State.State('wentAway', self.enterWentAway, self.exitWentAway, [
                'off']),
            State.State('already', self.enterAlready, self.exitAlready, [
                'off',
                'endFriendship']),
            State.State('endFriendship', self.enterEndFriendship, self.exitEndFriendship, [
                'off',
                'friendsNoMore']),
            State.State('friendsNoMore', self.enterFriendsNoMore, self.exitFriendsNoMore, [
                'off']),
            State.State('self', self.enterSelf, self.exitSelf, [
                'off']),
            State.State('asking', self.enterAsking, self.exitAsking, [
                'yes',
                'no',
                'otherTooMany',
                'maybe',
                'cancel',
                'wentAway']),
            State.State('yes', self.enterYes, self.exitYes, [
                'off']),
            State.State('no', self.enterNo, self.exitNo, [
                'off']),
            State.State('otherTooMany', self.enterOtherTooMany, self.exitOtherTooMany, [
                'off']),
            State.State('maybe', self.enterMaybe, self.exitMaybe, [
                'off']),
            State.State('down', self.enterDown, self.exitDown, [
                'off']),
            State.State('cancel', self.enterCancel, self.exitCancel, [
                'off'])], 'off', 'off')
        self.context = None
        OnscreenPanel.cleanupPanel('TeleportPanel')
        OnscreenPanel.cleanupPanel('AvatarDetailPanel')
        self.makePanel(rect = (-0.19, 0.81, 0.33, 0.99), bg = (1, 0.89, 0.77, 0.85))
        self.infoText = self.makeText(wordwrap = 13.5, scale = 0.06, pos = (0, 0.13), mayChange = 1)
        self.bOk = self.makeButton('Ok', scale = 0.075, pos = (0, -0.2), manage = 0, func = self._FriendInviter__handleOk, event = 'ok')
        self.bCancel = self.makeButton('Cancel', scale = 0.075, pos = (0, -0.2), manage = 0, func = self._FriendInviter__handleCancel, event = 'cancel')
        self.bYes = self.makeButton('Yes', scale = 0.075, pos = (-0.2, -0.1), manage = 0, func = self._FriendInviter__handleYes, event = 'yes')
        self.bNo = self.makeButton('No', scale = 0.075, pos = (0.2, -0.1), manage = 0, func = self._FriendInviter__handleNo, event = 'no')
        self.bList = self.makeButton('List Friends', scale = 0.05, pos = (0.0, -0.22), manage = 0, func = self._FriendInviter__handleList, event = 'list')
        self.accept(self.avDisableName, self._FriendInviter__handleDisableAvatar)
        self.show()
        self.fsm.enterInitialState()
        self.fsm.request('begin')

    
    def cleanup(self):
        self.fsm.request('cancel')
        self.fsm.request('off')
        OnscreenPanel.OnscreenPanel.cleanup(self)
        self.ignore(self.avDisableName)

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterBegin(self):
        myId = toonbase.localToon.doId
        if self.avId == myId:
            self.fsm.request('self')
        elif toonbase.tcr.isFriend(self.avId):
            self.fsm.request('already')
        else:
            tooMany = len(toonbase.localToon.friendsList) >= MaxFriends
            if tooMany:
                self.fsm.request('tooMany')
            else:
                self.fsm.request('notYet')

    
    def exitBegin(self):
        pass

    
    def enterTooMany(self):
        self.infoText.setText('You have too many friends on your list to add another one now.  You will have to remove some friends if you want to make friends with %s.' % self.avName)
        self.infoText.setPos(0.0, 0.2)
        self.bCancel.manage(self)
        self.bCancel.setPos(0.0, -0.16)
        self.bList.manage(self)
        self.bList.setPos(0.0, -0.26)

    
    def exitTooMany(self):
        self.bCancel.unmanage()
        self.bList.unmanage()

    
    def enterNotYet(self):
        self.infoText.setText('Would you like to make friends with %s?' % self.avName)
        self.bYes.manage(self)
        self.bNo.manage(self)
        self.bList.manage(self)

    
    def exitNotYet(self):
        self.bYes.unmanage()
        self.bNo.unmanage()
        self.bList.unmanage()

    
    def enterCheckAvailability(self):
        if not toonbase.tcr.doId2do.has_key(self.avId):
            self.fsm.request('wentAway')
            return None
        
        if not (toonbase.tcr.friendManager):
            self.notify.warning('No FriendManager available.')
            self.fsm.request('down')
            return None
        
        myId = toonbase.localToon.doId
        toonbase.tcr.friendManager.up_friendQuery(myId, self.avId)
        self.infoText.setText('Seeing if %s is available.' % self.avName)
        self.accept('friendConsidering', self._FriendInviter__friendConsidering)
        self.bCancel.manage(self)

    
    def exitCheckAvailability(self):
        self.ignore('friendConsidering')
        self.bCancel.unmanage()

    
    def enterNotAvailable(self):
        self.infoText.setText('%s is busy right now; try again later.' % self.avName)
        self.context = None
        self.bOk.manage(self)

    
    def exitNotAvailable(self):
        self.bOk.unmanage()

    
    def enterWentAway(self):
        self.infoText.setText('%s went away.' % self.avName)
        if self.context != None:
            toonbase.tcr.friendManager.up_cancelFriendQuery(self.context)
            self.context = None
        
        self.bOk.manage(self)

    
    def exitWentAway(self):
        self.bOk.unmanage()

    
    def enterAlready(self):
        self.infoText.freeze()
        self.infoText.setPos(0, 0.2)
        self.infoText.setText('%s is already your friend.\n\nDo you want to stay friends?' % self.avName)
        self.infoText.thaw()
        self.context = None
        self.bYes.manage(self)
        self.bNo.manage(self)
        self.bList.manage(self)

    
    def exitAlready(self):
        self.infoText.freeze()
        self.infoText.setText('')
        self.infoText.setPos(0, 0.13)
        self.infoText.thaw()
        self.bYes.unmanage()
        self.bNo.unmanage()
        self.bList.unmanage()

    
    def enterEndFriendship(self):
        self.infoText.setText('Are you sure you want to stop being friends with %s?' % self.avName)
        self.context = None
        self.bYes.manage(self)
        self.bNo.manage(self)
        self.bList.manage(self)

    
    def exitEndFriendship(self):
        self.bYes.unmanage()
        self.bNo.unmanage()
        self.bList.unmanage()

    
    def enterFriendsNoMore(self):
        toonbase.tcr.removeFriend(self.avId)
        self.infoText.setText('You are no longer friends with %s.' % self.avName)
        self.bOk.manage(self)
        if not toonbase.tcr.doId2do.has_key(self.avId):
            messenger.send(self.avDisableName)
        

    
    def exitFriendsNoMore(self):
        self.bOk.unmanage()

    
    def enterSelf(self):
        self.infoText.setText("You can't be friends with yourself!")
        self.context = None
        self.bOk.manage(self)

    
    def exitSelf(self):
        self.bOk.unmanage()

    
    def enterAsking(self):
        self.infoText.setText('Asking %s to be your friend.' % self.avName)
        self.accept('friendResponse', self._FriendInviter__friendResponse)
        self.bCancel.manage(self)

    
    def exitAsking(self):
        self.ignore('friendResponse')
        self.bCancel.unmanage()

    
    def enterYes(self):
        self.infoText.setText('%s said yes!' % self.avName)
        self.context = None
        self.bOk.manage(self)

    
    def exitYes(self):
        self.bOk.unmanage()

    
    def enterNo(self):
        self.infoText.setText("%s doesn't want to be your friend." % self.avName)
        self.context = None
        self.bOk.manage(self)

    
    def exitNo(self):
        self.bOk.unmanage()

    
    def enterOtherTooMany(self):
        self.infoText.setText('%s has too many friends already!' % self.avName)
        self.context = None
        self.bOk.manage(self)

    
    def exitOtherTooMany(self):
        self.bOk.unmanage()

    
    def enterMaybe(self):
        self.infoText.setText('%s was unable to answer.' % self.avName)
        self.context = None
        self.bOk.manage(self)

    
    def exitMaybe(self):
        self.bOk.unmanage()

    
    def enterDown(self):
        self.infoText.setText('Cannot make friends now.')
        self.context = None
        self.bOk.manage(self)

    
    def exitDown(self):
        self.bOk.unmanage()

    
    def enterCancel(self):
        if self.context != None:
            toonbase.tcr.friendManager.up_cancelFriendQuery(self.context)
            self.context = None
        
        self.fsm.request('off')

    
    def exitCancel(self):
        pass

    
    def __handleOk(self, okButton, item):
        if okButton == item:
            self.cleanup()
        

    
    def __handleCancel(self, cancelButton, item):
        if cancelButton == item:
            self.cleanup()
        

    
    def __handleYes(self, yesButton, item):
        if yesButton == item:
            if self.fsm.getCurrentState().getName() == 'notYet':
                self.fsm.request('checkAvailability')
            elif self.fsm.getCurrentState().getName() == 'endFriendship':
                self.fsm.request('friendsNoMore')
            else:
                self.cleanup()
        

    
    def __handleNo(self, noButton, item):
        if noButton == item:
            if self.fsm.getCurrentState().getName() == 'already':
                self.fsm.request('endFriendship')
            else:
                self.cleanup()
        

    
    def __handleList(self, friendButton, item):
        if friendButton == item:
            messenger.send('openFriendsList')
        

    
    def __friendConsidering(self, yesNoAlready, context):
        if yesNoAlready == 1:
            self.context = context
            self.fsm.request('asking')
        elif yesNoAlready == 0:
            self.fsm.request('notAvailable')
        elif yesNoAlready == 2:
            self.fsm.request('already')
        else:
            self.fsm.request('self')

    
    def __friendResponse(self, yesNoMaybe, context):
        if self.context != context:
            self.notify.warning('Unexpected change of context from %d to %d.' % (self.context, context))
            self.context = context
        
        if yesNoMaybe == 1:
            self.fsm.request('yes')
        elif yesNoMaybe == 0:
            self.fsm.request('no')
        elif yesNoMaybe == 3:
            self.fsm.request('otherTooMany')
        else:
            self.fsm.request('maybe')

    
    def __handleDisableAvatar(self):
        self.fsm.request('wentAway')


