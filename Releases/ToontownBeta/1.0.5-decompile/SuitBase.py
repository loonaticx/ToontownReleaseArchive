# Source Generated with Decompyle++
# File: SuitBase.pyo (Python 2.0)

from PandaModules import *
from ClockDelta import *
import math
import whrandom
import Point3
import DirectNotifyGlobal
import SuitBattleGlobals
TIME_BUFFER_PER_WPT = 0.25
TIME_DIVISOR = 100
DISTRIBUTE_TASK_CREATION = 0

class SuitBase:
    
    try:
        ENABLE_POSITION_UPDATES = simbase.config.GetBool('want-suit-positions', 0)
    except:
        ENABLE_POSITION_UPDATES = base.config.GetBool('want-suit-positions', 0)

    notify = DirectNotifyGlobal.directNotify.newCategory('SuitBase')
    
    def __init__(self):
        self.src = None
        self.dst = None
        self.myPath = None
        self.currWpt = 0
        self.prevWpt = 0
        self.oldWpt = 0
        self.moveInterrupted = 0
        self.moveInterruptedTime = 0
        self.dna = None
        self.level = 0
        self.myPathNum = 0
        self.currWptPos = None
        self.prevWptPos = None
        self.lastCurrWptVal = -1
        self.lastCurrPointVal = None
        self.lastNextWptVal = -1
        self.lastNextPointVal = None
        self.currTaskName = None
        self.virtualPos = None
        self.wptList = []
        self.currWptIdx = 0
        self.initialState = None
        self.finalState = None
        self.myDoneEvent = None
        return None

    
    def delete(self):
        return None

    
    def getStyleName(self):
        if self.dna:
            return self.dna.name
        else:
            self.notify.error('called getStyleName() before dna was set!')
            return 'unknown'

    
    def getLevel(self):
        return self.level

    
    def setLevel(self, level):
        self.level = level
        nameWLevel = self.name + '\nLevel ' + str(self.getActualLevel())
        self.setDisplayName(nameWLevel)

    
    def setDisplayName(self, str):
        self.notify.debug('setDisplayName(): setting suit name')
        self.nametag.setDisplayName(str)

    
    def getActualLevel(self):
        return SuitBattleGlobals.getActualFromRelativeLevel(self.getStyleName(), self.level) + 1

    
    def setPath(self, path):
        self.myPath = path
        self.myPathNum = self.myPath.getNumPoints()
        self.initialState = None
        self.finalState = None
        return None

    
    def getPath(self):
        return self.myPath

    
    def printPath(self):
        print '%d points in path' % self.myPathNum
        for currPathPt in range(self.myPathNum):
            indexVal = self.myPath.getPointIndex(currPathPt)
            print '\t', self.sp.dnaStore.getSuitPointWithIndex(indexVal)
        
        return None

    
    def setCurrPt(self, pathIndex):
        self.currWpt = pathIndex
        if pathIndex > 0:
            self.prevWpt = pathIndex - 1
            if pathIndex > 1:
                self.oldWpt = pathIndex - 2
            
        
        self.currWptPos = None
        self.prevWptPos = None
        return None
        currWaypoint = self.currPoint()
        prevWaypoint = self.prevPoint()
        if currWaypoint:
            self.currWptPos = currWaypoint.getPos()
        else:
            self.currWptPos = None
        if prevWaypoint:
            self.prevWptPos = prevWaypoint.getPos()
        else:
            self.prevWptPos = None
        return currWaypoint

    
    def handleTeleport(self, source, destination, startTime, currTime):
        if self.getPos() != source:
            self.setMyLoc(source)
        
        currPos = self.getPos()
        moveDist = Vec3(destination - currPos).length()
        timeToGetThere = moveDist * self.sp.suitWalkSpeed
        if timeToGetThere == 0:
            timeToGetThere = 1e-005
        
        percentThere = (currTime - startTime) / timeToGetThere
        if percentThere >= 1:
            self.setMyLoc(destination)
        elif percentThere > 0:
            self.setMyLoc(currPos + moveDist * percentThere)
        
        return None

    
    def setMyLoc(self, location):
        return None

    
    def atCurrWpt(self):
        point = self.currPointPos()
        if self.virtualPos and self.virtualPos == point:
            return 1
        elif self.getPos() == point:
            return 1
        
        return 0

    
    def incrementWpt(self):
        if self.atCurrWpt() and not (self.moveInterrupted):
            return 1
        else:
            return 0

    
    def nextPoint(self):
        if not (self.myPath):
            return None
        
        nextWpt = self.calcNextWpt()
        if nextWpt >= self.myPathNum:
            return None
        
        indexVal = self.myPath.getPointIndex(nextWpt)
        point = self.sp.pointIndexes[indexVal]
        return point

    
    def atEndOfPath(self):
        if self.currWpt >= self.myPathNum:
            return 1
        else:
            return 0

    
    def currPoint(self):
        if self.currWpt >= self.myPathNum:
            return None
        
        if self.wptList:
            point = self.wptList[self.currWptIdx][3]
        else:
            indexVal = self.myPath.getPointIndex(self.currWpt)
            point = self.sp.pointIndexes[indexVal]
        return point

    
    def currPointPos(self):
        if not (self.currWptPos):
            currPoint = self.currPoint()
            if currPoint:
                self.currWptPos = currPoint.getPos()
            else:
                self.currWptPos = self.prevPointPos()
        
        return self.currWptPos

    
    def prevPointPos(self):
        if not (self.prevWptPos):
            self.prevWptPos = self.prevPoint().getPos()
        
        return self.prevWptPos

    
    def pointByIndex(self, index):
        if not (self.myPath) or index >= self.myPathNum:
            return None
        
        indexVal = self.myPath.getPointIndex(index)
        point = self.sp.pointIndexes[indexVal]
        return point

    
    def prevPoint(self):
        if not (self.myPath) or self.prevWpt >= self.myPathNum:
            return None
        
        indexVal = self.myPath.getPointIndex(self.prevWpt)
        point = self.sp.pointIndexes[indexVal]
        return point

    
    def oldPoint(self):
        if self.oldWpt >= self.myPathNum:
            return None
        
        indexVal = self.myPath.getPointIndex(self.oldWpt)
        point = self.sp.pointIndexes[indexVal]
        return point

    
    def firstPoint(self, type = None):
        if not (self.myPath) or self.myPathNum < 1:
            return None
        
        currIndex = 0
        while currIndex < self.myPathNum:
            indexVal = self.myPath.getPointIndex(currIndex)
            point = self.sp.pointIndexes[indexVal]
            if type == None or type == point.getPointType():
                return point
            
            currIndex = currIndex + 1
        return None

    
    def lastPoint(self):
        if self.myPathNum < 1:
            return None
        
        indexVal = self.myPath.getPointIndex(self.myPathNum - 1)
        point = self.sp.pointIndexes[indexVal]
        return point

    
    def calcNextWpt(self):
        wpt = self.currWpt + 1
        return wpt

    
    def wptCheck(self):
        pass

    
    def calcWalkToStreetTime(self):
        prevPoint = self.prevPoint()
        if not prevPoint == None:
            if prevPoint.getPointType() == DNASuitPoint.FRONTDOORPOINT:
                pass
            if not (prevPoint.getPointType() == DNASuitPoint.SIDEDOORPOINT):
                return -1
            
        currPoint = self.currPoint()
        if currPoint == None or not (currPoint.getPointType() == DNASuitPoint.STREETPOINT):
            return -1
        
        return self.sp.dnaStore.getSuitEdgeTravelTime(self.myPath.getPointIndex(self.currWpt), self.myPath.getPointIndex(self.calcNextWpt()), self.sp.suitWalkSpeed)

    
    def moveToNextWpt(self, doneEvent = None):
        if self.incrementWpt():
            self.setCurrPt(self.calcNextWpt())
        
        return self.beginMove(doneEvent)

    
    def beginMove(self, doneEvent = None, destination = None, anim = 'walk'):
        pass

    
    def updateMove(self, task):
        return None

    
    def sendDoneEvent(self):
        if self.myDoneEvent:
            self.notify.debug('calling done event ' + self.myDoneEvent)
            doneEvt = self.myDoneEvent
            self.myDoneEvent = None
            messenger.send(doneEvt)
        
        return None

    
    def doneMove(self, task):
        self.notify.debug('done with move')
        if not (self.moveInterrupted):
            self.notify.debug('move was not interrupted')
            self.sendDoneEvent()
        
        return None

    
    def pauseMove(self):
        if self.currTaskName:
            taskMgr.removeTasksNamed(self.currTaskName)
            taskMgr.removeTasksNamed('doLater-' + self.currTaskName)
            self.currTaskName = None
        

    
    def clearOldMove(self):
        self.pauseMove()

    
    def interruptMove(self):
        self.moveInterruptedTime = globalClock.getFrameTime()
        self.moveInterrupted = 1
        self.pauseMove()
        return None

    
    def determineInitialState(self):
        if self.initialState:
            return self.initialState
        
        result = 'FromSky'
        prevPoint = self.firstPoint()
        if prevPoint:
            if prevPoint.getPointType() == DNASuitPoint.FRONTDOORPOINT or prevPoint.getPointType() == DNASuitPoint.SIDEDOORPOINT:
                result = 'FromBuilding'
            
        
        self.notify.debug('Determined initial state should be...' + result)
        self.initialState = result
        return result

    
    def determineNextState(self):
        currPoint = self.currPoint()
        prevPoint = self.prevPoint()
        nextPoint = self.nextPoint()
        if currPoint:
            if currPoint.getPointType() == DNASuitPoint.FRONTDOORPOINT or currPoint.getPointType() == DNASuitPoint.SIDEDOORPOINT:
                return 'WalkFromStreet'
            elif prevPoint.getPointType() == DNASuitPoint.FRONTDOORPOINT or prevPoint.getPointType() == DNASuitPoint.SIDEDOORPOINT:
                return 'WalkToStreet'
            else:
                return 'Bellicose'
        elif prevPoint:
            if prevPoint.getPointType() == DNASuitPoint.FRONTDOORPOINT or prevPoint.getPointType() == DNASuitPoint.SIDEDOORPOINT:
                return 'ToToonBuilding'
            elif self.fsm.getCurrentState().getName() == 'Battle':
                self.notify.warning('determineNextState() - in Battle!')
            
            return 'ToSky'
        
        return self.fsm.getCurrentState().getName()

    
    def determineFinalState(self):
        if self.finalState:
            return self.finalState
        
        result = 'ToSky'
        prevPoint = self.lastPoint()
        if prevPoint:
            if prevPoint.getPointType() == DNASuitPoint.FRONTDOORPOINT or prevPoint.getPointType() == DNASuitPoint.SIDEDOORPOINT:
                result = 'ToToonBuilding'
            
        
        self.notify.debug('Determined final state should be...' + result)
        self.finalState = result
        return result

    
    def createWptInfo(self, moveIn, state, wptInfos):
        pass

    
    def collectWptInfo(self, wptInfos):
        pass

    
    def genExtendedPath(self):
        self.virtualPos = self.prevPointPos()
        oldCurrWpt = self.currWpt
        oldPrevWpt = self.prevWpt
        wptInfos = []
        initState = self.determineInitialState()
        if initState == 'FromSky':
            moveIn = 1
        elif initState == 'FromBuilding':
            moveIn = 0
        
        self.createWptInfo(moveIn, initState, wptInfos)
        currPt = 0
        notDone = 1
        currWaypoint = self.currPoint()
        while notDone:
            self.createWptInfo(0, 'someBogusState', wptInfos)
            self.virtualPos = currWaypoint.getPos()
            self.setCurrPt(self.calcNextWpt())
            currWaypoint = self.currPoint()
            if not currWaypoint:
                notDone = 0
            
            currPt = currPt + 1
        lastState = self.determineFinalState()
        currWaypoint = self.currPoint()
        if currWaypoint:
            self.virtualPos = currWaypoint.getPos()
        else:
            self.virtualPos = self.prevPoint().getPos()
            self.setCurrPt(self.currWpt - 1)
        if lastState == 'ToToonBuilding' or lastState == 'ToCogBuilding':
            moveIn = 1
            self.createWptInfo(moveIn, lastState, wptInfos)
        
        self.setCurrPt(oldCurrWpt)
        self.virtualPos = None
        returnVal = self.collectWptInfo(wptInfos)
        return returnVal


