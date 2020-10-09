# Source Generated with Decompyle++
# File: ClothesShop.pyo (Python 2.0)

from ShowBaseGlobal import *
import PandaObject
import AvatarDNA
import StateData
from DirectGui import *

class ClothesShop(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.shopsVisited = []
        self.toon = None
        return None

    
    def enter(self, toon):
        base.disableMouse()
        self.toon = toon
        self.dna = self.toon.getStyle()
        self.bottomType = self.dna.getClothes()
        self.bottomChoice = self.dna.botTex
        self.topChoice = self.dna.topTex
        self.acceptOnce('next', self._ClothesShop__handleForward)
        self.acceptOnce('enter', self._ClothesShop__handleForward)
        return None

    
    def showButtons(self):
        self.topLButton.show()
        self.topRButton.show()
        self.bottomLButton.show()
        self.bottomRButton.show()

    
    def exit(self):
        del self.toon
        self.topLButton.hide()
        self.topRButton.hide()
        self.bottomLButton.hide()
        self.bottomRButton.hide()
        self.ignore('enter')
        self.ignore('next')

    
    def load(self):
        self.gui = loader.loadModelOnce('phase_3/models/gui/create_a_toon_gui')
        guiRArrowDown = self.gui.find('**/CrtATn_R_Arrow_DN')
        guiRArrowRollover = self.gui.find('**/CrtATn_R_Arrow_RLVR')
        guiRArrowUp = self.gui.find('**/CrtATn_R_Arrow_UP')
        guiLArrowDown = self.gui.find('**/CrtATn_LftArrow_DN')
        guiLArrowRollover = self.gui.find('**/CrtATn_LftArrow_RLVR')
        guiLArrowUp = self.gui.find('**/CrtATn_LftArrow_UP')
        self.topLButton = DirectButton(relief = None, image = (guiLArrowUp, guiLArrowDown, guiLArrowRollover), pos = (-0.9, 0, 0), command = self._ClothesShop__swapTop, extraArgs = [
            -1])
        self.topRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover), pos = (0, 0, 0), command = self._ClothesShop__swapTop, extraArgs = [
            1])
        self.bottomLButton = DirectButton(relief = None, image = (guiLArrowUp, guiLArrowDown, guiLArrowRollover), pos = (-0.9, 0, -0.4), command = self._ClothesShop__swapBottom, extraArgs = [
            -1])
        self.bottomRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover), pos = (0, 0, -0.4), command = self._ClothesShop__swapBottom, extraArgs = [
            1])
        self.topLButton.hide()
        self.topRButton.hide()
        self.bottomLButton.hide()
        self.bottomRButton.hide()
        return None

    
    def unload(self):
        self.gui.removeNode()
        del self.gui
        self.topLButton.destroy()
        self.topRButton.destroy()
        self.bottomLButton.destroy()
        self.bottomRButton.destroy()
        del self.topLButton
        del self.topRButton
        del self.bottomLButton
        del self.bottomRButton
        return None

    
    def __swapTop(self, offset):
        self.topChoice = (self.topChoice + offset) % AvatarDNA.numToonShirtTypes
        self.toon.style.topTex = self.topChoice
        self.toon.generateToonClothes()

    
    def __swapBottom(self, offset):
        self.bottomChoice = (self.bottomChoice + offset) % (AvatarDNA.numToonShortTypes + AvatarDNA.numToonSkirtTypes)
        switch = 0
        if self.bottomType == 's':
            if self.bottomChoice >= AvatarDNA.numToonShortTypes:
                self.bottomType = 'd'
                switch = 1
            
        elif self.bottomChoice < AvatarDNA.numToonShortTypes:
            self.bottomType = 's'
            switch = 1
        
        if self.bottomType == 's':
            self.toon.style.botTex = self.bottomChoice
        else:
            self.toon.style.botTex = self.bottomChoice - AvatarDNA.numToonShortTypes
        if switch:
            newTorso = self.dna.torso[0] + self.bottomType
            self.toon.swapToonTorso(newTorso)
            self.toon.loop('neutral', 0)
            self.toon.swapToonColor(self.dna)
        
        self.toon.generateToonClothes()

    
    def __handleForward(self):
        messenger.send(self.doneEvent)


