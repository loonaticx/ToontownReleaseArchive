# Source Generated with Decompyle++
# File: DirectEntry.pyo (Python 2.0)

from DirectFrame import *
ENTRY_FOCUS_STATE = PGEntry.SFocus
ENTRY_NO_FOCUS_STATE = PGEntry.SNoFocus
ENTRY_INACTIVE_STATE = PGEntry.SInactive

class DirectEntry(DirectFrame):
    
    def __init__(self, parent = guiTop, **kw):
        optiondefs = (('pgFunc', PGEntry, None), ('numStates', 3, None), ('width', 10, self.setup), ('numLines', 5, self.setup), ('focus', 0, self.setFocus), ('cursorKeys', 0, self.setCursorKeysActive), ('backgroundFocus', 0, self.setBackgroundFocus), ('initialText', '', INITOPT), ('command', None, None), ('extraArgs', [], None), ('rolloverSound', getDefaultRolloverSound(), self.setRolloverSound))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.onscreenText = self.createcomponent('text', (), None, OnscreenText.OnscreenText, (), parent = hidden, text = '', align = TMALIGNLEFT, font = getDefaultFont(), scale = 1, mayChange = 1)
        self.onscreenText.freeze()
        self.onscreenText.removeNode()
        self.bind(ACCEPT, self.commandFunc)
        self.initialiseoptions(DirectEntry)
        for i in range(self['numStates']):
            self.guiItem.setTextDef(i, self.onscreenText.textNode)
        
        if self['initialText']:
            self.set(self['initialText'])
        

    
    def setup(self):
        self.node().setup(self['width'], self['numLines'])

    
    def setFocus(self):
        PGEntry.setFocus(self.guiItem, self['focus'])

    
    def setCursorKeysActive(self):
        PGEntry.setCursorKeysActive(self.guiItem, self['cursorKeys'])

    
    def setBackgroundFocus(self):
        PGEntry.setBackgroundFocus(self.guiItem, self['backgroundFocus'])

    
    def setRolloverSound(self):
        if base.wantSfx:
            rolloverSound = self['rolloverSound']
            if rolloverSound:
                self.guiItem.setSound(ENTER + self.guiId, rolloverSound)
            else:
                self.guiItem.clearSound(ENTER + self.guiId)
        

    
    def commandFunc(self, event):
        if self['command']:
            apply(self['command'], [
                self.get()] + self['extraArgs'])
        

    
    def set(self, text):
        self.guiItem.setText(text)

    
    def get(self):
        return self.guiItem.getText()

    
    def setCursorPosition(self, pos):
        if pos < 0:
            self.guiItem.setCursorPosition(len(self.get()) + pos)
        else:
            self.guiItem.setCursorPosition(pos)


