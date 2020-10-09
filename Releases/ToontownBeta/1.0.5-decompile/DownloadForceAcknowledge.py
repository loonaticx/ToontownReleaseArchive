# Source Generated with Decompyle++
# File: DownloadForceAcknowledge.pyo (Python 2.0)

from ShowBaseGlobal import *
import DialogBox
import Button

class DownloadForceAcknowledge(DialogBox.DialogBox):
    
    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        DialogBox.DialogBox.__init__(self, message = '', doneEvent = doneEvent, style = DialogBox.Acknowledge)
        return None

    
    def enter(self, phase):
        doneStatus = { }
        if not launcher:
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [
                doneStatus])
        elif launcher.getPhaseComplete(phase):
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [
                doneStatus])
        else:
            doneStatus['mode'] = 'incomplete'
            self.doneStatus = doneStatus
            percentComplete = base.launcher.getPercentPhaseComplete(phase)
            self.setMessage("Sorry, you can't advance because download " + str(phase) + ' is only ' + `percentComplete` + '% complete.\n\nPlease try again later.')
            DialogBox.DialogBox.show(self)
        return None

    
    def exit(self):
        DialogBox.DialogBox.hide(self)
        self.ignoreAll()
        return None

    
    def handleOk(self, okButton, item):
        if okButton == item:
            messenger.send(self.doneEvent, [
                self.doneStatus])
        


