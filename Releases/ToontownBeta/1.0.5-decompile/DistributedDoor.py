# Source Generated with Decompyle++
# File: DistributedDoor.pyo (Python 2.0)

from ToonBaseGlobal import *
from ShowBaseGlobal import *
from IntervalGlobal import *
from ClockDelta import *
import DirectNotifyGlobal
import FSM
import DistributedObject

class DistributedDoor(DistributedObject.DistributedObject):
    doorAnimationTest = 0
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.fsm = FSM.FSM('DistributedDoor_right', [
            State.State('off', self.enterOff, self.exitOff, [
                'closing',
                'closed',
                'opening',
                'open']),
            State.State('closing', self.enterClosing, self.exitClosing, [
                'closed',
                'opening']),
            State.State('closed', self.enterClosed, self.exitClosed, [
                'opening']),
            State.State('opening', self.enterOpening, self.exitOpening, [
                'open']),
            State.State('open', self.enterOpen, self.exitOpen, [
                'closing',
                'open'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.exitDoorFSM = FSM.FSM('DistributedDoor_left', [
            State.State('off', self.exitDoorEnterOff, self.exitDoorExitOff, [
                'closing',
                'closed',
                'opening',
                'open']),
            State.State('closing', self.exitDoorEnterClosing, self.exitDoorExitClosing, [
                'closed',
                'opening']),
            State.State('closed', self.exitDoorEnterClosed, self.exitDoorExitClosed, [
                'opening']),
            State.State('opening', self.exitDoorEnterOpening, self.exitDoorExitOpening, [
                'open']),
            State.State('open', self.exitDoorEnterOpen, self.exitDoorExitOpen, [
                'closing',
                'open'])], 'off', 'off')
        self.exitDoorFSM.enterInitialState()

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        self.skipClosedDoor = 1
        self.avatarTracks = []
        self.avatarExitTracks = []
        self.avatarIDList = []
        self.doorTrack = None
        self.doorExitTrack = None

    
    def disable(self):
        self.fsm.request('off')
        self.exitDoorFSM.request('off')
        self.finishDoorTrack()
        if self.__dict__.has_key('building'):
            del self.building
        
        self.ignoreAll()
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        del self.fsm
        del self.exitDoorFSM
        DistributedObject.DistributedObject.delete(self)

    
    def setBlock(self, block):
        self.block = block
        self.accept('enterdoor_trigger_' + self.block, self.doorTrigger)

    
    def setSwing(self, flags):
        self.swing = flags & 1 != 0
        self.exitDoorSwing = flags & 2 != 0

    
    def setOtherZoneIDAndDOID(self, zoneID, distributedObjectID):
        self.otherZoneID = zoneID
        self.otherDOID = distributedObjectID

    
    def setState(self, state, sec, usec):
        self.fsm.request(state, [
            localElapsedTime(sec, usec)])

    
    def setExitDoorState(self, state, sec, usec):
        self.exitDoorFSM.request(state, [
            localElapsedTime(sec, usec)])

    
    def __getBuilding(self):
        if not self.__dict__.has_key('building'):
            if self.cr.playGame.hood.loader.geom.isEmpty():
                self.building = render.find('**/leftDoor')
                self.building.shorten()
            else:
                self.building = self.cr.playGame.hood.loader.geom.find('**/??' + self.block + ':*_landmark_*_DNARoot')
        
        return self.building

    
    def avatarInstantFeedbackTrack(self, avatar, duration):
        placeCamera = []
        placeCamera.append(LerpPosHprInterval(node = camera, other = avatar, duration = duration, pos = Point3(-10, -2, avatar.getHeight() + 2), hpr = Point3(-79, -20, 0), blendType = 'easeIn'))
        track = Track(placeCamera)
        return track

    
    def doorTrigger(self, args):
        self.cr.playGame.hood.loader.place.fsm.request('doorOut', [
            { }])
        toonbase.localToon.b_setAnimState('neutral', toonbase.localToon.animMultiplier)
        toonbase.localToon.b_setAnimState('off', toonbase.localToon.animMultiplier)
        self.avatarTrack = self.avatarInstantFeedbackTrack(toonbase.localToon, 1.0)
        self.avatarTrack.play()
        self.sendUpdate('requestEnter')

    
    def readyToExit(self):
        self.sendUpdate('requestExit')

    
    def avatarEnterDoorTrack(self, avatar, duration):
        placeCamera = []
        if avatar.doId == toonbase.localToon.doId:
            placeCamera.append(LerpPosHprInterval(node = camera, other = avatar, duration = duration, pos = Point3(0, -8, avatar.getHeight()), hpr = Point3(0, 0, 0), blendType = 'easeInOut'))
        else:
            placeCamera.append(WaitInterval(duration = duration))
        posHpr = self.cr.playGame.dnaStore.getPosHprFromBlockNumber(int(self.block))
        node = Node()
        otherNP = hidden.attachNewNode(node)
        otherNP.setPos(posHpr.getPos())
        otherNP.setHpr(posHpr.getHpr())
        moveHere = []
        moveHere.append(FunctionInterval(avatar.loop, extraArgs = [
            'walk']))
        moveHere.append(LerpPosHprInterval(node = avatar, other = otherNP, duration = duration, hpr = Point3(0, 0, 0), pos = Point3(1.5, 2, 0), blendType = 'easeIn'))
        if avatar.doId == toonbase.localToon.doId:
            request = {
                'mode': 'toonInterior',
                'hoodId': self.otherZoneID - self.otherZoneID % 100,
                'zoneId': self.otherZoneID,
                'avId': -1,
                'doorDOID': self.otherDOID }
            if self.otherZoneID % 1000 == 0:
                request['mode'] = 'playground'
            
            moveHere.append(FunctionInterval(self.cr.playGame.hood.loader.setState, extraArgs = [
                'waitForQuietZoneResponse',
                request]))
            moveHere.append(FunctionInterval(sys.stdout.write, extraArgs = [
                'end track enter door.\n\n']))
        
        track = MultiTrack([
            Track(placeCamera),
            Track(moveHere)], 'avatarEnterDoorTrack')
        return track

    
    def avatarEnqueueTrack(self, avatar, duration):
        posHpr = self.cr.playGame.dnaStore.getPosHprFromBlockNumber(int(self.block))
        standHere = []
        offset = Point3(1.5, -3 + -2 * len(self.avatarIDList), 0)
        node = Node()
        otherNP = hidden.attachNewNode(node)
        otherNP.setPos(posHpr.getPos())
        otherNP.setHpr(posHpr.getHpr())
        walkLike = [
            ActorInterval(avatar, 'walk', startTime = 1, duration = duration, endTime = 0.0001)]
        standHere.append(LerpPosHprInterval(node = avatar, other = otherNP, duration = duration, hpr = Point3(0, 0, 0), pos = offset, blendType = 'easeInOut'))
        standHere.append(FunctionInterval(avatar.loop, extraArgs = [
            'neutral']))
        track = MultiTrack([
            Track(walkLike),
            Track(standHere)], 'avatarEnqueueTrack')
        return track

    
    def toonEnter(self, avatarID):
        avatar = self.cr.doId2do[avatarID]
        track = self.avatarEnqueueTrack(avatar, 0.5)
        track.play()
        self.avatarTracks.append(track)
        self.avatarIDList.append(avatarID)

    
    def rejectEnter(self):
        pass

    
    def avatarExitTrack(self, avatar, duration):
        posHpr = self.cr.playGame.dnaStore.getPosHprFromBlockNumber(int(self.block))
        node = Node()
        otherNP = hidden.attachNewNode(node)
        otherNP.setPos(posHpr.getPos())
        otherNP.setHpr(posHpr.getHpr())
        moveCamera = []
        if avatar.doId == toonbase.localToon.doId:
            moveCamera.append(WaitInterval(duration = 2.0))
            moveCamera.append(PosHprInterval(camera, Point3(avatar.getPos() + Point3(-1.5, -5, avatar.getHeight())), Point3(avatar.getHpr() + Point3(179, 0, 0))))
            moveCamera.append(LerpPosHprInterval(node = camera, other = avatar, duration = duration * 2, pos = Point3(-1.5, -5, avatar.getHeight() + 2.0), hpr = Point3(179, 0, 0), blendType = 'easeInOut'))
            moveCamera.append(FunctionInterval(self.exitCompleted))
        else:
            moveCamera.append(WaitInterval(duration = 2.0 + duration))
        standHere = []
        standHere.append(WaitInterval(duration = 2.0))
        standHere.append(FunctionInterval(avatar.loop, extraArgs = [
            'walk']))
        standHere.append(PosHprInterval(avatar, Point3(otherNP.getPos() + Point3(-1.5, 2, 0)), Point3(otherNP.getHpr() + Point3(179, 0, 0))))
        standHere.append(LerpPosHprInterval(node = avatar, other = otherNP, duration = duration, hpr = Point3(179, 0, 0), pos = Point3(-1.5, -5, 0), blendType = 'easeInOut'))
        if avatar.doId == toonbase.localToon.doId:
            standHere.append(FunctionInterval(self.cr.playGame.hood.loader.place.setState, extraArgs = [
                'walk']))
        
        track = MultiTrack([
            Track(moveCamera),
            Track(standHere)], 'avatarExitTrack')
        return track

    
    def exitCompleted(self):
        self.cr.playGame.hood.loader.doneStatus['mode'] = 'doorOut'
        toonbase.localToon.b_setAnimState('walk', toonbase.localToon.animMultiplier)
        self.cr.playGame.hood.loader.place.fsm.request('walk')

    
    def toonExit(self, avatarID):
        if avatarID in self.avatarIDList:
            self.avatarIDList.remove(avatarID)
            if avatarID == toonbase.localToon.doId:
                self.exitCompleted()
            
        else:
            avatar = self.cr.doId2do[avatarID]
            track = self.avatarExitTrack(avatar, 0.2)
            track.play()
            self.avatarExitTracks.append(track)

    
    def finishDoorTrack(self):
        if self.doorTrack and self.doorTrack.isPlaying():
            self.doorTrack.stop()
            self.doorTrack.setFinalT()
            self.doorTrack = None
        

    
    def finishExitDoorDoorTrack(self):
        if self.doorExitTrack and self.doorExitTrack.isPlaying():
            self.doorExitTrack.stop()
            self.doorExitTrack.setFinalT()
            self.doorExitTrack = None
        

    
    def teleport(self):
        self._DistributedDoor__teleportToSafeZone(toonbase.localToon)

    
    def __teleportToSafeZone(self, toon):
        if toon.doId == toonbase.localToon.doId:
            camera.wrtReparentTo(toonbase.localToon)
            base.cam.node().setFov(DefaultCameraFov)
            target_sz = toonbase.localToon.defaultZone
            self.cr.playGame.hood.loader.place.fsm.request('teleportOut', [
                {
                    'mode': 'teleportOut',
                    'hoodId': target_sz,
                    'zoneId': target_sz,
                    'avId': -1 }])
        

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterClosing(self, ts):
        building = self._DistributedDoor__getBuilding()
        rightDoor = building.find('rightDoor')
        if not rightDoor.isEmpty():
            self.finishDoorTrack()
            newHpr = rightDoor.getHpr() + Vec3(-90, 0, 0)
            closeRightDoor = []
            closeRightDoor.append(LerpHprInterval(node = rightDoor, duration = 1.0, hpr = newHpr, blendType = 'easeInOut'))
            self.doorTrack = Track(closeRightDoor)
            self.doorTrack.play()
        else:
            self.notify.error('enterOpening(): did not find rightDoor')

    
    def exitClosing(self):
        pass

    
    def enterClosed(self, ts):
        if self.skipClosedDoor:
            self.skipClosedDoor = 0
            return None
        
        building = self._DistributedDoor__getBuilding()
        doorFrameHoleLeft = building.find('**/*_front/**/doorFrameHoleLeft')
        if not doorFrameHoleLeft.isEmpty():
            doorFrameHoleLeft.hide()
        else:
            self.notify.error('enterClosed(): did not find doorFrameHoleLeft')
        doorFrameHoleRight = building.find('**/*_front/**/doorFrameHoleRight')
        if not doorFrameHoleRight.isEmpty():
            doorFrameHoleRight.hide()
        else:
            self.notify.error('enterClosed(): did not find doorFrameHoleRight')
        leftDoor = building.find('leftDoor')
        if not leftDoor.isEmpty():
            leftDoor.hide()
        else:
            self.notify.error('enterClosed(): did not find leftDoor')
        rightDoor = building.find('rightDoor')
        if not rightDoor.isEmpty():
            rightDoor.hide()
        else:
            self.notify.error('enterClosed(): did not find rightDoor')

    
    def exitClosed(self):
        pass

    
    def enterOpening(self, ts):
        self.skipClosedDoor = 0
        building = self._DistributedDoor__getBuilding()
        leftDoor = building.find('leftDoor')
        if not leftDoor.isEmpty():
            leftDoor.show()
        else:
            self.notify.error('enterOpening(): did not find leftDoor')
        rightDoor = building.find('rightDoor')
        if not rightDoor.isEmpty():
            rightDoor.show()
            self.finishDoorTrack()
            newHpr = rightDoor.getHpr() + Vec3(90, 0, 0)
            openRightDoor = []
            openRightDoor.append(WaitInterval(duration = 0.4))
            openRightDoor.append(LerpHprInterval(node = rightDoor, duration = 0.6, hpr = newHpr, blendType = 'easeInOut'))
        else:
            self.notify.error('enterOpening(): did not find rightDoor')
        doorFrameHoleLeft = building.find('**/*_front/**/doorFrameHoleLeft;+s')
        if not doorFrameHoleLeft.isEmpty():
            doorFrameHoleLeft.show()
        
        doorFrameHoleRight = building.find('**/*_front/**/doorFrameHoleRight;+s')
        if not doorFrameHoleRight.isEmpty():
            doorFrameHoleRight.show()
        
        self.doorTrack = Track(openRightDoor)
        self.doorTrack.play()

    
    def exitOpening(self):
        self.finishDoorTrack()

    
    def enterOpen(self, ts):
        for avatarID in self.avatarIDList:
            avatar = self.cr.doId2do[avatarID]
            track = self.avatarEnterDoorTrack(avatar, 1.0)
            track.play()
            self.avatarTracks.append(track)
        
        self.avatarIDList = []

    
    def exitOpen(self):
        for track in self.avatarTracks:
            if track.isPlaying():
                track.stop()
                track.setFinalT()
            
        
        self.avatarTracks = []

    
    def exitDoorEnterOff(self):
        pass

    
    def exitDoorExitOff(self):
        pass

    
    def exitDoorEnterClosing(self, ts):
        building = self._DistributedDoor__getBuilding()
        leftDoor = building.find('leftDoor')
        if not leftDoor.isEmpty():
            self.finishExitDoorDoorTrack()
            newHpr = leftDoor.getHpr() + Vec3(90, 0, 0)
            closeLeftDoor = []
            closeLeftDoor.append(LerpHprInterval(node = leftDoor, duration = 1.0, hpr = newHpr, blendType = 'easeInOut'))
            self.doorExitTrack = Track(closeLeftDoor)
            self.doorExitTrack.play()
        else:
            self.notify.error('enterOpening(): did not find leftDoor')

    
    def exitDoorExitClosing(self):
        pass

    
    def exitDoorEnterClosed(self, ts):
        pass

    
    def exitDoorExitClosed(self):
        pass

    
    def exitDoorEnterOpening(self, ts):
        building = self._DistributedDoor__getBuilding()
        leftDoor = building.find('leftDoor')
        if not leftDoor.isEmpty():
            leftDoor.show()
            self.finishExitDoorDoorTrack()
            newHpr = leftDoor.getHpr() + Vec3(-90, 0, 0)
            openLeftDoor = []
            openLeftDoor.append(LerpHprInterval(node = leftDoor, duration = 0.6, hpr = newHpr, blendType = 'easeInOut'))
        else:
            self.notify.error('exitDoorEnterOpening(): did not find leftDoor')
        doorFrameHoleLeft = building.find('**/*_front/**/doorFrameHoleLeft;+s')
        if not doorFrameHoleLeft.isEmpty():
            doorFrameHoleLeft.show()
        
        doorFrameHoleRight = building.find('**/*_front/**/doorFrameHoleRight;+s')
        if not doorFrameHoleRight.isEmpty():
            doorFrameHoleRight.show()
        
        self.exitDoorTrack = Track(openLeftDoor)
        self.exitDoorTrack.play()

    
    def exitDoorExitOpening(self):
        pass

    
    def exitDoorEnterOpen(self, ts):
        pass

    
    def exitDoorExitOpen(self):
        pass


