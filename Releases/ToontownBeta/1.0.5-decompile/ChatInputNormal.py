# Source Generated with Decompyle++
# File: ChatInputNormal.pyo (Python 2.0)

import ChatInputScheme
import PandaObject
import ToontownGlobals
import GuiGlobals
import sys
from DirectGui import *

class ChatInputNormal(ChatInputScheme.ChatInputScheme, PandaObject.PandaObject):
    ExecNamespace = None
    
    def __init__(self, chatMgr, whisperId = -1):
        ChatInputScheme.ChatInputScheme.__init__(self, chatMgr)
        self.chatInputGui = loader.loadModel('phase_4/models/gui/chat_input_gui')
        self.chatFrame = DirectFrame(image = self.chatInputGui.find('**/Chat_Bx_FNL'), relief = None, pos = (-1.083, 0, 0.804), sortOrder = 10)
        self.chatFrame.hide()
        self.chatButton = DirectButton(parent = self.chatFrame, image = (self.chatInputGui.find('**/ChtBx_ChtBtn_UP'), self.chatInputGui.find('**/ChtBx_ChtBtn_DN'), self.chatInputGui.find('**/ChtBx_ChtBtn_RLVR')), pos = (0.182, 0, -0.088), relief = None, text = ('', 'Say It', 'Say It'), text_scale = 0.06, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -0.09), text_font = ToontownGlobals.getInterfaceFont(), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self._ChatInputNormal__chatButtonPressed)
        self.cancelButton = DirectButton(parent = self.chatFrame, image = (self.chatInputGui.find('**/CloseBtn_UP'), self.chatInputGui.find('**/CloseBtn_DN'), self.chatInputGui.find('**/CloseBtn_Rllvr')), pos = (-0.151, 0, -0.088), relief = None, text = ('', 'Cancel', 'Cancel'), text_scale = 0.06, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -0.09), text_font = ToontownGlobals.getInterfaceFont(), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self._ChatInputNormal__cancelButtonPressed)
        self.chatEntry = DirectEntry(parent = self.chatFrame, relief = None, scale = 0.05, pos = (-0.2, 0, 0.11), text_font = ToontownGlobals.getToonFont(), width = 8.6, numLines = 3, cursorKeys = 0, backgroundFocus = 0, command = self.sendChat)
        self.chatEntry.bind(OVERFLOW, self.chatOverflow)
        self.chatEntry.bind(TYPE, self.typeCallback)
        return None

    
    def typeCallback(self, extraArgs):
        messenger.send('enterNormalChat')

    
    def delete(self):
        loader.unloadModel('phase_4/models/gui/chat_input_gui')
        self.chatInputGui.removeNode()
        del self.chatInputGui
        self.chatFrame.destroy()
        del self.chatFrame
        del self.chatButton
        del self.cancelButton
        del self.chatEntry
        ChatInputScheme.ChatInputScheme.delete(self)
        return None

    
    def show(self):
        self.chatEntry['focus'] = 1
        self.chatFrame.show()
        return None

    
    def hide(self):
        self.chatEntry.set('')
        self.chatEntry['focus'] = 0
        self.chatFrame.hide()
        return None

    
    def sendChat(self, text):
        if text:
            if self.chatMgr.execChat:
                if text[0] == '>':
                    text = self._ChatInputNormal__execMessage(text[1:])
                
            
            self.chatMgr.sendChatString(text)
        
        self.hide()
        self.chatMgr.fsm.request('mainMenu')
        return None

    
    def chatOverflow(self, overflowText):
        self.sendChat(self.chatEntry.get())
        return None

    
    def __execMessage(self, message):
        if not (ChatInputNormal.ExecNamespace):
            ChatInputNormal.ExecNamespace = { }
            exec 'from ShowBaseGlobal import *' in globals(), ChatInputNormal.ExecNamespace
            exec 'from ToonBaseGlobal import *' in globals(), ChatInputNormal.ExecNamespace
        
        
        try:
            return str(eval(message, globals(), ChatInputNormal.ExecNamespace))
        except SyntaxError:
            
            try:
                exec message in globals(), ChatInputNormal.ExecNamespace
                return 'ok'
            except:
                exception = sys.exc_info()[0]
                extraInfo = sys.exc_info()[1]
                if extraInfo:
                    return str(extraInfo)
                else:
                    return str(exception)

        except:
            exception = sys.exc_info()[0]
            extraInfo = sys.exc_info()[1]
            if extraInfo:
                return str(extraInfo)
            else:
                return str(exception)


    
    def __cancelButtonPressed(self):
        self.chatEntry.set('')
        self.chatMgr.fsm.request('mainMenu')
        return None

    
    def __chatButtonPressed(self):
        self.sendChat(self.chatEntry.get())
        return None


