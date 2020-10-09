# Source Generated with Decompyle++
# File: DistributedBoat.pyo (Python 2.0)

from ShowBaseGlobal import *
from PandaObject import *
from ClockDelta import *
from IntervalGlobal import *
import DistributedObject
import FSM
import State
import NodePath
import Mopath

class DistributedBoat(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.eastWestMopath = Mopath.Mopath()
        self.westEastMopath = Mopath.Mopath()
        self.fsm = FSM.FSM('DistributedBoat', [
            State.State('off', self.enterOff, self.exitOff, [
                'DockedEast',
                'SailingWest',
                'DockedWest',
                'SailingEast']),
            State.State('DockedEast', self.enterDockedEast, self.exitDockedEast, [
                'SailingWest',
                'SailingEast',
                'DockedWest']),
            State.State('SailingWest', self.enterSailingWest, self.exitSailingWest, [
                'DockedWest',
                'SailingEast',
                'DockedEast']),
            State.State('DockedWest', self.enterDockedWest, self.exitDockedWest, [
                'SailingEast',
                'SailingWest',
                'DockedEast']),
            State.State('SailingEast', self.enterSailingEast, self.exitSailingEast, [
                'DockedEast',
                'DockedWest',
                'SailingWest'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def generate(self):
        self.setupMultiTracks()
        self.accept('on-floor', self._DistributedBoat__handleOnFloor)
        self.accept('off-floor', self._DistributedBoat__handleOffFloor)

    
    def setupMultiTracks(self):
        boat = toonbase.tcr.name2nodePath['donalds_boat']
        self.eastWestMopath.loadFile('phase_6/paths/dd-e-w')
        ewMopathInterval = MopathInterval(self.eastWestMopath, boat, name = 'ew-mopath')
        ewBoatTrack = Track([
            ewMopathInterval], 'ew-boat-track')
        EW_BOAT_START = ewBoatTrack.getIntervalStartTime('ew-mopath')
        EW_BOAT_END = ewBoatTrack.getIntervalEndTime('ew-mopath')
        self.westEastMopath.loadFile('phase_6/paths/dd-w-e')
        weMopathInterval = MopathInterval(self.westEastMopath, boat, name = 'we-mopath')
        weBoatTrack = Track([
            weMopathInterval], 'we-boat-track')
        WE_BOAT_START = weBoatTrack.getIntervalStartTime('we-mopath')
        WE_BOAT_END = weBoatTrack.getIntervalEndTime('we-mopath')
        PIER_TIME = 5.0
        eastPier = self.cr.playGame.DDHood.loader.geom.find('**/east_pier')
        ePierHpr = eastPier.getHpr()
        ePierTargetHpr = Vec3(ePierHpr[0], 0.9999, ePierHpr[2])
        ePierDownInterval = LerpHprInterval(eastPier, PIER_TIME, ePierHpr, ePierTargetHpr, name = 'e-pier-down')
        ePierDownTrack = Track([
            ePierDownInterval], 'e-pier-down-track')
        westPier = self.cr.playGame.DDHood.loader.geom.find('**/west_pier')
        wPierHpr = westPier.getHpr()
        wPierTargetHpr = Vec3(wPierHpr[0], 114.0, wPierHpr[2])
        wPierUpInterval = LerpHprInterval(westPier, PIER_TIME, wPierTargetHpr, wPierHpr, name = 'w-pier-up')
        wPierUpTrack = Track([
            wPierUpInterval], 'w-pier-up-track')
        wPierUpStart = EW_BOAT_END - wPierUpInterval.getDuration()
        wPierUpTrack.setIntervalStartTime('w-pier-up', wPierUpStart)
        wPierDownInterval = LerpHprInterval(westPier, PIER_TIME, wPierHpr, wPierTargetHpr, name = 'w-pier-down')
        wPierDownTrack = Track([
            wPierDownInterval], 'w-pier-down-track')
        ePierUpInterval = LerpHprInterval(eastPier, PIER_TIME, ePierTargetHpr, ePierHpr, name = 'e-pier-up')
        ePierUpTrack = Track([
            ePierUpInterval], 'e-pier-up-track')
        ePierUpStart = WE_BOAT_END - ePierUpInterval.getDuration()
        ePierUpTrack.setIntervalStartTime('e-pier-up', ePierUpStart)
        if base.wantSfx:
            dockSound = self.cr.playGame.DDHood.loader.dockSound
            foghornSound = self.cr.playGame.DDHood.loader.foghornSound
            bellSound = self.cr.playGame.DDHood.loader.bellSound
            ePierSound = SoundInterval(dockSound, name = 'e-pier-sound')
            wPierSound = SoundInterval(dockSound, name = 'w-pier-sound')
            ewPierSoundTrack = Track([
                ePierSound,
                wPierSound], 'ew-pier-sound-track')
            wPierUpTime = wPierUpTrack.getIntervalStartTime('w-pier-up')
            ewPierSoundTrack.setIntervalStartTime('w-pier-sound', wPierUpTime)
            wePierSoundTrack = Track([
                wPierSound,
                ePierSound], 'we-pier-sound-track')
            ePierUpTime = ePierUpTrack.getIntervalStartTime('e-pier-up')
            wePierSoundTrack.setIntervalStartTime('e-pier-sound', ePierUpTime)
            BellSound = SoundInterval(bellSound, name = 'bell')
            FoghornSound = SoundInterval(foghornSound, name = 'horn')
            HornTrack = Track([
                BellSound,
                FoghornSound], 'horn-track')
            hornTime = EW_BOAT_END - FoghornSound.getDuration() + 2.0
            HornTrack.setIntervalStartTime('horn', hornTime)
            self.ewMultiTrack = MultiTrack([
                ewBoatTrack,
                ePierDownTrack,
                wPierUpTrack,
                ewPierSoundTrack,
                HornTrack], 'ew-multitrack')
            self.weMultiTrack = MultiTrack([
                weBoatTrack,
                wPierDownTrack,
                ePierUpTrack,
                wePierSoundTrack,
                HornTrack], 'we-multitrack')
        else:
            self.ewMultiTrack = MultiTrack([
                ewBoatTrack,
                ePierDownTrack,
                wPierUpTrack], 'ew-multitrack')
            self.weMultiTrack = MultiTrack([
                weBoatTrack,
                wPierDownTrack,
                ePierUpTrack], 'we-multitrack')

    
    def disable(self):
        self.ignore('on-floor')
        self.ignore('off-floor')
        self.fsm.request('off')
        DistributedObject.DistributedObject.disable(self)
        self.ewMultiTrack.stop()
        self.weMultiTrack.stop()

    
    def delete(self):
        self.eastWestMopath.reset()
        self.westEastMopath.reset()
        self.ewMultiTrack = None
        self.weMultiTrack = None
        DistributedObject.DistributedObject.delete(self)

    
    def setState(self, state, sec, usec):
        self.fsm.request(state, [
            localElapsedTime(sec, usec)])

    
    def __handleOnFloor(self, collEntry):
        if collEntry.getIntoNode().getName() == 'donalds_boat_floor':
            self.cr.playGame.DDHood.loader.place.activityFsm.request('OnBoat')
        

    
    def __handleOffFloor(self, collEntry):
        if collEntry.getIntoNode().getName() == 'donalds_boat_floor':
            self.cr.playGame.DDHood.loader.place.activityFsm.request('off')
        

    
    def enterOff(self):
        return None

    
    def exitOff(self):
        return None

    
    def enterDockedEast(self, ts):
        self.weMultiTrack.setFinalT()
        return None

    
    def exitDockedEast(self):
        return None

    
    def enterSailingWest(self, ts):
        dur = self.ewMultiTrack.getDuration()
        if ts <= dur:
            self.ewMultiTrack.play(ts)
        else:
            self.ewMultiTrack.setT(dur)

    
    def exitSailingWest(self):
        if self.ewMultiTrack.isPlaying():
            self.ewMultiTrack.stop()
            self.ewMultiTrack.setFinalT()
        

    
    def enterDockedWest(self, ts):
        self.ewMultiTrack.setFinalT()
        return None

    
    def exitDockedWest(self):
        return None

    
    def enterSailingEast(self, ts):
        dur = self.weMultiTrack.getDuration()
        if ts <= dur:
            self.weMultiTrack.play(ts)
        else:
            self.weMultiTrack.setT(dur)

    
    def exitSailingEast(self):
        if self.weMultiTrack.isPlaying():
            self.weMultiTrack.stop()
            self.weMultiTrack.setFinalT()
        
        return None


