# Source Generated with Decompyle++
# File: DistributedSuitInterior.pyo (Python 2.0)

from ClockDelta import *
import DirectNotifyGlobal
import FSM
import DistributedObject
import State

class DistributedSuitInterior(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.toons = []
        self.activeIntervals = { }
        self.elevatorName = self.uniqueName('elevator')
        self.fsm = FSM.FSM('DistributedSuitInterior', [
            State.State('Elevator', self.enterElevator, self.exitElevator, [
                'Battle',
                'Reset']),
            State.State('Battle', self.enterBattle, self.exitBattle, [
                'Resting',
                'Reward',
                'Reset']),
            State.State('Resting', self.enterResting, self.exitResting, [
                'Elevator',
                'Reset']),
            State.State('Reward', self.enterReward, self.exitReward, [
                'Reset']),
            State.State('Reset', self.enterReset, self.exitReset, [
                'Off']),
            State.State('Off', self.enterOff, self.exitOff, [
                'Elevator',
                'Battle',
                'Reset'])], 'Off', 'Off')
        self.fsm.enterInitialState()

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)

    
    def disable(self):
        self._DistributedSuitInterior__cleanupIntervals()
        self.ignoreAll()
        self.toons = []

    
    def delete(self):
        DistributedObject.DistributedObject.delete(self)

    
    def __addToon(self, toon):
        self.accept(toon.uniqueName('disable'), self._DistributedSuitInterior__handleUnexpectedExit, extraArgs = [
            toon])

    
    def __handleUnexpectedExit(self, toon):
        self.notify.warning('handleUnexpectedExit() - toon: %d' % toon.doId)
        self._DistributedSuitInterior__removeToon(toon, unexpected = 1)

    
    def __removeToon(self, toon, unexpected = 0):
        if self.toons.count(toon) == 1:
            self.toons.remove(toon)
        
        self.ignore(toon.uniqueName('disable'))

    
    def __finishInterval(self, name):
        if self.activeIntervals.has_key(name):
            interval = self.activeIntervals[name]
            if interval.isPlaying():
                interval.setFinalT()
            
        

    
    def __cleanupIntervals(self):
        for interval in self.activeIntervals.values():
            interval.stop()
        
        self.activeIntervals = { }

    
    def setToons(self, toonIds):
        self.toonIds = toonIds
        oldtoons = self.toons
        self.toons = []
        for toonId in toonIds:
            if toonId != 0 and self.cr.doId2do.has_key(toonId):
                toon = self.cr.doId2do[toonId]
                self.toons.append(toon)
                if oldtoons.count(toon) == 0:
                    self._DistributedSuitInterior__addToon(toon)
                
            
        
        for toon in oldtoons:
            if self.toons.count(toon) == 0:
                self._DistributedSuitInterior__removeToon(toon)
            
        

    
    def setState(self, state, sec, usec):
        self.fsm.request(state, [
            localElapsedTime(sec, usec)])

    
    def d_elevatorDone(self, toonId):
        self.sendUpdate('elevatorDone', [
            toonId])

    
    def enterOff(self, ts = 0):
        return None

    
    def exitOff(self):
        return None

    
    def __playElevator(self, ts, name, callback):
        elevIvals = []
        elevIvals.append(WaitInterval(BattleBase.ELEVATOR_T))
        elevIvals.append(FunctionInterval(callback))
        track = Track(elevIvals)
        dur = track.getDuration()
        if ts <= dur:
            track.play(ts)
            self.activeIntervals[name] = track
        else:
            track.setT(dur, event = IVAL_INIT)

    
    def enterElevator(self, ts = 0):
        self._DistributedSuitInterior__playElevator(ts, self.elevatorName, self._DistributedSuitInterior__handleElevatorDone)
        return None

    
    def __handleElevatorDone(self):
        self.d_elevatorDone(toonbase.localToon.doId)

    
    def exitElevator(self):
        self._DistributedSuitInterior__finishInterval(self.elevatorName)
        return None

    
    def enterBattle(self, ts = 0):
        return None

    
    def exitBattle(self):
        return None

    
    def enterResting(self, ts = 0):
        return None

    
    def exitResting(self):
        return None

    
    def enterReward(self, ts = 0):
        return None

    
    def exitReward(self):
        return None

    
    def enterReset(self, ts = 0):
        return None

    
    def exitReset(self):
        return None


