# Source Generated with Decompyle++
# File: DistributedToon.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
from ClockDelta import *
from IntervalGlobal import *
import DirectNotifyGlobal
import DistributedAvatar
import Toon
import FSM

class DistributedToon(DistributedAvatar.DistributedAvatar, Toon.Toon):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToon')
    notify.setDebug(1)
    
    def __init__(self, cr):
        
        try:
            self.DistributedToon_initialized
        except:
            self.DistributedToon_initialized = 1
            DistributedAvatar.DistributedAvatar.__init__(self, cr)
            Toon.Toon.__init__(self)
            self.safeZonesVisited = []
            self.teleportCheat = base.config.GetBool('teleport-all', 0)
            self.track = None
            self.animFSM = FSM.FSM('DistributedToon', [
                State.State('off', self.enterOff, self.exitOff, [
                    'neutral',
                    'sad-neutral',
                    'walk',
                    'run',
                    'sad-walk',
                    'swim',
                    'OpenBook',
                    'ReadBook',
                    'CloseBook',
                    'TeleportOut',
                    'TeleportIn']),
                State.State('neutral', self.enterNeutral, self.exitNeutral, [
                    'sad-neutral',
                    'walk',
                    'run',
                    'swim',
                    'sad-walk',
                    'off',
                    'OpenBook',
                    'ReadBook',
                    'CloseBook',
                    'TeleportOut',
                    'TeleportIn']),
                State.State('sad-neutral', self.enterSadNeutral, self.exitSadNeutral, [
                    'neutral',
                    'walk',
                    'run',
                    'swim',
                    'sad-walk',
                    'off',
                    'OpenBook',
                    'ReadBook',
                    'CloseBook',
                    'TeleportOut',
                    'TeleportIn']),
                State.State('walk', self.enterWalk, self.exitWalk, [
                    'neutral',
                    'sad-neutral',
                    'run',
                    'swim',
                    'sad-walk',
                    'off',
                    'OpenBook',
                    'ReadBook',
                    'CloseBook',
                    'TeleportOut',
                    'TeleportIn']),
                State.State('run', self.enterRun, self.exitRun, [
                    'walk',
                    'neutral',
                    'sad-neutral',
                    'swim',
                    'sad-walk',
                    'off',
                    'OpenBook',
                    'ReadBook',
                    'CloseBook',
                    'TeleportOut',
                    'TeleportIn']),
                State.State('swim', self.enterSwim, self.exitSwim, [
                    'walk',
                    'run',
                    'neutral',
                    'sad-neutral',
                    'sad-walk',
                    'OpenBook',
                    'ReadBook',
                    'CloseBook',
                    'TeleportIn',
                    'TeleportOut',
                    'off']),
                State.State('sad-walk', self.enterSadWalk, self.exitSadWalk, [
                    'walk',
                    'run',
                    'neutral',
                    'sad-neutral',
                    'swim',
                    'off',
                    'OpenBook',
                    'ReadBook',
                    'CloseBook',
                    'TeleportIn',
                    'TeleportOut']),
                State.State('OpenBook', self.enterOpenBook, self.exitOpenBook, [
                    'walk',
                    'run',
                    'neutral',
                    'sad-neutral',
                    'swim',
                    'off',
                    'ReadBook',
                    'CloseBook',
                    'TeleportIn',
                    'TeleportOut']),
                State.State('ReadBook', self.enterReadBook, self.exitReadBook, [
                    'walk',
                    'run',
                    'neutral',
                    'sad-neutral',
                    'off',
                    'sad-walk',
                    'OpenBook',
                    'CloseBook',
                    'TeleportIn',
                    'TeleportOut']),
                State.State('CloseBook', self.enterCloseBook, self.exitCloseBook, [
                    'walk',
                    'run',
                    'neutral',
                    'sad-neutral',
                    'off',
                    'sad-walk',
                    'OpenBook',
                    'ReadBook',
                    'TeleportIn',
                    'TeleportOut']),
                State.State('TeleportOut', self.enterTeleportOut, self.exitTeleportOut, [
                    'walk',
                    'run',
                    'neutral',
                    'sad-neutral',
                    'off',
                    'sad-walk',
                    'TeleportIn']),
                State.State('TeleportIn', self.enterTeleportIn, self.exitTeleportIn, [
                    'walk',
                    'run',
                    'swim',
                    'neutral',
                    'sad-neutral',
                    'off',
                    'sad-walk',
                    'OpenBook',
                    'TeleportOut'])], 'off', 'off')

        self.animFSM.enterInitialState()
        return None

    
    def disable(self):
        self.animFSM.request('off')
        self.stopBlink()
        self.stopLookAroundNow()
        if self.track != None:
            self.track.stop()
        
        self.track = None
        DistributedAvatar.DistributedAvatar.disable(self)

    
    def delete(self):
        
        try:
            self.DistributedToon_deleted
        except:
            self.DistributedToon_deleted = 1
            self.stopBlink()
            self.stopLookAroundNow()
            del self.animFSM
            del self.safeZonesVisited
            DistributedAvatar.DistributedAvatar.delete(self)
            Toon.Toon.delete(self)


    
    def generate(self):
        self.startBlink()
        DistributedAvatar.DistributedAvatar.generate(self)

    
    def setDefaultShard(self, shard):
        self.defaultShard = shard
        self.notify.debug('setting default shard to %s' % shard)

    
    def setDefaultZone(self, zone):
        hoodPhase = toonbase.tcr.hoodMgr.getPhaseFromHood(zone)
        if launcher and not launcher.getPhaseComplete(hoodPhase):
            self.notify.debug('default zone %s not downloaded yet. Reverting to ToontownCentral.' % zone)
            self.defaultZone = ToontownCentral
        else:
            self.notify.debug('setting default zone to %s' % zone)
            self.defaultZone = zone

    
    def setShtickerBook(self, string):
        self.notify.debug('setting Shticker Book to %s' % string)

    
    def setFriendsList(self, friendsList):
        self.friendsList = friendsList
        self.notify.debug('setting friends list to %s' % self.friendsList)
        messenger.send('friendsListChanged')

    
    def setInterface(self, string):
        self.notify.debug('setting interface to %s' % string)

    
    def setZonesVisited(self, hoods):
        self.safeZonesVisited = hoods
        self.notify.debug('setting safe zone list to %s' % self.safeZonesVisited)

    
    def setHoodsVisited(self, hoods):
        self.hoodsVisited = hoods
        self.notify.debug('setting hood list to %s' % self.hoodsVisited)

    
    def getStarLevel(self):
        level = 0
        for i in range(len(StarHPLevels)):
            if self.maxHp < StarHPLevels[i]:
                break
            else:
                level = i + 1
        
        return level

    
    def setTutorialAck(self, tutorialAck):
        self.tutorialAck = tutorialAck
        return None

    
    def b_setAnimState(self, animName, animMultiplier, callback = None, extraArgs = []):
        self.setAnimState(animName, animMultiplier, None, None, callback, extraArgs)
        self.d_setAnimState(animName, animMultiplier)

    
    def d_setAnimState(self, animName, animMultiplier):
        timestamp = getServerTime()
        self.sendUpdate('setAnimState', [
            animName,
            animMultiplier] + timestamp)
        return None

    
    def setAnimState(self, animName, animMultiplier, sec, usec, callback = None, extraArgs = []):
        if sec == None:
            ts = 0.0
        else:
            ts = localElapsedTime(sec, usec)
        self.animFSM.request(animName, [
            ts,
            callback,
            extraArgs])
        if animName != 'off' and animName != 'OpenBook' and animName != 'ReadBook' and animName != 'CloseBook' and animName != 'TeleportIn' and animName != 'TeleportOut':
            self.setPlayRate(animMultiplier, animName)
        
        return None

    
    def enterOff(self, ts = 0, callback = None, extraArgs = []):
        pass

    
    def exitOff(self):
        pass

    
    def enterNeutral(self, ts = 0, callback = None, extraArgs = []):
        self.loop('neutral')
        return None

    
    def exitNeutral(self):
        self.stop()
        return None

    
    def enterSadNeutral(self, ts = 0, callback = None, extraArgs = []):
        self.loop('sad-neutral')
        return None

    
    def exitSadNeutral(self):
        self.stop()
        return None

    
    def enterWalk(self, ts = 0, callback = None, extraArgs = []):
        self.loop('walk')
        return None

    
    def exitWalk(self):
        self.stop()
        return None

    
    def enterRun(self, ts = 0, callback = None, extraArgs = []):
        self.loop('run')
        return None

    
    def exitRun(self):
        self.stop()
        return None

    
    def enterSwim(self, ts = 0, callback = None, extraArgs = []):
        self.loop('swim')
        self.getGeomNode().setP(-89.0)
        self.getGeomNode().setZ(4.0)
        for shadow in self.dropShadows:
            shadow.hide()
        
        self._DistributedToon__startBobSwimTask()
        return None

    
    def exitSwim(self):
        self.stop()
        self.getGeomNode().setPos(0, 0, 0)
        self.getGeomNode().setHpr(0, 0, 0)
        for shadow in self.dropShadows:
            shadow.show()
        
        self._DistributedToon__stopBobSwimTask()
        return None

    
    def __startBobSwimTask(self):
        swimTaskName = self.taskName('swimBobTask')
        taskMgr.removeTasksNamed('swimTask')
        taskMgr.removeTasksNamed(swimTaskName)
        newTask = Task.loop(self.getGeomNode().lerpPosXYZ(0, -3, 3, 1, blendType = 'easeInOut'), self.getGeomNode().lerpPosXYZ(0, -3, 4, 1, blendType = 'easeInOut'))
        taskMgr.spawnTaskNamed(newTask, swimTaskName)
        return None

    
    def __stopBobSwimTask(self):
        swimTaskName = self.taskName('swimBobTask')
        taskMgr.removeTasksNamed(swimTaskName)
        return None

    
    def enterSadWalk(self, ts = 0, callback = None, extraArgs = []):
        self.loop('sad-walk')
        return None

    
    def exitSadWalk(self):
        self.stop()
        return None

    
    def enterOpenBook(self, ts = 0, callback = None, extraArgs = []):
        self.stopLookAround()
        self.lerpLookAt(Point3(0, 1, -2))
        if callback != None:
            readTrack = Track([
                ActorInterval(self, 'book', startTime = 1.2, endTime = 1.5),
                WaitInterval(0.5),
                FunctionInterval(callback)])
        else:
            readTrack = Track([
                ActorInterval(self, 'book', startTime = 1.2, endTime = 1.5)])
        bookIvals = [
            FunctionInterval(self.showBooks)]
        bookTracks = []
        for bookActor in self.bookActors:
            bookTracks.append(Track([
                ActorInterval(bookActor, 'book', startTime = 1.2, endTime = 1.5)]))
        
        bookIvals.append(MultiTrack(bookTracks))
        bookTrack = Track(bookIvals)
        self.track = MultiTrack([
            readTrack,
            bookTrack])
        dur = self.track.getDuration()
        if ts <= dur:
            self.track.play(ts)
        else:
            self.track.setT(dur)
            self.notify.debug('enterOpenBook() - ts: %f dur: %f' % (ts, dur))
        return None

    
    def exitOpenBook(self):
        if self.track != None:
            if self.track.isPlaying():
                self.track.stop()
            
        
        self.track = None
        self.hideBooks()
        self.startLookAround()
        return None

    
    def enterReadBook(self, ts = 0, callback = None, extraArgs = []):
        self.stopLookAround()
        self.lerpLookAt(Point3(0, 1, -2))
        self.showBooks()
        for bookActor in self.bookActors:
            bookActor.pingpong('book', 38, 118)
        
        self.pingpong('book', 38, 118)
        return None

    
    def exitReadBook(self):
        self.hideBooks()
        for bookActor in self.bookActors:
            bookActor.stop()
        
        self.stop()
        self.startLookAround()
        return None

    
    def enterCloseBook(self, ts = 0, callback = None, extraArgs = []):
        if callback != None:
            closeTrack = Track([
                ActorInterval(self, 'book', startTime = 4.96, endTime = 6.5),
                FunctionInterval(callback, extraArgs = extraArgs)])
        else:
            closeTrack = Track([
                ActorInterval(self, 'book', startTime = 4.96, endTime = 6.5)])
        bookIvals = [
            FunctionInterval(self.showBooks)]
        bookTracks = []
        for bookActor in self.bookActors:
            bookTracks.append(Track([
                ActorInterval(bookActor, 'book', startTime = 4.96, endTime = 6.5)]))
        
        bookIvals.append(MultiTrack(bookTracks))
        bookIvals.append(FunctionInterval(self.hideBooks))
        bookTrack = Track(bookIvals)
        self.track = MultiTrack([
            closeTrack,
            bookTrack])
        dur = self.track.getDuration()
        if ts <= dur:
            self.track.play(ts)
        else:
            self.track.setT(dur)
            self.notify.debug('enterOpenBook() - ts: %f dur: %f' % (ts, dur))
        return None

    
    def exitCloseBook(self):
        if self.track != None:
            if self.track.isPlaying():
                self.track.stop()
            
        
        self.track = None
        self.hideBooks()
        return None

    
    def enterTeleportOut(self, ts = 0, callback = None, extraArgs = []):
        
        def showHoles(holes, hands):
            index = 0
            for hole in holes:
                hole.reparentTo(hands[index])
                index += 1
            

        
        def reparentHoles(holes, toon):
            holes[0].reparentTo(toon)
            holes[1].reparentTo(hidden)
            holes[2].reparentTo(hidden)

        holes = self.holeActors
        hands = self.getRightHands()
        holeIvals = []
        holeIvals.append(FunctionInterval(showHoles, extraArgs = [
            holes,
            hands]))
        holeIvals.append((1.708, FunctionInterval(reparentHoles, extraArgs = [
            holes,
            self])))
        holeIvals.append((3.4, FunctionInterval(holes[0].reparentTo, extraArgs = [
            hidden])))
        if callback != None:
            holeIvals.append(FunctionInterval(callback, extraArgs = extraArgs))
        
        holeTracks = [
            Track(holeIvals)]
        for hole in holes:
            holeTracks.append(Track([
                ActorInterval(hole, 'hole', duration = 3.4)]))
        
        holeTracks.append(Track([
            ActorInterval(self, 'teleport', duration = 3.4)]))
        self.track = MultiTrack(holeTracks)
        dur = self.track.getDuration()
        if ts <= dur:
            self.track.play(ts)
        else:
            self.track.setT(dur)
            self.notify.debug('enterTeleportOut() - ts: %f dur: %f' % (ts, dur))
        return None

    
    def exitTeleportOut(self):
        if self.track != None:
            if self.track.isPlaying():
                self.track.stop()
            
        
        self.track = None
        for hole in self.holeActors:
            hole.reparentTo(hidden)
        
        self.show()
        return None

    
    def enterTeleportIn(self, ts = 0, callback = None, extraArgs = []):
        hole = self.holeActors[0]
        holeIvals = []
        holeIvals.append(FunctionInterval(hole.reparentTo, extraArgs = [
            self]))
        pos = Point3(0, -2.4, 0)
        holeIvals.append(FunctionInterval(hole.setPos, extraArgs = [
            self,
            pos]))
        holeIvals.append(ActorInterval(hole, 'hole', startTime = 3.4, endTime = 3.1))
        holeIvals.append(WaitInterval(0.6))
        holeIvals.append(ActorInterval(hole, 'hole', startTime = 3.1, endTime = 3.4))
        
        def restoreHole(hole):
            hole.setPos(0, 0, 0)
            hole.reparentTo(hidden)

        holeIvals.append(FunctionInterval(restoreHole, extraArgs = [
            hole]))
        holeTrack = Track(holeIvals)
        toonIvals = []
        toonIvals.append((0.3, FunctionInterval(self.show)))
        toonIvals.append(ActorInterval(self, 'jump', startTime = 0.45))
        if callback != None:
            toonIvals.append(FunctionInterval(callback, extraArgs = extraArgs))
        
        toonTrack = Track(toonIvals)
        self.track = MultiTrack([
            holeTrack,
            toonTrack])
        dur = self.track.getDuration()
        if ts <= dur:
            self.track.play(ts)
        else:
            self.track.setT(dur)
            self.notify.debug('enterTeleportIn() - ts: %f dur: %f' % (ts, dur))
        return None

    
    def exitTeleportIn(self):
        if self.track != None:
            if self.track.isPlaying():
                self.track.stop()
            
        
        self.track = None
        for hole in self.holeActors:
            hole.setPos(0, 0, 0)
            hole.reparentTo(hidden)
        
        self.show()
        return None

    
    def b_setQuests(self, questList):
        flattenedQuests = []
        for quest in questList:
            flattenedQuests.extend(quest)
        
        self.setQuests(flattenedQuests)
        self.d_setQuests(flattenedQuests)

    
    def d_setQuests(self, flattenedQuests):
        self.sendUpdate('setQuests', [
            flattenedQuests])

    
    def setQuests(self, flattenedQuests):
        self.notify.debug('setting quests to %s' % flattenedQuests)
        questList = []
        questLen = 5
        for i in range(0, len(flattenedQuests), questLen):
            questList.append(flattenedQuests[i:i + questLen])
        
        self.quests = questList

    
    def getQuests(self):
        return self.quests


