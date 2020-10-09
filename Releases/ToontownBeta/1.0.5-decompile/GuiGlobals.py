# Source Generated with Decompyle++
# File: GuiGlobals.pyo (Python 2.0)

from ShowBaseGlobal import *
import GuiManager
guiMgr = GuiManager.GuiManager.getPtr(base.win, base.mak.node(), base.render2d.node())
font = None
sndClick = None
sndRollover = None
panel = None
drawOrder = 100

def getDefaultFont():
    global font
    if font == None:
        font = loader.loadFont('models/fonts/Comic')
    
    return font


def setDefaultFont(newFont):
    global font
    font = newFont


def getDefaultPanel():
    return panel


def setDefaultPanel(newPanel):
    global panel
    panel = newPanel


def getDefaultDrawOrder():
    return drawOrder


def setDefaultDrawOrder(newDrawOrder):
    global drawOrder
    drawOrder = newDrawOrder


def getDefaultRolloverSound():
    global sndRollover
    if not (base.wantSfx):
        return None
    
    if sndRollover == None:
        sndRollover = base.loadSfx('phase_3/audio/sfx/GUI_rollover.mp3')
    
    return sndRollover


def getDefaultClickSound():
    global sndClick
    if not (base.wantSfx):
        return None
    
    if sndClick == None:
        sndClick = base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.mp3')
    
    return sndClick


def getNewRolloverFunctor(sound = None):
    val = None
    if sound:
        roll = sound
    else:
        roll = getDefaultRolloverSound()
    if roll:
        val = AudioGuiFunctor(roll)
    else:
        val = AudioGuiFunctor()
    return val


def getNewClickFunctor(sound = None):
    val = None
    if sound:
        click = sound
    else:
        click = getDefaultClickSound()
    if click:
        val = AudioGuiFunctor(click)
    else:
        val = AudioGuiFunctor()
    return val

