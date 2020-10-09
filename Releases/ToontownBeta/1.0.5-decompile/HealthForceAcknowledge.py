# Source Generated with Decompyle++
# File: HealthForceAcknowledge.pyo (Python 2.0)

from ShowBaseGlobal import *
import DialogBox
import Button

class HealthForceAcknowledge(DialogBox.DialogBox):
    
    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        DialogBox.DialogBox.__init__(self, message = '', doneEvent = doneEvent, style = DialogBox.Acknowledge)

    
    def enter(self, hpLevel):
        doneStatus = { }
        toonHp = toonbase.localToon.getHp()
        if toonHp >= hpLevel:
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [
                doneStatus])
        else:
            doneStatus['mode'] = 'incomplete'
            self.doneStatus = doneStatus
            self.setMessage('You cannot leave the playground until your Laffmeter is smiling!')
            DialogBox.DialogBox.show(self)

    
    def exit(self):
        DialogBox.DialogBox.hide(self)
        self.ignoreAll()

    
    def handleOk(self, okButton, item):
        if okButton == item:
            messenger.send(self.doneEvent, [
                self.doneStatus])
        


