# Source Generated with Decompyle++
# File: FriendsListPanel.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
import PandaObject
import Button
import ListBox
import DirectNotifyGlobal
import OnscreenPanel
import AvatarPanel
FLPOnline = 1
FLPAll = 2
FLPEnemies = 3

class FriendsListPanel(OnscreenPanel.OnscreenPanel):
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendsListPanel')
    currentFriendsListPanel = None
    
    def __init__(self, panelType):
        OnscreenPanel.OnscreenPanel.__init__(self, 'FriendsListPanel')
        if FriendsListPanel.currentFriendsListPanel:
            FriendsListPanel.currentFriendsListPanel.cleanup()
        
        FriendsListPanel.currentFriendsListPanel = self
        self.lb = None
        self.avatars = None
        self.panelType = panelType
        toonbase.localToon.obscureFriendsListButton(1)
        if AvatarPanel.AvatarPanel.currentAvatarPanel:
            AvatarPanel.AvatarPanel.currentAvatarPanel.cleanup()
            AvatarPanel.AvatarPanel.currentAvatarPanel = None
        
        self.makePanel(rect = (0.82, 1.32, 0.01, 0.99), bg = (1, 0.89, 0.77, 0.85))
        self.titleText = self.makeText('', scale = 0.06, pos = (0, 0.4), mayChange = 1)
        self.makeButton('Close', scale = 0.05, pos = (0.0, -0.46), func = self._FriendsListPanel__handleClose, event = 'close')
        arrow = loader.loadModelOnce('phase_3/models/props/page-arrow')
        self.bNext = self.makeButton('Next', label = arrow, scale = 0.05, pos = (0.2, -0.44), func = self._FriendsListPanel__handleNext, litStyle = (1, 1, 0, 1), downStyle = (0, 0, 0, 1), manage = 0, event = 'next')
        if arrow:
            arrow.setR(180)
        
        self.bPrev = self.makeButton('Prev', label = arrow, scale = 0.05, pos = (-0.2, -0.44), func = self._FriendsListPanel__handlePrev, litStyle = (1, 1, 0, 1), downStyle = (0, 0, 0, 1), manage = 0, event = 'prev')
        if arrow:
            arrow.removeNode()
        
        self.accept('friendOnline', self._FriendsListPanel__friendOnline)
        self.accept('friendOffline', self._FriendsListPanel__friendOffline)
        self.accept('friendsListChanged', self._FriendsListPanel__friendsListChanged)
        self._FriendsListPanel__reinit()

    
    def __reinit(self):
        if self.panelType == FLPOnline:
            self.titleText.setText('Online friends')
            self.bNext.manage(self)
            self.bNext.startBehavior()
            self.bPrev.unmanage()
            self.panelGeom.setColor(1, 0.89, 0.77, 0.85)
        elif self.panelType == FLPAll:
            self.titleText.setText('All friends')
            self.bNext.manage(self)
            self.bPrev.manage(self)
            self.bNext.startBehavior()
            self.bPrev.startBehavior()
            self.panelGeom.setColor(0.89, 0.89, 0.89, 0.85)
        elif self.panelType == FLPEnemies:
            self.titleText.setText('Ignored Toons')
            self.bNext.unmanage()
            self.bPrev.manage(self)
            self.bPrev.startBehavior()
            self.panelGeom.setColor(1, 0.6, 0.6, 0.85)
        
        self._FriendsListPanel__makeListBox()
        self.show()

    
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
        avatars = []
        index = 0
        if self.panelType == FLPOnline:
            for doId in toonbase.localToon.friendsList:
                if toonbase.tcr.isFriendOnline(doId):
                    handle = toonbase.tcr.identifyFriend(doId)
                    if handle != None:
                        avatars.append(('FriendsList-' + str(index), handle.getName(), handle, 'FriendsListDoit', toonbase.localToon.friendsList.index(doId)))
                        index += 1
                    
                
            
        elif self.panelType == FLPAll:
            for doId in toonbase.localToon.friendsList:
                handle = toonbase.tcr.identifyFriend(doId)
                if handle != None:
                    avatars.append(('FriendsList-' + str(index), handle.getName(), handle, 'FriendsListDoit', toonbase.localToon.friendsList.index(doId)))
                    index += 1
                
            
        
        self._FriendsListPanel__acceptClicks(avatars)
        self.lb.addItems(avatars)
        self.lbUp.manage(self)
        self.lbDown.manage(self)
        self.lb.manage(self)

    
    def __acceptClicks(self, avatars):
        self._FriendsListPanel__ignoreClicks()
        self.avatars = avatars
        self.accept('FriendsListDoit', self._FriendsListPanel__handlePickedFriend)

    
    def __ignoreClicks(self):
        if self.avatars != None:
            self.ignore('FriendsListDoit')
        

    
    def __handlePickedFriend(self, item, idx):
        doId = toonbase.localToon.friendsList[idx]
        handle = toonbase.tcr.identifyFriend(doId)
        messenger.send('clickedNametag', [
            handle])

    
    def __friendOnline(self, doId):
        if self.panelType == FLPOnline:
            self._FriendsListPanel__makeListBox()
        

    
    def __friendOffline(self, doId):
        if self.panelType == FLPOnline:
            self._FriendsListPanel__makeListBox()
        

    
    def __friendsListChanged(self):
        if self.panelType != FLPEnemies:
            self._FriendsListPanel__makeListBox()
        

    
    def cleanup(self):
        if OnscreenPanel.OnscreenPanel.cleanup(self):
            if self.lb != None:
                self.lb.cleanup()
            
            self._FriendsListPanel__ignoreClicks()
            toonbase.localToon.obscureFriendsListButton(-1)
        
        self.ignore('friendOnline')
        self.ignore('friendOffline')
        self.ignore('friendsListChanged')

    
    def __handleClose(self, closeButton, item):
        if item == closeButton:
            self.cleanup()
            FriendsListPanel.currentFriendsListPanel = None
        

    
    def __handleNext(self, nextButton, item):
        if item == nextButton:
            if self.panelType < FLPEnemies:
                self.panelType += 1
            
            self._FriendsListPanel__reinit()
        

    
    def __handlePrev(self, prevButton, item):
        if item == prevButton:
            if self.panelType > FLPOnline:
                self.panelType -= 1
            
            self._FriendsListPanel__reinit()
        


