# Source Generated with Decompyle++
# File: DistributedCannonGame.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from DistributedMinigame import *
import FSM
import State
import ToontownGlobals
import ToontownTimer
import OnscreenText
import NodePath
import Task
import Trajectory
import math
import copy
import ToonHead
import ClockObject
import ClockDelta
import CannonGameGlobals
from DirectGui import *
LAND_TIME = 2
WORLD_SCALE = 2.0
GROUND_SCALE = 1.4 * WORLD_SCALE
CANNON_SCALE = 1.0
FAR_PLANE_DIST = 600 * WORLD_SCALE
CANNON_Y = -int((CannonGameGlobals.TowerYRange / 2) * 1.3)
CANNON_X_SPACING = 12
CANNON_Z = 20
CANNON_ROTATION_MIN = -20
CANNON_ROTATION_MAX = 20
CANNON_ROTATION_VEL = 15.0
CANNON_ANGLE_MIN = 10
CANNON_ANGLE_MAX = 85
CANNON_ANGLE_VEL = 15.0
CANNON_MOVE_UPDATE_FREQ = 0.5
CAMERA_PULLBACK_MIN = 20
CAMERA_PULLBACK_MAX = 40
MAX_LOOKAT_OFFSET = 80
TOON_TOWER_THRESHOLD = 150
SHADOW_Z_OFFSET = 0.1
TOWER_CURRENT_Z = 0.02
TOWER_TARGET_Z = SHADOW_Z_OFFSET
TOWER_Z_ADJUST = TOWER_TARGET_Z - TOWER_CURRENT_Z
TOWER_HEIGHT = 43.85 + TOWER_Z_ADJUST
TOWER_RADIUS = 10.5
BUCKET_HEIGHT = 36 + TOWER_Z_ADJUST
INITIAL_VELOCITY = 94.0
WHISTLE_SPEED = INITIAL_VELOCITY * 0.55

