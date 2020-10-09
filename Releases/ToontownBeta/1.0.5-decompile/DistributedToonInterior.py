# Source Generated with Decompyle++
# File: DistributedToonInterior.pyo (Python 2.0)

from ToonBaseGlobal import *
from ShowBaseGlobal import *
from IntervalGlobal import *
from ClockDelta import *
import ToonInterior
import DirectNotifyGlobal
import FSM
import DistributedObject
import State
import DNADoor

class DistributedToonInterior(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.fsm = FSM.FSM('DistributedToonInterior', [
            State.State('off', self.enterOff, self.exitOff, [
                'toon',
                'beingTakenOver']),
            State.State('toon', self.enterToon, self.exitToon, [
                'beingTakenOver']),
            State.State('beingTakenOver', self.enterBeingTakenOver, self.exitBeingTakenOver, [
                'off'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)

    
    def disable(self):
        self.ignoreAll()
        self.interior.removeNode()

    
    def delete(self):
        DistributedObject.DistributedObject.delete(self)

    
    def setZoneIDAndBlock(self, zoneID, block):
        self.zoneID = zoneID
        self.block = block

    
    def setState(self, state, sec, usec):
        self.fsm.request(state, [
            localElapsedTime(sec, usec)])

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterToon(self, ts):
        interior = loader.loadModel('phase_7/models/modules/toon_interior')
        self.interior = loader.loadModel('phase_7/models/modules/toon_interior')
        interior.reparentTo(render)
        door = toonbase.tcr.playGame.dnaStore.findNode('door_double_round_ur')
        doorNP = door.copyTo(interior)
        door_origin = interior.attachNewNode(Node())
        door_origin.setPos(Vec3(0, 1, 0))
        door_origin.setHpr(Vec3(180, 0, 0))
        color = Vec4(1, 1, 1, 1)
        DNADoor.DNADoor.setupDoor(doorNP, interior, door_origin, toonbase.tcr.playGame.dnaStore, str(self.block), color)

    
    def exitToon(self, ts):
        pass

    
    def enterBeingTakenOver(self, ts):
        pass

    
    def exitBeingTakenOver(self, ts):
        pass


