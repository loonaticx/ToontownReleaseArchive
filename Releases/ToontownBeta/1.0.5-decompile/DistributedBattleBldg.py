# Source Generated with Decompyle++
# File: DistributedBattleBldg.pyo (Python 2.0)

from PandaModules import *
from IntervalGlobal import *
from BattleBase import *
import DistributedBattleBase
import DirectNotifyGlobal
import MovieUtil
import Suit
import Actor
import SuitBattleGlobals
import State

class DistributedBattleBldg(DistributedBattleBase.DistributedBattleBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBattleBldg')
    camFOFov = 30.0
    camFOPos = Point3(0, -10, 4)
    
    def __init__(self, cr):
        DistributedBattleBase.DistributedBattleBase.__init__(self, cr)
        self.fsm.addState(State.State('BuildingReward', self.enterBuildingReward, self.exitBuildingReward, [
            'Resume']))
        offState = self.fsm.getStateNamed('Off')
        offState.addTransition('BuildingReward')
        rewardState = self.fsm.getStateNamed('Reward')
        rewardState.addTransition('BuildingReward')

    
    def __faceOff(self, ts, name, callback):
        elevatorPos = self.toons[0].getPos()
        suitLeader = 1
        delay = FACEOFF_TAUNT_T
        suitTracks = []
        for suit in self.suits:
            suitIvals = []
            suitIvals.append(FunctionInterval(suit.loop, extraArgs = [
                'neutral']))
            suitIvals.append(FunctionInterval(suit.headsUp, extraArgs = [
                elevatorPos]))
            if suitLeader == 1:
                suitLeader = 0
                taunt = SuitBattleGlobals.getFaceoffTaunt(suit.getStyleName())
                suitIvals.append(FunctionInterval(suit.setChat, extraArgs = [
                    taunt,
                    CFSpeech | CFTimeout]))
            
            (destPos, destHpr) = self.getActorPosHpr(suit, self.suits)
            suitIvals.append((delay, FunctionInterval(suit.clearChat)))
            suitIvals.append(self.createAdjustInterval(suit, destPos, destHpr))
            suitTracks.append(Track(suitIvals))
        
        suitTrack = Track([
            MultiTrack(suitTracks)])
        toonTracks = []
        for toon in self.toons:
            toonIvals = []
            (destPos, destHpr) = self.getActorPosHpr(toon, self.toons)
            toonIvals.append((delay, self.createAdjustInterval(toon, destPos, destHpr, toon = 1)))
            toonTracks.append(Track(toonIvals))
        
        toonTrack = Track([
            MultiTrack(toonTracks)])
        camIvals = []
        
        def setCamFov(fov):
            base.cam.node().setFov(fov)

        camIvals.append(FunctionInterval(camera.wrtReparentTo, extraArgs = [
            self.suits[0]]))
        camIvals.append(FunctionInterval(setCamFov, extraArgs = [
            self.camFOFov]))
        camIvals.append(FunctionInterval(camera.setPosHpr, extraArgs = [
            0,
            18,
            suit.getHeight() * 0.66,
            -180,
            5,
            0]))
        camIvals.append(WaitInterval(delay))
        camIvals.append(FunctionInterval(setCamFov, extraArgs = [
            self.camFov]))
        camIvals.append(FunctionInterval(camera.wrtReparentTo, extraArgs = [
            self]))
        camIvals.append(FunctionInterval(camera.setPos, extraArgs = [
            self.camFOPos]))
        camIvals.append(FunctionInterval(camera.lookAt, extraArgs = [
            self.srow[0][0]]))
        camTrack = Track(camIvals)
        mtrack = MultiTrack([
            suitTrack,
            toonTrack,
            camTrack])
        done = FunctionInterval(callback)
        track = Track([
            mtrack,
            done], name)
        dur = track.getDuration()
        if ts <= dur:
            track.play(ts)
            self.activeIntervals[name] = track
        else:
            self.notify.debug('__faceOff() - ts: %f dur: %f' % (ts, dur))
            track.setT(dur, event = IVAL_INIT)

    
    def enterFaceOff(self, ts):
        self.notify.debug('enterFaceOff()')
        self.delayDeleteToons(1)
        self._DistributedBattleBldg__faceOff(ts, self.faceOffName, self._DistributedBattleBldg__handleFaceOffDone)
        return None

    
    def __handleFaceOffDone(self):
        self.notify.debug('FaceOff done')
        self.d_faceOffDone(toonbase.localToon.doId)

    
    def exitFaceOff(self):
        self.notify.debug('exitFaceOff()')
        self.delayDeleteToons(0)
        self.finishInterval(self.faceOffName)
        return None

    
    def enterReward(self, ts):
        self.notify.debug('enterReward()')
        self.delayDeleteToons(1)
        if self.hasLocalToon():
            NametagGlobals.setMasterArrowsOn(0)
        
        self.movie.playReward(ts, self.uniqueName('reward'), self._DistributedBattleBldg__handleRewardDone)
        return None

    
    def __handleRewardDone(self):
        self.notify.debug('Reward done')
        if self.hasLocalToon():
            self.d_rewardDone(toonbase.localToon.doId)
        
        self.movie.resetReward()

    
    def exitReward(self):
        self.notify.debug('exitReward()')
        self.delayDeleteToons(0)
        self.movie.resetReward(finish = 1)
        NametagGlobals.setMasterArrowsOn(1)
        return None

    
    def enterBuildingReward(self, ts):
        self.delayDeleteToons(1)
        if self.hasLocalToon():
            NametagGlobals.setMasterArrowsOn(0)
        
        self.movie.playReward(ts, self.uniqueName('building-reward'), self._DistributedBattleBldg__handleBuildingRewardDone)
        return None

    
    def __handleBuildingRewardDone(self):
        if self.hasLocalToon():
            self.d_rewardDone(toonbase.localToon.doId)
        
        self.movie.resetReward()

    
    def exitBuildingReward(self):
        self.delayDeleteToons(0)
        self.movie.resetReward(finish = 1)
        NametagGlobals.setMasterArrowsOn(1)
        return None

    
    def enterResume(self, ts = 0):
        self.notify.debug('enterResume()')
        if self.hasLocalToon():
            self.removeLocalToon()
        
        return None

    
    def exitResume(self):
        return None


