# Source Generated with Decompyle++
# File: ChatManager.pyo (Python 2.0)

import Task
import string
import sys
import PandaObject
import ToontownGlobals
import GuiGlobals
import ChatInputNormal
import ChatInputQuickTalker
import FSM
import State
from DirectGui import *
OnScreen = 0
OffScreen = 1
Thought = 2
ThoughtPrefix = '.'

def isThought(message):
    if len(message) == 0:
        return 0
    elif string.find(message, ThoughtPrefix, 0, len(ThoughtPrefix)) >= 0:
        return 1
    else:
        return 0


def removeThoughtPrefix(message):
    if isThought(message):
        return message[len(ThoughtPrefix):]
    else:
        return message


class ChatManager(PandaObject.PandaObject):
    
    def __init__(self):
        self.execChat = base.config.GetBool('exec-chat', 0)
        self.fsm = FSM.FSM('chatManager', [
            State.State('off', self.enterOff, self.exitOff, [
                'mainMenu']),
            State.State('mainMenu', self.enterMainMenu, self.exitMainMenu, [
                'quickTalker',
                'normalChat']),
            State.State('quickTalker', self.enterQuickTalker, self.exitQuickTalker, [
                'mainMenu']),
            State.State('normalChat', self.enterNormalChat, self.exitNormalChat, [
                'mainMenu'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.chatInputGui = loader.loadModel('phase_4/models/gui/chat_input_gui')
        self.normalButton = DirectButton(image = (self.chatInputGui.find('**/ChtBx_ChtBtn_UP'), self.chatInputGui.find('**/ChtBx_ChtBtn_DN'), self.chatInputGui.find('**/ChtBx_ChtBtn_RLVR')), pos = (-1.2647, 0, 0.928), scale = 1.179, relief = None, image_color = Vec4(1, 1, 1, 1), text = ('', 'Chat', 'Chat'), text_scale = 0.06, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -0.09), text_font = ToontownGlobals.getInterfaceFont(), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self._ChatManager__normalButtonPressed)
        self.normalButton.hide()
        self.qtButton = DirectButton(image = (self.chatInputGui.find('**/ChtBx_ChtBtn_UP'), self.chatInputGui.find('**/ChtBx_ChtBtn_DN'), self.chatInputGui.find('**/ChtBx_ChtBtn_RLVR')), pos = (-1.129, 0, 0.928), scale = 1.179, relief = None, image_color = Vec4(0.75, 1, 0.75, 1), text = ('', 'ToonTalker', 'ToonTalker'), text_scale = 0.06, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -0.09), text_font = ToontownGlobals.getInterfaceFont(), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self._ChatManager__qtButtonPressed)
        self.qtButton.hide()
        if launcher:
            self.canChat = launcher.getChatPermission()
            chatOverride = base.config.GetBool('chat-override', 0)
            if chatOverride:
                self.canChat = 1
            
        else:
            self.canChat = base.config.GetBool('chat-permission', 1)
        self.chatInputNormal = ChatInputNormal.ChatInputNormal(self)
        self.chatInputQuickTalker = ChatInputQuickTalker.ChatInputQuickTalker(self)
        return None

    
    def delete(self):
        del self.fsm
        self.chatInputNormal.delete()
        del self.chatInputNormal
        self.chatInputQuickTalker.delete()
        del self.chatInputQuickTalker
        loader.unloadModel('phase_4/models/gui/chat_input_gui')
        self.chatInputGui.removeNode()
        del self.chatInputGui
        self.normalButton.destroy()
        del self.normalButton
        self.qtButton.destroy()
        del self.qtButton

    
    def stop(self):
        self.fsm.request('off')

    
    def start(self):
        self.fsm.request('mainMenu')

    
    def sendChatString(self, message):
        chatFlags = CFSpeech | CFTimeout
        if isThought(message):
            message = removeThoughtPrefix(message)
            chatFlags = CFThought
        
        messenger.send('chatUpdate', [
            message,
            chatFlags])

    
    def sendQTChatMessage(self, QTmessage):
        messenger.send('chatUpdateQT', [
            QTmessage])

    
    def chatPermission(self):
        return self.canChat

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterMainMenu(self):
        if self.canChat:
            self.normalButton.show()
            self.chatInputNormal.chatEntry['backgroundFocus'] = 1
            self.acceptOnce('enterNormalChat', self.fsm.request, [
                'normalChat'])
        else:
            self.chatInputNormal.chatEntry['backgroundFocus'] = 0
        self.qtButton.show()

    
    def exitMainMenu(self):
        if self.canChat:
            self.ignore('enterNormalChat')
            self.normalButton.hide()
        
        self.qtButton.hide()

    
    def enterQuickTalker(self):
        if self.canChat:
            self.chatInputNormal.chatEntry['backgroundFocus'] = 0
        
        self.chatInputQuickTalker.show()

    
    def exitQuickTalker(self):
        self.chatInputQuickTalker.hide()

    
    def enterNormalChat(self):
        self.chatInputNormal.show()

    
    def exitNormalChat(self):
        self.chatInputNormal.hide()

    
    def __normalButtonPressed(self):
        self.fsm.request('normalChat')

    
    def __qtButtonPressed(self):
        self.fsm.request('quickTalker')


