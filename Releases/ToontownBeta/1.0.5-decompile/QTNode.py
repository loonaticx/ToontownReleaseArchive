# Source Generated with Decompyle++
# File: QTNode.pyo (Python 2.0)

from GuiGlobals import *
from PandaObject import *
from ToontownGlobals import *
import NamedNode
import NodePath
import Button
import types

class QTNode(PandaObject):
    font = getToonFont()
    
    def __init__(self, name):
        self.name = name
        self.phraseList = []
        self.nodepath = hidden.attachNewNode('QTNode-' + name)
        self.buttons = []
        self.managed = 0
        self.clearSelectionHandler()
        self.buttonPressedEvent = 'QTNodeButtonPressed'

    
    def __del__(self):
        self.deleteMenu()
        del self.nodepath

    
    def __findPhrasePair(self, key):
        phrasePair = None
        if isinstance(key, types.StringType):
            for pp in self.phraseList:
                if pp[0] == key:
                    phrasePair = pp
                    break
                
            
        elif key < len(self.phraseList):
            phrasePair = self.phraseList[key]
        
        return phrasePair

    
    def __getitem__(self, key):
        phrasePair = self._QTNode__findPhrasePair(key)
        if phrasePair == None:
            return None
        else:
            return phrasePair[1]

    
    def __setitem__(self, key, value):
        phrasePair = self._QTNode__findPhrasePair(key)
        if phrasePair == None:
            phrasePair = self.phraseList.append([
                key,
                value])
        else:
            phrasePair[1] = value

    
    def getPhrase(self, index):
        pp = self._QTNode__findPhrasePair(index)
        if pp == None:
            return ''
        else:
            return pp[0]

    
    def __createDisplayText(self, phrasePair):
        text = phrasePair[0]
        if phrasePair[1] != QTSend:
            text = text + '...'
        
        return text

    
    def __createButtonName(self, index):
        return 'QTMenu' + self.name + 'Button' + str(index)

    
    def createMenu(self):
        self.deleteMenu()
        width = 0
        font = QTNode.font
        text = TextNode()
        text.setFont(font)
        for pp in self.phraseList:
            dText = self._QTNode__createDisplayText(pp)
            w = text.calcWidth(dText)
            width = max(width, w)
        
        width = width * 1.1
        z = 0
        dz = -0.055
        index = 0
        for pp in self.phraseList:
            dText = self._QTNode__createDisplayText(pp)
            btn = Button.Button(self._QTNode__createButtonName(index), label = dText, font = QTNode.font, scale = 0.055, width = width, align = TMALIGNLEFT, pos = (0.0, z), upStyle = (1.0, 1.0, 1.0, 0.6))
            btn.lLit.setBackgroundColor(1.0, 1.0, 0.0, 0.5)
            self.buttons.append(btn)
            z = z + dz
            index = index + 1
        

    
    def deleteMenu(self):
        self.unmanage()
        self.buttons = []

    
    def manage(self):
        if self.managed == 0:
            index = 0
            for b in self.buttons:
                b.setBehaviorEvent(self.buttonPressedEvent)
                b.setBehaviorEventParameter(index)
                b.manage(self.nodepath)
                b.startBehavior()
                index = index + 1
            
            self.managed = 1
            self.accept(self.buttonPressedEvent, self._QTNode__buttonPressed)
        

    
    def unmanage(self):
        if self.managed != 0:
            self.ignore(self.buttonPressedEvent)
            for b in self.buttons:
                b.stopBehavior()
                b.unmanage()
            
            self.managed = 0
        

    
    def setSelectionHandler(self, handler):
        self.selectionHandler = handler

    
    def clearSelectionHandler(self):
        self.setSelectionHandler(None)

    
    def __owns(self, item):
        for x in self.buttons:
            if item == x.button:
                return 1
            
        
        return None

    
    def __buttonPressed(self, item, index):
        if self._QTNode__owns(item):
            if self.selectionHandler:
                self.selectionHandler(index)
            
        


QTSend = QTNode('send')
