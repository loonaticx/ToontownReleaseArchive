# Source Generated with Decompyle++
# File: DistributedRingGame.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from DistributedMinigame import *
import FSM
import State
import ToontownTimer
import Task
import ArrowKeys
import Ring
import RingTrack
import RingGameGlobals
import RingGroup
import RandomNumGen
import ClockDelta

class DistributedRingGame(DistributedMinigame):
    colorNames = ('red', 'green', 'blue', 'yellow')
    UP_KEY = 'up'
    DOWN_KEY = 'down'
    LEFT_KEY = 'left'
    RIGHT_KEY = 'right'
    UPDATE_ENVIRON_TASK = 'RingGameUpdateEnvironTask'
    UPDATE_LOCALTOON_TASK = 'RingGameUpdateLocalToonTask'
    UPDATE_RINGS_TASK = 'RingGameUpdateRingsTask'
    
    def __init__(self, cr):
        DistributedMinigame.__init__(self, cr)
        self.gameFSM = FSM.FSM('DistributedRingGame', [
            State.State('off', self.enterOff, self.exitOff, [
                'swim']),
            State.State('swim', self.enterSwim, self.exitSwim, [
                'finish']),
            State.State('finish', self.enterFinish, self.exitFinish, [
                'off'])], 'off', 'off')
        self.frameworkFSM.getStateNamed('game').addChild(self.gameFSM)

    
    def getTitle(self):
        return 'Ring Game'

    
    def getInstructions(self):
        if self.isSinglePlayer():
            return 'Swim through as many rings as you can.'
        else:
            return 'Swim through the ' + self.colorNames[self.avIdList.index(self.localAvId)] + ' rings. If anyone misses a ring, nobody ' + 'gets any jellybeans!'

    
    def generate(self):
        DistributedMinigame.generate(self)

    
    def disable(self):
        DistributedMinigame.disable(self)

    
    def __defineConstants(self):
        self.TOON_SWIM_VEL = 12.0
        self.FAR_PLANE_DIST = 250
        self.MAX_TOONXY = 10.0
        self.TOONXY_SPEED = self.MAX_TOONXY / 1.0
        self.WATER_DEPTH = 35.0
        self.ENVIRON_LENGTH = 150.0
        self.ENVIRON_START_OFFSET = 30.0
        self.TOON_INITIAL_SPACING = 4.0
        self.WATER_COLOR = Vec4(0, 0, 0.6, 1)

    
    def load(self):
        DistributedMinigame.load(self)
        self._DistributedRingGame__defineConstants()
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.posInTopRightCorner()
        self.timer.hide()
        loadBase = 'phase_4/models/minigames/'
        self.environModel = loader.loadModel(loadBase + 'swimming_game.bam')
        self.environModel.setHpr(0, 90, 0)
        self.environModel.setPos(0, self.WATER_DEPTH / 2.0, self.ENVIRON_LENGTH / 2.0)
        self.environModel.flattenMedium()
        self.ringModel = loader.loadModel(loadBase + 'swimming_game_ring.bam')
        self.ringModel.setP(90)

    
    def unload(self):
        DistributedMinigame.unload(self)
        self.timer.destroy()
        del self.timer
        del self.environModel
        del self.ringModel

    
    def onstage(self):
        DistributedMinigame.onstage(self)
        self.arrowKeys = ArrowKeys.ArrowKeys()
        toon = toonbase.localToon
        toon.reparentTo(render)
        toon.loop('swim')
        toon.setPos(0, 0, 0)
        toon.setHpr(0, 0, 0)
        self._DistributedRingGame__placeToon(self.localAvId)
        camera.reparentTo(render)
        camera.setPos(0, 0, -30)
        camera.lookAt(0, 0, 0)
        self._DistributedRingGame__oldCamFar = base.cam.node().getFar()
        base.cam.node().setFar(self.FAR_PLANE_DIST)
        self.oldBgColor = base.win.getGsg().getColorClearValue()
        base.win.getGsg().setColorClearValue(self.WATER_COLOR)
        self._DistributedRingGame__fog = Fog(Fog.MLinear)
        if base.wantFog:
            self._DistributedRingGame__fog.setColor(self.WATER_COLOR)
            self._DistributedRingGame__fog.setRange(0.1, self.FAR_PLANE_DIST - 1.0)
            render.setFog(self._DistributedRingGame__fog)
        
        self.environNode = render.attachNewNode('environNode')
        self.environBlocks = []
        for i in range(0, 3):
            instance = self.environModel.instanceTo(self.environNode)
            z = self.ENVIRON_LENGTH * i
            instance.setZ(z)
            self.environBlocks.append(instance)
            for j in range(0, i):
                instance = self.environModel.instanceTo(self.environNode)
                x = self.ENVIRON_LENGTH * (j + 1)
                instance.setZ(z)
                instance.setX(-x)
                self.environBlocks.append(instance)
            
            for j in range(0, i):
                instance = self.environModel.instanceTo(self.environNode)
                x = self.ENVIRON_LENGTH * (j + 1)
                instance.setZ(z)
                instance.setX(x)
                self.environBlocks.append(instance)
            
        
        self._DistributedRingGame__spawnUpdateEnvironTask()
        self.ringNode = render.attachNewNode('ringNode')

    
    def offstage(self):
        DistributedMinigame.offstage(self)
        base.cam.node().setFar(self._DistributedRingGame__oldCamFar)
        if self.oldBgColor:
            base.win.getGsg().setColorClearValue(self.oldBgColor)
        
        render.clearFog()
        self._DistributedRingGame__killUpdateEnvironTask()
        self._DistributedRingGame__killUpdateRingsTask()
        self.arrowKeys.destroy()
        del self.arrowKeys
        for block in self.environBlocks:
            del block
        
        self.environNode.removeNode()
        del self.environNode
        self.ringNode.removeNode()
        del self.ringNode
        toon = toonbase.localToon
        toon.reparentTo(hidden)

    
    def __placeToon(self, avId):
        toon = self.getAvatar(avId)
        i = self.avIdList.index(avId)
        numToons = float(len(self.avIdList))
        x = i * self.TOON_INITIAL_SPACING
        x -= self.TOON_INITIAL_SPACING * (numToons - 1) / 2.0
        toon.setPos(x, 0, 0)
        toon.setHpr(0, 0, 0)

    
    def setGameReady(self):
        DistributedMinigame.setGameReady(self)
        for avId in self.remoteAvIdList:
            toon = self.getAvatar(avId)
            if toon:
                toon.reparentTo(render)
                toon.loop('swim')
                self._DistributedRingGame__placeToon(avId)
            
        

    
    def setGameStart(self):
        DistributedMinigame.setGameStart(self)
        self.gameFSM.request('swim')

    
    def enterOff(self):
        self.notify.debug('enterOff')

    
    def exitOff(self):
        pass

    
    def enterSwim(self):
        self.notify.debug('enterSwim')
        self.timer.show()
        time = RingGameGlobals.TIMER_LEN
        self.timer.setTime(time)
        self.timer.countdown(time, self._DistributedRingGame__timerUp)
        self._DistributedRingGame__numRingGroups = RingGameGlobals.NUM_RING_GROUPS
        self._DistributedRingGame__ringGroupsPassed = 0
        self._DistributedRingGame__generateRings()
        self._DistributedRingGame__spawnUpdateLocalToonTask()

    
    def __randomRingTrack(self):
        track = []
        rnd = self._DistributedRingGame__randomNumGen
        
        def randPos(rnd = rnd):
            return [
                rnd.random() * 2.0 - 1.0,
                rnd.random() * 2.0 - 1.0]

        originPos = randPos()
        trackLen = rnd.randint(3, 9)
        curPos = originPos
        destPos = originPos
        for i in range(0, trackLen):
            if i == trackLen - 1:
                destPos = originPos
            else:
                destPos = randPos()
            track.append([
                1.0 / trackLen,
                RingTrack.ringLerp,
                [
                    curPos,
                    destPos]])
        
        return track

    
    def __generateRings(self):
        self._DistributedRingGame__ringGroups = []
        for i in range(0, self._DistributedRingGame__numRingGroups):
            track = self._DistributedRingGame__randomRingTrack()
            ringGroup = RingGroup.RingGroup(len(self.avIdList), self.ringModel, [
                track] * 4, self.MAX_TOONXY)
            self._DistributedRingGame__ringGroups.append(ringGroup)
            ringGroup.reparentTo(self.ringNode)
            ringGroup.setZ(i * 50.0)
        

    
    def __destroyRings(self):
        for group in self._DistributedRingGame__ringGroups:
            pass
        
        del self._DistributedRingGame__ringGroups

    
    def __timerUp(self):
        self.gameFSM.request('finish')

    
    def __spawnUpdateLocalToonTask(self):
        self._DistributedRingGame__initPosBroadcast()
        task = Task.Task(self._DistributedRingGame__updateLocalToonTask)
        taskMgr.spawnTaskNamed(task, self.UPDATE_LOCALTOON_TASK)

    
    def __killUpdateLocalToonTask(self):
        taskMgr.removeTasksNamed(self.UPDATE_LOCALTOON_TASK)

    
    def __initPosBroadcast(self):
        self._DistributedRingGame__posBroadcastPeriod = 0.1
        self._DistributedRingGame__timeSinceLastPosBroadcast = 0.0
        self._DistributedRingGame__lastPosBroadcast = self.getAvatar(self.localAvId).getPos()
        lt = self.getAvatar(self.localAvId)
        lt.d_setPosHpr(lt.getX(), lt.getY(), lt.getZ(), lt.getH(), lt.getP(), lt.getR())

    
    def __posBroadcast(self, dt):
        self._DistributedRingGame__timeSinceLastPosBroadcast += dt
        if self._DistributedRingGame__timeSinceLastPosBroadcast > self._DistributedRingGame__posBroadcastPeriod:
            self._DistributedRingGame__timeSinceLastPosBroadcast -= self._DistributedRingGame__posBroadcastPeriod
            pos = self.getAvatar(self.localAvId).getPos()
            if pos[0] != self._DistributedRingGame__lastPosBroadcast[0] or pos[1] != self._DistributedRingGame__lastPosBroadcast[1]:
                self.getAvatar(self.localAvId).d_setXY(pos[0], pos[1])
            
        

    
    def __updateLocalToonTask(self, task):
        dt = globalClock.getDt()
        toonPos = self.getAvatar(self.localAvId).getPos()
        pos = [
            toonPos[0],
            toonPos[1]]
        xVel = 0.0
        if self.arrowKeys.leftPressed():
            xVel -= self.TOONXY_SPEED
        
        if self.arrowKeys.rightPressed():
            xVel += self.TOONXY_SPEED
        
        pos[0] += xVel * dt
        if pos[0] < -(self.MAX_TOONXY):
            pos[0] = -(self.MAX_TOONXY)
        
        if pos[0] > self.MAX_TOONXY:
            pos[0] = self.MAX_TOONXY
        
        yVel = 0.0
        if self.arrowKeys.upPressed():
            yVel -= self.TOONXY_SPEED
        
        if self.arrowKeys.downPressed():
            yVel += self.TOONXY_SPEED
        
        pos[1] += yVel * dt
        if pos[1] < -(self.MAX_TOONXY):
            pos[1] = -(self.MAX_TOONXY)
        
        if pos[1] > self.MAX_TOONXY:
            pos[1] = self.MAX_TOONXY
        
        toonPos.setX(pos[0])
        toonPos.setY(pos[1])
        self.getAvatar(self.localAvId).setPos(toonPos)
        self._DistributedRingGame__posBroadcast(dt)
        return Task.cont

    
    def exitSwim(self):
        self._DistributedRingGame__killUpdateLocalToonTask()
        self.arrowKeys.clearPressHandlers()
        self.arrowKeys.clearReleaseHandlers()
        self._DistributedRingGame__destroyRings()

    
    def enterFinish(self):
        self.notify.debug('enterFinish')
        self.gameOver()
        self.gameFSM.request('off')

    
    def exitFinish(self):
        pass

    
    def __spawnUpdateEnvironTask(self):
        task = Task.Task(self._DistributedRingGame__updateEnvironTask)
        taskMgr.spawnTaskNamed(task, self.UPDATE_ENVIRON_TASK)

    
    def __killUpdateEnvironTask(self):
        taskMgr.removeTasksNamed(self.UPDATE_ENVIRON_TASK)

    
    def __updateEnvironTask(self, task):
        t = globalClock.getFrameTime() - self._DistributedRingGame__timeBase
        distance = t * self.TOON_SWIM_VEL
        distance %= self.ENVIRON_LENGTH
        distance += self.ENVIRON_START_OFFSET
        self.environNode.setZ(-distance)
        return Task.cont

    
    def __spawnUpdateRingsTask(self):
        task = Task.Task(self._DistributedRingGame__updateRingsTask)
        taskMgr.spawnTaskNamed(task, self.UPDATE_RINGS_TASK)

    
    def __killUpdateRingsTask(self):
        taskMgr.removeTasksNamed(self.UPDATE_RINGS_TASK)

    
    def __updateRingsTask(self, task):
        t = globalClock.getFrameTime() - self._DistributedRingGame__ringTimeBase
        distance = t * self.TOON_SWIM_VEL
        distance -= self.ENVIRON_START_OFFSET
        self.ringNode.setZ(-distance)
        return Task.cont

    
    def setTimeBase(self, sec, usec):
        self._DistributedRingGame__timeBase = ClockDelta.serverTime2frameTimeDelta(sec, usec)

    
    def setRandomSeed(self, x, y, z):
        seed = [
            x,
            y,
            z]
        self.notify.debug('setRandomSeed: ' + str(seed))
        self._DistributedRingGame__randomNumGen = RandomNumGen.RandomNumGen(seed)

    
    def setRingTimeBase(self, sec, usec):
        self._DistributedRingGame__ringTimeBase = ClockDelta.serverTime2frameTimeDelta(sec, usec)
        self._DistributedRingGame__spawnUpdateRingsTask()

    
    def setAllToonsGotRings(self, flag):
        self.notify.debug('setAllToonsGotRings: ' + str(flag))


