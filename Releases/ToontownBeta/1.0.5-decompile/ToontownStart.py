# Source Generated with Decompyle++
# File: ToontownStart.pyo (Python 2.0)

import time
import os
import sys
import __builtin__

try:
    launcher
except:
    launcher = None
    __builtin__.launcher = launcher

pollingDelay = 0.5
if launcher:
    print 'ToontownStart: Polling for game2 to finish...'
    while not launcher.getGame2Done():
        time.sleep(pollingDelay)
    print 'ToontownStart: Game2 is finished.'

print 'ToontownStart: Starting the game.'
from PandaModules import *
tempLoader = PandaLoader()
backgroundNode = tempLoader.loadSync(Filename('phase_3/models/gui/loading-background'))
import ToontownGlobals
from ShowBaseGlobal import *
import GuiGlobals
GuiGlobals.setDefaultFont(ToontownGlobals.getInterfaceFont())
GuiGlobals.setDefaultPanel('phase_3/models/props/panel')
import DirectGuiGlobals
DirectGuiGlobals.setDefaultFont(ToontownGlobals.getInterfaceFont())
backgroundNodePath = base.render2d.attachNewNode(backgroundNode)
backgroundNodePath.setPos(0.0, 0.0, 0.0)
backgroundNodePath.setScale(1.01)
backgroundNodePath.find('**/fg').setBin('fixed', 20)
backgroundNodePath.find('**/bg').setBin('fixed', 10)
base.win.update()
if launcher:
    launcher.setPandaWindowOpen()

if base.wantMusic:
    music = base.musicManager.getSound('phase_3/audio/bgm/tt_theme.mid')
    if music:
        music.setLoop(1)
        music.setVolume(0.9)
        music.play()
    
else:
    music = None
import ToontownLoader
tempLoaderOther = ToontownLoader.ToontownLoader(base)
base.loader = tempLoaderOther
__builtin__.loader = tempLoaderOther
serverVersion = base.config.GetString('server-version', 'no_version_set')
import OnscreenText
version = OnscreenText.OnscreenText(serverVersion, pos = (-1.2, -0.975), scale = 0.06, fg = Vec4(0, 0, 1, 0.6))
loader.beginBulkLoad('init', 80, pos = Vec3(0.48, 0.0, -0.92), namePos = Vec3(0.025, 0.0, -0.03))
from ToonBaseGlobal import *
from MessengerGlobal import *
import ToontownClientRepository
toontest = base.config.GetBool('want-aitest', 0)
if launcher and not launcher.isDummy():
    if toontest:
        dcfile = os.path.join(launcher.getInstallDir(), 'phase_3/etc/toontest.dc')
    else:
        dcfile = os.path.join(launcher.getInstallDir(), 'phase_3/etc/toon.dc')
elif toontest:
    dcfile = 'phase_3/etc/toontest.dc'
else:
    dcfile = 'phase_3/etc/toon.dc'
if not os.path.exists(dcfile):
    if toontest:
        dcfile = os.path.expandvars('$TOONTOWN/src/configfiles/toontest.dc')
    else:
        dcfile = os.path.expandvars('$TOONTOWN/src/configfiles/toon.dc')
    if not os.path.exists(dcfile):
        print 'Could not find toon.dc file'
        sys.exit()
    

tcr = ToontownClientRepository.ToontownClientRepository(dcfile, serverVersion, launcher)
tcr.music = music
del music
toonbase.initNametagGlobals()
toonbase.tcr = tcr
loader.endBulkLoad('init')
if launcher:
    toonbase.startShow(tcr, launcher.getGameServer())
else:
    toonbase.startShow(tcr)
backgroundNodePath.reparentTo(hidden)
backgroundNodePath.removeNode()
del backgroundNodePath
del backgroundNode
del tempLoader
del tempLoaderOther
version.cleanup()
del version
base.loader = toonbase.loader
__builtin__.loader = toonbase.loader
if not launcher:
    run()

