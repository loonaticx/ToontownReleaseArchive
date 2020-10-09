# Source Generated with Decompyle++
# File: ActorInterval.pyo (Python 2.0)

from PandaModules import *
from Interval import *
import math
import DirectNotifyGlobal

class ActorInterval(Interval):
    notify = directNotify.newCategory('ActorInterval')
    animNum = 1
    
    def __init__(self, actor, animName, loop = 0, duration = 0.0, startTime = 0.0, endTime = None, name = None):
        id = 'Actor-%d' % ActorInterval.animNum
        ActorInterval.animNum += 1
        self.actor = actor
        self.animName = animName
        self.loop = loop
        self.frameRate = self.actor.getFrameRate(self.animName)
        self.numFrames = self.actor.getNumFrames(self.animName)
        self.startTime = startTime
        if name == None:
            name = id
        
        reverse = 0
        if duration == 0.0:
            if endTime == None:
                duration = max(self.actor.getDuration(self.animName) - startTime, 0.0)
            else:
                duration = endTime - startTime
                if duration < 0.0:
                    duration = -duration
                
        
        if endTime == None:
            self.finishTime = self.startTime + duration
        else:
            self.finishTime = endTime
        if self.startTime > self.finishTime:
            reverse = 1
        
        Interval.__init__(self, name, duration, reverse = reverse)
        self.stopEvent = id + '_stopEvent'
        if self.loop:
            self.stopEventList = [
                self.stopEvent]
        

    
    def calcFrame(self, t):
        segmentLength = abs(self.finishTime - self.startTime)
        offset = t % segmentLength
        if t == self.getDuration() and offset < 0.0001:
            offset = segmentLength
        
        if self.reverse == 0:
            floatFrame = self.frameRate * (self.startTime + offset)
        else:
            negOffset = self.startTime - self.finishTime - offset
            floatFrame = self.frameRate * (self.finishTime + negOffset)
        frame = max(0, int(math.ceil(floatFrame)) - 1)
        return frame % self.numFrames

    
    def goToT(self, t):
        frame = self.calcFrame(t)
        self.actor.pose(self.animName, frame)
        self.notify.debug('goToT() - %s pose to frame: %d' % (self.name, frame))
        return frame

    
    def updateFunc(self, t, event = IVAL_NONE):
        if self.actor.isEmpty():
            self.notify.warning('updateFunc() - %s empty actor!' % self.name)
            return None
        
        if t >= self.getDuration():
            self.actor.stop()
            frame = self.goToT(self.getDuration())
            if self.loop:
                self.ignore(self.stopEvent)
            
            self.notify.debug('updateFunc() - %s stoping at frame: ' % self.name + '%d Num frames: %d' % (frame, self.numFrames))
        elif self.loop == 1:
            if event == IVAL_INIT:
                self.goToT(t)
                self.actor.loop(self.animName, restart = 0)
                self.acceptOnce(self.stopEvent, self.actor.stop)
                self.notify.debug('updateFunc() - IVAL_INIT %s looping anim' % self.name)
            
        else:
            self.goToT(t)


