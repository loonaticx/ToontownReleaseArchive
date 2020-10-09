# Source Generated with Decompyle++
# File: PlayByPlayPanel.pyo (Python 2.0)

from DirectObject import *
from ShowBaseGlobal import *
from GuiGlobals import *
from ToontownBattleGlobals import *
from ToontownGlobals import *
from SuitBattleGlobals import *
import DirectNotifyGlobal
import string
import OnscreenText
import BattleBase

class PlayByPlayText(OnscreenText.OnscreenText):
    notify = DirectNotifyGlobal.directNotify.newCategory('PlayByPlayText')
    
    def __init__(self):
        OnscreenText.OnscreenText.__init__(self, mayChange = 1, pos = (0.0, 0.75), scale = 0.1, font = getSignFont())
        return None


