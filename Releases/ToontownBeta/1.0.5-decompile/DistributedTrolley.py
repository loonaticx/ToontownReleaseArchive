# Source Generated with Decompyle++
# File: DistributedTrolley.pyo (Python 2.0)

from ShowBaseGlobal import *
from PandaObject import *
from ClockDelta import *
from IntervalGlobal import *
from TrolleyConstants import *
import ToontownGlobals
import DistributedObject
import DirectNotifyGlobal
import FSM
import State
import NodePath

class DistributedTrolley(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTrolley')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.localToonOnBoard = 0
        self.fsm = FSM.FSM('DistributedTrolley', [
            State.State('off', self.enterOff, self.exitOff, [
                'entering',
                'waitEmpty',
                'waitCountdown',
                'leaving']),
            State.State('entering', self.enterEntering, self.exitEntering, [
                'waitEmpty']),
            State.State('waitEmpty', self.enterWaitEmpty, self.exitWaitEmpty, [
                'waitCountdown']),
            State.State('waitCountdown', self.enterWaitCountdown, self.exitWaitCountdown, [
                'waitEmpty',
                'leaving']),
            State.State('leaving', self.enterLeaving, self.exitLeaving, [
                'entering'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.trolleyAwaySfx = base.loadSfx('phase_4/audio/sfx/SZ_trolley_away.mp3')
        self.trolleyBellSfx = base.loadSfx('phase_4/audio/sfx/SZ_trolley_bell.mp3')
        return None

    
    def generate(self):
        self.loader = self.cr.playGame.hood.loader
        self.trolleyStation = self.loader.geom.find('**/*trolley_station*')
        self.trolleyCar = self.trolleyStation.find('**/trolley_car')
        trolleyEnterStartPos = Point3(-20, 14, -1)
        trolleyEnterEndPos = Point3(15, 14, -1)
        trolleyEnterPosInterval = LerpPosInterval(self.trolleyCar, TROLLEY_ENTER_TIME, trolleyEnterEndPos, startPos = trolleyEnterStartPos, blendType = 'easeOut', name = 'TrolleyEnterPos')
        trolleyEnterTrack = Track([
            trolleyEnterPosInterval], 'trolleyEnter')
        trolleyEnterSoundTrack = Track([
            SoundInterval(self.trolleyAwaySfx)])
        self.trolleyEnterMultiTrack = MultiTrack([
            trolleyEnterTrack,
            trolleyEnterSoundTrack])
        trolleyExitStartPos = Point3(15, 14, -1)
        trolleyExitEndPos = Point3(50, 14, -1)
        trolleyExitPosInterval = LerpPosInterval(self.trolleyCar, TROLLEY_EXIT_TIME, trolleyExitEndPos, startPos = trolleyExitStartPos, blendType = 'easeIn', name = 'TrolleyExitPos')
        trolleyExitTrack = Track([
            trolleyExitPosInterval], 'trolleyExit')
        trolleyExitBellInterval = SoundInterval(self.trolleyBellSfx)
        trolleyExitAwayInterval = SoundInterval(self.trolleyAwaySfx)
        self.trolleyExitMultiTrack = MultiTrack([
            trolleyExitTrack,
            trolleyExitBellInterval,
            trolleyExitAwayInterval])
        return None

    
    def disable(self):
        DistributedObject.DistributedObject.disable(self)
        self.fsm.request('off')
        del self.loader
        del self.trolleyEnterMultiTrack
        del self.trolleyExitMultiTrack
        del self.trolleyStation
        del self.trolleyCar
        return None

    
    def delete(self):
        base.unloadSfx(self.trolleyAwaySfx)
        base.unloadSfx(self.trolleyBellSfx)
        DistributedObject.DistributedObject.delete(self)
        del self.fsm
        return None

    
    def setState(self, state, sec, usec):
        self.fsm.request(state, [
            localElapsedTime(sec, usec)])
        return None

    
    def handleEnterSphere(self, collEntry):
        self.notify.debug('Entering Trolley Sphere....')
        self.loader.place.detectedTrolleyCollision()
        if toonbase.localToon.hp > 0:
            toon = toonbase.localToon
            self.sendUpdate('requestBoard', [
                toon.getX(),
                toon.getY(),
                toon.getZ(),
                toon.getH(),
                toon.getP(),
                toon.getR()])
            return None
        

    
    def fillSlot0(self, avId, x, y, z, h, p, r, sec, usec):
        self.fillSlot(0, avId, x, y, z, h, p, r, sec, usec)

    
    def fillSlot1(self, avId, x, y, z, h, p, r, sec, usec):
        self.fillSlot(1, avId, x, y, z, h, p, r, sec, usec)

    
    def fillSlot2(self, avId, x, y, z, h, p, r, sec, usec):
        self.fillSlot(2, avId, x, y, z, h, p, r, sec, usec)

    
    def fillSlot3(self, avId, x, y, z, h, p, r, sec, usec):
        self.fillSlot(3, avId, x, y, z, h, p, r, sec, usec)

    
    def fillSlot(self, index, avId, x, y, z, h, p, r, sec, usec):
        if avId == 0:
            pass
        1
        if avId == toonbase.localToon.getDoId():
            self.loader.place.trolley.fsm.request('boarding', [
                self.trolleyCar])
            self.localToonOnBoard = 1
        
        if avId == toonbase.localToon.getDoId():
            self.loader.place.trolley.fsm.request('boarded')
        
        if self.cr.doId2do.has_key(avId):
            toon = self.cr.doId2do[avId]
            toon.wrtReparentTo(self.trolleyCar)
            track = Track([
                FunctionInterval(toon.animFSM.request, extraArgs = [
                    'run']),
                FunctionInterval(toon.headsUpPreserveScale, extraArgs = [
                    -5,
                    -4.5 + index * 3,
                    1.4]),
                LerpPosInterval(toon, TOON_BOARD_TIME * 0.75, Point3(-5, -4.5 + index * 3, 1.4)),
                LerpHprInterval(toon, TOON_BOARD_TIME * 0.25, Point3(90, 0, 0)),
                FunctionInterval(toon.animFSM.request, extraArgs = [
                    'neutral']),
                FunctionInterval((lambda self = self, toon = toon: self.ignore(toon.uniqueName('disable'))))])
            self.acceptOnce(toon.uniqueName('disable'), (lambda track = track: track.stop()))
            track.play()
        else:
            DistributedTrolley.notify.warning('toon: ' + str(avId) + " doesn't exist, and" + ' cannot board the trolley!')
        return None

    
    def emptySlot0(self, avId, sec, usec):
        self.emptySlot(0, avId, sec, usec)

    
    def emptySlot1(self, avId, sec, usec):
        self.emptySlot(1, avId, sec, usec)

    
    def emptySlot2(self, avId, sec, usec):
        self.emptySlot(2, avId, sec, usec)

    
    def emptySlot3(self, avId, sec, usec):
        self.emptySlot(3, avId, sec, usec)

    
    def notifyLocalToonOffTrolley(self, avId):
        if avId == toonbase.localToon.getDoId():
            self.loader.place.trolley.handleOffTrolley()
            self.localToonOnBoard = 0
        
        return None

    
    def emptySlot(self, index, avId, sec, usec):
        if avId == 0:
            pass
        1
        if self.cr.doId2do.has_key(avId):
            toon = self.cr.doId2do[avId]
            toon.wrtReparentTo(render)
            track = Track([
                FunctionInterval(toon.animFSM.request, extraArgs = [
                    'run']),
                LerpPosInterval(toon, TOON_EXIT_TIME, Point3(21 - index * 3, -2.5, 0.02), other = self.trolleyStation),
                FunctionInterval(toon.animFSM.request, extraArgs = [
                    'neutral']),
                FunctionInterval(self.notifyLocalToonOffTrolley, extraArgs = [
                    avId]),
                FunctionInterval((lambda self = self, toon = toon: self.ignore(toon.uniqueName('disable'))))])
            self.acceptOnce(toon.uniqueName('disable'), (lambda track = track: track.stop()))
            track.play()
            if avId == toonbase.localToon.getDoId():
                self.loader.place.trolley.fsm.request('exiting')
            
        else:
            DistributedTrolley.notify.warning('toon: ' + str(avId) + " doesn't exist, and" + ' cannot exit the trolley!')
        return None

    
    def rejectBoard(self, avId):
        self.loader.place.trolley.handleRejectBoard()
        return None

    
    def setMinigameZone(self, zoneId, minigameId):
        self.localToonOnBoard = 0
        messenger.send('playMinigame', [
            zoneId,
            minigameId])
        return None

    
    def enterOff(self):
        return None

    
    def exitOff(self):
        return None

    
    def enterEntering(self, ts):
        self.trolleyEnterMultiTrack.play(ts)
        return None

    
    def exitEntering(self):
        return None

    
    def enterWaitEmpty(self, ts):
        self.accept('entertrolley_sphere', self.handleEnterSphere)
        return None

    
    def exitWaitEmpty(self):
        self.ignore('entertrolley_sphere')
        return None

    
    def enterWaitCountdown(self, ts):
        self.accept('entertrolley_sphere', self.handleEnterSphere)
        self.accept('trolleyExitButton', self.handleExitButton)
        self.clockNode = TextNode()
        self.clockNode.setFont(ToontownGlobals.getSignFont())
        self.clockNode.setAlign(TMALIGNCENTER)
        self.clockNode.setTextColor(0.9, 0.1, 0.1, 1)
        self.clockNode.setText('10')
        self.clock = self.trolleyStation.attachNewNode(self.clockNode)
        self.clock.setBillboardAxis()
        self.clock.setPosHprScale(15.86, 13.82, 11.68, -0.0, 0.0, 0.0, 3.02, 3.02, 3.02)
        print ts
        if ts < TROLLEY_COUNTDOWN_TIME:
            self.countdown(TROLLEY_COUNTDOWN_TIME - ts)
        
        return None

    
    def timerTask(self, task):
        countdownTime = int(task.duration - task.time)
        timeStr = str(countdownTime)
        if self.clockNode.getText() != timeStr:
            self.clockNode.setText(timeStr)
        
        if task.time >= task.duration:
            return Task.done
        else:
            return Task.cont

    
    def countdown(self, duration):
        self.countdownTask = Task.Task(self.timerTask)
        self.countdownTask.duration = duration
        taskMgr.removeTasksNamed('trolleyTimerTask')
        return taskMgr.spawnTaskNamed(self.countdownTask, 'trolleyTimerTask')

    
    def handleExitButton(self):
        self.sendUpdate('requestExit')
        return None

    
    def exitWaitCountdown(self):
        self.ignore('entertrolley_sphere')
        self.ignore('trolleyExitButton')
        taskMgr.removeTasksNamed('trolleyTimerTask')
        self.clock.removeNode()
        del self.clock
        del self.clockNode
        return None

    
    def enterLeaving(self, ts):
        if self.localToonOnBoard:
            self.loader.place.trolley.fsm.request('trolleyLeaving')
        
        self.trolleyExitMultiTrack.play(ts)
        return None

    
    def exitLeaving(self):
        return None


