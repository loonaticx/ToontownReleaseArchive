# Source Generated with Decompyle++
# File: TutorialForceAcknowledge.pyo (Python 2.0)

from ShowBaseGlobal import *
import DialogBox
import Button

class TutorialForceAcknowledge(DialogBox.DialogBox):
    
    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        DialogBox.DialogBox.__init__(self, message = '', doneEvent = doneEvent, style = DialogBox.Acknowledge)
        return None

    
    def enter(self):
        doneStatus = { }
        doneStatus['mode'] = 'incomplete'
        self.doneStatus = doneStatus
        self.setMessage('You are going the wrong way! Go find Mickey!')
        DialogBox.DialogBox.show(self)
        toonbase.localToon.loop('neutral')
        return None

    
    def exit(self):
        DialogBox.DialogBox.hide(self)
        self.ignoreAll()
        return None

    
    def handleOk(self, okButton, item):
        if okButton == item:
            messenger.send(self.doneEvent, [
                self.doneStatus])
        


