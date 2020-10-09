# Source Generated with Decompyle++
# File: NameShop.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
import PandaObject
import OnscreenText
import TextNode
import AvatarDNA
import Avatar
import ChatInput
import ChatFilter
import ChatManager
import StateData
import FSM
import State
import OnscreenPanel
from TaskManagerGlobal import *
import DialogBox
MAX_NAME_WIDTH = 9

class NameShop(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, parentFSM, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.shopsVisited = []
        self.filter = ChatFilter.ChatFilter()
        self.name = ''
        self.toon = None
        self.parentFSM = parentFSM
        return None

    
    def enter(self, toon):
        if toon == None:
            return None
        else:
            self.toon = toon
        if self.isLoaded == 0:
            self.load()
        
        base.disableMouse()
        if self.nameLabel:
            self.nameLabel.reparentTo(aspect2d)
        
        if self.nameBalloon:
            self.nameBalloon.reparentTo(aspect2d)
        
        self._NameShop__resetInput()
        self.nameDisplay.setText(self.name)
        return None

    
    def __overflowNameInput(self):
        self.rejectName('That name is too long. Please try again.')

    
    def exit(self):
        if self.isLoaded == 0:
            return None
        
        self.ignore('chat_exit')
        self.ignore('chat_overflow')
        self.ignore('next')
        self.nameLabel.reparentTo(hidden)
        self.nameBalloon.reparentTo(hidden)
        self.name = self.nameDisplay.getText()
        self.nameInput.reparentTo(base.dataUnused)
        return None

    
    def load(self):
        if self.isLoaded == 1:
            return None
        
        self.nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input')
        self.nameLabel = OnscreenText.OnscreenText('Please type a name:', parent = hidden, style = OnscreenText.ScreenPrompt, pos = (0.15, 0.55))
        self.nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input')
        self.nameBalloon.setPos(-0.2, 0.0, 0.35)
        self.nameBalloon.setScale(0.08, 0.08, 0.08)
        self.nameDisplay = TextNode.TextNode()
        self.nameDisplay.setFont(getToonFont())
        self.nameDisplay.setText('')
        self.nameDisplay.setTextColor(0.0, 0.0, 0.0, 1.0)
        self.nameDisplayNode = self.nameBalloon.attachNewNode(self.nameDisplay)
        self.nameInput = base.mak.attachNewNode(ChatInput.ChatInput(self.nameDisplay))
        self.nameInput.node().setMaxWidth(MAX_NAME_WIDTH)
        self.nameInput.node().reset()
        self.isLoaded = 1
        return None

    
    def unload(self):
        if self.isLoaded == 0:
            return None
        
        self.exit()
        OnscreenPanel.cleanupPanel('globalDialog')
        self.nameInput.removeNode()
        del self.nameInput
        self.nameDisplayNode.removeNode()
        del self.nameDisplayNode
        del self.nameDisplay
        self.nameBalloon.removeNode()
        del self.nameBalloon
        del self.nameLabel
        del self.toon
        self.ignoreAll()
        del self.parentFSM
        del self.filter
        self.isLoaded = 0
        return None

    
    def setShopsVisited(self, list):
        self.shopsVisited = list

    
    def __checkName(self):
        self.ignore('next')
        self.ignore('chat_exit')
        self.ignore('chat_overflow')
        self.name = self.nameDisplay.getText()
        if self.name == '':
            self.rejectName('You must enter a name first.')
        elif self.filter.isValid(self.name):
            messenger.send('NameShop-name', [
                self.name])
        else:
            self.rejectName('That name is not allowed. Please try again.')

    
    def acceptName(self):
        self.toon.setName(self.name)
        messenger.send(self.doneEvent)

    
    def rejectName(self, str):
        self.nameInput.node().reset()
        self.name = ''
        self.rejectDialog = DialogBox.DialogBox(doneEvent = 'rejectDone', message = str, style = DialogBox.Acknowledge)
        self.rejectDialog.show()
        self.acceptOnce('rejectDone', self._NameShop__handleReject)

    
    def __handleReject(self):
        self.rejectDialog.cleanup()
        self._NameShop__resetInput()

    
    def __resetInput(self):
        self.ignore('next')
        self.ignore('chat_exit')
        self.ignore('chat_overflow')
        self.acceptOnce('next', self._NameShop__checkName)
        self.acceptOnce('chat_exit', self._NameShop__checkName)
        self.acceptOnce('chat_overflow', self._NameShop__overflowNameInput)
        self.nameInput.reparentTo(base.mak)


