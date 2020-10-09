# Source Generated with Decompyle++
# File: MinigameAvatarScorePanel.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
import OnscreenPanel
import LaffMeter

class MinigameAvatarScorePanel(OnscreenPanel.OnscreenPanel):
    
    def __init__(self, avId, avName):
        self.avId = avId
        if toonbase.tcr.doId2do.has_key(self.avId):
            self.avatar = toonbase.tcr.doId2do[self.avId]
        else:
            self.avatar = None
        panelName = 'MinigameAvatarScorePanel_' + str(avId)
        OnscreenPanel.OnscreenPanel.__init__(self, panelName)
        self.makePanel(rect = (0.0, 0.4, 0.0, 0.24), bg = (1, 0.89, 0.77, 0.85))
        self.nameText = self.makeText(avName, scale = 0.066, pos = (0.0, 0.06))
        self.scoreText = self.makeText('0', scale = 0.1, pos = (0.1, -0.07), mayChange = 1)
        if self.avatar:
            self.laffMeter = LaffMeter.LaffMeter(self.avatar.style, self.avatar.hp, self.avatar.maxHp)
            self.laffMeter.reparentTo(self)
            self.laffMeter.setPos(-0.085, 0, -0.035)
            self.laffMeter.setScale(0.05)
            self.laffMeter.start()
        else:
            self.laffMeter = None
        self.show()

    
    def cleanup(self):
        if self.laffMeter:
            self.laffMeter.destroy()
            del self.laffMeter
        
        del self.nameText
        del self.scoreText
        OnscreenPanel.OnscreenPanel.cleanup(self)

    
    def setScore(self, score):
        self.scoreText.setText(str(score))


