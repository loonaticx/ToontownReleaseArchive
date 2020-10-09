# Source Generated with Decompyle++
# File: StarForceAcknowledge.pyo (Python 2.0)

from ShowBaseGlobal import *
import DialogBox
import Button

class StarForceAcknowledge(DialogBox.DialogBox):
    
    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        DialogBox.DialogBox.__init__(self, message = '', doneEvent = doneEvent, style = DialogBox.Acknowledge)

    
    def enter(self, starLevel):
        doneStatus = { }
        toonStarLevel = toonbase.localToon.getStarLevel()
        if toonStarLevel >= starLevel:
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [
                doneStatus])
        else:
            doneStatus['mode'] = 'incomplete'
            self.doneStatus = doneStatus
            if toonStarLevel == 1:
                self.setMessage('Sorry, you need ' + str(starLevel) + ' stars to enter. ' + 'You only have ' + str(toonStarLevel) + ' star.')
            else:
                self.setMessage('Sorry, you need ' + str(starLevel) + ' stars to enter. ' + 'You only have ' + str(toonStarLevel) + ' stars.')
            DialogBox.DialogBox.show(self)

    
    def exit(self):
        DialogBox.DialogBox.hide(self)
        self.ignoreAll()

    
    def handleOk(self, okButton, item):
        if okButton == item:
            messenger.send(self.doneEvent, [
                self.doneStatus])
        


