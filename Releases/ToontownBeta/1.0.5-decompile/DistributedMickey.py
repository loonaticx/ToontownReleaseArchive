# Source Generated with Decompyle++
# File: DistributedMickey.pyo (Python 2.0)

from ShowBaseGlobal import *
from IntervalGlobal import *
from ClockDelta import *
import AvatarDNA
import DistributedChar
import DirectNotifyGlobal
import FSM
import State
import ToontownGlobals
import MickeyChatter
import MickeyPaths
import string
import copy

class DistributedMickey(DistributedChar.DistributedChar):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMickey')
    
    def __init__(self, cr):
        
        try:
            self.DistributedMickey_initialized
        except:
            self.DistributedMickey_initialized = 1
            DistributedChar.DistributedChar.__init__(self, cr)
            dna = AvatarDNA.AvatarDNA()
            dna.newChar('mk')
            self.setDNA(dna)
            self.setName('Mickey')
            self.fsm = FSM.FSM('DistributedMickey', [
                State.State('Off', self.enterOff, self.exitOff, [
                    'Neutral']),
                State.State('Neutral', self.enterNeutral, self.exitNeutral, [
                    'Walk']),
                State.State('Walk', self.enterWalk, self.exitWalk, [
                    'Neutral'])], 'Off', 'Off')
            self.fsm.enterInitialState()
            self._DistributedMickey__initCollisions()


    
    def __del__(self):
        self._DistributedMickey__deleteCollisions()

    
    def __initCollisions(self):
        self.cSphere = CollisionSphere(0.0, 0.0, 0.0, 8.0)
        self.cSphere.setTangible(0)
        self.cSphereNode = CollisionNode('mickeyBlatherSphere')
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.attachNewNode(self.cSphereNode)
        self.cSphereNodePath.hide()
        self.cSphereNode.setCollideMask(ToontownGlobals.WallBitmask)
        self.acceptOnce('enter' + self.cSphereNode.getName(), self._DistributedMickey__handleCollisionSphereEnter)

    
    def __deleteCollisions(self):
        del self.cSphere
        del self.cSphereNode
        self.cSphereNodePath.removeNode()
        del self.cSphereNodePath

    
    def __doDisableStuff(self):
        self.ignore('exitSafeZone')
        self.stopBlink()
        self.ignoreAll()
        self._DistributedMickey__chatTrack.stop()
        self.fsm.requestFinalState()

    
    def disable(self):
        self._DistributedMickey__doDisableStuff()
        DistributedChar.DistributedChar.disable(self)

    
    def delete(self):
        
        try:
            self.DistributedMickey_deleted
        except:
            self.DistributedMickey_deleted = 1
            self._DistributedMickey__doDisableStuff()
            DistributedChar.DistributedChar.delete(self)


    
    def generate(self):
        DistributedChar.DistributedChar.generate(self)
        self.reparentTo(render)
        self.setPos(MickeyPaths.getNodePos(MickeyPaths.startNode))
        self.setHpr(0, 0, 0)
        self.startBlink()
        self._DistributedMickey__chatTrack = Track([])
        self.acceptOnce('enter' + self.cSphereNode.getName(), self._DistributedMickey__handleCollisionSphereEnter)
        self.accept('exitSafeZone', self._DistributedMickey__handleExitSafeZone)
        self.fsm.request('Neutral')

    
    def __handleExitSafeZone(self):
        self._DistributedMickey__handleCollisionSphereExit(None)

    
    def __handleCollisionSphereEnter(self, collEntry):
        self.notify.debug('Entering collision sphere...')
        toon = toonbase.localToon
        self.sendUpdate('avatarEnter', [
            toonbase.localToon.getDoId()])
        self.accept('chatUpdate', self._DistributedMickey__handleChatUpdate)
        self.accept('chatUpdateQT', self._DistributedMickey__handleChatUpdateQT)
        self.acceptOnce('exit' + self.cSphereNode.getName(), self._DistributedMickey__handleCollisionSphereExit)

    
    def __handleCollisionSphereExit(self, collEntry):
        self.notify.debug('Exiting collision sphere...')
        toon = toonbase.localToon
        self.sendUpdate('avatarExit', [
            toonbase.localToon.getDoId()])
        self.ignore('chatUpdate')
        self.ignore('chatUpdateQT')
        self.acceptOnce('enter' + self.cSphereNode.getName(), self._DistributedMickey__handleCollisionSphereEnter)

    
    def __handleChatUpdate(self, msg, chatFlats):
        self.sendUpdate('setNearbyAvatarChat', [
            toonbase.localToon.getDoId(),
            msg])

    
    def __handleChatUpdateQT(self, qtList):
        self.sendUpdate('setNearbyAvatarQT', [
            toonbase.localToon.getDoId(),
            qtList])

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterNeutral(self):
        self.notify.debug('Neutral Mickey...')
        self.loop('neutral')

    
    def exitNeutral(self):
        pass

    
    def enterWalk(self):
        self.notify.debug('Walking Mickey... from ' + str(self._DistributedMickey__walkInfo[0]) + ' to ' + str(self._DistributedMickey__walkInfo[1]))
        posPoints = MickeyPaths.getPointsFromTo(self._DistributedMickey__walkInfo[0], self._DistributedMickey__walkInfo[1])
        moveTrack = self._DistributedMickey__makePathTrack(self, posPoints, ToontownGlobals.MickeySpeed)
        animTrack = Track([
            FunctionInterval(self.loop, extraArgs = [
                'walk'])])
        walkAnimTrack = MultiTrack([
            moveTrack,
            animTrack])
        doneTrack = Track([
            FunctionInterval(messenger.send, extraArgs = [
                'mickeyWalkDone'])])
        self._DistributedMickey__walkTrack = Track([
            walkAnimTrack,
            doneTrack])
        self.accept('mickeyWalkDone', self._DistributedMickey__doneWalking)
        self._DistributedMickey__walkTrack.play(localElapsedTime(self._DistributedMickey__walkInfo[2], self._DistributedMickey__walkInfo[3]))

    
    def __doneWalking(self):
        self.fsm.request('Neutral')

    
    def exitWalk(self):
        self.ignore('mickeyWalkDone')
        self._DistributedMickey__walkTrack.stop()
        self._DistributedMickey__walkTrack.setFinalT()

    
    def __makeTurnToHeadingTrack(self, heading):
        curHpr = self.getHpr()
        destHpr = self.getHpr()
        destHpr.setX(heading)
        turnVel = 180.0
        distance = abs(min(360.0, destHpr[0]) - min(360.0, curHpr[0]))
        if distance > 180.0:
            distance = 180.0 - distance - 180.0
        
        time = distance / turnVel
        turnTracks = []
        if time > 0.2:
            turnTracks.append(Track([
                FunctionInterval(self.loop, extraArgs = [
                    'walk']),
                WaitInterval(time),
                FunctionInterval(self.loop, extraArgs = [
                    'neutral'])]))
        
        turnTracks.append(Track([
            LerpHprInterval(self, time, destHpr, name = 'lerpMickeyHpr')]))
        return MultiTrack(turnTracks)

    
    def setChat(self, category, msg, avId):
        if self.cr.doId2do.has_key(avId):
            avatar = self.cr.doId2do[avId]
            str = MickeyChatter.MickeyChatter[category][msg]
            if '%' in str:
                str = copy.deepcopy(str)
                avName = avatar.getName()
                str = string.replace(str, '%', avName)
            
            tracks = []
            if category != MickeyChatter.GOODBYE:
                curHpr = self.getHpr()
                self.lookAt(avatar)
                destHpr = self.getHpr()
                self.setHpr(curHpr)
                tracks.append(self._DistributedMickey__makeTurnToHeadingTrack(destHpr[0]))
            
            tracks.append(Track([
                FunctionInterval(self.setChatAbsolute, extraArgs = [
                    str,
                    CFSpeech | CFTimeout])]))
            self._DistributedMickey__chatTrack.stop()
            self._DistributedMickey__chatTrack = Track(tracks)
            self._DistributedMickey__chatTrack.play()
        

    
    def __makePathTrack(self, nodePath, posPoints, velocity):
        intervals = []
        for pointIndex in range(len(posPoints) - 1):
            startPoint = posPoints[pointIndex]
            endPoint = posPoints[pointIndex + 1]
            intervals.append(FunctionInterval(nodePath.setPos, extraArgs = [
                startPoint]))
            intervals.append(FunctionInterval(nodePath.headsUpPreserveScale, extraArgs = [
                endPoint[0],
                endPoint[1],
                endPoint[2]]))
            distance = Vec3(endPoint - startPoint).length()
            duration = distance / velocity
            intervals.append(LerpPosInterval(nodePath, duration = duration, pos = Point3(endPoint), startPos = Point3(startPoint)))
        
        track = Track(intervals)
        return track

    
    def setWalk(self, srcNode, destNode, sec, usec):
        self._DistributedMickey__walkInfo = (srcNode, destNode, sec, usec)
        self.fsm.request('Walk')


