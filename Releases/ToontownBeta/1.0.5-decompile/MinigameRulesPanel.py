# Source Generated with Decompyle++
# File: MinigameRulesPanel.pyo (Python 2.0)

from PandaModules import *
import Task
import StateData
from ToontownGlobals import *
from DirectGui import *
import ToontownTimer

class MinigameRulesPanel(StateData.StateData):
    TIMEOUT = 16
    
    def __init__(self, panelName, gameTitle, instructions, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.gameTitle = gameTitle
        self.instructions = instructions
        return None

    
    def load(self):
        self.minigameGui = loader.loadModel('phase_4/models/gui/minigame_rules_gui')
        self.buttonGui = loader.loadModelOnce('phase_4/models/gui/inventory_gui')
        self.frame = DirectFrame(image = self.minigameGui.find('**/minigame-rules-panel'), relief = None, pos = (0.1375, 0, -0.6667))
        self.gameTitleText = DirectLabel(parent = self.frame, text = self.gameTitle, scale = 0.11, text_font = getSignFont(), text_fg = (1.0, 0.33, 0.33, 1.0), pos = (-0.046, 0.2, 0.092), relief = None)
        self.instructionsText = DirectLabel(parent = self.frame, text = self.instructions, scale = 0.07, text_align = TMALIGNLEFT, text_wordwrap = 16.0, pos = (-1.05, 0.05, 0), relief = None)
        self.playButton = DirectButton(parent = self.frame, relief = None, image = (self.buttonGui.find('**/InventoryButtonUp'), self.buttonGui.find('**/InventoryButtonDown'), self.buttonGui.find('**/InventoryButtonRollover')), image_color = Vec4(0, 0.9, 0.1, 1), text = 'PLAY', text_fg = (1, 1, 1, 1), text_pos = (0, -0.02, 0), text_scale = 0.06, pos = (1.0025, 0, -0.203), scale = 1.05, command = self.playCallback)
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.reparentTo(self.frame)
        self.timer.setScale(0.4)
        self.timer.setPos(0.997, 0, 0.064)
        self.frame.hide()
        return None

    
    def unload(self):
        self.minigameGui.removeNode()
        del self.minigameGui
        self.buttonGui.removeNode()
        del self.buttonGui
        self.frame.destroy()
        del self.frame
        del self.gameTitleText
        del self.instructionsText
        del self.playButton
        del self.timer
        return None

    
    def enter(self):
        self.frame.show()
        self.timer.countdown(self.TIMEOUT, self.playCallback)
        self.accept('enter', self.playCallback)
        return None

    
    def exit(self):
        self.frame.hide()
        self.timer.stop()
        self.ignore('enter')
        return None

    
    def playCallback(self):
        messenger.send(self.doneEvent)
        return None


