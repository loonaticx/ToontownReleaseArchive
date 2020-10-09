# Source Generated with Decompyle++
# File: TownBattleRunPanel.pyo (Python 2.0)

from PandaModules import *
import DialogBox
import StateData
import DirectNotifyGlobal

class TownBattleRunPanel(StateData.StateData, DialogBox.DialogBox):
    notify = DirectNotifyGlobal.directNotify.newCategory('TownBattleRunPanel')
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        DialogBox.DialogBox.__init__(self, doneEvent = 'townBattleRunPanelDone', message = 'Run all the way back to the playground?', style = DialogBox.TwoChoice)
        self._TownBattleRunPanel__doneEvent = doneEvent
        return None

    
    def enter(self):
        StateData.StateData.enter(self)
        self.show()
        self.acceptOnce('townBattleRunPanelDone', self._TownBattleRunPanel__doneHandler)
        return None

    
    def exit(self):
        StateData.StateData.exit(self)
        self.hide()
        self.ignore('townBattleRunPanelDone')
        return None

    
    def __doneHandler(self):
        doneStatus = self.doneStatus
        if doneStatus == 'ok':
            doneStatus = { }
            doneStatus['mode'] = 'Yes'
            messenger.send(self._TownBattleRunPanel__doneEvent, [
                doneStatus])
        elif doneStatus == 'cancel':
            doneStatus = { }
            doneStatus['mode'] = 'Back'
            messenger.send(self._TownBattleRunPanel__doneEvent, [
                doneStatus])
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))
        return None


