# Source Generated with Decompyle++
# File: TownBattleChooseAvatarPanel.pyo (Python 2.0)

from PandaModules import *
from ToontownBattleGlobals import *
import ToontownGlobals
import StateData
import DirectNotifyGlobal
import BattleBase
from DirectGui import *

class TownBattleChooseAvatarPanel(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('ChooseAvatarPanel')
    
    def __init__(self, doneEvent, toon):
        self.notify.info('Init choose panel...')
        StateData.StateData.__init__(self, doneEvent)
        self.numAvatars = 0
        self.chosenAvatar = 0
        self.toon = toon
        return None

    
    def load(self):
        self.gui = loader.loadModelOnce('phase_5/models/gui/battle_gui')
        self.frame = DirectFrame(relief = None, image = self.gui.find('**/BtlPick_TAB'), image_color = Vec4(1, 0.2, 0.2, 1))
        self.frame.hide()
        self.statusFrame = DirectFrame(parent = self.frame, relief = None, image = self.gui.find('**/ToonBtl_Status_BG'), image_color = Vec4(0.5, 0.9, 0.5, 1), pos = (0.611, 0, 0))
        self.textFrame = DirectFrame(parent = self.frame, relief = None, image = self.gui.find('**/PckMn_Select_Tab'), image_color = Vec4(1, 1, 0, 1), text = 'WHICH AVATAR?', text_fg = Vec4(0, 0, 0, 1), text_pos = (0, -0.025, 0), text_scale = 0.08, pos = (-0.013, 0, 0.013))
        if self.toon:
            self.textFrame['text'] = 'WHICH TOON?'
        else:
            self.textFrame['text'] = 'WHICH COG?'
        self.avatarButtons = []
        for i in range(4):
            button = DirectButton(parent = self.frame, relief = None, image = (self.gui.find('**/PckMn_Arrow_Up'), self.gui.find('**/PckMn_Arrow_Dn'), self.gui.find('**/PckMn_Arrow_Rlvr')), command = self._TownBattleChooseAvatarPanel__handleAvatar, extraArgs = [
                i])
            if self.toon:
                button.setScale(1, 1, -1)
                button.setPos(0, 0, -0.2)
            else:
                button.setScale(1, 1, 1)
                button.setPos(0, 0, 0.2)
            self.avatarButtons.append(button)
        
        self.backButton = DirectButton(parent = self.frame, relief = None, image = (self.gui.find('**/PckMn_BackBtn'), self.gui.find('**/PckMn_BackBtn_Dn'), self.gui.find('**/PckMn_BackBtn_Rlvr')), pos = (-0.647, 0, 0.006), scale = 1.05, text = 'BACK', text_scale = 0.05, text_pos = (0.01, -0.012), text_fg = Vec4(0, 0, 0.8, 1), command = self._TownBattleChooseAvatarPanel__handleBack)
        return None

    
    def unload(self):
        self.gui.removeNode()
        del self.gui
        self.frame.destroy()
        del self.frame
        del self.statusFrame
        del self.textFrame
        del self.avatarButtons
        del self.backButton
        return None

    
    def enter(self, numAvatars, localNum = None, luredIndices = None, trappedIndices = None, track = None):
        self.frame.show()
        invalidTargets = []
        if not (self.toon):
            if len(luredIndices) > 0:
                if track == BattleBase.TRAP or track == BattleBase.LURE:
                    invalidTargets += luredIndices
                
            
            if len(trappedIndices) > 0:
                if track == BattleBase.TRAP:
                    invalidTargets += trappedIndices
                
            
        
        self._TownBattleChooseAvatarPanel__placeButtons(numAvatars, invalidTargets, localNum)
        return None

    
    def exit(self):
        self.frame.hide()
        return None

    
    def __handleBack(self):
        doneStatus = {
            'mode': 'Back' }
        messenger.send(self.doneEvent, [
            doneStatus])
        return None

    
    def __handleAvatar(self, avatar):
        doneStatus = {
            'mode': 'Avatar',
            'avatar': avatar }
        messenger.send(self.doneEvent, [
            doneStatus])
        return None

    
    def adjustCogs(self, numAvatars, luredIndices, trappedIndices, track):
        invalidTargets = []
        if len(luredIndices) > 0:
            if track == BattleBase.TRAP or track == BattleBase.LURE:
                invalidTargets += luredIndices
            
        
        if len(trappedIndices) > 0:
            if track == BattleBase.TRAP:
                invalidTargets += trappedIndices
            
        
        self._TownBattleChooseAvatarPanel__placeButtons(numAvatars, invalidTargets, None)
        return None

    
    def adjustToons(self, numToons, localNum):
        self._TownBattleChooseAvatarPanel__placeButtons(numToons, [], localNum)
        return None

    
    def __placeButtons(self, numAvatars, invalidTargets, localNum):
        for i in range(4):
            if numAvatars > i and i not in invalidTargets and i != localNum:
                self.avatarButtons[i].show()
            else:
                self.avatarButtons[i].hide()
        
        if numAvatars == 1:
            self.avatarButtons[0].setX(0)
        elif numAvatars == 2:
            self.avatarButtons[0].setX(0.2)
            self.avatarButtons[1].setX(-0.2)
        elif numAvatars == 3:
            self.avatarButtons[0].setX(0.4)
            self.avatarButtons[1].setX(0.0)
            self.avatarButtons[2].setX(-0.4)
        elif numAvatars == 4:
            self.avatarButtons[0].setX(0.6)
            self.avatarButtons[1].setX(0.2)
            self.avatarButtons[2].setX(-0.2)
            self.avatarButtons[3].setX(-0.6)
        else:
            self.notify.error('Invalid number of avatars: %s' % numAvatars)
        return None


