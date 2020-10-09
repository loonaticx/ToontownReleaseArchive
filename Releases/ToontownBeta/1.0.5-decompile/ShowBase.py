# Source Generated with Decompyle++
# File: ShowBase.pyo (Python 2.0)

from PandaModules import *
from DirectNotifyGlobal import *
from MessengerGlobal import *
from TaskManagerGlobal import *
from EventManagerGlobal import *
from PythonUtil import *
from ParticleManagerGlobal import *
from PhysicsManagerGlobal import *
import Task
import EventManager
import math
import sys
import Transitions
import Loader
import time
import FSM
import State
globalClock = ClockObject.getGlobalClock()

class ShowBase:
    notify = directNotify.newCategory('ShowBase')
    
    def __init__(self):
        self.config = ConfigConfigureGetConfigConfigShowbase
        self.wantTk = self.config.GetBool('want-tk', 0)
        self.wantAnySound = self.config.GetBool('want-sound', 1)
        self.wantSfx = self.config.GetBool('audio-sfx-active', 1)
        self.wantMusic = self.config.GetBool('audio-music-active', 1)
        self.wantFog = self.config.GetBool('want-fog', 1)
        if not self.wantSfx:
            pass
        if not (self.wantMusic):
            self.wantAnySound = None
        
        if not (self.wantAnySound):
            self.wantSfx = None
            self.wantMusic = None
        
        self.wantDIRECT = self.config.GetBool('want-directtools', 0)
        self.wantStats = self.config.GetBool('want-stats', 0)
        taskMgr.taskTimerVerbose = self.config.GetBool('task-timer-verbose', 0)
        taskMgr.pStatsTasks = self.config.GetBool('pstats-tasks', 0)
        taskMgr.resumeFunc = PStatClient.resumeAfterPause
        fsmRedefine = self.config.GetBool('fsm-redefine', 0)
        State.FsmRedefine = fsmRedefine
        self.renderTop = NodePath(NamedNode('renderTop'))
        self.render = self.renderTop.attachNewNode('render')
        self.render.setColorOff()
        self.hidden = NodePath(NamedNode('hidden'))
        self.dataRoot = NodePath(NamedNode('dataRoot'), DataRelation.getClassType())
        self.dataRootNode = self.dataRoot.node()
        self.dataUnused = NodePath(NamedNode('dataUnused'), DataRelation.getClassType())
        self.pipe = makeGraphicsPipe()
        chanConfig = makeGraphicsWindow(self.pipe, self.render.arc())
        self.win = chanConfig.getWin()
        self.oldexitfunc = getattr(sys, 'exitfunc', None)
        sys.exitfunc = self.exitfunc
        self.cameraList = []
        for i in range(chanConfig.getNumGroups()):
            self.cameraList.append(self.render.attachNewNode(chanConfig.getGroupNode(i)))
        
        self.groupList = []
        for i in range(chanConfig.getNumDrs()):
            self.groupList.append(chanConfig.getGroupMembership(i))
        
        self.camera = self.cameraList[0]
        self.cTrav = 0
        self.camList = []
        for camera in self.cameraList:
            self.camList.append(camera.find('**/+Camera'))
        
        self.cam = self.camera.find('**/+Camera')
        self.camNode = self.cam.node()
        self.render2d = NodePath(setupPanda2d(self.win, 'render2d'))
        self.aspectRatio = 4.0 / 3.0
        self.aspect2d = self.render2d.attachNewNode('aspect2d')
        self.aspect2d.setScale(1.0 / self.aspectRatio, 1.0, 1.0)
        self.a2dTop = 1.0
        self.a2dBottom = -1.0
        self.a2dLeft = -(self.aspectRatio)
        self.a2dRight = self.aspectRatio
        self.renderAux = NodePath(NamedNode('renderAux'))
        self.camAux = self.renderAux.attachNewNode(Camera('camAux'))
        self.camAux.node().shareProjection(self.cam.node().getProjection())
        addRenderLayer(self.win, self.renderAux.node(), self.camAux.node())
        self.mak = self.dataRoot.attachNewNode(MouseAndKeyboard(self.win, 0, 'mak'))
        self.mouseWatcherNode = MouseWatcher('mouseWatcher')
        self.mouseWatcher = self.mak.attachNewNode(self.mouseWatcherNode)
        self.mouseValve = self.mouseWatcher.attachNewNode(DataValve('mouseValve'))
        self.mouseControl = DataValve.Control()
        self.mouseValve.node().setControl(0, self.mouseControl)
        self.onControl = DataValve.Control()
        self.trackball = self.dataUnused.attachNewNode(Trackball('trackball'))
        self.drive = self.dataUnused.attachNewNode(DriveInterface('drive'))
        self.mouse2cam = self.dataUnused.attachNewNode(Transform2SG('mouse2cam'))
        self.mouse2cam.node().setArc(self.camera.arc())
        self.useDrive()
        self.buttonThrower = self.mouseWatcher.attachNewNode(ButtonThrower())
        self.loader = Loader.Loader(self)
        self.eventMgr = eventMgr
        self.messenger = messenger
        self.taskMgr = taskMgr
        self.particleMgr = particleMgr
        self.particleMgr.setFrameStepping(1)
        self.particleMgrEnabled = 0
        self.physicsMgr = physicsMgr
        integrator = LinearEulerIntegrator()
        self.physicsMgr.attachLinearIntegrator(integrator)
        self.physicsMgrEnabled = 0
        self.physicsMgrAngular = 0
        self.createAudioManager()
        self.createStats()
        self.transitions = Transitions.Transitions(self.loader)
        import __builtin__
        __builtin__.base = self
        __builtin__.render2d = self.render2d
        __builtin__.aspect2d = self.aspect2d
        __builtin__.render = self.render
        __builtin__.hidden = self.hidden
        __builtin__.camera = self.camera
        __builtin__.loader = self.loader
        __builtin__.taskMgr = self.taskMgr
        __builtin__.eventMgr = self.eventMgr
        __builtin__.messenger = self.messenger
        __builtin__.config = self.config
        __builtin__.run = self.run
        if self.wantTk:
            import TkGlobal
        
        if self.wantDIRECT:
            import DirectSession
            direct.enable()
        else:
            __builtin__.direct = None
            self.direct = None
        self.restart()

    
    def exitfunc(self):
        self.win.closeWindow()
        del self.win
        del self.pipe
        if self.oldexitfunc:
            self.oldexitfunc()
        

    
    def addAngularIntegrator(self):
        if self.physicsMgrAngular == 0:
            self.physicsMgrAngular = 1
            integrator = AngularEulerIntegrator()
            self.physicsMgr.attachAngularIntegrator(integrator)
        

    
    def enableParticles(self):
        self.particleMgrEnabled = 1
        self.physicsMgrEnabled = 1
        self.taskMgr.removeTasksNamed('manager-update')
        self.taskMgr.spawnTaskNamed(Task.Task(self.updateManagers), 'manager-update')

    
    def disableParticles(self):
        self.particleMgrEnabled = 0
        self.physicsMgrEnabled = 0
        self.taskMgr.removeTasksNamed('manager-update')

    
    def toggleParticles(self):
        if self.particleMgrEnabled == 0:
            self.enableParticles()
        else:
            self.disableParticles()

    
    def isParticleMgrEnabled(self):
        return self.particleMgrEnabled

    
    def isPhysicsMgrEnabled(self):
        return self.physicsMgrEnabled

    
    def updateManagers(self, state):
        dt = min(globalClock.getDt(), 0.1)
        if self.particleMgrEnabled == 1:
            self.particleMgr.doParticles(dt)
        
        if self.physicsMgrEnabled == 1:
            self.physicsMgr.doPhysics(dt)
        
        return Task.cont

    
    def createStats(self):
        if self.wantStats:
            PStatClient.connect()
        

    
    def createAudioManager(self):
        if self.wantAnySound:
            if self.wantSfx:
                self.sfxManager = AudioManager.createAudioManager()
                if not self.sfxManager.isValid():
                    self.wantSfx = None
                
            
            if self.wantMusic:
                self.musicManager = AudioManager.createAudioManager()
                if not self.musicManager.isValid():
                    self.wantMusic = None
                
            
            if not self.wantSfx:
                pass
            if not (self.wantMusic):
                self.wantAnySound = None
            
        

    
    def loadSfx(self, name):
        if name and base.wantSfx:
            sound = self.sfxManager.getSound(name)
            if sound == None:
                self.notify.warning('Could not load sound file %s.' % name)
            
            return sound
        

    
    def loadMusic(self, name):
        if name and base.wantMusic:
            sound = self.musicManager.getSound(name)
            if sound == None:
                self.notify.warning('Could not load music file %s.' % name)
            
            return sound
        

    
    def unloadSfx(self, sfx):
        if sfx:
            del sfx
        

    
    def unloadMusic(self, music):
        if music:
            del music
        

    
    def playSfx(self, sfx, looping = 0, interupt = 1, volume = None, time = 0.0):
        if sfx and base.wantSfx:
            if volume != None:
                sfx.setVolume(volume)
            
            if interupt or sfx.status() != AudioSound.PLAYING:
                sfx.setTime(time)
                sfx.setLoop(looping)
                sfx.play()
            
        

    
    def playMusic(self, music, looping = 0, interupt = 1, volume = None, restart = None, time = 0.0):
        if music and base.wantMusic:
            if volume != None:
                music.setVolume(volume)
            
            if interupt or music.status() != AudioSound.PLAYING:
                music.setTime(time)
                music.setLoop(looping)
                music.play()
            
            if restart:
                restart[0].accept('restart-music', restart[1])
            
        

    
    def stopSfx(self, sfx):
        if sfx and base.wantSfx:
            sfx.stop()
        

    
    def stopMusic(self, music, restart = None):
        if music and base.wantMusic:
            music.stop()
            if restart:
                restart[0].ignore('restart-music')
            
        

    
    def dataloop(self, state):
        traverseDataGraph(self.dataRootNode)
        return Task.cont

    
    def igloop(self, state):
        if self.cTrav:
            self.cTrav.traverse(self.render)
        
        self.win.update()
        return Task.cont

    
    def restart(self):
        self.shutdown()
        self.taskMgr.spawnTaskNamed(Task.Task(self.igloop, 50), 'igloop')
        self.taskMgr.spawnTaskNamed(Task.Task(self.dataloop, -50), 'dataloop')
        self.eventMgr.restart()

    
    def shutdown(self):
        self.taskMgr.removeTasksNamed('igloop')
        self.taskMgr.removeTasksNamed('dataloop')
        self.eventMgr.shutdown()

    
    def toggleBackface(self):
        return toggleBackface(self.render.arc())

    
    def backfaceCullingOn(self):
        if self.toggleBackface():
            self.toggleBackface()
        

    
    def backfaceCullingOff(self):
        if not self.toggleBackface():
            self.toggleBackface()
        

    
    def toggleTexture(self):
        return toggleTexture(self.render.arc())

    
    def textureOn(self):
        if not self.toggleTexture():
            self.toggleTexture()
        

    
    def textureOff(self):
        if self.toggleTexture():
            self.toggleTexture()
        

    
    def toggleWireframe(self):
        return toggleWireframe(self.render.arc())

    
    def wireframeOn(self):
        if not self.toggleWireframe():
            self.toggleWireframe()
        

    
    def wireframeOff(self):
        if self.toggleWireframe():
            self.toggleWireframe()
        

    
    def disableMouse(self):
        self.mouse2cam.reparentTo(self.dataUnused)

    
    def enableMouse(self):
        self.mouse2cam.reparentTo(self.mouseInterface)

    
    def setMouseOnArc(self, newArc):
        self.mouse2cam.node().setArc(newArc)

    
    def useDrive(self):
        self.trackball.reparentTo(self.dataUnused)
        self.mouseInterface = self.drive
        self.mouseInterfaceNode = self.mouseInterface.node()
        self.drive.node().reset()
        self.drive.reparentTo(self.mouseValve, 0)
        self.mouse2cam.reparentTo(self.drive)
        self.drive.node().setZ(4.0)

    
    def useTrackball(self):
        self.drive.reparentTo(self.dataUnused)
        self.mouseInterface = self.trackball
        self.mouseInterfaceNode = self.mouseInterface.node()
        self.trackball.reparentTo(self.mouseValve, 0)
        self.mouse2cam.reparentTo(self.trackball)

    
    def oobe(self):
        
        try:
            self.oobeMode
        except:
            self.oobeMode = 0
            self.oobeCamera = self.hidden.attachNewNode('oobeCamera')
            self.oobeCameraTrackball = self.oobeCamera.attachNewNode('oobeCameraTrackball')
            self.oobeControl = DataValve.Control()
            self.mouseValve.node().setControl(1, self.oobeControl)
            self.oobeTrackball = self.mouseValve.attachNewNode(Trackball('oobeTrackball'), 1)
            self.oobe2cam = self.oobeTrackball.attachNewNode(Transform2SG('oobe2cam'))
            self.oobe2cam.node().setArc(self.oobeCameraTrackball.arc())
            self.oobeButtonEventsType = TypeRegistry.ptr().findType('ButtonEvents_ButtonEventDataTransition')
            self.oobeVis = loader.loadModelOnce('models/misc/camera')
            if self.oobeVis:
                self.oobeVis.arc().setFinal(1)
            
            self.oobeCullFrustum = None
            mods = ModifierButtons(self.mouseValve.node().getModifierButtons())
            mods.addButton(KeyboardButton.control())
            self.mouseValve.node().setModifierButtons(mods)

        if self.oobeMode:
            if self.oobeCullFrustum != None:
                self.oobeCull()
            
            self.oobeControl.setOff()
            self.mouseControl.setOn()
            if self.oobeVis:
                self.oobeVis.reparentTo(self.hidden)
            
            self.cam.reparentTo(self.camera)
            self.oobeCamera.reparentTo(self.hidden)
            self.oobeMode = 0
        else:
            mods = ModifierButtons(self.mouseValve.node().getModifierButtons())
            mods.allButtonsUp()
            self.oobeControl.setButtons(mods)
            mods.buttonDown(KeyboardButton.control())
            self.mouseControl.setButtons(mods)
            self.mouseValve.node().setFineControl(0, self.oobeButtonEventsType, self.onControl)
            cameraParent = NodePath(self.camera)
            cameraParent.shorten(1)
            self.oobeCamera.reparentTo(cameraParent)
            self.oobeCamera.clearMat()
            mat = Mat4.translateMat(0, -10, 3) * self.camera.getMat(cameraParent)
            mat.invertInPlace()
            self.oobeTrackball.node().setMat(mat)
            self.cam.reparentTo(self.oobeCameraTrackball)
            if self.oobeVis:
                self.oobeVis.reparentTo(self.camera)
            
            self.oobeMode = 1

    
    def oobeCull(self):
        
        try:
            if not (self.oobeMode):
                self.oobe()
        except:
            self.oobe()

        if self.oobeCullFrustum == None:
            pnode = ProjectionNode('oobeCull')
            pnode.setProjection(self.camNode.getProjection())
            self.oobeCullFrustum = self.camera.attachNewNode(pnode)
            numDrs = self.camNode.getNumDrs()
            for d in range(0, numDrs):
                dr = self.camNode.getDr(d)
                dr.setCullFrustum(pnode)
            
        else:
            numDrs = self.camNode.getNumDrs()
            for d in range(0, numDrs):
                dr = self.camNode.getDr(d)
                dr.setCullFrustum(self.camNode)
            
            self.oobeCullFrustum.removeNode()
            self.oobeCullFrustum = None

    
    def screenshot(self, namePrefix = 'screenshot'):
        date = time.ctime(time.time())
        frameCount = globalClock.getFrameCount()
        date = date.replace(' ', '-')
        date = date.replace(':', '-')
        imageName = namePrefix + '-' + date + '-' + str(frameCount) + '.bmp'
        self.notify.info('Taking screenshot: ' + imageName)
        takeSnapshot(self.win, imageName)

    
    def DisableAudio(self):
        if self.wantSfx:
            self.sfxManager.setActive(0)
        
        if self.wantMusic:
            self.musicManager.setActive(0)
        
        self.notify.debug('Disabling audio')

    
    def EnableAudio(self):
        if self.wantSfx:
            self.sfxManager.setActive(1)
        
        if self.wantMusic:
            self.musicManager.setActive(1)
        
        self.notify.debug('Enabling audio')

    
    def run(self):
        self.taskMgr.run()


