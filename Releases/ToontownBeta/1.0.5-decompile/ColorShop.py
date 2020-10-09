# Source Generated with Decompyle++
# File: ColorShop.pyo (Python 2.0)

from ShowBaseGlobal import *
import PandaObject
import AvatarDNA
import StateData
from DirectGui import *

class ColorShop(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.toon = None
        return None

    
    def enter(self, toon):
        base.disableMouse()
        self.toon = toon
        self.dna = toon.getStyle()
        self.headChoice = AvatarDNA.defaultColorList.index(self.dna.headColor)
        self.armChoice = AvatarDNA.defaultColorList.index(self.dna.armColor)
        self.legChoice = AvatarDNA.defaultColorList.index(self.dna.legColor)
        self.acceptOnce('next', self._ColorShop__handleForward)
        self.acceptOnce('enter', self._ColorShop__handleForward)
        return None

    
    def showButtons(self):
        self.headLButton.show()
        self.headRButton.show()
        self.armLButton.show()
        self.armRButton.show()
        self.legsLButton.show()
        self.legsRButton.show()
        return None

    
    def exit(self):
        self.ignore('next')
        self.ignore('enter')
        del self.toon
        self.headLButton.hide()
        self.headRButton.hide()
        self.armLButton.hide()
        self.armRButton.hide()
        self.legsLButton.hide()
        self.legsRButton.hide()
        return None

    
    def load(self):
        self.gui = loader.loadModelOnce('phase_3/models/gui/create_a_toon_gui')
        guiRArrowDown = self.gui.find('**/CrtATn_R_Arrow_DN')
        guiRArrowRollover = self.gui.find('**/CrtATn_R_Arrow_RLVR')
        guiRArrowUp = self.gui.find('**/CrtATn_R_Arrow_UP')
        guiLArrowDown = self.gui.find('**/CrtATn_LftArrow_DN')
        guiLArrowRollover = self.gui.find('**/CrtATn_LftArrow_RLVR')
        guiLArrowUp = self.gui.find('**/CrtATn_LftArrow_UP')
        self.headLButton = DirectButton(relief = None, image = (guiLArrowUp, guiLArrowDown, guiLArrowRollover), pos = (-0.9, 0, 0.3), command = self._ColorShop__swapHeadColor, extraArgs = [
            -1])
        self.headRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover), pos = (0, 0, 0.3), command = self._ColorShop__swapHeadColor, extraArgs = [
            1])
        self.armLButton = DirectButton(relief = None, image = (guiLArrowUp, guiLArrowDown, guiLArrowRollover), pos = (-0.9, 0, -0.1), command = self._ColorShop__swapArmColor, extraArgs = [
            -1])
        self.armRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover), pos = (0, 0, -0.1), command = self._ColorShop__swapArmColor, extraArgs = [
            1])
        self.legsLButton = DirectButton(relief = None, image = (guiLArrowUp, guiLArrowDown, guiLArrowRollover), pos = (-0.9, 0, -0.5), command = self._ColorShop__swapLegColor, extraArgs = [
            -1])
        self.legsRButton = DirectButton(relief = None, image = (guiRArrowUp, guiRArrowDown, guiRArrowRollover), pos = (0, 0, -0.5), command = self._ColorShop__swapLegColor, extraArgs = [
            1])
        self.headLButton.hide()
        self.headRButton.hide()
        self.armLButton.hide()
        self.armRButton.hide()
        self.legsLButton.hide()
        self.legsRButton.hide()
        return None

    
    def unload(self):
        self.gui.removeNode()
        del self.gui
        self.headLButton.destroy()
        self.headRButton.destroy()
        self.armLButton.destroy()
        self.armRButton.destroy()
        self.legsLButton.destroy()
        self.legsRButton.destroy()
        del self.headLButton
        del self.headRButton
        del self.armLButton
        del self.armRButton
        del self.legsLButton
        del self.legsRButton
        return None

    
    def __swapHeadColor(self, offset):
        self.headChoice = (self.headChoice + offset) % len(AvatarDNA.defaultColorList)
        newColor = AvatarDNA.defaultColorList[self.headChoice]
        self.dna.headColor = newColor
        self.toon.swapToonColor(self.dna)

    
    def __swapArmColor(self, offset):
        self.armChoice = (self.armChoice + offset) % len(AvatarDNA.defaultColorList)
        newColor = AvatarDNA.defaultColorList[self.armChoice]
        self.dna.armColor = newColor
        self.toon.swapToonColor(self.dna)

    
    def __swapLegColor(self, offset):
        self.legChoice = (self.legChoice + offset) % len(AvatarDNA.defaultColorList)
        newColor = AvatarDNA.defaultColorList[self.legChoice]
        self.dna.legColor = newColor
        self.toon.swapToonColor(self.dna)

    
    def __handleForward(self):
        messenger.send(self.doneEvent)


