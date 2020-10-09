# Source Generated with Decompyle++
# File: DialogBox.pyo (Python 2.0)

from DirectObject import *
from ShowBaseGlobal import *
from GuiGlobals import *
import DirectNotifyGlobal
import string
import OnscreenText
import Button
import StateData
import OnscreenPanel
NoButtons = 0
Acknowledge = 1
TwoChoice = 2

class DialogBox(OnscreenPanel.OnscreenPanel):
    notify = DirectNotifyGlobal.directNotify.newCategory('DialogBox')
    
    def __init__(self, message = '', doneEvent = None, style = NoButtons, font = getDefaultFont(), wordwrap = 12, okButtonText = 'OK', cancelButtonText = 'Cancel'):
        if doneEvent == None and style != NoButtons:
            self.notify.error('Boxes with buttons must specify a doneEvent.')
        
        self._DialogBox__doneEvent = doneEvent
        self.message = message
        self.style = style
        self.font = font
        self.wordwrap = wordwrap
        self.okButtonText = okButtonText
        self.cancelButtonText = cancelButtonText
        OnscreenPanel.OnscreenPanel.__init__(self, 'globalDialog')
        self.makePanel(rect = (-0.5, 0.5, -0.4, 0.4), drawOrder = 32000, font = self.font, bg = (0.8, 0.8, 0.8, 1.0))
        self.makeText(self.message, wordwrap = self.wordwrap, scale = 0.08, pos = (0.0, 0.25))
        if self.style == TwoChoice:
            self.makeButton(self.okButtonText, pos = (-0.325, -0.25), func = self.handleOk, event = 'ok')
            self.makeButton(self.cancelButtonText, pos = (0.2, -0.25), func = self.handleCancel, event = 'cancel')
        elif self.style == Acknowledge:
            self.makeButton(self.okButtonText, pos = (0.0, -0.25), func = self.handleOk, event = 'ok')
        elif self.style == NoButtons:
            pass
        else:
            self.notify.error('No such style as: ' + str(self.style))
        return None

    
    def show(self):
        base.transitions.fadeScreen()
        OnscreenPanel.OnscreenPanel.show(self)
        return None

    
    def hide(self):
        base.transitions.noTransitions()
        OnscreenPanel.OnscreenPanel.hide(self)
        return None

    
    def cleanup(self):
        self.hide()
        OnscreenPanel.OnscreenPanel.cleanup(self)
        return None

    
    def handleOk(self, okButton, item):
        if okButton == item:
            self.doneStatus = 'ok'
            messenger.send(self._DialogBox__doneEvent)
        

    
    def handleCancel(self, cancelButton, item):
        if cancelButton == item:
            self.doneStatus = 'cancel'
            messenger.send(self._DialogBox__doneEvent)
        

    
    def setMessage(self, message):
        self.panelText[0].setText(message)


