# Source Generated with Decompyle++
# File: OptionsPage.pyo (Python 2.0)

from ShowBaseGlobal import *
import ShtikerPage
import DialogBox
from DirectGui import *

class OptionsPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    
    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.title = DirectLabel(parent = self, relief = None, text = 'Options', text_scale = 0.12, pos = (0, 0, 0.6))
        self.exitButton = DirectButton(parent = self, relief = RAISED, text = 'Exit Toontown', text_scale = 0.08, pos = (0, 0, -0.5), pad = (0.04, 0.04), borderWidth = (0.02, 0.02), command = self._OptionsPage__exitShowWithConfirm)

    
    def unload(self):
        del self.title
        del self.exitButton
        ShtikerPage.ShtikerPage.unload(self)

    
    def __exitShowWithConfirm(self):
        self.confirm = DialogBox.DialogBox(doneEvent = 'confirmDone', message = 'Exit Toontown?', style = DialogBox.TwoChoice)
        self.confirm.show()
        self.accept('confirmDone', self._OptionsPage__handleConfirm)
        return None

    
    def __handleConfirm(self):
        status = self.confirm.doneStatus
        self.ignore('confirmDone')
        self.confirm.cleanup()
        del self.confirm
        if status == 'ok':
            self.doneStatus = {
                'mode': 'exit' }
            messenger.send(self.doneEvent)
        
        return None


