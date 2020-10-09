# Source Generated with Decompyle++
# File: ToonBase.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
from DirectObject import *
from PythonUtil import *
import DirectNotifyGlobal
import DialogBox
import DownloadWatcher
import ToontownLoader
import GuiGlobals

class ToonBase(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonBase')
    
    def __init__(self):
        base.disableMouse()
        camera.setPosHpr(0, 0, 0, 0, 0, 0)
        base.cam.node().setFov(DefaultCameraFov)
        base.cam.node().setFar(DefaultCameraFar)
        ClockObject.getGlobalClock().setMaxDt(0.14)
        if base.config.GetBool('want-particles', 1) == 1:
            self.notify.debug('Enabling particles')
            base.enableParticles()
        
        self.base = base
        self.accept(ScreenshotHotkey, base.screenshot)
        self.loader = ToontownLoader.ToontownLoader(base)
        self.accept('PandaPaused', base.DisableAudio)
        self.accept('PandaRestarted', base.EnableAudio)

    
    def initNametagGlobals(self):
        arrow = loader.loadModelNode('phase_3/models/props/arrow')
        card = loader.loadModelNode('phase_3/models/props/panel')
        speech3d = ChatBalloon(loader.loadModelNode('phase_3/models/props/chatbox'))
        thought3d = ChatBalloon(loader.loadModelNode('phase_3/models/props/chatbox_thought_cutout'))
        speech2d = ChatBalloon(loader.loadModelNode('phase_3/models/props/chatbox_noarrow'))
        NametagGlobals.setCamera(base.camNode)
        NametagGlobals.setArrowModel(arrow)
        NametagGlobals.setNametagCard(card, VBase4(-0.5, 0.5, -0.5, 0.5))
        NametagGlobals.setMouseWatcher(base.mouseWatcherNode)
        NametagGlobals.setSpeechBalloon3d(speech3d)
        NametagGlobals.setThoughtBalloon3d(thought3d)
        NametagGlobals.setSpeechBalloon2d(speech2d)
        NametagGlobals.setThoughtBalloon2d(thought3d)
        rolloverSound = GuiGlobals.getDefaultRolloverSound()
        if rolloverSound:
            NametagGlobals.setRolloverSound(rolloverSound)
        
        clickSound = GuiGlobals.getDefaultClickSound()
        if clickSound:
            NametagGlobals.setClickSound(clickSound)
        
        NametagGlobals.setToonNode(base.camNode)
        self.marginManager = MarginManager()
        self.margins = base.aspect2d.attachNewNode(self.marginManager)
        mm = self.marginManager
        mm.addGridCell(0, 1, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop)
        mm.addGridCell(0, 2, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop)
        mm.addGridCell(0, 3, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop)
        mm.addGridCell(0.5, 0, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop)
        mm.addGridCell(1.5, 0, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop)
        mm.addGridCell(2.5, 0, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop)
        mm.addGridCell(3.5, 0, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop)
        mm.addGridCell(4.5, 0, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop)
        mm.addGridCell(5, 2, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop)
        mm.addGridCell(5, 1, base.a2dLeft, base.a2dRight, base.a2dBottom, base.a2dTop)

    
    def cleanupDownloadWatcher(self):
        self.downloadWatcher.cleanup()
        self.downloadWatcher = None

    
    def startShow(self, tcr, launcherServerIP = None):
        self.tcr = tcr
        base.win.update()
        if launcher:
            self.downloadWatcher = DownloadWatcher.DownloadWatcher()
            self.acceptOnce('launcherAllPhasesComplete', self.cleanupDownloadWatcher)
        
        serverIP = base.config.GetString('server-ip', '')
        if serverIP:
            self.notify.info('Using server-ip to set serverIP to: ' + `serverIP`)
        elif launcherServerIP:
            serverIP = launcherServerIP
            self.notify.info('Using launcher to set serverIP to: ' + `serverIP`)
        else:
            serverType = base.config.GetString('server-type', '')
            if serverType:
                if serverType == 'prod':
                    serverIP = prodServerIP
                elif serverType == 'dev':
                    serverIP = devServerIP
                elif serverType == 'debug':
                    serverIP = debugServerIP
                else:
                    self.notify.error('Unknown server type: ' + serverType)
                self.notify.info('Using server-type to set serverIP to: ' + `serverIP`)
            else:
                serverIP = prodServerIP
                self.notify.info('Defaulting serverIP to: ' + `serverIP`)
        serverPort = base.config.GetInt('server-port', 80)
        tcr.loginFSM.request('login', [
            serverIP,
            serverPort])

    
    def exitShow(self):
        self.notify.info('Exiting Toontown')
        if launcher:
            launcher.setPandaErrorCode(0)
        
        sys.exit()
        return None


