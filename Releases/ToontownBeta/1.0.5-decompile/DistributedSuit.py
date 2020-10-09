# Source Generated with Decompyle++
# File: DistributedSuit.pyo (Python 2.0)

from ShowBaseGlobal import *
from IntervalGlobal import *
from ClockDelta import *
import DistributedAvatar
import Suit
import ToontownGlobals
import libdirectGlobals
import Point3
import math
import Vec3
import Vec2
import whrandom
import DistributedBattle
import FSM
import State
import SuitTimings
import SuitBase
import DistributedSuitPlanner
import AvatarDNA
import copy
import DirectNotifyGlobal
import SuitDialog
from DirectGeometry import CLAMP
import BattleProps
BATTLE_READY_RADIUS_EASY = 4.0
BATTLE_READY_RADIUS_MEDIUM = 8.0
BATTLE_READY_RADIUS_HARD = 16.0
BATTLE_IGNORE_TIME = 6
BATTLE_WAIT_TIME = 3
CATCHUP_SPEED_MULTIPLIER = 3
USE_INTERVALS = 1
ALLOW_BATTLE_DETECT = 1

class DistributedSuit(DistributedAvatar.DistributedAvatar, Suit.Suit, SuitBase.SuitBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSuit')
    ENABLE_PARTIAL_PATHS = 1
    ENABLE_EXPANDED_NAME = 0
    STREET_HEIGHT_OFFSET = -0.5
    SHADOW_HEIGHT_OFFSET = 0.025
    
    def __init__(self, cr):
        
        try:
            self.DistributedSuit_initialized
        except:
            self.DistributedSuit_initialized = 1
            DistributedAvatar.DistributedAvatar.__init__(self, cr)
            Suit.Suit.__init__(self)
            SuitBase.SuitBase.__init__(self)
            self.timeBehind = 0
            self.moveLerp = None
            self.startTime = [
                0,
                0]
            self.src = None
            self.dst = None
            self.resumePos = None
            self.cSphere = None
            self.cSphereNode = None
            self.cSphereNodePath = None
            self.cSphereBitMask = None
            self.bSphere = None
            self.bSphereNode = None
            self.bSphereNodePath = None
            self.bSphereBitMask = None
            self.cRay = None
            self.cRayNode = None
            self.cRayNodePath = None
            self.cRayBitMask = None
            self.lifter = None
            self.floorOffset = 0.0
            self.cTrav = None
            self.currMultiTrack = None
            self.requestedStateList = []
            self.trackResumeTime = 0
            self.sp = None
            self.prop = None
            self.initState = None
            self.finalState = None
            self.reparentTo(hidden)
            self.loop('neutral')
            self.pathBeginTime = None
            self.noMove = 0
            self.currEdge = 0
            self.prevEdgesTime = 0
            self.fsm = FSM.FSM('DistributedSuit', [
                State.State('Off', self.enterOff, self.exitOff, [
                    'FromSky',
                    'FromBuilding',
                    'Bellicose',
                    'Battle',
                    'ToToonBuilding',
                    'ToCogBuilding',
                    'ToSky',
                    'WalkToStreet']),
                State.State('FromSky', self.enterFromSky, self.exitFromSky, [
                    'Bellicose',
                    'Battle',
                    'ToSky',
                    'WaitForServer']),
                State.State('FromBuilding', self.enterFromBuilding, self.exitFromBuilding, [
                    'WalkToStreet',
                    'Bellicose',
                    'Battle',
                    'ToSky',
                    'WaitForServer']),
                State.State('WalkToStreet', self.enterWalkToStreet, self.exitWalkToStreet, [
                    'Bellicose',
                    'Battle',
                    'ToSky',
                    'ToToonBuilding',
                    'ToCogBuilding',
                    'WaitForServer',
                    'WalkFromStreet']),
                State.State('WalkFromStreet', self.enterWalkFromStreet, self.exitWalkFromStreet, [
                    'ToToonBuilding',
                    'ToCogBuilding',
                    'WaitForToToonBuilding',
                    'ToSky',
                    'WaitForServer']),
                State.State('Bellicose', self.enterBellicose, self.exitBellicose, [
                    'WaitForBattle',
                    'Battle',
                    'WalkFromStreet',
                    'ToSky',
                    'WaitForServer']),
                State.State('Battle', self.enterBattle, self.exitBattle, [
                    'Bellicose',
                    'ToToonBuilding',
                    'ToCogBuilding',
                    'ToSky']),
                State.State('WaitForBattle', self.enterWaitForBattle, self.exitWaitForBattle, [
                    'Battle',
                    'Bellicose',
                    'ToToonBuilding',
                    'ToCogBuilding',
                    'ToSky']),
                State.State('WaitForToToonBuilding', self.enterWaitForToToonBuilding, self.exitWaitForToToonBuilding, [
                    'ToToonBuilding',
                    'Battle',
                    'ToSky']),
                State.State('WaitForServer', self.enterWaitForServer, self.exitWaitForServer, [
                    'WalkFromStreet',
                    'Bellicose',
                    'WalkToStreet',
                    'FromToonBuilding',
                    'ToToonBuilding',
                    'FromBuilding',
                    'ToSky']),
                State.State('ToToonBuilding', self.enterToToonBuilding, self.exitToToonBuilding, []),
                State.State('ToCogBuilding', self.enterToCogBuilding, self.exitToCogBuilding, []),
                State.State('ToSky', self.enterToSky, self.exitToSky, [])], 'Off', 'Off')
            self.fsm.enterInitialState()

        self.ghost = None
        return None

    
    def generate(self):
        if self.notify.getDebug():
            self.notify.debug('DistributedSuit %d: generating' % self.getDoId())
        
        DistributedAvatar.DistributedAvatar.generate(self)
        self.loop('neutral')

    
    def disable(self):
        self.notify.debug('DistributedSuit %d: disabling' % self.getDoId())
        self.localSetState('Off')
        DistributedAvatar.DistributedAvatar.disable(self)
        self.ignoreAll()
        self._DistributedSuit__removeCollisionData()
        if self.ghost:
            self.ghost.reparentTo(hidden)
            self.ghost = None
        
        self.cleanupLoseActor()
        self.stop()
        self.clearOldMove()
        return None

    
    def delete(self):
        
        try:
            self.DistributedSuit_deleted
        except:
            self.DistributedSuit_deleted = 1
            self.notify.debug('DistributedSuit %d: deleting' % self.getDoId())
            del self.fsm
            del self.dna
            del self.sp
            DistributedAvatar.DistributedAvatar.delete(self)
            Suit.Suit.delete(self)
            SuitBase.SuitBase.delete(self)

        return None

    
    def __removeCollisionData(self):
        self.enableRaycast(enable = 0)
        self.cSphere = None
        self.cSphereNodePath = None
        self.cSphereNode = None
        self.bSphere = None
        self.bSphereNode = None
        self.bSphereNodePath = None
        self.cRay = None
        self.cRayNode = None
        self.cRayNodePath = None
        self.lifter = None
        self.floorOffset = None
        self.cTrav = None

    
    def setDNAString(self, dnaString):
        if not (self.dna):
            if self.notify.getDebug():
                self.notify.debug('setting dna string for %d...' % self.getDoId())
            
            self.dna = AvatarDNA.AvatarDNA()
            self.dna.makeFromNetString(dnaString)
            self.setDNA(self.dna)
        
        return None

    
    def setLevelDist(self, level):
        if self.notify.getDebug():
            self.notify.debug('Got level %d from server for suit %d' % (level, self.getDoId()))
        
        self.setLevel(level)

    
    def setPositionInfo(self, posStr):
        if not (self.ENABLE_POSITION_UPDATES) and self.fsm.getCurrentState().getName() == 'Off' or self.fsm.getCurrentState().getName() == 'Battle':
            return None
        
        positionInfo = eval(posStr)
        
        try:
            myId = self.getDoId()
        except:
            myId = -1

        dist = Vec2.Vec2(self.getPos()[0] - float(positionInfo[1]), self.getPos()[1] - float(positionInfo[2]))
        l = dist.length()
        self.notify.debug('SUIT ' + str(myId) + ' IS OUT OF POSITION BY ' + str(l) + ' (' + self.fsm.getCurrentState().getName() + ') !!!!!')
        if not (self.ghost):
            self.ghost = loader.loadModelOnce('models/directmodels/smiley')
            self.ghost.reparentTo(render)
        
        serverPos = Vec3.Vec3(float(positionInfo[1]), float(positionInfo[2]), float(positionInfo[3]) + 8)
        self.ghost.setPos(serverPos)

    
    def setCurrentHpr(self):
        if self.currPoint():
            if self.prevPoint():
                self.setHpr(self.calculateNewHpr(self.prevPointPos(), self.currPointPos()), 0.0, 0.0)
            else:
                self.setHpr(self.calculateNewHpr(self.getPos(), self.currPointPos()), 0.0, 0.0)
        else:
            self.setHpr(self.calculateNewHpr(self.prevPointPos(), self.getPos()), 0.0, 0.0)

    
    def calculateNewHpr(self, currPos, currDst):
        xDiff = currDst[0] - currPos[0]
        yDiff = currDst[1] - currPos[1]
        if xDiff > 0 and yDiff == 0:
            return -90
        elif xDiff < 0 and yDiff == 0:
            return 90
        elif yDiff > 0 and xDiff == 0:
            return 0
        elif yDiff < 0 and xDiff == 0:
            return 180
        else:
            angle = math.atan2(currDst[1] - currPos[1], currDst[0] - currPos[0])
            return rad2Deg(angle) - 90

    
    def calculateNewHprByEdge(self, prevEdge, currEdge):
        returnVal = rad2Deg(math.acos(CLAMP(prevEdge.dot(currEdge), -1, 1)))
        return returnVal

    
    def adjustMoveTime(self, time):
        bestTime = time / CATCHUP_SPEED_MULTIPLIER
        if self.timeBehind > bestTime:
            self.timeBehind = self.timeBehind - time - bestTime
            moveTime = bestTime
        else:
            time = time - self.timeBehind
            self.timeBehind = 0
        return time

    
    def updateMoveTime(self, currPos, currDst):
        moveDist = Vec2.Vec2(currDst[0] - currPos[0], currDst[1] - currPos[1]).length()
        moveTime = moveDist / self.sp.suitWalkSpeed
        return self.adjustMoveTime(moveTime)

    
    def updateMoveTimeByIdx(self, currPosIdx, currDstIdx):
        moveTime = self.sp.dnaStore.getSuitEdgeTravelTime(currPosIdx, currDstIdx, self.sp.suitWalkSpeed)
        return moveTime

    
    def beginMove(self, doneEvent = None, destination = None, source = None, anim = 'walk', time = -1):
        if source:
            currPos = Point3.Point3(source)
        elif self.virtualPos:
            currPos = self.virtualPos
        else:
            currPos = self.prevPointPos()
        if destination:
            currDst = Point3.Point3(destination)
        else:
            currDst = self.currPointPos()
        if anim != 'fly':
            currPos.setZ(self.STREET_HEIGHT_OFFSET)
            currDst.setZ(self.STREET_HEIGHT_OFFSET)
        
        if time == -1:
            moveTime = self.updateMoveTimeByIdx(self.myPath.getPointIndex(self.prevWpt), self.myPath.getPointIndex(self.currWpt))
        else:
            moveTime = time
        if doneEvent:
            intervalName = doneEvent
        else:
            intervalName = self.taskName('DistSuitIval' + str(self.currWpt))
        returnIntervals = []
        if source:
            beginPos = currPos
        else:
            beginPos = None
        if anim != 'fly':
            returnIntervals.append(FunctionInterval(self.setCurrentHpr))
        
        returnIntervals.append(LerpPosInterval(self, moveTime, currDst, startPos = beginPos, name = intervalName))
        return returnIntervals

    
    def resumeTrack(self, timeScale = 1.0):
        if not (self.currMultiTrack):
            return None
        
        if self.trackResumeTime <= self.currMultiTrack.getDuration():
            if self.trackResumeTime < 0:
                self.trackResumeTime = 0
            
            self.currMultiTrack.play(self.trackResumeTime, scale = timeScale)
            if self.notify.getDebug():
                self.notify.debug('resuming move with duration of: ' + str(self.currMultiTrack.getDuration()) + 'resume time of: ' + str(self.trackResumeTime) + 'time scale of: ' + str(timeScale))
            
        elif self.notify.getDebug():
            self.notify.debug('Not moving, resume time is > than duration' + str(self.trackResumeTime) + ' ' + str(self.currMultiTrack.getDuration()))
        
        self.localSetState('Off')
        self.noMove = 1
        return None

    
    def setMoveTask(self, sourceIndex, destIndex, sec, usec):
        if self.sp == None:
            return None
        
        debug = self.notify.getDebug()
        if not (self.ENABLE_PARTIAL_PATHS) and self.currMultiTrack and self.startTime == [
            sec,
            usec] and self.myPath and self.myPath.getNumPoints() > 0 and self.myPath.getPointIndex(0) == sourceIndex and self.myPath.getPointIndex(self.myPath.getNumPoints() - 1) == destIndex:
            if debug:
                self.notify.debug('receiving move task a second time, ' + 'using previous')
            
            for currTask in self.currMultiTrack.tlist[0].ilist:
                if isinstance(currTask[0], EventInterval):
                    self.accept(currTask[0].name, self.assignmentIntervalDone)
                
            
            self.trackResumeTime = localElapsedTime(self.startTime[0], self.startTime[1])
            self.resumeTrack()
            return None
        
        self.clearOldMove()
        self.src = self.sp.pointIndexes[sourceIndex]
        self.dst = self.sp.pointIndexes[destIndex]
        self.startTime = [
            sec,
            usec]
        if debug:
            self.notify.debug('...setting move task with ' + str(sourceIndex) + ' and ' + str(destIndex) + ' and ' + str(self.startTime[0]) + ' and ' + str(self.startTime[1]))
            self.notify.debug('source: ' + str(self.src.getPos()[0]) + ' ' + str(self.src.getPos()[1]) + ' ' + str(self.src.getPos()[2]))
            self.notify.debug('dest: ' + str(self.dst.getPos()[0]) + ' ' + str(self.dst.getPos()[1]) + ' ' + str(self.dst.getPos()[2]))
        
        srcAndDst = [
            self.src,
            self.dst]
        path = self.sp.genPath(srcAndDst)
        if path.getNumPoints() <= 0:
            self.notify.debug('No path generated!  Assignment not used')
        
        self.setPath(path)
        self.setCurrPt(1)
        initialPos = srcAndDst[0].getPos()
        initialPos.setZ(self.STREET_HEIGHT_OFFSET)
        self.setPos(initialPos)
        self.dropShadows[0].setPos(Point3.Point3(0, 0, self.SHADOW_HEIGHT_OFFSET))
        if not (self.currMultiTrack) and not (self.ENABLE_PARTIAL_PATHS):
            self.currMultiTrack = self.genExtendedPath()
            self.trackResumeTime = localElapsedTime(self.startTime[0], self.startTime[1])
            if debug:
                self.notify.debug('times: ' + str(globalClock.getFrameTime()) + ' ' + str(self.startTime) + ' ' + str(self.trackResumeTime))
                totalTime = self.currMultiTrack.tlist[0]._Track__computeDuration()
                self.notify.debug('Waypoint List Time: ' + str(totalTime))
            
            self.pathBeginTime = None
            self.resumeTrack()
            self.currWptTime = 0
        elif not (self.currMultiTrack) and self.ENABLE_PARTIAL_PATHS:
            self.currMultiTrack = self.genPartialExtendedPath(play = 0)
            if debug:
                self.notify.debug('times: ' + str(globalClock.getFrameTime()) + ' ' + str(self.startTime) + ' ' + str(self.trackResumeTime))
                totalTime = self.currMultiTrack.tlist[0]._Track__computeDuration()
                self.notify.debug('Waypoint List Time: ' + str(totalTime))
            
            self.pathBeginTime = None
            self.resumeTrack()
            self.currWptTime = 0
        
        return None

    
    def beginBuildingMove(self, moveIn, doneEvent, suit = 0):
        doorPt = Point3.Point3(0)
        buildingPt = Point3.Point3(0)
        streetPt = Point3.Point3(0)
        if self.virtualPos:
            doorPt.assign(self.virtualPos)
        else:
            doorPt.assign(self.getPos())
        if moveIn:
            streetPt = self.prevPointPos()
        else:
            streetPt = self.currPointPos()
        dx = doorPt[0] - streetPt[0]
        dy = doorPt[1] - streetPt[1]
        buildingPt = Point3.Point3(doorPt[0] + dx, doorPt[1] + dy, doorPt[2])
        if moveIn:
            if suit:
                moveTime = SuitTimings.toSuitBuilding
            else:
                moveTime = SuitTimings.toToonBuilding
            return self.beginMove(doneEvent, buildingPt, time = moveTime)
        else:
            return self.beginMove(doneEvent, doorPt, buildingPt, time = SuitTimings.fromBuilding)
        return None

    
    def attachPropeller(self):
        if self.prop == None:
            self.prop = BattleProps.globalPropPool.getProp('propeller')
        
        head = self.find('**/joint-head')
        self.prop.reparentTo(head)

    
    def detachPropeller(self):
        if self.prop:
            self.prop.reparentTo(hidden)
            self.prop = None
        

    
    def beginSupaFlyMove(self, moveIn, doneEvent = None):
        currPt = Point3.Point3(0)
        skyPt = Point3.Point3(0)
        if self.virtualPos:
            currPt.assign(self.virtualPos)
            skyPt.assign(self.virtualPos)
        else:
            currPt.assign(self.getPos())
            skyPt.assign(self.getPos())
        if moveIn:
            skyPt.setZ(currPt.getZ() + SuitTimings.fromSky * self.sp.suitWalkSpeed)
        else:
            skyPt.setZ(currPt.getZ() + SuitTimings.toSky * self.sp.suitWalkSpeed)
        groundF = 28
        dur = self.getDuration('landing')
        fr = self.getFrameRate('landing')
        animTimeInAir = groundF / fr
        impactLength = dur - animTimeInAir
        timeTillLanding = SuitTimings.fromSky - impactLength
        waitTime = timeTillLanding - animTimeInAir
        if self.prop == None:
            self.prop = BattleProps.globalPropPool.getProp('propeller')
        
        propDur = self.prop.getDuration('propeller')
        lastSpinFrame = 8
        fr = self.prop.getFrameRate('propeller')
        spinTime = lastSpinFrame / fr
        openTime = (lastSpinFrame + 1) / fr
        if moveIn:
            shadowFuncInt1 = FunctionInterval(self.dropShadows[0].wrtReparentTo, extraArgs = [
                render])
            lerpIntList = self.beginMove(doneEvent, currPt, skyPt, anim = 'fly', time = timeTillLanding)
            lerpWaitInt = WaitInterval(impactLength)
            shadowScaleInt = LerpScaleInterval(self.dropShadows[0], timeTillLanding, self.dropShadows[0].getScale(render), startScale = Point3.Point3(0.01, 0.01, 0.01))
            shadowFuncInt2 = FunctionInterval(self.dropShadows[0].wrtReparentTo, extraArgs = [
                self.getGeomNode()])
            shadowFuncInt3 = FunctionInterval(self.dropShadows[0].setPos, extraArgs = [
                Point3.Point3(0, 0, self.SHADOW_HEIGHT_OFFSET)])
            funcIntPose = FunctionInterval(self.pose, extraArgs = [
                'landing',
                0])
            waitInt = WaitInterval(waitTime)
            actInt = ActorInterval(self, 'landing', loop = 0, duration = dur)
            funcIntWalk = FunctionInterval(self.loop, extraArgs = [
                'walk'])
            funcIntProp1 = FunctionInterval(self.attachPropeller)
            actIntProp1 = ActorInterval(self.prop, 'propeller', loop = 0, duration = waitTime + spinTime, startTime = 0.0, endTime = spinTime)
            actIntProp2 = ActorInterval(self.prop, 'propeller', loop = 0, duration = propDur - openTime, startTime = openTime)
            funcIntProp2 = FunctionInterval(self.detachPropeller)
            return ([
                shadowFuncInt1] + lerpIntList + [
                lerpWaitInt], [
                shadowScaleInt,
                shadowFuncInt2,
                shadowFuncInt3], [
                funcIntPose,
                waitInt,
                actInt,
                funcIntWalk], [
                funcIntProp1,
                actIntProp1,
                actIntProp2,
                funcIntProp2])
        else:
            shadowFuncInt1 = FunctionInterval(self.dropShadows[0].wrtReparentTo, extraArgs = [
                render])
            lerpWaitInt = WaitInterval(impactLength)
            lerpIntList = self.beginMove(doneEvent, skyPt, None, anim = 'fly', time = timeTillLanding)
            lerpWaitInt2 = WaitInterval(impactLength)
            shadowScaleInt = LerpScaleInterval(self.dropShadows[0], timeTillLanding, Point3.Point3(0.01, 0.01, 0.01), startScale = self.dropShadows[0].getScale(self))
            shadowFuncInt2 = FunctionInterval(self.dropShadows[0].reparentTo, extraArgs = [
                self.getGeomNode()])
            shadowFuncInt3 = FunctionInterval(self.dropShadows[0].setPos, extraArgs = [
                Point3.Point3(0, 0, self.SHADOW_HEIGHT_OFFSET)])
            actInt = ActorInterval(self, 'landing', loop = 0, startTime = dur, endTime = 0.0)
            funcIntProp1 = FunctionInterval(self.attachPropeller)
            actIntProp1 = ActorInterval(self.prop, 'propeller', loop = 0, endTime = openTime, startTime = propDur)
            actIntProp2 = ActorInterval(self.prop, 'propeller', loop = 0, duration = propDur - openTime, startTime = spinTime, endTime = 0.0)
            funcIntProp2 = FunctionInterval(self.detachPropeller)
            return ([
                shadowFuncInt1,
                lerpWaitInt] + lerpIntList, [
                lerpWaitInt2,
                shadowScaleInt,
                shadowFuncInt2,
                shadowFuncInt3], [
                actInt], [
                funcIntProp1,
                actIntProp1,
                actIntProp2,
                funcIntProp2])
        return None

    
    def enableBattleDetect(self, task = None):
        if not ALLOW_BATTLE_DETECT:
            self.notify.debug('not allowing battle detection')
            return Task.done
        
        if self.notify.getDebug():
            self.notify.debug('Setting up collision info for ' + str(self.getDoId()))
        
        if self.bSphereNodePath and self.bSphereNode:
            self.bSphereNodePath.reparentTo(self)
            self.accept('enter' + self.bSphereNode.getName(), self._DistributedSuit__handleToonCollision)
        elif self.notify.getDebug():
            self.notify.debug('DistributedSuit: entering bellicose but ' + 'collision info not initialized')
        
        return Task.done

    
    def disableBattleDetect(self):
        if hasattr(self, 'doId'):
            myDoId = self.getDoId()
        else:
            myDoId = -1
        if self.notify.getDebug():
            self.notify.debug('Removing collision info for ' + str(myDoId))
        
        if self.bSphereNode:
            self.ignore('enter' + self.bSphereNode.getName())
        
        if self.bSphereNodePath:
            self.bSphereNodePath.reparentTo(hidden)
        

    
    def enableRaycast(self, enable = 1):
        if not (self.cTrav) and not hasattr(self, 'cRayNode') or not (self.cRayNode):
            return None
        
        self.cTrav.removeCollider(self.cRayNode)
        if enable:
            if self.notify.getDebug():
                self.notify.debug('enabling raycast')
            
            self.cTrav.addCollider(self.cRayNode, self.lifter)
        elif self.notify.getDebug():
            self.notify.debug('disabling raycast')
        
        return None

    
    def suitEnterZone(self, newZone):
        if isinstance(newZone, CollisionEntry):
            newZoneId = int(newZone.getIntoNode().getName())
        else:
            newZoneId = newZone
        if self.notify.getDebug():
            self.notify.debug('suit ' + str(self.getDoId()) + ' is in zone ' + str(newZoneId))
        

    
    def waitForBattleDone(self, task):
        if self.notify.getDebug():
            self.notify.debug('battle is done...moving on')
        
        self.timeBehind = self.updateMoveTime(self.getPos(), self.currPointPos())
        self.localSetState('Bellicose')
        self.moveInterrupted = 0
        return Task.done

    
    def fromSky(self, doneEvent):
        pass

    
    def fromBuilding(self, doneEvent):
        self.loop('walk', 0)
        enable = 1
        self.enableRaycast(enable)

    
    def walkToStreet(self, doneEvent):
        self.loop('walk', 0)
        enable = 1
        self.enableRaycast(enable)

    
    def wptCheck(self):
        if not (self.myPath):
            return 1
        
        if self.calcNextWpt() >= self.myPath.getNumPoints():
            self.sendDoneEvent()
            return 1
        
        if self.atCurrWpt():
            ptMovingTo = self.nextPoint()
        else:
            ptMovingTo = self.currPoint()
        if ptMovingTo.getPointType() == DNASuitPoint.FRONTDOORPOINT or ptMovingTo.getPointType() == DNASuitPoint.SIDEDOORPOINT:
            if self.notify.getDebug():
                self.notify.debug('moving to a front door' + str(ptMovingTo.getIndex()))
            
            currState = self.fsm.getCurrentState().getName()
            if not (currState == 'WalkFromStreet'):
                if self.notify.getDebug():
                    self.notify.debug('time to walk from street')
                
                self.sendDoneEvent()
                return 1
            
        
        return 0

    
    def createWptInfo(self, moveIn, state, wptInfos):
        animIntervals = []
        lerpIntervals = []
        scaleShadowIntervals = []
        propAnimIntervals = []
        if state[0] != 'T' and state[0] != 'F':
            lerpIntervals = self.moveToNextWpt()
            incWpt = 1
            if self.currWpt == 1 and self.initState == 'FromBuilding':
                lerpIntervals.append(FunctionInterval(self.enableRaycast, extraArgs = [
                    0]))
            elif self.currWpt == self.myPath.getNumPoints() - 2 and self.finalState == 'ToToonBuilding' or self.finalState == 'ToCogBuilding':
                lerpIntervals.append(FunctionInterval(self.enableRaycast, extraArgs = [
                    1]))
            
        elif state == 'FromSky':
            taskName = self.taskName('iName' + str(self.currWpt - 1))
            (lerpIntervals, scaleShadowIntervals, animIntervals, propAnimIntervals) = self.beginSupaFlyMove(moveIn, taskName)
            incWpt = 0
        elif state == 'FromBuilding':
            taskName = self.taskName('iName' + str(self.currWpt - 1))
            lerpIntervals = self.beginBuildingMove(moveIn, taskName)
            incWpt = 0
        elif state == 'ToToonBuilding' or state == 'ToCogBuilding':
            taskName = self.taskName('iName' + str(self.currWpt))
            lerpIntervals = self.beginBuildingMove(moveIn, taskName, state == 'ToCogBuilding')
            incWpt = 0
        
        if len(lerpIntervals) > 0:
            wptDoneInterval = FunctionInterval(self.assignmentIntervalDone, extraArgs = [
                incWpt,
                self.currWpt,
                self.prevWpt])
            lerpIntervals = lerpIntervals + [
                wptDoneInterval]
        
        wptInfosLen = len(wptInfos)
        if wptInfosLen > 0:
            wptInfos[0] = wptInfos[0] + lerpIntervals
        else:
            wptInfos.append(lerpIntervals)
            if len(scaleShadowIntervals) > 0:
                wptInfos.append(scaleShadowIntervals)
                wptInfos.append(animIntervals)
                wptInfos.append(propAnimIntervals)
            

    
    def collectWptInfo(self, wptInfos):
        tracks = []
        tracks.append(Track(wptInfos[0], self.taskName('lerpTrack')))
        if len(wptInfos) > 1:
            tracks.append(Track(wptInfos[1], self.taskName('shadowLerpTrack')))
        
        if len(wptInfos) > 2:
            tracks.append(Track(wptInfos[2], self.taskName('shadowScaleTrack')))
        
        if len(wptInfos) > 3:
            tracks.append(Track(wptInfos[3], self.taskName('animTrack')))
        
        if len(wptInfos) > 4:
            tracks.append(Track(wptInfos[4], self.taskName('propAnimTrack')))
        
        mtrack = MultiTrack(tracks, self.taskName('myMultiTrack'))
        return mtrack

    
    def handleBellicoseWpt(self, doneEvent):
        if not self.wptCheck():
            self.moveToNextWpt(doneEvent)
        
        return None

    
    def walkFromStreet(self, doneEvent):
        self.loop('walk', 0)

    
    def toSky(self, doneEvent):
        self.virtualPos = None
        moveIn = 0
        intervalList = []
        (lerpIntervals, scaleShadowIntervals, animIntervals, propAnimIntervals) = self.beginSupaFlyMove(moveIn, doneEvent)
        if len(lerpIntervals) > 0:
            for currLerpInt in lerpIntervals:
                intervalList.append(currLerpInt)
            
            intervalList.append(EventInterval(self.taskName('toSky-done-event'), sentArgs = [
                0,
                self.currWpt,
                self.prevWpt]))
            self.accept(doneEvent, self.assignmentIntervalDone)
        
        tracks = []
        tracks.append(Track(intervalList, self.taskName('lerpTrack')))
        tracks.append(Track(scaleShadowIntervals, self.taskName('shadowScaleTrack')))
        tracks.append(Track(animIntervals, self.taskName('animTrack')))
        tracks.append(Track(propAnimIntervals, self.taskName('propAnimTrack')))
        if self.currMultiTrack:
            self.currMultiTrack.stop()
        
        self.currMultiTrack = MultiTrack(tracks, self.taskName('myMultiTrack'))
        self.trackResumeTime = 0
        self.resumeTrack()
        self.loop('neutral', 0)

    
    def toBuilding(self, state):
        moveIn = 1
        wptInfos = []
        currWpt = self.currPoint()
        if currWpt:
            self.virtualPos = currWpt.getPos()
        else:
            self.virtualPos = self.prevPointPos()
            self.setCurrPt(self.currWpt - 1)
        self.createWptInfo(moveIn, state, wptInfos)
        tracks = []
        tracks.append(Track(wptInfos[0], self.taskName('exitTrack')))
        if self.currMultiTrack:
            self.currMultiTrack.stop()
        
        self.currMultiTrack = MultiTrack(tracks, self.taskName('exitMultiTrack'))
        self.trackResumeTime = 0
        self.resumeTrack()
        self.loop('walk', 0)

    
    def toToonBuilding(self, doneEvent):
        self.toBuilding('ToToonBuilding')

    
    def toCogBuilding(self, doneEvent):
        self.toBuilding('ToCogBuilding')

    
    def b_setBrushOff(self, index):
        self.setBrushOff(index)
        self.d_setBrushOff(index)
        return None

    
    def d_setBrushOff(self, index):
        self.sendUpdate('setBrushOff', [
            index])

    
    def setBrushOff(self, index):
        self.setChatAbsolute(SuitDialog.getBrushOffText(self.getStyleName(), index), CFSpeech | CFTimeout)

    
    def localSetState(self, state):
        if self.virtualPos:
            return 1
        
        debug = self.notify.getDebug()
        if self.fsm.getCurrentState().getName() == state:
            if debug:
                self.notify.debug('State change ignored, already in ' + 'state' + str(state))
            
            return 0
        
        if debug:
            self.notify.debug('DistributedSuit: entering state: %s from %s' % (state, self.fsm.getCurrentState().getName()))
        
        return self.fsm.request(state)

    
    def setState(self, state):
        if not (self.myPath):
            self.notify.debug('DistributedSuit.setState:  no path, not ' + 'setting state')
            return None
        
        if self.myPath.getNumPoints() <= 0:
            self.notify.debug('State request ignored, suit has no assignment')
            return None
        
        if self.notify.getDebug():
            self.notify.debug(str(self.getDoId()) + ': received state request %s from server' % state)
        
        result = self.localSetState(state)
        if not result:
            if self.notify.getDebug():
                self.notify.debug('state transition (from %s to %s) rejected' % (self.fsm.getCurrentState().getName(), state))
            
        
        return result

    
    def setSPDoId(self, doId):
        self.sp = toonbase.localToon.cr.doId2do.get(doId, None)
        if self.sp == None:
            self.notify.debug('Uh oh...no suit planner found!')
        

    
    def enterCogBuilding(self):
        return None

    
    def flyAway(self):
        return None

    
    def initializeBodyCollisions(self, collIdStr):
        self.cSphere = CollisionSphere(0.0, 0.0, 0.0, 1.0)
        self.cSphereNode = CollisionNode(self.taskName('barrierSphere'))
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.attachNewNode(self.cSphereNode)
        self.cSphereNodePath.hide()
        self.cSphereBitMask = ToontownGlobals.WallBitmask
        self.cSphereNode.setCollideMask(self.cSphereBitMask)
        self.cSphere.setTangible(1)
        self.bSphere = CollisionSphere(0.0, 0.0, 0.0, BATTLE_READY_RADIUS_EASY)
        self.bSphereNode = CollisionNode(self.taskName('bSphere'))
        self.bSphereNode.addSolid(self.bSphere)
        self.bSphereNodePath = self.attachNewNode(self.bSphereNode)
        self.bSphereNodePath.reparentTo(hidden)
        self.bSphereNodePath.hide()
        self.bSphereBitMask = ToontownGlobals.WallBitmask
        self.bSphereNode.setCollideMask(self.bSphereBitMask)
        self.bSphere.setTangible(0)
        self.cRay = CollisionRay(0.0, 0.0, 6.0, 0.0, 0.0, -1.0)
        self.cRayNode = CollisionNode(self.taskName('cRay'))
        self.cRayNode.addSolid(self.cRay)
        self.cRayNodePath = self.attachNewNode(self.cRayNode)
        self.cRayNodePath.hide()
        self.cRayBitMask = ToontownGlobals.FloorBitmask
        self.cRayNode.setFromCollideMask(self.cRayBitMask)
        self.cRayNode.setIntoCollideMask(BitMask32.allOff())
        self.lifter = CollisionHandlerFloor()
        self.floorOffset = 0.1
        self.lifter.setOffset(self.floorOffset)
        self.lifter.setMaxVelocity(8.0)
        self.lifter.addCollider(self.cRayNode, self.arc())
        self.cTrav = toonbase.localToon.cTrav
        return None

    
    def disableBodyCollisions(self):
        self.enableRaycast(enable = 0)
        if self.cRayNodePath:
            self.cRayNodePath.removeNode()
        
        del self.cRayNode
        del self.cRay
        if self.bSphereNodePath:
            self.bSphereNodePath.removeNode()
        
        del self.bSphereNode
        del self.bSphere
        if self.cSphereNodePath:
            self.cSphereNodePath.removeNode()
        
        del self.cSphereNode
        del self.cSphere
        del self.lifter

    
    def d_requestBattle(self, toonId, pos, hpr):
        self.cr.playGame.hood.loader.place.setState('WaitForBattle')
        self.sendUpdate('requestBattle', [
            toonId,
            pos[0],
            pos[1],
            pos[2],
            hpr[0],
            hpr[1],
            hpr[2]])
        return None

    
    def denyBattle(self):
        self.notify.debug('denyBattle()')
        self.cr.playGame.hood.loader.place.setState('walk')

    
    def __handleToonCollision(self, collEntry):
        toonId = toonbase.localToon.getDoId()
        self.notify.debug('Distributed suit: requesting a Battle with ' + 'toon: %d' % toonId)
        self.d_requestBattle(toonId, self.getPos(), self.getHpr())
        self.localSetState('WaitForBattle')
        return None

    
    def waitForServer(self):
        self.notify.debug('waitForServer: Stopping track...')
        self.trackResumeTime = self.currMultiTrack.stop()
        self.loop('neutral')
        SuitBase.SuitBase.pauseMove(self)
        self.currTaskName = self.taskName('waitForServerDone')
        taskMgr.doMethodLater(8, self._DistributedSuit__handleWaitForServerDone, self.currTaskName)
        return None

    
    def clearFutureStateList(self):
        self.requestedStateList = None

    
    def clearOldMove(self):
        self.timeBehind = 0
        self.moveInterrupted = 0
        self.currEdge = 0
        self.prevEdgesTime = 0
        self.initState = None
        self.finalState = None
        if self.currMultiTrack:
            if self.pathBeginTime:
                self.notify.debug('TIME SINCE PATH WAS BEGUN: ' + str(globalClock.getRealTime() - self.pathBeginTime))
            
            self.currMultiTrack.stop()
            self.currMultiTrack = None
        
        self.pauseMove()

    
    def pauseMove(self):
        if self.moveLerp:
            self.moveLerp.uponDeath = None
            taskMgr.removeTask(self.moveLerp)
            taskMgr.removeTasksNamed(self.taskName('moveTaskName'))
            self.moveLerp = None
        
        if self.currMultiTrack:
            self.notify.debug('clearOldMove: Stopping track...')
            self.trackResumeTime = self.currMultiTrack.stop()
            if self.pathBeginTime:
                self.notify.debug('TIME SINCE PATH WAS BEGUN: ' + str(globalClock.getRealTime() - self.pathBeginTime))
            
            self.detachPropeller()
        
        self.clearFutureStateList()
        SuitBase.SuitBase.pauseMove(self)
        return None

    
    def bellicoseIntervalDone(self):
        if self.notify.getDebug():
            self.notify.debug('bellicose interval done...')
        
        if self.wptCheck():
            self.notify.debug('...end of bellicose')
        else:
            self.setCurrPt(self.calcNextWpt())
        return Task.done

    
    def assignmentIntervalDone(self, incrementWpt, currWpt, prevWpt):
        if self.notify.getDebug():
            self.notify.debug('assignment interval done...')
        
        if self.wptCheck():
            self.notify.debug('...end of assignment')
        elif incrementWpt:
            self.setCurrPt(currWpt)
            self.setCurrPt(self.calcNextWpt())
        
        if self.notify.getDebug():
            idx1 = self.myPath.getPointIndex(self.prevWpt)
            if self.calcNextWpt() >= self.myPath.getNumPoints():
                self.notify.debug('abruptly reached end of assignment')
                self.sendDoneEvent()
                return None
            
            idx2 = self.myPath.getPointIndex(self.currWpt)
            newEdgeZoneName = self.sp.dnaStore.getSuitEdgeZone(idx1, idx2)
            newEdgeZone = int(self.sp.extractGroupName(newEdgeZoneName))
            self.notify.debug('suit ' + str(self.getDoId()) + ' got zone ' + str(newEdgeZone) + ' from edge ' + str(idx1) + ' to ' + str(idx2))
            if self.ENABLE_EXPANDED_NAME:
                newNameDisp = str(newEdgeZone) + '\n' + str(self.getDoId()) + '\n' + self.name + '\n' + 'Level ' + str(self.getActualLevel())
                self.setDisplayName(newNameDisp)
            
        

    
    def bellicose(self):
        if USE_INTERVALS:
            if self.moveInterrupted and self.currPoint():
                if self.notify.getDebug():
                    self.notify.debug('resuming interrupted move')
                
                timePassed = globalClock.getFrameTime() - self.moveInterruptedTime
                self.trackResumeTime = self.trackResumeTime + timePassed
                SuitBase.SuitBase.pauseMove(self)
                self.currTaskName = self.taskName('resume-done')
                self.accept(self.currTaskName, self._DistributedSuit__backOnTrackDone)
                lerpIntervalList = self.beginMove(self.currTaskName)
                if len(lerpIntervalList) > 0:
                    lerpTrack = Track(lerpIntervalList, self.taskName('lerpTrack'))
                    lerpTrack.play(0)
                
                self.resumePos = None
            
        elif self.notify.getDebug():
            self.notify.debug('starting bellicose move')
        
        SuitBase.SuitBase.pauseMove(self)
        self.currTaskName = self.taskName('bellicose-done')
        self.accept(self.currTaskName, self._DistributedSuit__handleBellicoseDone)
        self.handleBellicoseWpt(self.currTaskName)
        self.loop('walk')
        if not (self.moveInterrupted):
            pass
        1
        self.moveInterrupted = 0
        return None

    
    def __backOnTrackDone(self):
        if self.notify.getDebug():
            self.notify.debug('Back on track, resuming path')
        
        timeLeftOnTrack = self.currMultiTrack.getDuration() - self.trackResumeTime
        if CATCHUP_SPEED_MULTIPLIER > 1:
            timeScale = 1.0
        else:
            timeScale = 1.0
        self.resumeTrack(timeScale)
        self.timeBehind = 0
        return None

    
    def bellicoseExit(self):
        return None

    
    def interruptMove(self):
        if self.notify.getDebug():
            self.notify.debug('interrupting move...')
        
        SuitBase.SuitBase.interruptMove(self)
        self.resumePos = Point3.Point3(0)
        self.resumePos.assign(self.getPos())
        return None

    
    def __findCurrentEdge(self):
        if not (self.initState):
            self.initState = self.determineInitialState()
        
        if not (self.finalState):
            self.finalState = self.determineFinalState()
        
        if self.currEdge == 0:
            self.currEdge += 1
            if self.initState == 'FromSky':
                edgeTime = SuitTimings.fromSky
            elif self.initState == 'FromBuilding':
                edgeTime = SuitTimings.fromBuilding
            
            self.prevEdgesTime = self.prevEdgesTime + edgeTime
            if self.prevEdgesTime > self.trackResumeTime:
                self.trackResumeTime = self.trackResumeTime - self.prevEdgesTime - edgeTime
                return self.currEdge - 1
            
        
        startEdge = self.currEdge
        for currPathPt in range(startEdge, self.myPathNum - 1):
            self.currEdge = self.currEdge + 1
            edgeTime = self.sp.dnaStore.getSuitEdgeTravelTime(self.myPath.getPointIndex(currPathPt - 1), self.myPath.getPointIndex(currPathPt), self.sp.suitWalkSpeed)
            self.prevEdgesTime = self.prevEdgesTime + edgeTime
            if self.prevEdgesTime > self.trackResumeTime:
                self.trackResumeTime = self.trackResumeTime - self.prevEdgesTime - edgeTime
                return self.currEdge - 1
            
        
        if self.currEdge == self.myPathNum - 1:
            self.currEdge = self.currEdge + 1
            if self.finalState == 'ToToonBuilding':
                edgeTime = SuitTimings.toToonBuilding
            elif self.finalState == 'ToCogBuilding':
                edgeTime = SuitTimings.toSuitBuilding
            elif self.finalState == 'ToSky':
                edgeTime = SuitTimings.toSky
            
            self.prevEdgesTime = self.prevEdgesTime + edgeTime
            if self.prevEdgesTime > self.trackResumeTime:
                self.trackResumeTime = self.trackResumeTime - self.prevEdgesTime - edgeTime
                return self.currEdge - 1
            
        
        self.currEdge = self.currEdge + 1
        return self.currEdge - 1

    
    def genPartialExtendedPath(self, play = 0):
        debug = self.notify.getDebug()
        self.trackResumeTime = localElapsedTime(self.startTime[0], self.startTime[1])
        currEdgeIdx = self._DistributedSuit__findCurrentEdge()
        currPt = max(1, currEdgeIdx)
        currPt = min(self.myPathNum - 1, currPt)
        self.setCurrPt(currPt)
        currWpt = self.currPoint()
        if debug:
            self.notify.debug('SETTING CURRWPT TO: ' + str(currPt))
        
        initialPos = self.prevPointPos()
        initialPos.setZ(self.STREET_HEIGHT_OFFSET)
        self.setPos(initialPos)
        self.virtualPos = initialPos
        oldCurrWpt = self.currWpt
        oldPrevWpt = self.prevWpt
        wptInfos = []
        if currEdgeIdx == 0:
            if self.initState == 'FromSky':
                moveIn = 1
            elif self.initState == 'FromBuilding':
                moveIn = 0
            
            self.createWptInfo(moveIn, self.initState, wptInfos)
        
        maxEdges = 1
        endReached = 0
        for currEdge in range(maxEdges):
            if self.atEndOfPath():
                endReached = 1
                break
            
            self.createWptInfo(0, 'unknown', wptInfos)
            self.virtualPos = currWpt.getPos()
            setCurrPtEndTime = globalClock.getRealTime()
            self.setCurrPt(self.calcNextWpt())
            currWpt = self.currPoint()
            if not currWpt:
                endReached = 1
                break
            
        
        if endReached:
            if self.finalState == 'ToToonBuilding' or self.finalState == 'ToCogBuilding':
                moveIn = 1
                if currWpt:
                    self.virtualPos = currWpt.getPos()
                else:
                    self.virtualPos = self.prevPointPos()
                    self.setCurrPt(self.currWpt - 1)
                self.createWptInfo(moveIn, self.finalState, wptInfos)
            elif self.finalState == 'ToSky':
                nextPathSegInt = FunctionInterval(self.localSetState, extraArgs = [
                    'WaitForServer'])
                wptInfos[0].append(nextPathSegInt)
            
        elif not endReached and len(wptInfos) > 0:
            nextPathSegInt = FunctionInterval(self.genPartialExtendedPath, extraArgs = [
                1])
            wptInfos[0].append(nextPathSegInt)
        
        self.setCurrPt(oldCurrWpt)
        self.virtualPos = None
        returnVal = self.collectWptInfo(wptInfos)
        if play:
            self.currMultiTrack = returnVal
            if debug:
                self.notify.debug('(genPartialExtendedPath) times: ' + str(globalClock.getFrameTime()) + ' ' + str(self.startTime) + ' ' + str(self.trackResumeTime))
                totalTime = self.currMultiTrack.tlist[0]._Track__computeDuration()
                self.notify.debug('Waypoint List Time: ' + str(totalTime))
            
            self.pathBeginTime = None
            self.resumeTrack()
            self.currWptTime = 0
        
        return returnVal

    
    def enterOff(self):
        self.hideNametag3d()
        self.hideNametag2d()
        self.notify.debug('enterOff()')
        self.disableBattleDetect()
        self.reparentTo(hidden)
        self.loop('neutral')
        self.pauseMove()
        enable = 0
        self.enableRaycast(enable)
        return None

    
    def exitOff(self):
        self.enableBattleDetect()
        self.reparentTo(render)
        self.showNametag3d()
        self.showNametag2d()
        return None

    
    def enterFromSky(self):
        SuitBase.SuitBase.pauseMove(self)
        self.currTaskName = self.taskName('fromSky-done')
        self.fromSky(self.currTaskName)
        self.accept(self.currTaskName, self._DistributedSuit__handleFromSkyDone)
        return None

    
    def exitFromSky(self):
        SuitBase.SuitBase.pauseMove(self)
        return None

    
    def __handleFromSkyDone(self):
        self.localSetState('WaitForServer')
        return None

    
    def enterFromBuilding(self):
        SuitBase.SuitBase.pauseMove(self)
        self.currTaskName = self.taskName('fromBuilding-done')
        self.accept(self.currTaskName, self._DistributedSuit__handleFromBuildingDone)
        self.fromBuilding(self.currTaskName)
        return None

    
    def exitFromBuilding(self):
        SuitBase.SuitBase.pauseMove(self)
        return None

    
    def __handleFromBuildingDone(self):
        self.localSetState('WaitForServer')
        return None

    
    def enterWalkToStreet(self):
        SuitBase.SuitBase.pauseMove(self)
        self.currTaskName = self.taskName('walkToStreet-done')
        self.accept(self.currTaskName, self._DistributedSuit__handleWalkToStreetDone)
        self.walkToStreet(self.currTaskName)
        return None

    
    def exitWalkToStreet(self):
        SuitBase.SuitBase.pauseMove(self)
        return None

    
    def __handleWalkToStreetDone(self):
        self.localSetState('WaitForServer')
        return None

    
    def enterWalkFromStreet(self):
        SuitBase.SuitBase.pauseMove(self)
        self.currTaskName = self.taskName('walkFromStreet-done')
        self.accept(self.currTaskName, self._DistributedSuit__handleWalkFromStreetDone)
        self.walkFromStreet(self.currTaskName)
        return None

    
    def exitWalkFromStreet(self):
        SuitBase.SuitBase.pauseMove(self)
        return None

    
    def __handleWalkFromStreetDone(self):
        return None

    
    def enterBellicose(self):
        self.bellicose()
        return None

    
    def exitBellicose(self):
        self.bellicoseExit()
        return None

    
    def __handleBellicoseDone(self):
        self.handleBellicoseWpt(self.currTaskName)
        return None

    
    def enterBattle(self):
        self.notify.debug('DistributedSuit: entering a Battle')
        self.disableBattleDetect()
        self.interruptMove()
        self.enableRaycast(enable = 0)
        return None

    
    def exitBattle(self):
        SuitBase.SuitBase.pauseMove(self)
        return None

    
    def enterWaitForBattle(self):
        self.loop('neutral', 0)
        self.interruptMove()
        self.disableBattleDetect()
        return None

    
    def exitWaitForBattle(self):
        self.interruptMove()
        self.enableBattleDetect()
        return None

    
    def enterWaitForToToonBuilding(self):
        return None

    
    def exitWaitForToToonBuilding(self):
        return None

    
    def enterWaitForServer(self):
        self.waitForServer()
        return None

    
    def exitWaitForServer(self):
        self.resumeTrack()
        return None

    
    def __handleWaitForServerDone(self, task):
        self.notify.debug('suit is getting tired of waiting for the server')
        return Task.done

    
    def enterToToonBuilding(self):
        SuitBase.SuitBase.pauseMove(self)
        self.currTaskName = self.taskName('toToonBuilding-done')
        self.accept(self.currTaskName, self._DistributedSuit__handleToToonBuildingDone)
        self.toToonBuilding(self.currTaskName)
        return None

    
    def exitToToonBuilding(self):
        SuitBase.SuitBase.pauseMove(self)
        return None

    
    def __handleToToonBuildingDone(self):
        self.loop('neutral', 0)
        self.localSetState('Off')

    
    def enterToCogBuilding(self):
        self.toCogBuilding()
        return None

    
    def exitToCogBuilding(self):
        return None

    
    def enterToSky(self):
        self.clearOldMove()
        self.currTaskName = self.taskName('toSky-done')
        self.accept(self.currTaskName, self._DistributedSuit__handleToSkyDone)
        self.toSky(self.currTaskName)
        return None

    
    def exitToSky(self):
        return None

    
    def __handleToSkyDone(self):
        self.loop('neutral', 0)
        self.localSetState('Off')

    
    def setHeight(self, height):
        Suit.Suit.setHeight(self, height)
        return None


