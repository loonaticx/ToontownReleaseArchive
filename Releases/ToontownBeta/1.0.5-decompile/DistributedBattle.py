# Source Generated with Decompyle++
# File: DistributedBattle.pyo (Python 2.0)

from PandaModules import *
from IntervalGlobal import *
from BattleBase import *
import ToontownGlobals
import DistributedBattleBase
import CollisionSphere
import CollisionNode
import DirectNotifyGlobal
import MovieUtil
import Suit
import Actor
import SuitBattleGlobals

class DistributedBattle(DistributedBattleBase.DistributedBattleBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBattle')
    camFOFov = 30.0
    camFOPos = Point3(0, -10, 4)
    
    def __init__(self, cr):
        DistributedBattleBase.DistributedBattleBase.__init__(self, cr)
        self._DistributedBattle__setupCollisions(self.uniqueName('battle-collide'))

    
    def delete(self):
        DistributedBattleBase.DistributedBattleBase.delete(self)
        self._DistributedBattle__removeCollisionData()

    
    def setPosition(self, x, y, z):
        self.notify.debug('setPosition() - %d %d %d' % (x, y, z))
        pos = Point3(x, y, -0.475)
        self.setPos(pos)

    
    def setInitialSuitPos(self, x, y, z):
        self.initialSuitPos = Point3(x, y, z)
        self.headsUp(self.initialSuitPos)

    
    def setMembers(self, suits, suitsJoining, suitsPending, suitsActive, suitsLured, suitTraps, toons, toonsJoining, toonsPending, toonsActive, toonsRunning, sec, usec):
        oldtoons = DistributedBattleBase.DistributedBattleBase.setMembers(self, suits, suitsJoining, suitsPending, suitsActive, suitsLured, suitTraps, toons, toonsJoining, toonsPending, toonsActive, toonsRunning, sec, usec)
        if len(self.toons) == 4 and len(oldtoons) < 4:
            self.notify.debug('setMembers() - battle is now full of toons')
            self._DistributedBattle__closeBattleCollision()
        elif len(self.toons) < 4 and len(oldtoons) == 4:
            self._DistributedBattle__openBattleCollision()
        

    
    def __setupCollisions(self, name):
        self.cSphere = CollisionSphere.CollisionSphere(0.0, 0.0, 0.0, 9.0)
        self.cSphereNode = CollisionNode.CollisionNode(name)
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.attachNewNode(self.cSphereNode)
        self.cSphereNodePath.reparentTo(hidden)
        self.cSphereNodePath.hide()
        self.cSphereBitMask = ToontownGlobals.WallBitmask
        self.cSphereNode.setCollideMask(self.cSphereBitMask)
        self.cSphere.setTangible(0)

    
    def __removeCollisionData(self):
        del self.cSphere
        del self.cSphereNodePath
        del self.cSphereNode
        self.cSphereBitMask = None

    
    def __enableCollision(self):
        self.cSphereNodePath.reparentTo(self)
        if len(self.toons) < 4:
            self.accept('enter' + self.cSphereNode.getName(), self._DistributedBattle__handleLocalToonCollision)
        

    
    def __handleLocalToonCollision(self, collEntry):
        self.notify.debug('localToonCollision')
        self.cr.playGame.hood.loader.place.setState('WaitForBattle')
        toon = toonbase.localToon
        self.d_toonRequestJoin(toon.doId, toon.getPos(self))
        self.localToonFsm.request('WaitForServer')

    
    def denyLocalToonJoin(self):
        self.notify.debug('denyLocalToonJoin()')
        self.cr.playGame.hood.loader.place.setState('walk')
        self.localToonFsm.request('NoLocalToon')

    
    def __disableCollision(self):
        self.ignore('enter' + self.cSphereNode.getName())
        self.cSphereNodePath.reparentTo(hidden)

    
    def __openBattleCollision(self):
        self.cSphere.setTangible(0)
        if not self.hasLocalToon():
            self._DistributedBattle__enableCollision()
        

    
    def __closeBattleCollision(self):
        self.cSphere.setTangible(1)
        self.ignore('enter' + self.cSphereNode.getName())

    
    def __faceOff(self, ts, name, callback):
        suit = self.suits[0]
        suitSpot = self.srow[0][0]
        suitHpr = self.srowHpr[0][0]
        toon = self.toons[0]
        toonSpot = self.trow[0][0]
        toonHpr = self.trowHpr[0][0]
        suitIvals = []
        toonIvals = []
        camIvals = []
        suitIvals.append(FunctionInterval(suit.loop, extraArgs = [
            'neutral']))
        suitIvals.append(FunctionInterval(suit.headsUp, extraArgs = [
            toon.getPos()]))
        taunt = SuitBattleGlobals.getFaceoffTaunt(suit.getStyleName())
        suitIvals.append(FunctionInterval(suit.setChatAbsolute, extraArgs = [
            taunt,
            CFSpeech | CFTimeout]))
        toonIvals.append(FunctionInterval(toon.loop, extraArgs = [
            'neutral']))
        toonIvals.append(FunctionInterval(toon.headsUp, extraArgs = [
            suit.getPos()]))
        
        def setCamFov(fov):
            base.cam.node().setFov(fov)

        camIvals.append(FunctionInterval(camera.wrtReparentTo, extraArgs = [
            suit]))
        camIvals.append(FunctionInterval(setCamFov, extraArgs = [
            self.camFOFov]))
        camIvals.append(FunctionInterval(camera.setPosHpr, extraArgs = [
            0,
            18,
            suit.getHeight() * 0.66,
            -180,
            5,
            0]))
        delay = FACEOFF_TAUNT_T
        camIvals.append(WaitInterval(delay))
        sFaceSpot = FunctionInterval(suit.headsUp, extraArgs = [
            self,
            suitSpot])
        suitIvals.append((delay, sFaceSpot))
        suitIvals.append(FunctionInterval(suit.clearChat))
        tFaceSpot = FunctionInterval(toon.headsUp, extraArgs = [
            self,
            toonSpot])
        toonIvals.append((delay, tFaceSpot))
        faceoffTime = self.calcFaceoffTime(self.getPos(), self.initialSuitPos)
        suitIvals.append(FunctionInterval(suit.loop, extraArgs = [
            'walk']))
        suitIvals.append(LerpPosInterval(suit, faceoffTime, suitSpot, other = self))
        suitIvals.append(FunctionInterval(suit.loop, extraArgs = [
            'neutral']))
        suitIvals.append(FunctionInterval(suit.setHpr, extraArgs = [
            self,
            suitHpr]))
        toonIvals.append(FunctionInterval(toon.loop, extraArgs = [
            'run']))
        toonIvals.append(LerpPosInterval(toon, faceoffTime, toonSpot, other = self))
        toonIvals.append(FunctionInterval(toon.loop, extraArgs = [
            'neutral']))
        toonIvals.append(FunctionInterval(toon.setHpr, extraArgs = [
            self,
            toonHpr]))
        camIvals.append(FunctionInterval(setCamFov, extraArgs = [
            self.camFov]))
        camIvals.append(FunctionInterval(camera.wrtReparentTo, extraArgs = [
            self]))
        camIvals.append(FunctionInterval(camera.setPos, extraArgs = [
            self.camFOPos]))
        camIvals.append(FunctionInterval(camera.lookAt, extraArgs = [
            suit.getPos(self)]))
        camIvals.append(WaitInterval(faceoffTime))
        suitTrack = Track(suitIvals)
        toonTrack = Track(toonIvals)
        camTrack = Track(camIvals)
        mtrack = MultiTrack([
            suitTrack,
            toonTrack])
        done = FunctionInterval(callback)
        track = Track([
            mtrack,
            done], name)
        dur = track.getDuration()
        if ts <= dur:
            track.play(ts)
            self.activeIntervals[name] = track
            if self.hasLocalToon():
                camTrack.play(ts)
            
        else:
            self.notify.debug('__faceOff() - ts: %f dur: %f' % (ts, dur))
            track.setT(dur, event = IVAL_INIT)

    
    def enterFaceOff(self, ts):
        self.notify.debug('enterFaceOff()')
        self.delayDeleteToons(1)
        self._DistributedBattle__faceOff(ts, self.faceOffName, self._DistributedBattle__handleFaceOffDone)
        return None

    
    def __handleFaceOffDone(self):
        self.notify.debug('FaceOff done')
        if toonbase.localToon == self.toons[0]:
            self.d_faceOffDone(toonbase.localToon.doId)
        

    
    def exitFaceOff(self):
        self.notify.debug('exitFaceOff()')
        self.delayDeleteToons(0)
        self.finishInterval(self.faceOffName)
        return None

    
    def enterReward(self, ts):
        self.notify.debug('enterReward()')
        self._DistributedBattle__disableCollision()
        self.delayDeleteToons(1)
        if self.hasLocalToon():
            NametagGlobals.setMasterArrowsOn(0)
            if self.localToonActive() == 0:
                self.removeInactiveLocalToon(toonbase.localToon)
            
        
        self.movie.playReward(ts, self.uniqueName('reward'), self._DistributedBattle__handleRewardDone)
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

    
    def enterResume(self, ts = 0):
        self.notify.debug('enterResume()')
        if self.hasLocalToon():
            self.removeLocalToon()
        
        return None

    
    def exitResume(self):
        return None

    
    def enterNoLocalToon(self):
        self.notify.debug('enterNoLocalToon()')
        self._DistributedBattle__enableCollision()
        return None

    
    def exitNoLocalToon(self):
        self._DistributedBattle__disableCollision()
        return None

    
    def enterWaitForServer(self):
        self.notify.debug('enterWaitForServer()')
        return None

    
    def exitWaitForServer(self):
        return None


