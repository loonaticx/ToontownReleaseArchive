# Source Generated with Decompyle++
# File: ChatInputQuickTalker.pyo (Python 2.0)

import ChatInputScheme
import PandaObject
import ToontownGlobals
import GuiGlobals
import QTGraph
import QTNode
import FSM
import State
from DirectGui import *

class ChatInputQuickTalker(ChatInputScheme.ChatInputScheme, PandaObject.PandaObject):
    
    def __init__(self, chatMgr):
        ChatInputScheme.ChatInputScheme.__init__(self, chatMgr)
        self.soundQTMenu = base.loadSfx('phase_4/audio/sfx/GUI_quicktalker.mp3')
        self.sentenceList = []
        self.chatInputGui = loader.loadModel('phase_4/models/gui/chat_input_gui')
        self.frame = DirectFrame(image = self.chatInputGui.find('**/quick_talker'), relief = None, pos = (-0.435, 0, 0.905), sortOrder = 10)
        self.frame.hide()
        self.backButton = DirectButton(parent = self.frame, image = (self.chatInputGui.find('**/ChtBx_BackBtn_UP'), self.chatInputGui.find('**/ChtBx_BackBtn_DN'), self.chatInputGui.find('**/ChtBx_BackBtn_Rllvr')), relief = None, pos = (0.7073, 0, 0.0125), text = ('', 'Back', 'Back'), text_scale = 0.06, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -0.1), text_font = ToontownGlobals.getInterfaceFont(), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self._ChatInputQuickTalker__backButtonPressed)
        self.chatButton = DirectButton(parent = self.frame, image = (self.chatInputGui.find('**/ChtBx_ChtBtn_UP'), self.chatInputGui.find('**/ChtBx_ChtBtn_DN'), self.chatInputGui.find('**/ChtBx_ChtBtn_RLVR')), relief = None, pos = (0.8, 0, 0.0125), text = ('', 'Say It', 'Say It'), text_scale = 0.06, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -0.1), text_font = ToontownGlobals.getInterfaceFont(), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self._ChatInputQuickTalker__chatButtonPressed)
        self.cancelButton = DirectButton(parent = self.frame, image = (self.chatInputGui.find('**/CloseBtn_UP'), self.chatInputGui.find('**/CloseBtn_DN'), self.chatInputGui.find('**/CloseBtn_Rllvr')), relief = None, pos = (-0.783, 0, 0.0125), text = ('', 'Cancel', 'Cancel'), text_scale = 0.06, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -0.1), text_font = ToontownGlobals.getInterfaceFont(), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self._ChatInputQuickTalker__cancelButtonPressed)
        self.displayText = DirectLabel(parent = self.frame, relief = None, text = '', text_font = ToontownGlobals.getToonFont(), text_fg = Vec4(0, 0, 0, 1), text_pos = (-0.55, -0.008), text_scale = 0.06)
        self.chatHead = self.frame.attachNewNode('chatHead')
        self.fsm = FSM.FSM('QuickTalker', [
            State.State('Hidden', self._ChatInputQuickTalker__enterHidden, self._ChatInputQuickTalker__exitHidden, [
                'Constructing']),
            State.State('Constructing', self._ChatInputQuickTalker__enterConstructing, self._ChatInputQuickTalker__exitConstructing, [
                'ConstructingTransition',
                'SayIt',
                'Hidden']),
            State.State('ConstructingTransition', self._ChatInputQuickTalker__enterConstructingTransition, self._ChatInputQuickTalker__exitConstructingTransition, [
                'Constructing',
                'Hidden']),
            State.State('SayIt', self._ChatInputQuickTalker__enterSayIt, self._ChatInputQuickTalker__exitSayIt, [
                'Hidden'])], 'Hidden', 'Hidden')
        self.fsm.enterInitialState()
        return None

    
    def delete(self):
        base.unloadSfx(self.soundQTMenu)
        del self.soundQTMenu
        loader.unloadModel('phase_4/models/gui/chat_input_gui')
        self.frame.destroy()
        del self.frame
        del self.backButton
        del self.chatButton
        del self.cancelButton
        del self.displayText
        del self.fsm
        del self.sentenceList
        ChatInputScheme.ChatInputScheme.delete(self)

    
    def show(self):
        self.curQTnode = QTGraph.QTGraph['start']
        self.fsm.request('Constructing')

    
    def hide(self):
        self.fsm.request('Hidden')

    
    def getSentenceCleartext(self):
        sentence = ''
        for entry in self.sentenceList:
            sentence = sentence + entry[0].getPhrase(entry[1])
        
        return sentence

    
    def getSentenceEncoded(self):
        sentence = []
        for entry in self.sentenceList:
            sentence.append(entry[1])
        
        return sentence

    
    def __cancelButtonPressed(self):
        self.chatMgr.fsm.request('mainMenu')

    
    def __backButtonPressed(self):
        if len(self.sentenceList) == 0:
            self.chatMgr.fsm.request('mainMenu')
        else:
            prevState = self.sentenceList.pop(len(self.sentenceList) - 1)
            self.newQTnode = prevState[0]
            self.fsm.request('ConstructingTransition')

    
    def __chatButtonPressed(self):
        self.fsm.request('SayIt')

    
    def __enterHidden(self):
        self.sentenceList = []
        self.frame.hide()

    
    def __exitHidden(self):
        pass

    
    def __enterConstructing(self):
        self.frame.show()
        self.displayText['text'] = self.getSentenceCleartext()
        textNode = self.displayText.component('text0').node()
        width = textNode.getWidth() * 0.06
        self.chatHead.setPos(-0.7 + width, 0.0, -0.06)
        self.curQTnode.nodepath.reparentTo(self.chatHead)
        self.curQTnode.nodepath.setPos(0, 0, 0)
        self.curQTnode.setSelectionHandler(self._ChatInputQuickTalker__selectionMade)
        self.curQTnode.manage()
        base.playSfx(self.soundQTMenu)

    
    def __selectionMade(self, index):
        self.newQTnode = self.curQTnode[index]
        self.sentenceList.append([
            self.curQTnode,
            index])
        if self.newQTnode == QTNode.QTSend:
            self.fsm.request('SayIt')
        else:
            self.fsm.request('ConstructingTransition')

    
    def __exitConstructing(self):
        self.curQTnode.clearSelectionHandler()
        self.curQTnode.unmanage()
        self.curQTnode.nodepath.reparentTo(hidden)
        del self.curQTnode

    
    def __enterConstructingTransition(self):
        self.curQTnode = self.newQTnode
        self.fsm.request('Constructing')

    
    def __exitConstructingTransition(self):
        pass

    
    def __enterSayIt(self):
        self.chatMgr.sendQTChatMessage(self.getSentenceEncoded())
        self.chatMgr.fsm.request('mainMenu')

    
    def __exitSayIt(self):
        pass


