# Source Generated with Decompyle++
# File: TownBattleWaitPanel.pyo (Python 2.0)

from ShowBaseGlobal import *
import StateData
from DirectGui import *

class TownBattleWaitPanel(StateData.StateData):
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        return None

    
    def load(self):
        self.gui = loader.loadModelOnce('phase_5/models/gui/battle_gui')
        self.frame = DirectFrame(relief = None, image = self.gui.find('**/Waiting4Others'), text = 'Waiting for\nother players...', text_pos = (-0.3, 0, 0), text_scale = 0.1, text_align = TMALIGNLEFT, pos = (0, 0, 0), scale = 0.75)
        self.frame.hide()
        self.backButton = DirectButton(parent = self.frame, relief = None, image = (self.gui.find('**/PckMn_BackBtn'), self.gui.find('**/PckMn_BackBtn_Dn'), self.gui.find('**/PckMn_BackBtn_Rlvr')), pos = (-0.647, 0, -0.011), scale = 1.05, text = 'BACK', text_scale = 0.05, text_pos = (0.01, -0.012), text_fg = Vec4(0, 0, 0.8, 1), command = self._TownBattleWaitPanel__handleBack)
        return None

    
    def unload(self):
        self.gui.removeNode()
        del self.gui
        self.frame.destroy()
        del self.frame
        del self.backButton
        return None

    
    def enter(self):
        self.frame.show()
        return None

    
    def exit(self):
        self.frame.hide()
        return None

    
    def __handleBack(self):
        doneStatus = {
            'mode': 'Back' }
        messenger.send(self.doneEvent, [
            doneStatus])
        return None


