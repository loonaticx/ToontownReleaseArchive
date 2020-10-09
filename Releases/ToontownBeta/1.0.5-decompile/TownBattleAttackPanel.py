# Source Generated with Decompyle++
# File: TownBattleAttackPanel.pyo (Python 2.0)

from DirectObject import *
from ShowBaseGlobal import *
from GuiGlobals import *
import DirectNotifyGlobal
import string
import OnscreenText
import Button
import StateData
import OnscreenPanel

class TownBattleAttackPanel(StateData.StateData):
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        return None

    
    def load(self):
        return None

    
    def unload(self):
        return None

    
    def enter(self):
        StateData.StateData.enter(self)
        toonbase.localToon.inventory.show()
        self.accept('inventory-selection', self._TownBattleAttackPanel__handleInventory)
        self.accept('inventory-run', self._TownBattleAttackPanel__handleRun)
        self.accept('inventory-sos', self._TownBattleAttackPanel__handleSOS)
        self.accept('inventory-pass', self._TownBattleAttackPanel__handlePass)
        return None

    
    def exit(self):
        StateData.StateData.exit(self)
        self.ignore('inventory-selection')
        self.ignore('inventory-run')
        self.ignore('inventory-sos')
        self.ignore('inventory-pass')
        toonbase.localToon.inventory.hide()
        return None

    
    def __handleRun(self):
        doneStatus = {
            'mode': 'Run' }
        messenger.send(self.doneEvent, [
            doneStatus])
        return None

    
    def __handleSOS(self):
        doneStatus = {
            'mode': 'SOS' }
        messenger.send(self.doneEvent, [
            doneStatus])
        return None

    
    def __handlePass(self):
        doneStatus = {
            'mode': 'Pass' }
        messenger.send(self.doneEvent, [
            doneStatus])
        return None

    
    def __handleInventory(self, track, level):
        if toonbase.localToon.inventory.numItem(track, level) > 0:
            doneStatus = { }
            doneStatus['mode'] = 'Inventory'
            doneStatus['track'] = track
            doneStatus['level'] = level
            messenger.send(self.doneEvent, [
                doneStatus])
        else:
            self.notify.error("An item we don't have: track %s level %s was selected." % [
                track,
                level])
        return None


