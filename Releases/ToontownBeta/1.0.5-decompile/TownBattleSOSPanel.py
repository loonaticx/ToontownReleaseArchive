# Source Generated with Decompyle++
# File: TownBattleSOSPanel.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
import PandaObject
import Button
import ListBox
import DirectNotifyGlobal
import OnscreenPanel
import StateData

class TownBattleSOSPanel(OnscreenPanel.OnscreenPanel, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('TownBattleSOSPanel')
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)

    
    def cleanup(self):
        self.unload()

    
    def load(self):
        if self.isLoaded:
            return None
        
        self.lb = None
        self.friends = None
        OnscreenPanel.OnscreenPanel.__init__(self, 'SOSPanel')
        self.makePanel(rect = (-0.25, 0.25, -0.49, 0.49), bg = (0.9, 0.1, 0.1, 0.8))
        self.titleText = self.makeText(scale = 0.06, pos = (0, 0.4), mayChange = 1)
        self.backButton = self.makeButton('Back', manage = 0, scale = 0.05, pos = (-0.15, -0.46), func = self._TownBattleSOSPanel__handleBack, event = 'back')
        self.hide()
        self.isLoaded = 1

    
    def enter(self, time):
        self.show()
        self.accept('friendOnline', self._TownBattleSOSPanel__friendOnline)
        self.accept('friendOffline', self._TownBattleSOSPanel__friendOffline)
        self.accept('friendsListChanged', self._TownBattleSOSPanel__friendsListChanged)
        self.backButton.manage(self)
        self.backButton.startBehavior()
        self._TownBattleSOSPanel__reinit()

    
    def exit(self):
        self.hide()
        self._TownBattleSOSPanel__ignoreClicks()
        self.ignore('friendOnline')
        self.ignore('friendOffline')
        self.ignore('friendsListChanged')
        self.backButton.unmanage()

    
    def unload(self):
        if not (self.isLoaded):
            return None
        
        if OnscreenPanel.OnscreenPanel.cleanup(self):
            if self.lb != None:
                self.lb.cleanup()
            
        
        del self.backButton
        del self.titleText
        self.isLoaded = 0

    
    def updateTimer(self, time):
        pass

    
    def __reinit(self):
        self.titleText.setText('Call which friend?')
        self._TownBattleSOSPanel__makeListBox()

    
    def __makeListBox(self):
        if self.lb != None:
            self.lb.cleanup()
            self.lb = None
            del self.lbUp
            del self.lbDown
        
        self.lb = ListBox.ListBox('FriendsList', 15, scale = 0.046, width = 8, font = getToonFont())
        self.lbUp = self.lb.getUpButton()
        self.lbDown = self.lb.getDownButton()
        self.lb.setPos(0, 0.3)
        self.lbUp.setPos(0, 0.36)
        self.lbDown.setPos(0, -0.4)
        friends = []
        index = 0
        for doId in toonbase.localToon.friendsList:
            if toonbase.tcr.isFriendOnline(doId):
                handle = toonbase.tcr.identifyFriend(doId)
                if handle != None:
                    friends.append(('FriendsList-' + str(index), handle.getName(), handle, 'FriendsListDoit', toonbase.localToon.friendsList.index(doId)))
                    index += 1
                
            
        
        if len(friends) == 0:
            self.titleText.setText('No one to call!')
        
        self._TownBattleSOSPanel__acceptClicks(friends)
        self.lb.addItems(friends)
        self.lbUp.manage(self)
        self.lbDown.manage(self)
        self.lb.manage(self)

    
    def __acceptClicks(self, friends):
        self._TownBattleSOSPanel__ignoreClicks()
        self.friends = friends
        self.accept('FriendsListDoit', self._TownBattleSOSPanel__handlePickedFriend)

    
    def __ignoreClicks(self):
        if self.friends != None:
            self.ignore('FriendsListDoit')
        

    
    def __handlePickedFriend(self, item, idx):
        doId = toonbase.localToon.friendsList[idx]
        doneStatus = { }
        doneStatus['mode'] = 'Friend'
        doneStatus['friend'] = doId
        messenger.send(self.doneEvent, [
            doneStatus])

    
    def __handleBack(self, backButton, item):
        if item == backButton:
            doneStatus = { }
            doneStatus['mode'] = 'Back'
            messenger.send(self.doneEvent, [
                doneStatus])
        

    
    def __friendOnline(self, doId):
        self._TownBattleSOSPanel__makeListBox()

    
    def __friendOffline(self, doId):
        self._TownBattleSOSPanel__makeListBox()

    
    def __friendsListChanged(self):
        self._TownBattleSOSPanel__makeListBox()


