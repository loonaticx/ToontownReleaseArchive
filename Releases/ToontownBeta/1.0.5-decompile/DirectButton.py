# Source Generated with Decompyle++
# File: DirectButton.pyo (Python 2.0)

from DirectFrame import *
BUTTON_READY_STATE = PGButton.SReady
BUTTON_DEPRESSED_STATE = PGButton.SDepressed
BUTTON_ROLLOVER_STATE = PGButton.SRollover
BUTTON_INACTIVE_STATE = PGButton.SInactive

class DirectButton(DirectFrame):
    
    def __init__(self, parent = guiTop, **kw):
        optiondefs = (('pgFunc', PGButton, None), ('numStates', 4, None), ('invertedFrames', (1,), None), ('command', None, None), ('extraArgs', [], None), ('commandButtons', (LMB,), self.setCommandButtons), ('rolloverSound', getDefaultRolloverSound(), self.setRolloverSound), ('clickSound', getDefaultClickSound(), self.setClickSound), ('pressEffect', 1, INITOPT))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        if self['pressEffect']:
            np = self.stateNodePath[1].attachNewNode('pressEffect')
            np.setScale(0.98)
            self.stateNodePath[1] = np
        
        self.initialiseoptions(DirectButton)

    
    def setCommandButtons(self):
        if LMB in self['commandButtons']:
            self.guiItem.addClickButton(MouseButton.one())
            self.bind(B1CLICK, self.commandFunc)
        else:
            self.unbind(B1CLICK)
            self.guiItem.removeClickButton(MouseButton.one())
        if MMB in self['commandButtons']:
            self.guiItem.addClickButton(MouseButton.two())
            self.bind(B2CLICK, self.commandFunc)
        else:
            self.unbind(B2CLICK)
            self.guiItem.removeClickButton(MouseButton.two())
        if RMB in self['commandButtons']:
            self.guiItem.addClickButton(MouseButton.three())
            self.bind(B3CLICK, self.commandFunc)
        else:
            self.unbind(B3CLICK)
            self.guiItem.removeClickButton(MouseButton.three())

    
    def commandFunc(self, event):
        if self['command']:
            apply(self['command'], self['extraArgs'])
        

    
    def setClickSound(self):
        if base.wantSfx:
            clickSound = self['clickSound']
            self.guiItem.clearSound(B1PRESS + self.guiId)
            self.guiItem.clearSound(B2PRESS + self.guiId)
            self.guiItem.clearSound(B3PRESS + self.guiId)
            if clickSound:
                if LMB in self['commandButtons']:
                    self.guiItem.setSound(B1PRESS + self.guiId, clickSound)
                
                if MMB in self['commandButtons']:
                    self.guiItem.setSound(B2PRESS + self.guiId, clickSound)
                
                if RMB in self['commandButtons']:
                    self.guiItem.setSound(B3PRESS + self.guiId, clickSound)
                
            
        

    
    def setRolloverSound(self):
        if base.wantSfx:
            rolloverSound = self['rolloverSound']
            if rolloverSound:
                self.guiItem.setSound(ENTER + self.guiId, rolloverSound)
            else:
                self.guiItem.clearSound(ENTER + self.guiId)
        


