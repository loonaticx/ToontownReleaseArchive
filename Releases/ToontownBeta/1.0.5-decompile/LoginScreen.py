# Source Generated with Decompyle++
# File: LoginScreen.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
import PandaObject
import OnscreenText
import TextNode
import ChatInput
import ChatFilter
import ChatManager
import StateData
from TaskManagerGlobal import *
MAX_NAME_LEN = 20

class LoginScreen(PandaObject.PandaObject, StateData.StateData):
    AutoLoginName = base.config.GetString('auto-login', '')
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.soundForward = None
        return None

    
    def enter(self):
        if self.AutoLoginName:
            self.loginName = self.AutoLoginName
            messenger.send(self.doneEvent)
            return None
        
        if self.isLoaded == 0:
            self.load()
        
        base.disableMouse()
        if self.title:
            self.title.reparentTo(aspect2d)
        
        if self.nameLabel:
            self.nameLabel.reparentTo(aspect2d)
        
        if self.nameBalloon:
            self.nameBalloon.reparentTo(aspect2d)
        
        if self.confirm:
            self.confirm.reparentTo(aspect2d)
        
        self.loginName = ''
        if self.nameInput:
            self.accept('chat_exit', self._LoginScreen__updateName)
            self.accept('chat_overflow', self._LoginScreen__updateName)
        
        return None

    
    def exit(self):
        if self.isLoaded == 0:
            return None
        
        self.ignore('chat_exit')
        self.ignore('chat_overflow')
        self.title.reparentTo(hidden)
        self.confirm.reparentTo(hidden)
        self.nameBalloon.reparentTo(hidden)
        self.nameLabel.reparentTo(hidden)
        self.nameInput.reparentTo(base.dataUnused)
        return None

    
    def load(self):
        if self.isLoaded == 1:
            return None
        
        self.title = OnscreenText.OnscreenText('ToonTown Online Login', parent = hidden, style = OnscreenText.ScreenTitle, pos = (0.0, 0.8))
        self.nameLabel = OnscreenText.OnscreenText('Please type your account name:', parent = hidden, style = OnscreenText.ScreenPrompt, pos = (0.0, 0.5))
        self.nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input')
        self.nameBalloon.setPos(-0.35, 0.0, 0.2)
        self.nameBalloon.setScale(0.08, 0.08, 0.08)
        self.nameDisplay = TextNode.TextNode()
        self.nameDisplay.setFont(getToonFont())
        self.nameDisplay.setTextColor(0.0, 0.0, 0.0, 1.0)
        self.nameDisplay.setText('')
        self.nameDisplayNode = self.nameBalloon.attachNewNode(self.nameDisplay)
        self.confirm = OnscreenText.OnscreenText(style = OnscreenText.NameConfirm, pos = (0.0, -0.8))
        self.filter = ChatFilter.ChatFilter()
        self.nameInput = base.mak.attachNewNode(ChatInput.ChatInput(self.nameDisplay))
        self.nameInput.node().setMaxChars(MAX_NAME_LEN)
        self.nameInput.node().reset()
        self.soundForward = base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.mp3')
        self.isLoaded = 1
        return None

    
    def unload(self):
        if self.isLoaded == 0:
            return None
        
        self.exit()
        self.nameBalloon.removeNode()
        self.nameLabel.removeNode()
        self.nameLabel.cleanup()
        self.nameLabel = None
        self.nameInput.removeNode()
        self.isLoaded = 0
        return None

    
    def getLoginName(self):
        return self.loginName

    
    def __updateName(self):
        base.playSfx(self.soundForward)
        name = self.nameDisplay.getText()
        self.loginName = name
        messenger.send(self.doneEvent)


