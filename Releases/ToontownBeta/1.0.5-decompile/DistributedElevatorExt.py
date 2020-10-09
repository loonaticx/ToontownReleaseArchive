# Source Generated with Decompyle++
# File: DistributedElevatorExt.pyo (Python 2.0)

from ShowBaseGlobal import *
from PandaObject import *
from ClockDelta import *
from IntervalGlobal import *
from ElevatorConstants import *
from ToontownGlobals import *
import DistributedObject
import DirectNotifyGlobal
import FSM
import State
import NodePath
import CollisionSphere
import CollisionNode

class DistributedElevatorExt(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedElevatorExt')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.localToonOnBoard = 0
        self.fsm = FSM.FSM('DistributedElevatorExt', [
            State.State('off', self.enterOff, self.exitOff, [
                'opening',
                'waitEmpty',
                'waitCountdown',
                'closing',
                'closed']),
            State.State('opening', self.enterOpening, self.exitOpening, [
                'waitEmpty']),
            State.State('waitEmpty', self.enterWaitEmpty, self.exitWaitEmpty, [
                'waitCountdown']),
            State.State('waitCountdown', self.enterWaitCountdown, self.exitWaitCountdown, [
                'waitEmpty',
                'closing']),
            State.State('closing', self.enterClosing, self.exitClosing, [
                'closed']),
            State.State('closed', self.enterClosed, self.exitClosed, [
                'opening'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.wantDoors = config.GetBool('want-doors', 0)
        return None

    
    def generate(self):
        self.elevatorNodePath = hidden.attachNewNode('elevatorNodePath')
        self.elevatorModel = loader.loadModelOnce('phase_5/models/modules/elevator')
        self.elevatorModel.reparentTo(self.elevatorNodePath)
        self.leftDoor = self.elevatorModel.find('**/left-door')
        self.rightDoor = self.elevatorModel.find('**/right-door')
        self.elevatorSphere = CollisionSphere.CollisionSphere(0, 6, 0, 5)
        self.elevatorSphere.setTangible(0)
        self.elevatorSphereNode = CollisionNode.CollisionNode()
        self.elevatorSphereNode.setIntoCollideMask(WallBitmask)
        self.elevatorSphereNode.addSolid(self.elevatorSphere)
        self.elevatorSphereNodePath = self.elevatorNodePath.attachNewNode(self.elevatorSphereNode)
        self.elevatorSphereNodePath.hide()
        self.elevatorSphereNodePath.setName(self.uniqueName('elevatorSphere'))
        self.elevatorSphereNodePath.reparentTo(self.elevatorNodePath)
        self.openPosRight = Point3(0, 0, 0)
        self.closedPosRight = Point3(-3.5, 0, 0)
        self.openPosLeft = Point3(0, 0, 0)
        self.closedPosLeft = Point3(3.5, 0, 0)
        leftOpenInterval = LerpPosInterval(self.leftDoor, ELEVATOR_OPEN_TIME, self.openPosLeft, startPos = self.closedPosLeft, blendType = 'easeOut', name = self.uniqueName('leftDoorOpen'))
        rightOpenInterval = LerpPosInterval(self.rightDoor, ELEVATOR_OPEN_TIME, self.openPosRight, startPos = self.closedPosRight, blendType = 'easeOut', name = self.uniqueName('rightDoorOpen'))
        self.openMultiTrack = MultiTrack([
            leftOpenInterval,
            rightOpenInterval])
        leftCloseInterval = LerpPosInterval(self.leftDoor, ELEVATOR_CLOSE_TIME, self.closedPosLeft, startPos = self.openPosLeft, blendType = 'easeOut', name = self.uniqueName('leftDoorClose'))
        rightCloseInterval = LerpPosInterval(self.rightDoor, ELEVATOR_CLOSE_TIME, self.closedPosRight, startPos = self.openPosRight, blendType = 'easeOut', name = self.uniqueName('rightDoorClose'))
        self.closeMultiTrack = MultiTrack([
            leftCloseInterval,
            rightCloseInterval])
        return None

    
    def disable(self):
        DistributedObject.DistributedObject.disable(self)
        self.fsm.request('off')
        return None

    
    def delete(self):
        del self.bldg
        self.elevatorNodePath.removeNode()
        del self.elevatorNodePath
        del self.openMultiTrack
        del self.closeMultiTrack
        del self.fsm
        DistributedObject.DistributedObject.delete(self)
        return None

    
    def setBldgDoId(self, bldgDoId):
        self.bldgDoId = bldgDoId
        self.bldg = self.cr.doId2do[bldgDoId]
        self.bossLevel = self.bldg.getBossLevel()
        doorOrigin = self.bldg.getSuitDoorOrigin()
        self.elevatorNodePath.reparentTo(doorOrigin)
        self.elevatorNodePath.setScale(render, Vec3(1, 1, 1))
        self.elevatorNodePath.setPosHpr(0, 0, 0, 0, 0, 0)
        return None

    
    def setFloor(self, floorNumber):
        return None

    
    def setState(self, state, sec, usec):
        self.fsm.request(state, [
            localElapsedTime(sec, usec)])
        return None

    
    def handleEnterSphere(self, collEntry):
        self.notify.debug('Entering Elevator Sphere....')
        self.cr.playGame.hood.loader.place.detectedElevatorCollision()
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
            self.cr.playGame.hood.loader.place.elevator.fsm.request('boarding', [
                self.elevatorNodePath])
            self.localToonOnBoard = 1
        
        if avId == toonbase.localToon.getDoId():
            self.cr.playGame.hood.loader.place.elevator.fsm.request('boarded')
        
        if self.cr.doId2do.has_key(avId):
            toon = self.cr.doId2do[avId]
            toon.wrtReparentTo(self.elevatorNodePath)
            ElevatorPoints = [
                [
                    -1.5,
                    5,
                    0],
                [
                    1.5,
                    5,
                    0],
                [
                    -2.5,
                    3,
                    0],
                [
                    2.5,
                    3,
                    0]]
            track = Track([
                FunctionInterval(toon.animFSM.request, extraArgs = [
                    'run']),
                FunctionInterval(toon.headsUpPreserveScale, extraArgs = ElevatorPoints[index]),
                LerpPosInterval(toon, TOON_BOARD_ELEVATOR_TIME * 0.75, apply(Point3, ElevatorPoints[index])),
                LerpHprInterval(toon, TOON_BOARD_ELEVATOR_TIME * 0.25, Point3(180, 0, 0)),
                FunctionInterval(toon.animFSM.request, extraArgs = [
                    'neutral']),
                FunctionInterval((lambda self = self, toon = toon: self.ignore(toon.uniqueName('disable'))))])
            self.acceptOnce(toon.uniqueName('disable'), (lambda track = track: track.stop()))
            track.play()
        else:
            self.notify.warning('toon: ' + str(avId) + " doesn't exist, and" + ' cannot board the elevator!')
        return None

    
    def emptySlot0(self, avId, sec, usec):
        self.emptySlot(0, avId, sec, usec)

    
    def emptySlot1(self, avId, sec, usec):
        self.emptySlot(1, avId, sec, usec)

    
    def emptySlot2(self, avId, sec, usec):
        self.emptySlot(2, avId, sec, usec)

    
    def emptySlot3(self, avId, sec, usec):
        self.emptySlot(3, avId, sec, usec)

    
    def notifyLocalToonOffElevator(self, avId):
        if avId == toonbase.localToon.getDoId():
            self.cr.playGame.hood.loader.place.elevator.handleOffElevator()
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
                LerpPosInterval(toon, TOON_EXIT_ELEVATOR_TIME, Point3(0, -5, 0), other = self.elevatorNodePath),
                FunctionInterval(toon.animFSM.request, extraArgs = [
                    'neutral']),
                FunctionInterval(self.notifyLocalToonOffElevator, extraArgs = [
                    avId]),
                FunctionInterval((lambda self = self, toon = toon: self.ignore(toon.uniqueName('disable'))))])
            self.acceptOnce(toon.uniqueName('disable'), (lambda track = track: track.stop()))
            track.play()
            if avId == toonbase.localToon.getDoId():
                messenger.send('exitElevator')
            
        else:
            self.notify.warning('toon: ' + str(avId) + " doesn't exist, and" + ' cannot exit the elevator!')
        return None

    
    def rejectBoard(self, avId):
        messenger.send('rejectBoard')
        return None

    
    def forceDoorsOpen(self):
        self.leftDoor.setPos(self.openPosLeft)
        self.rightDoor.setPos(self.openPosRight)

    
    def forceDoorsClosed(self):
        self.leftDoor.setPos(self.closedPosLeft)
        self.rightDoor.setPos(self.closedPosRight)

    
    def enterOff(self):
        return None

    
    def exitOff(self):
        return None

    
    def enterOpening(self, ts):
        self.openMultiTrack.play(ts)
        return None

    
    def exitOpening(self):
        return None

    
    def enterWaitEmpty(self, ts):
        self.forceDoorsOpen()
        if self.wantDoors:
            self.accept(self.uniqueName('enterelevatorSphere'), self.handleEnterSphere)
        
        return None

    
    def exitWaitEmpty(self):
        self.ignore(self.uniqueName('enterelevatorSphere'))
        return None

    
    def enterWaitCountdown(self, ts):
        self.forceDoorsOpen()
        self.accept('enterelevatorSphere', self.handleEnterSphere)
        self.accept('elevatorExitButton', self.handleExitButton)
        self.clockNode = TextNode()
        self.clockNode.setFont(getSignFont())
        self.clockNode.setAlign(TMALIGNCENTER)
        self.clockNode.setTextColor(0.5, 0.5, 0.5, 1)
        self.clockNode.setText('10')
        self.clock = self.elevatorNodePath.attachNewNode(self.clockNode)
        self.clock.setPosHprScale(0, 6.4, 6.0, 0, 0, 0, 2.0, 2.0, 2.0)
        print ts
        if ts < ELEVATOR_COUNTDOWN_TIME:
            self.countdown(ELEVATOR_COUNTDOWN_TIME - ts)
        
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
        taskMgr.removeTasksNamed('elevatorTimerTask')
        return taskMgr.spawnTaskNamed(self.countdownTask, 'elevatorTimerTask')

    
    def handleExitButton(self):
        self.sendUpdate('requestExit')
        return None

    
    def exitWaitCountdown(self):
        self.ignore('enterelevatorSphere')
        self.ignore('elevatorExitButton')
        taskMgr.removeTasksNamed('elevatorTimerTask')
        self.clock.removeNode()
        del self.clock
        del self.clockNode
        return None

    
    def enterClosing(self, ts):
        if self.localToonOnBoard:
            self.cr.playGame.hood.loader.place.elevator.fsm.request('elevatorClosing')
        
        self.closeMultiTrack.play(ts)
        return None

    
    def exitClosing(self):
        return None

    
    def enterClosed(self, ts):
        self.forceDoorsClosed()
        return None

    
    def exitClosed(self):
        return None