class DistributedCannonGame(DistributedMinigame):
    font = ToontownGlobals.getToonFont()
    LOCAL_CANNON_MOVE_TASK = 'localCannonMoveTask'
    HIT_GROUND = 0
    HIT_TOWER = 1
    HIT_WATER = 2
    FIRE_KEY = 'control'
    UP_KEY = 'up'
    DOWN_KEY = 'down'
    LEFT_KEY = 'left'
    RIGHT_KEY = 'right'
    INTRO_TASK_NAME = 'CannonGameIntro'
    INTRO_TASK_NAME_CAMERA_LERP = 'CannonGameIntroCamera'
    
    def __init__(self, cr):
        DistributedMinigame.__init__(self, cr)
        self.gameFSM = FSM.FSM('DistributedCannonGame', [
            State.State('off', self.enterOff, self.exitOff, [
                'start']),
            State.State('start', self.enterStart, self.exitStart, [
                'aim',
                'finish']),
            State.State('aim', self.enterAim, self.exitAim, [
                'shoot',
                'finish']),
            State.State('shoot', self.enterShoot, self.exitShoot, [
                'aim',
                'finish']),
            State.State('finish', self.enterFinish, self.exitFinish, [
                'off'])], 'off', 'off')
        self.gameFSM.enterInitialState()
        self.frameworkFSM.getStateNamed('game').addChild(self.gameFSM)
        self.cannonLocationDict = { }
        self.cannonPositionDict = { }
        self.cannonDict = { }
        self.toonModelDict = { }
        self.dropShadowDict = { }
        self.toonHeadDict = { }
        self.toonScaleDict = { }
        self.leftPressed = 0
        self.rightPressed = 0
        self.upPressed = 0
        self.downPressed = 0
        self.cannonMoving = 0
        self.modelCount = 14

    
    def getTitle(self):
        return 'Cannon Game'

    
    def getInstructions(self):
        return 'Shoot your toon into the water tower.'

    
    def generate(self):
        DistributedMinigame.generate(self)

    
    def handleAnnounceGenerate(self, obj):
        DistributedMinigame.handleAnnounceGenerate(self, obj)

    
    def disable(self):
        DistributedMinigame.disable(self)

    
    def load(self):
        DistributedMinigame.load(self)
        self.sky = loader.loadModel('phase_4/models/props/TT_sky')
        self.ground = loader.loadModel('phase_4/models/minigames/toon_cannon_gameground')
        self.tower = loader.loadModel('phase_4/models/minigames/toon_cannon_water_tower')
        self.cannon = loader.loadModel('phase_4/models/minigames/toon_cannon')
        self.dropShadow = loader.loadModel('phase_3/models/props/drop_shadow')
        self.hill = loader.loadModel('phase_4/models/minigames/cannon_hill')
        self.sky.setScale(WORLD_SCALE)
        self.ground.setScale(GROUND_SCALE)
        self.cannon.setScale(CANNON_SCALE)
        self.dropShadow.setColor(0, 0, 0, 0.5)
        self.ground.setColor(0.85, 0.85, 0.85, 1.0)
        self.hill.setScale(1, 1, CANNON_Z / 20.0)
        self.dropShadow.setBin('fixed', 0, 1)
        self.music = base.loadMusic('phase_4/audio/bgm/MG_cannon_game.mid')
        self.sndCannonMove = base.loadSfx('phase_4/audio/sfx/MG_cannon_adjust.mp3')
        self.sndCannonFire = base.loadSfx('phase_4/audio/sfx/MG_cannon_fire_alt.mp3')
        self.sndHitGround = base.loadSfx('phase_4/audio/sfx/MG_cannon_hit_dirt.mp3')
        self.sndHitTower = base.loadSfx('phase_4/audio/sfx/MG_cannon_hit_tower.mp3')
        self.sndHitWater = base.loadSfx('phase_4/audio/sfx/MG_cannon_splash.mp3')
        self.sndWhizz = base.loadSfx('phase_4/audio/sfx/MG_cannon_whizz.mp3')
        self.sndWin = base.loadSfx('phase_4/audio/sfx/MG_win.mp3')
        guiModel = 'phase_4/models/gui/cannon_game_gui'
        cannonGui = loader.loadModel(guiModel)
        self.aimPad = DirectFrame(image = cannonGui.find('**/CannonFire_PAD'), relief = None, pos = (0.7, 0, -0.553333), scale = 0.8)
        self.aimPad.hide()
        self.fireButton = DirectButton(parent = self.aimPad, image = ((guiModel, '**/Fire_Btn_UP'), (guiModel, '**/Fire_Btn_DN'), (guiModel, '**/Fire_Btn_RLVR')), relief = None, pos = (0.0115741, 0, 0.00505051), scale = 1.0, command = self._DistributedCannonGame__firePressed)
        self.upButton = DirectButton(parent = self.aimPad, image = ((guiModel, '**/Cannon_Arrow_UP'), (guiModel, '**/Cannon_Arrow_DN'), (guiModel, '**/Cannon_Arrow_RLVR')), relief = None, pos = (0.0115741, 0, 0.221717))
        self.downButton = DirectButton(parent = self.aimPad, image = ((guiModel, '**/Cannon_Arrow_UP'), (guiModel, '**/Cannon_Arrow_DN'), (guiModel, '**/Cannon_Arrow_RLVR')), relief = None, pos = (0.0136112, 0, -0.210101), image_hpr = (0, 0, 180))
        self.leftButton = DirectButton(parent = self.aimPad, image = ((guiModel, '**/Cannon_Arrow_UP'), (guiModel, '**/Cannon_Arrow_DN'), (guiModel, '**/Cannon_Arrow_RLVR')), relief = None, pos = (-0.199352, 0, -0.000505269), image_hpr = (0, 0, 90))
        self.rightButton = DirectButton(parent = self.aimPad, image = ((guiModel, '**/Cannon_Arrow_UP'), (guiModel, '**/Cannon_Arrow_DN'), (guiModel, '**/Cannon_Arrow_RLVR')), relief = None, pos = (0.219167, 0, -0.00101024), image_hpr = (0, 0, -90))
        self.aimPad.setColor(1, 1, 1, 0.9)
        
        def bindButton(button, upHandler, downHandler):
            button.bind(B1PRESS, (lambda x, handler = upHandler: handler()))
            button.bind(B1RELEASE, (lambda x, handler = downHandler: handler()))

        bindButton(self.upButton, self._DistributedCannonGame__upPressed, self._DistributedCannonGame__upReleased)
        bindButton(self.downButton, self._DistributedCannonGame__downPressed, self._DistributedCannonGame__downReleased)
        bindButton(self.leftButton, self._DistributedCannonGame__leftPressed, self._DistributedCannonGame__leftReleased)
        bindButton(self.rightButton, self._DistributedCannonGame__rightPressed, self._DistributedCannonGame__rightReleased)
        self.gameTimer = ToontownTimer.ToontownTimer()
        self.gameTimer.posInTopRightCorner()
        self.gameTimer.hide()

    
    def unload(self):
        DistributedMinigame.unload(self)
        toonbase.localToon.stopSky(self.sky)
        self.sky.removeNode()
        del self.sky
        self.ground.removeNode()
        del self.ground
        self.tower.removeNode()
        del self.tower
        del self.cannon
        del self.dropShadowDict
        del self.dropShadow
        self.hill.removeNode()
        del self.hill
        base.unloadMusic(self.music)
        del self.music
        base.unloadSfx(self.sndCannonMove)
        base.unloadSfx(self.sndCannonFire)
        base.unloadSfx(self.sndHitGround)
        base.unloadSfx(self.sndHitTower)
        base.unloadSfx(self.sndHitWater)
        base.unloadSfx(self.sndWhizz)
        base.unloadSfx(self.sndWin)
        del self.sndCannonMove
        del self.sndCannonFire
        del self.sndHitGround
        del self.sndHitTower
        del self.sndHitWater
        del self.sndWhizz
        del self.sndWin
        self.aimPad.destroy()
        del self.aimPad
        del self.fireButton
        del self.upButton
        del self.downButton
        del self.leftButton
        del self.rightButton
        for avId in self.toonHeadDict.keys():
            head = self.toonHeadDict[avId]
            head.stopBlink()
            head.stopLookAroundNow()
            av = self.getAvatar(avId)
            if av:
                av.nametag.removeNametag(head.tag)
            
            head.delete()
        
        del self.toonHeadDict
        for model in self.toonModelDict.values():
            model.removeNode()
        
        del self.toonModelDict
        del self.toonScaleDict
        for avId in self.avIdList:
            self.cannonDict[avId][0].removeNode()
            del self.cannonDict[avId][0]
        
        del self.cannonDict
        self.gameTimer.destroy()
        del self.gameTimer
        del self.cannonLocationDict
        self.frameworkFSM.getStateNamed('game').removeChild(self.gameFSM)
        del self.gameFSM

    
    def onstage(self):
        DistributedMinigame.onstage(self)
        self._DistributedCannonGame__createCannons()
        for avId in self.avIdList:
            self.cannonDict[avId][0].reparentTo(render)
        
        self.tower.reparentTo(render)
        self.sky.reparentTo(render)
        self.ground.reparentTo(render)
        self.hill.setPosHpr(0, CANNON_Y + 2.33, 0, 0, 0, 0)
        self.hill.reparentTo(render)
        self._DistributedCannonGame__createToonModels(self.localAvId)
        camera.reparentTo(render)
        self._DistributedCannonGame__oldCamFar = base.cam.node().getFar()
        base.cam.node().setFar(FAR_PLANE_DIST)
        self._DistributedCannonGame__startIntro()
        base.transitions.irisIn(0.4)
        base.playMusic(self.music, looping = 1, volume = 0.8)

    
    def offstage(self):
        self.sky.reparentTo(hidden)
        self.ground.reparentTo(hidden)
        self.hill.reparentTo(hidden)
        self.tower.reparentTo(hidden)
        for avId in self.avIdList:
            self.cannonDict[avId][0].reparentTo(hidden)
            self.dropShadowDict[avId].reparentTo(hidden)
        
        self._DistributedCannonGame__stopIntro()
        base.cam.node().setFar(self._DistributedCannonGame__oldCamFar)
        DistributedMinigame.offstage(self)

    
    def __createCannons(self):
        for avId in self.avIdList:
            cannon = self.cannon.copyTo(hidden)
            barrel = cannon.find('**/cannon')
            self.cannonDict[avId] = [
                cannon,
                barrel]
        
        numAvs = len(self.avIdList)
        for i in range(numAvs):
            avId = self.avIdList[i]
            self.cannonLocationDict[avId] = Point3(i * CANNON_X_SPACING - (numAvs - 1) * CANNON_X_SPACING / 2, CANNON_Y, CANNON_Z)
            self.cannonPositionDict[avId] = [
                0,
                CANNON_ANGLE_MIN]
            self.cannonDict[avId][0].setPos(self.cannonLocationDict[avId])
            self._DistributedCannonGame__updateCannonPosition(avId)
        

    
    def setGameReady(self):
        DistributedMinigame.setGameReady(self)
        for avId in self.avIdList:
            if avId != self.localAvId:
                self._DistributedCannonGame__createToonModels(avId)
            
        

    
    def __createToonModels(self, avId):
        toon = self.getAvatar(avId)
        self.toonScaleDict[avId] = toon.getScale()
        toon.useLOD(1000)
        toonParent = render.attachNewNode('toonOriginChange')
        toon.reparentTo(toonParent)
        toon.setPosHpr(0, 0, -(toon.getHeight() / 2.0), 0, 0, 0)
        self.toonModelDict[avId] = toonParent
        head = ToonHead.ToonHead()
        head.setupHead(self.getAvatar(avId).style)
        head.reparentTo(hidden)
        self.toonHeadDict[avId] = head
        toon = self.getAvatar(avId)
        tag = NametagFloat3d()
        tag.setContents(Nametag.CSpeech | Nametag.CThought)
        tag.setBillboardOffset(0)
        tag.setAvatarNode(head.node())
        toon.nametag.addNametag(tag)
        tagPath = head.attachNewNode(tag.upcastToNamedNode())
        tagPath.setPos(0, 0, 1)
        head.tag = tag
        self.getAvatar(avId).loop('neutral')
        self._DistributedCannonGame__loadToonInCannon(avId)
        for dropShadow in self.getAvatar(avId).dropShadows:
            dropShadow.hide()
        
        self.dropShadowDict[avId] = self.dropShadow.instanceTo(hidden)

    
    def setGameStart(self):
        DistributedMinigame.setGameStart(self)
        self._DistributedCannonGame__stopIntro()
        self.gameFSM.request('start')

    
    def setTowerPosition(self, x, y, z):
        self.towerPos = Point3(x, y, z + TOWER_Z_ADJUST)
        self.tower.setPos(self.towerPos)
        self.notify.debug('setTowerPosition: ' + str(self.towerPos))

    
    def setCannonPosition(self, avId, zRot, angle):
        self.notify.error('setCannonPosition should not be called on the client')

    
    def setCannonLit(self, avId, zRot, angle):
        self.notify.error('setCannonLit should not be called on the client')

    
    def updateCannonPosition(self, avId, zRot, angle):
        if self._DistributedCannonGame__gameOver:
            return None
        
        if avId != self.localAvId:
            self.cannonPositionDict[avId] = [
                zRot,
                angle]
            self._DistributedCannonGame__updateCannonPosition(avId)
        

    
    def setCannonWillFire(self, avId, sec, usec, zRot, angle):
        if self._DistributedCannonGame__gameOver:
            return None
        
        self.notify.debug('setCannonWillFire: ' + str(avId) + ': zRot=' + str(zRot) + ', angle=' + str(angle) + ', time=' + str(sec) + ',' + str(usec))
        self.cannonPositionDict[avId][0] = zRot
        self.cannonPositionDict[avId][1] = angle
        self._DistributedCannonGame__updateCannonPosition(avId)
        task = Task.Task(self._DistributedCannonGame__fireCannonTask)
        task.avId = avId
        task.fireTime = ClockDelta.serverTime2frameTimeDelta(sec, usec)
        curTime = globalClock.getFrameTime()
        timeToWait = task.fireTime - curTime
        if timeToWait > 0.0:
            fireTask = Task.sequence(Task.pause(timeToWait), task)
        else:
            fireTask = task
        fireTask = task
        taskMgr.spawnTaskNamed(fireTask, 'fireCannon' + str(avId))
        self.airborneToons += 1

    
    def setToonWillLandInWater(self, avId, sec, usec):
        self.notify.error('setToonWillLandInWater should not be called on the client')

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterStart(self):
        self._DistributedCannonGame__putCameraBehindCannon()
        if base.config.GetBool('cannon-game-timer', 1):
            self.gameTimer.show()
            self.gameTimer.countdown(CannonGameGlobals.GameTime, self._DistributedCannonGame__gameTimerExpired)
        
        self._DistributedCannonGame__gameOver = 0
        self.airborneToons = 0
        self.allToonsLandedCallback = None
        self.gameFSM.request('aim')

    
    def __gameTimerExpired(self):
        self.notify.debug('game timer expired')
        self.gameFSM.request('finish')

    
    def exitStart(self):
        pass

    
    def enterAim(self):
        self._DistributedCannonGame__enableAimInterface()
        self._DistributedCannonGame__putCameraBehindCannon()

    
    def exitAim(self):
        self._DistributedCannonGame__disableAimInterface()

    
    def enterShoot(self):
        self._DistributedCannonGame__broadcastLocalCannonPosition()
        self.sendUpdate('setCannonLit', [
            self.localAvId,
            self.cannonPositionDict[self.localAvId][0],
            self.cannonPositionDict[self.localAvId][1]])

    
    def exitShoot(self):
        pass

    
    def __somebodyWon(self, avId):
        if avId == self.localAvId:
            base.playSfx(self.sndWin)
        
        self.gameFSM.request('finish')

    
    def enterFinish(self):
        if self.airborneToons:
            self.allToonsLandedCallback = self.endGame
        else:
            self.endGame()

    
    def endGame(self):
        base.stopMusic(self.music)
        self.gameOver()
        self._DistributedCannonGame__cleanThingsUp()
        self._DistributedCannonGame__gameOver = 1
        self.gameFSM.request('off')

    
    def exitFinish(self):
        pass

    
    def __cleanThingsUp(self):
        for avId in self.avIdList:
            av = self.getAvatar(avId)
            if av:
                for dropShadow in av.dropShadows:
                    dropShadow.show()
                
                av.resetLOD()
            
            taskMgr.removeTasksNamed('fireCannon' + str(avId))
            taskMgr.removeTasksNamed('flyingToon' + str(avId))
        

    
    def setGameAbort(self):
        self._DistributedCannonGame__cleanThingsUp()
        DistributedMinigame.setGameAbort(self)

    
    def setGameExit(self):
        self._DistributedCannonGame__cleanThingsUp()
        DistributedMinigame.setGameExit(self)

    
    def __enableAimInterface(self):
        self.aimPad.show()
        self.accept(self.FIRE_KEY, self._DistributedCannonGame__fireKeyPressed)
        self.accept(self.UP_KEY, self._DistributedCannonGame__upKeyPressed)
        self.accept(self.DOWN_KEY, self._DistributedCannonGame__downKeyPressed)
        self.accept(self.LEFT_KEY, self._DistributedCannonGame__leftKeyPressed)
        self.accept(self.RIGHT_KEY, self._DistributedCannonGame__rightKeyPressed)
        self._DistributedCannonGame__spawnLocalCannonMoveTask()

    
    def __disableAimInterface(self):
        self.aimPad.hide()
        self.ignore(self.FIRE_KEY)
        self.ignore(self.UP_KEY)
        self.ignore(self.DOWN_KEY)
        self.ignore(self.LEFT_KEY)
        self.ignore(self.RIGHT_KEY)
        self.ignore(self.FIRE_KEY + '-up')
        self.ignore(self.UP_KEY + '-up')
        self.ignore(self.DOWN_KEY + '-up')
        self.ignore(self.LEFT_KEY + '-up')
        self.ignore(self.RIGHT_KEY + '-up')
        self._DistributedCannonGame__killLocalCannonMoveTask()

    
    def __fireKeyPressed(self):
        self.ignore(self.FIRE_KEY)
        self.accept(self.FIRE_KEY + '-up', self._DistributedCannonGame__fireKeyReleased)
        self._DistributedCannonGame__firePressed()

    
    def __upKeyPressed(self):
        self.ignore(self.UP_KEY)
        self.accept(self.UP_KEY + '-up', self._DistributedCannonGame__upKeyReleased)
        self._DistributedCannonGame__upPressed()

    
    def __downKeyPressed(self):
        self.ignore(self.DOWN_KEY)
        self.accept(self.DOWN_KEY + '-up', self._DistributedCannonGame__downKeyReleased)
        self._DistributedCannonGame__downPressed()

    
    def __leftKeyPressed(self):
        self.ignore(self.LEFT_KEY)
        self.accept(self.LEFT_KEY + '-up', self._DistributedCannonGame__leftKeyReleased)
        self._DistributedCannonGame__leftPressed()

    
    def __rightKeyPressed(self):
        self.ignore(self.RIGHT_KEY)
        self.accept(self.RIGHT_KEY + '-up', self._DistributedCannonGame__rightKeyReleased)
        self._DistributedCannonGame__rightPressed()

    
    def __fireKeyReleased(self):
        self.ignore(self.FIRE_KEY + '-up')
        self.accept(self.FIRE_KEY, self._DistributedCannonGame__fireKeyPressed)
        self._DistributedCannonGame__fireReleased()

    
    def __leftKeyReleased(self):
        self.ignore(self.LEFT_KEY + '-up')
        self.accept(self.LEFT_KEY, self._DistributedCannonGame__leftKeyPressed)
        self._DistributedCannonGame__leftReleased()

    
    def __rightKeyReleased(self):
        self.ignore(self.RIGHT_KEY + '-up')
        self.accept(self.RIGHT_KEY, self._DistributedCannonGame__rightKeyPressed)
        self._DistributedCannonGame__rightReleased()

    
    def __upKeyReleased(self):
        self.ignore(self.UP_KEY + '-up')
        self.accept(self.UP_KEY, self._DistributedCannonGame__upKeyPressed)
        self._DistributedCannonGame__upReleased()

    
    def __downKeyReleased(self):
        self.ignore(self.DOWN_KEY + '-up')
        self.accept(self.DOWN_KEY, self._DistributedCannonGame__downKeyPressed)
        self._DistributedCannonGame__downReleased()

    
    def __firePressed(self):
        self.notify.debug('fire pressed')
        self.gameFSM.request('shoot')

    
    def __upPressed(self):
        self.notify.debug('up pressed')
        self.upPressed = self._DistributedCannonGame__enterControlActive(self.upPressed)

    
    def __downPressed(self):
        self.notify.debug('down pressed')
        self.downPressed = self._DistributedCannonGame__enterControlActive(self.downPressed)

    
    def __leftPressed(self):
        self.notify.debug('left pressed')
        self.leftPressed = self._DistributedCannonGame__enterControlActive(self.leftPressed)

    
    def __rightPressed(self):
        self.notify.debug('right pressed')
        self.rightPressed = self._DistributedCannonGame__enterControlActive(self.rightPressed)

    
    def __upReleased(self):
        self.notify.debug('up released')
        self.upPressed = self._DistributedCannonGame__exitControlActive(self.upPressed)

    
    def __downReleased(self):
        self.notify.debug('down released')
        self.downPressed = self._DistributedCannonGame__exitControlActive(self.downPressed)

    
    def __leftReleased(self):
        self.notify.debug('left released')
        self.leftPressed = self._DistributedCannonGame__exitControlActive(self.leftPressed)

    
    def __rightReleased(self):
        self.notify.debug('right released')
        self.rightPressed = self._DistributedCannonGame__exitControlActive(self.rightPressed)

    
    def __enterControlActive(self, control):
        return control + 1

    
    def __exitControlActive(self, control):
        return max(0, control - 1)

    
    def __spawnLocalCannonMoveTask(self):
        self.leftPressed = 0
        self.rightPressed = 0
        self.upPressed = 0
        self.downPressed = 0
        self.cannonMoving = 0
        task = Task.Task(self._DistributedCannonGame__localCannonMoveTask)
        task.lastPositionBroadcastTime = 0.0
        taskMgr.spawnTaskNamed(task, self.LOCAL_CANNON_MOVE_TASK)

    
    def __killLocalCannonMoveTask(self):
        taskMgr.removeTasksNamed(self.LOCAL_CANNON_MOVE_TASK)
        if self.cannonMoving:
            base.stopSfx(self.sndCannonMove)
        

    
    def __localCannonMoveTask(self, task):
        pos = self.cannonPositionDict[self.localAvId]
        oldRot = pos[0]
        oldAng = pos[1]
        rotVel = 0
        if self.leftPressed:
            rotVel += CANNON_ROTATION_VEL
        
        if self.rightPressed:
            rotVel -= CANNON_ROTATION_VEL
        
        pos[0] += rotVel * globalClock.getDt()
        if pos[0] < CANNON_ROTATION_MIN:
            pos[0] = CANNON_ROTATION_MIN
        elif pos[0] > CANNON_ROTATION_MAX:
            pos[0] = CANNON_ROTATION_MAX
        
        angVel = 0
        if self.upPressed:
            angVel += CANNON_ANGLE_VEL
        
        if self.downPressed:
            angVel -= CANNON_ANGLE_VEL
        
        pos[1] += angVel * globalClock.getDt()
        if pos[1] < CANNON_ANGLE_MIN:
            pos[1] = CANNON_ANGLE_MIN
        elif pos[1] > CANNON_ANGLE_MAX:
            pos[1] = CANNON_ANGLE_MAX
        
        if oldRot != pos[0] or oldAng != pos[1]:
            if self.cannonMoving == 0:
                self.cannonMoving = 1
                base.playSfx(self.sndCannonMove, looping = 1)
            
            self._DistributedCannonGame__updateCannonPosition(self.localAvId)
            if task.time - task.lastPositionBroadcastTime > CANNON_MOVE_UPDATE_FREQ:
                task.lastPositionBroadcastTime = task.time
                self._DistributedCannonGame__broadcastLocalCannonPosition()
            
        elif self.cannonMoving:
            self.cannonMoving = 0
            base.stopSfx(self.sndCannonMove)
            self._DistributedCannonGame__broadcastLocalCannonPosition()
        
        return Task.cont

    
    def __broadcastLocalCannonPosition(self):
        self.sendUpdate('setCannonPosition', [
            self.localAvId,
            self.cannonPositionDict[self.localAvId][0],
            self.cannonPositionDict[self.localAvId][1]])

    
    def __updateCannonPosition(self, avId):
        self.cannonDict[avId][0].setHpr(self.cannonPositionDict[avId][0], 0.0, 0.0)
        self.cannonDict[avId][1].setHpr(0.0, self.cannonPositionDict[avId][1], 0.0)

    
    def __getCameraPositionBehindCannon(self):
        return Point3(self.cannonLocationDict[self.localAvId][0], CANNON_Y - 25.0, CANNON_Z + 7)

    
    def __putCameraBehindCannon(self):
        camera.setPos(self._DistributedCannonGame__getCameraPositionBehindCannon())
        camera.setHpr(0, 0, 0)

    
    def __loadToonInCannon(self, avId):
        self.toonModelDict[avId].reparentTo(hidden)
        head = self.toonHeadDict[avId]
        head.startBlink()
        head.startLookAround()
        head.reparentTo(self.cannonDict[avId][1])
        head.setPosHpr(0, 6, 0, 0, -45, 0)
        sc = self.toonScaleDict[avId]
        head.setScale(render, sc[0], sc[1], sc[2])

    
    def __toRadians(self, angle):
        return angle * 2.0 * math.pi / 360.0

    
    def __toDegrees(self, angle):
        return angle * 360.0 / 2.0 * math.pi

    
    def __fireCannonTask(self, task):
        launchTime = task.fireTime
        avId = task.avId
        self.notify.debug('FIRING CANNON FOR AVATAR ' + str(avId))
        head = self.toonHeadDict[avId]
        startPos = head.getPos(render)
        startHpr = head.getHpr(render)
        head.stopBlink()
        head.stopLookAroundNow()
        head.reparentTo(hidden)
        av = self.toonModelDict[avId]
        av.reparentTo(render)
        av.setPos(startPos)
        av.setHpr(startHpr)
        hpr = self.cannonDict[avId][1].getHpr(render)
        towerPos = self.tower.getPos(render)
        rotation = self._DistributedCannonGame__toRadians(hpr[0])
        angle = self._DistributedCannonGame__toRadians(hpr[1])
        horizVel = INITIAL_VELOCITY * math.cos(angle)
        xVel = horizVel * -math.sin(rotation)
        yVel = horizVel * math.cos(rotation)
        zVel = INITIAL_VELOCITY * math.sin(angle)
        startVel = Vec3(xVel, yVel, zVel)
        trajectory = Trajectory.Trajectory(launchTime, startPos, startVel)
        self.notify.debug('start position: ' + str(startPos))
        self.notify.debug('start velocity: ' + str(startVel))
        towerList = [
            towerPos + Point3(0, 0, BUCKET_HEIGHT),
            TOWER_RADIUS,
            TOWER_HEIGHT - BUCKET_HEIGHT]
        (timeOfImpact, hitWhat) = self._DistributedCannonGame__calcToonImpact(trajectory, towerList)
        self.notify.debug('time of launch: ' + str(launchTime))
        self.notify.debug('time of impact: ' + str(timeOfImpact))
        self.notify.debug('location of impact: ' + str(trajectory.getPos(timeOfImpact)))
        shootTask = Task.Task(self._DistributedCannonGame__shootTask)
        flyTask = Task.Task(self._DistributedCannonGame__flyTask)
        seqDoneTask = Task.Task(self._DistributedCannonGame__flySequenceDoneTask)
        info = { }
        info['avId'] = avId
        info['trajectory'] = trajectory
        info['launchTime'] = launchTime
        info['timeOfImpact'] = timeOfImpact
        info['hitWhat'] = hitWhat
        info['toon'] = self.toonModelDict[avId]
        info['hRot'] = self.cannonPositionDict[avId][0]
        info['haveWhistled'] = 0
        info['maxCamPullback'] = CAMERA_PULLBACK_MIN
        (info['timeEnterTowerXY'], info['timeExitTowerXY']) = trajectory.calcEnterAndLeaveCylinderXY(self.tower.getPos(render), TOWER_RADIUS)
        shootTask.info = info
        flyTask.info = info
        seqDoneTask.info = info
        seqTask = Task.sequence(shootTask, flyTask, Task.pause(LAND_TIME), seqDoneTask)
        taskMgr.spawnTaskNamed(seqTask, 'flyingToon' + str(avId))
        if avId == self.localAvId:
            if info['hitWhat'] == self.HIT_WATER:
                (sec, usec) = ClockDelta.frameTime2serverTimeDelta(info['timeOfImpact'])
                self.sendUpdate('setToonWillLandInWater', [
                    avId,
                    sec,
                    usec])
            
        
        return Task.done

    
    def __calcToonImpact(self, trajectory, waterTower):
        waterDiscCenter = Point3(waterTower[0])
        waterDiscCenter.setZ(waterDiscCenter[2] + waterTower[2])
        t_waterImpact = trajectory.checkCollisionWithDisc(waterDiscCenter, waterTower[1])
        if t_waterImpact > 0:
            self.notify.debug('toon will land in the water')
            return (t_waterImpact, self.HIT_WATER)
        
        t_towerImpact = trajectory.checkCollisionWithCylinderSides(waterTower[0], waterTower[1], waterTower[2])
        self.notify.debug('time of tower impact: ' + str(t_towerImpact))
        if t_towerImpact > 0:
            self.notify.debug('toon will hit the tower')
            return (t_towerImpact, self.HIT_TOWER)
        
        t_groundImpact = trajectory.checkCollisionWithGround()
        if t_groundImpact > 0:
            self.notify.debug('toon will hit the ground')
            return (t_groundImpact, self.HIT_GROUND)
        else:
            self.notify.error('__calcToonImpact: toon never impacts ground?')
            return (self.startTime, self.HIT_GROUND)

    
    def __shootTask(self, task):
        base.playSfx(self.sndCannonFire)
        self.dropShadowDict[task.info['avId']].reparentTo(render)
        return Task.done

    
    def __flyTask(self, task):
        curTime = task.time + task.info['launchTime']
        t = min(curTime, task.info['timeOfImpact'])
        pos = task.info['trajectory'].getPos(t)
        task.info['toon'].setPos(pos)
        shadowPos = Point3(pos)
        if t >= task.info['timeEnterTowerXY'] and t <= task.info['timeExitTowerXY']:
            shadowPos.setZ(self.tower.getPos(render)[2] + TOWER_HEIGHT + SHADOW_Z_OFFSET)
        else:
            shadowPos.setZ(SHADOW_Z_OFFSET)
        self.dropShadowDict[task.info['avId']].setPos(shadowPos)
        vel = task.info['trajectory'].getVel(t)
        run = math.sqrt(vel[0] * vel[0] + vel[1] * vel[1])
        rise = vel[2]
        theta = self._DistributedCannonGame__toDegrees(math.atan(rise / run))
        task.info['toon'].setHpr(task.info['hRot'], -90 + theta, 0)
        if task.info['avId'] == self.localAvId:
            lookAt = self.tower.getPos(render)
            lookAt.setZ(lookAt.getZ() - TOWER_HEIGHT / 2.0)
            towerPos = self.tower.getPos(render)
            towerPos.setZ(TOWER_HEIGHT)
            ttVec = Vec3(pos - towerPos)
            toonTowerDist = ttVec.length()
            multiplier = 0.0
            if toonTowerDist < TOON_TOWER_THRESHOLD:
                up = Vec3(0.0, 0.0, 1.0)
                perp = up.cross(vel)
                perp.normalize()
                if ttVec.dot(perp) > 0.0:
                    perp = Vec3(-perp[0], -perp[1], -perp[2])
                
                a = 1.0 - toonTowerDist / TOON_TOWER_THRESHOLD
                a_2 = a * a
                multiplier = -2.0 * a_2 * a + 3 * a_2
                lookAt = lookAt + perp * multiplier * MAX_LOOKAT_OFFSET
            
            foo = Vec3(pos - lookAt)
            foo.normalize()
            task.info['maxCamPullback'] = max(task.info['maxCamPullback'], CAMERA_PULLBACK_MIN + multiplier * (CAMERA_PULLBACK_MAX - CAMERA_PULLBACK_MIN))
            foo = foo * task.info['maxCamPullback']
            camPos = pos + Point3(foo)
            camera.setPos(camPos)
            camera.lookAt(pos)
        
        if task.info['haveWhistled'] == 0:
            if -vel[2] > WHISTLE_SPEED:
                if t < task.info['timeOfImpact'] - 0.5:
                    task.info['haveWhistled'] = 1
                    base.playSfx(self.sndWhizz)
                
            
        
        if t == task.info['timeOfImpact']:
            if task.info['haveWhistled']:
                base.stopSfx(self.sndWhizz)
            
            self.dropShadowDict[task.info['avId']].reparentTo(hidden)
            if task.info['hitWhat'] == self.HIT_WATER:
                base.playSfx(self.sndHitWater)
                task.info['toon'].setHpr(task.info['hRot'], 0, 0)
                self._DistributedCannonGame__somebodyWon(task.info['avId'])
            elif task.info['hitWhat'] == self.HIT_TOWER:
                base.playSfx(self.sndHitTower)
            elif task.info['hitWhat'] == self.HIT_GROUND:
                base.playSfx(self.sndHitGround)
            
            return Task.done
        
        return Task.cont

    
    def __flySequenceDoneTask(self, task):
        self._DistributedCannonGame__loadToonInCannon(task.info['avId'])
        if task.info['avId'] == self.localAvId:
            self.gameFSM.request('aim')
        
        self.airborneToons -= 1
        if 0 == self.airborneToons:
            if self.allToonsLandedCallback:
                self.allToonsLandedCallback()
            
        
        return Task.done

    
    def __startIntro(self):
        self.T_WATER = 1
        self.T_WATER2LONGVIEW = 1
        self.T_LONGVIEW = 1
        self.T_LONGVIEW2TOONHEAD = 2
        self.T_TOONHEAD = 2
        self.T_TOONHEAD2CANNONBACK = 2
        taskLookInWater = Task.Task(self._DistributedCannonGame__taskLookInWater)
        taskPullBackFromWater = Task.Task(self._DistributedCannonGame__taskPullBackFromWater)
        taskFlyUpToToon = Task.Task(self._DistributedCannonGame__flyUpToToon)
        taskFlyToBackOfCannon = Task.Task(self._DistributedCannonGame__flyToBackOfCannon)
        commonData = { }
        taskLookInWater.data = commonData
        taskPullBackFromWater.data = commonData
        taskFlyUpToToon.data = commonData
        taskFlyToBackOfCannon.data = commonData
        introTask = Task.sequence(taskLookInWater, Task.pause(self.T_WATER), taskPullBackFromWater, Task.pause(self.T_WATER2LONGVIEW + self.T_LONGVIEW), taskFlyUpToToon, Task.pause(self.T_LONGVIEW2TOONHEAD + self.T_TOONHEAD), taskFlyToBackOfCannon)
        taskMgr.spawnTaskNamed(introTask, self.INTRO_TASK_NAME)

    
    def __stopIntro(self):
        taskMgr.removeTasksNamed(self.INTRO_TASK_NAME)
        taskMgr.removeTasksNamed(self.INTRO_TASK_NAME_CAMERA_LERP)
        camera.wrtReparentTo(render)

    
    def __spawnCameraLookAtLerp(self, targetPos, targetLookAt, duration):
        oldPos = camera.getPos()
        oldHpr = camera.getHpr()
        camera.setPos(targetPos)
        camera.lookAt(targetLookAt)
        targetHpr = camera.getHpr()
        camera.setPos(oldPos)
        camera.setHpr(oldHpr)
        camera.lerpPosHpr(Point3(targetPos), targetHpr, duration, blendType = 'easeInOut', task = self.INTRO_TASK_NAME_CAMERA_LERP)

    
    def __taskLookInWater(self, task):
        task.data['cannonCenter'] = Point3(0, CANNON_Y, CANNON_Z)
        task.data['towerWaterCenter'] = Point3(self.towerPos + Point3(0, 0, TOWER_HEIGHT))
        task.data['vecTowerToCannon'] = Point3(task.data['cannonCenter'] - task.data['towerWaterCenter'])
        vecAwayFromCannons = Vec3(Point3(0, 0, 0) - task.data['vecTowerToCannon'])
        vecAwayFromCannons.setZ(0.0)
        vecAwayFromCannons.normalize()
        camLoc = Point3(vecAwayFromCannons * 20) + Point3(0, 0, 20)
        camLoc = camLoc + task.data['towerWaterCenter']
        camera.setPos(camLoc)
        camera.lookAt(task.data['towerWaterCenter'])
        task.data['vecAwayFromCannons'] = vecAwayFromCannons
        return Task.done

    
    def __taskPullBackFromWater(self, task):
        camLoc = Point3(task.data['vecAwayFromCannons'] * 40) + Point3(0, 0, 20)
        camLoc = camLoc + task.data['towerWaterCenter']
        lookAt = task.data['cannonCenter']
        self._DistributedCannonGame__spawnCameraLookAtLerp(camLoc, lookAt, self.T_WATER2LONGVIEW)
        return Task.done

    
    def __flyUpToToon(self, task):
        headPos = self.toonHeadDict[self.localAvId].getPos(render)
        camLoc = headPos + Point3(0, 5, 0)
        lookAt = Point3(headPos)
        self._DistributedCannonGame__spawnCameraLookAtLerp(camLoc, lookAt, self.T_LONGVIEW2TOONHEAD)
        return Task.done

    
    def __flyToBackOfCannon(self, task):
        lerpNode = hidden.attachNewNode('CannonGameCameraLerpNode')
        lerpNode.reparentTo(render)
        lerpNode.setPos(self.cannonLocationDict[self.localAvId] + Point3(0, 1, 0))
        relCamPos = camera.getPos(lerpNode)
        relCamHpr = camera.getHpr(lerpNode)
        startRotation = lerpNode.getHpr()
        endRotation = Point3(-180, 0, 0)
        lerpNode.setHpr(endRotation)
        camera.setPos(self._DistributedCannonGame__getCameraPositionBehindCannon())
        endPos = camera.getPos(lerpNode)
        lerpNode.setHpr(startRotation)
        camera.reparentTo(lerpNode)
        camera.setPos(relCamPos)
        camera.setHpr(relCamHpr)
        lerpNode.lerpHpr(endRotation, self.T_TOONHEAD2CANNONBACK, blendType = 'easeInOut', task = self.INTRO_TASK_NAME_CAMERA_LERP)
        camera.lerpPos(endPos, self.T_TOONHEAD2CANNONBACK, blendType = 'easeInOut', task = self.INTRO_TASK_NAME_CAMERA_LERP)
        return Task.done


