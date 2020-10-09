# Source Generated with Decompyle++
# File: BodyShop.pyo (Python 2.0)

from ShowBaseGlobal import *
import PandaObject
import AvatarDNA
import StateData
from DirectGui import *

class BodyShop(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.toon = None
        self.torsoChoice = 0
        self.legsChoice = 0
        self.headChoice = 0
        return None

    
    def enter(self, toon):
        base.disableMouse()
        self.toon = toon
        self.dna = self.toon.getStyle()
        self.torsoChoice = AvatarDNA.toonHeadTypes.index(self.dna.head)
        self.legsChoice = AvatarDNA.toonTorsoTypes.index(self.dna.torso)
        self.headChoice = AvatarDNA.toonLegTypes.index(self.dna.legs)
        self.acceptOnce('next', self._BodyShop__handleForward)
        self.acceptOnce('enter', self._BodyShop__handleForward)
        return None

    
    def showButtons(self):
        self.headLButton.show()
        self.headRButton.show()
        self.torsoLButton.show()
        self.torsoRButton.show()
        self.legsLButton.show()
        self.legsRButton.show()

    
    def exit(self):
        del self.toon
        self.headLButton.hide()
        self.headRButton.hide()
        self.torsoLButton.hide()
        self.torsoRButton.hide()
        self.legsLButton.hide()
        self.legsRButton.hide()
        self.ignore('next')
        self.ignore('enter')

    
    def load(self):
        self.gui = loader.loadModelOnce('phase_3/models/gui/create_a_toon_gui')
        guiRArrowDown = self.gui.find('**/CrtATn_R_Arrow_DN')
        guiRArrowRollover = self.gui.find('**/CrtATn_R_Arrow_RLVR')
        guiRArrowUp = self.gui.find('**/CrtATn_R_Arrow_UP')
        guiLArrowDown = self.gui.find('**/CrtATn_LftArrow_DN')
        guiLArrowRollover = self.gui.find('**/CrtATn_LftArrow_RLVR')
        guiLArrowUp = self.gui.find('**/CrtATn_LftArrow_UP')
        self.headLButton = DirectButton(relief = None, image = (guiLArrowUp, guiLArrowDown, guiLArrowRollover), pos = (-0.9, 0, 0.3), command = self._BodyShop__swapHead, extraArgs = [
            -1])
        self.headRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover), pos = (0, 0, 0.3), command = self._BodyShop__swapHead, extraArgs = [
            1])
        self.torsoLButton = DirectButton(relief = None, image = (guiLArrowUp, guiLArrowDown, guiLArrowRollover), pos = (-0.9, 0, -0.1), command = self._BodyShop__swapTorso, extraArgs = [
            -1])
        self.torsoRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover), pos = (0, 0, -0.1), command = self._BodyShop__swapTorso, extraArgs = [
            1])
        self.legsLButton = DirectButton(relief = None, image = (guiLArrowUp, guiLArrowDown, guiLArrowRollover), pos = (-0.9, 0, -0.5), command = self._BodyShop__swapLegs, extraArgs = [
            -1])
        self.legsRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover), pos = (0, 0, -0.5), command = self._BodyShop__swapLegs, extraArgs = [
            1])
        self.headLButton.hide()
        self.headRButton.hide()
        self.torsoLButton.hide()
        self.torsoRButton.hide()
        self.legsLButton.hide()
        self.legsRButton.hide()

    
    def unload(self):
        self.gui.removeNode()
        del self.gui
        self.headLButton.destroy()
        self.headRButton.destroy()
        self.torsoLButton.destroy()
        self.torsoRButton.destroy()
        self.legsLButton.destroy()
        self.legsRButton.destroy()
        del self.headLButton
        del self.headRButton
        del self.torsoLButton
        del self.torsoRButton
        del self.legsLButton
        del self.legsRButton
        return None

    
    def __swapTorso(self, offset):
        self.torsoChoice = (self.torsoChoice + offset) % len(AvatarDNA.toonTorsoTypes)
        torso = AvatarDNA.toonTorsoTypes[self.torsoChoice]
        newTorso = torso[0] + self.dna.getClothes()[0]
        self.dna.torso = newTorso
        self.toon.swapToonTorso(newTorso)
        self.toon.loop('neutral', 0)
        self.toon.swapToonColor(self.dna)

    
    def __swapLegs(self, offset):
        self.legsChoice = (self.legsChoice + offset) % len(AvatarDNA.toonLegTypes)
        newLegs = AvatarDNA.toonLegTypes[self.legsChoice]
        self.dna.legs = newLegs
        self.toon.swapToonLegs(newLegs)
        self.toon.loop('neutral', 0)
        self.toon.swapToonColor(self.dna)

    
    def __swapHead(self, offset):
        self.headChoice = (self.headChoice + offset) % len(AvatarDNA.toonHeadTypes)
        newHead = AvatarDNA.toonHeadTypes[self.headChoice]
        self.dna.head = newHead
        self.toon.swapToonHead(newHead)
        self.toon.loop('neutral', 0)
        self.toon.swapToonColor(self.dna)

    
    def __handleForward(self):
        messenger.send(self.doneEvent)


