# Source Generated with Decompyle++
# File: SuitPlannerBase.pyo (Python 2.0)

from PandaModules import *
import whrandom
import string
import DirectNotifyGlobal
import ToontownGlobals

class SuitPlannerBase:
    notify = DirectNotifyGlobal.directNotify.newCategory('SuitPlannerBase')
    
    def __init__(self):
        self.clock = ClockObject.getGlobalClock()
        self.suitWalkSpeed = 4.8
        self.dnaStore = None
        self.pointIndexes = { }
        return None

    
    def setupDNA(self):
        if self.dnaStore:
            return None
        
        self.dnaStore = DNAStorage()
        dnaFileName = self.genDNAFileName()
        loadDNAFileAI(self.dnaStore, dnaFileName, CSDefault)
        self.initDNAInfo()
        return None

    
    def genDNAFileName(self):
        zone = self.getZoneId()
        hoodId = zone - zone % 1000
        hood = ToontownGlobals.dnaMap[hoodId]
        phase = ToontownGlobals.streetPhaseMap[hoodId]
        
        try:
            if simbase.aiService:
                return './' + hood + '_' + str(zone) + '.dna'
            else:
                return 'phase_' + str(phase) + '/dna/' + hood + '_' + str(zone) + '.dna'
        except:
            return 'phase_' + str(phase) + '/dna/' + hood + '_' + str(zone) + '.dna'


    
    def getZoneId(self):
        return self.zoneId

    
    def setZoneId(self, zoneId):
        self.notify.debug('setting zone id for suit planner')
        self.zoneId = zoneId
        self.setupDNA()

    
    def extractGroupName(self, groupFullName):
        return string.split(groupFullName, ':', 1)[0]

    
    def initDNAInfo(self):
        self.battlePosDict = { }
        for i in range(self.dnaStore.getNumDNAVisGroupsAI()):
            vg = self.dnaStore.getDNAVisGroupAI(i)
            zoneId = int(self.extractGroupName(vg.getName()))
            if vg.getNumBattleCells() == 1:
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()
            elif vg.getNumBattleCells() > 1:
                self.notify.warning('multiple battle cells for zone: %d' % zoneId)
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()
            else:
                self.notify.warning('no battle cell for zone: %d' % zoneId)
                self.battlePosDict[zoneId] = Point3(0, 0, 0)
        
        self.dnaStore.resetDNAGroups()
        self.dnaStore.resetDNAVisGroups()
        self.dnaStore.resetDNAVisGroupsAI()
        self.streetPointList = []
        self.frontdoorPointList = []
        self.sidedoorPointList = []
        numPoints = self.dnaStore.getNumSuitPoints()
        for i in range(numPoints):
            point = self.dnaStore.getSuitPointAtIndex(i)
            if point.getPointType() == DNASuitPoint.STREETPOINT:
                self.streetPointList.append(point)
            elif point.getPointType() == DNASuitPoint.FRONTDOORPOINT:
                self.frontdoorPointList.append(point)
            elif point.getPointType() == DNASuitPoint.SIDEDOORPOINT:
                self.sidedoorPointList.append(point)
            
            self.pointIndexes[point.getIndex()] = point
        
        return None

    
    def performPathTest(self):
        if not self.notify.getDebug():
            return None
        
        startAndEnd = self.pickPath()
        if not startAndEnd:
            return None
        
        startPoint = startAndEnd[0]
        endPoint = startAndEnd[1]
        path = self.dnaStore.getSuitPath(startPoint, endPoint)
        numPathPoints = path.getNumPoints()
        for i in range(numPathPoints - 1):
            zone = self.dnaStore.getSuitEdgeZone(path.getPointIndex(i), path.getPointIndex(i + 1))
            travelTime = self.dnaStore.getSuitEdgeTravelTime(path.getPointIndex(i), path.getPointIndex(i + 1), self.suitWalkSpeed)
            self.notify.debug('edge from point ' + `i` + ' to point ' + `i + 1` + ' is in zone: ' + `zone` + ' and will take ' + `travelTime` + ' seconds to walk.')
        
        return None

    
    def genPath(self, srcAndDst):
        return self.dnaStore.getSuitPath(srcAndDst[0], srcAndDst[1])

    
    def getDnaStore(self):
        return self.dnaStore


