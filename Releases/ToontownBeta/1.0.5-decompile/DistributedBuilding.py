# Source Generated with Decompyle++
# File: DistributedBuilding.pyo (Python 2.0)

from ShowBaseGlobal import *
from ClockDelta import *
import DirectNotifyGlobal
import FSM
import DistributedObject

class DistributedBuilding(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.suitDoorOrigin = None
        self.fsm = FSM.FSM('DistributedBuilding', [
            State.State('off', self.enterOff, self.exitOff, [
                'becomingToon',
                'toon',
                'becomingSuit',
                'suit']),
            State.State('becomingToon', self.enterBecomingToon, self.exitBecomingToon, [
                'toon']),
            State.State('toon', self.enterToon, self.exitToon, [
                'becomingSuit']),
            State.State('becomingSuit', self.enterBecomingSuit, self.exitBecomingSuit, [
                'suit']),
            State.State('suit', self.enterSuit, self.exitSuit, [
                'becomingToon'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.bossLevel = 0

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        self.skipSetToToon = 1
        self.townTopLevel = self.cr.playGame.hood.loader.geom

    
    def disable(self):
        self.fsm.request('off')
        del self.townTopLevel
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        DistributedObject.DistributedObject.delete(self)

    
    def setBlock(self, block):
        self.block = block

    
    def setSuitData(self, suitTrack, difficulty):
        self.track = suitTrack
        self.difficulty = difficulty

    
    def setState(self, state, sec, usec):
        self.fsm.request(state, [
            localElapsedTime(sec, usec)])

    
    def getSuitDoorOrigin(self):
        return self.suitDoorOrigin

    
    def getBossLevel(self):
        return self.bossLevel

    
    def setBossLevel(self, bossLevel):
        self.bossLevel = bossLevel
        return None

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterBecomingToon(self, ts):
        pass

    
    def exitBecomingToon(self):
        pass

    
    def enterToon(self, ts):
        self.setToToon()

    
    def exitToon(self):
        pass

    
    def enterBecomingSuit(self, ts):
        pass

    
    def exitBecomingSuit(self):
        pass

    
    def enterSuit(self, ts):
        self.setToSuit()

    
    def exitSuit(self):
        pass

    
    def getNodePaths(self):
        nodePath = []
        npc = self.townTopLevel.findAllMatches('**/?b' + self.block + ':*_DNARoot;+s')
        for i in range(npc.getNumPaths()):
            nodePath.append(npc.getPath(i))
        
        return nodePath

    
    def setToSuit(self):
        self.skipSetToToon = 0
        nodes = self.getNodePaths()
        for i in nodes:
            name = i.getName()
            if name[0] == 's':
                i.unstash()
            elif name[0] == 't':
                if name.find('_landmark_') != -1:
                    i.stash()
                else:
                    i.stash()
            
        
        npc = hidden.findAllMatches('landmarkBlocks/sb' + self.block + ':*_landmark_*_DNARoot')
        for i in range(npc.getNumPaths()):
            nodePath = npc.getPath(i)
            suitNP = self.cr.playGame.dnaStore.findNode('suit_landmark_' + chr(self.track) + str(self.difficulty))
            zoneID = self.cr.playGame.dnaStore.getZoneFromBlockNumber(int(self.block))
            newParentNP = toonbase.tcr.playGame.hood.loader.zoneDict[zoneID]
            newNP = suitNP.copyTo(newParentNP)
            newNP.setName('sb' + self.block + ':_landmark__DNARoot')
            newNP.setPosHprScale(nodePath, Vec3(0), Vec3(0), Vec3(1))
            newNP.flattenMedium()
            self.suitDoorOrigin = newNP.find('**/*_door_origin')
            return None
        

    
    def setToToon(self):
        if self.skipSetToToon:
            self.skipSetToToon = 0
            return None
        
        self.suitDoorOrigin = None
        nodes = self.getNodePaths()
        for i in nodes:
            name = i.getName()
            if name[0] == 's':
                if name.find('_landmark_') != -1:
                    i.removeNode()
                else:
                    i.stash()
            elif name[0] == 't':
                if name.find('_landmark_') != -1:
                    i.unstash()
                else:
                    i.unstash()
            
        


