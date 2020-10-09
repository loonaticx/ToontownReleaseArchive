# Source Generated with Decompyle++
# File: Timer.pyo (Python 2.0)

import ClockObject
import Task

class Timer:
    
    def __init__(self):
        self.clock = ClockObject.ClockObject.getGlobalClock()
        self.finalT = 0.0
        self.currT = 0.0
        self.name = 'default-timer'
        self.started = 0
        self.callback = None

    
    def start(self, t, name):
        if self.started:
            self.stop()
        
        self.callback = None
        self.finalT = t
        self.name = name
        self.startT = self.clock.getFrameTime()
        self.currT = 0.0
        taskMgr.spawnMethodNamed(self._Timer__timerTask, self.name + '-run')
        self.started = 1

    
    def startCallback(self, t, callback):
        if self.started:
            self.stop()
        
        self.callback = callback
        self.finalT = t
        self.name = 'default-timer'
        self.startT = self.clock.getFrameTime()
        self.currT = 0.0
        taskMgr.spawnMethodNamed(self._Timer__timerTask, self.name + '-run')
        self.started = 1

    
    def stop(self):
        if not (self.started):
            return 0.0
        
        taskMgr.removeTasksNamed(self.name + '-run')
        self.started = 0
        return self.currT

    
    def resume(self):
        self.start(self.finalT - self.currT, self.name)

    
    def restart(self):
        self.start(self.finalT, self.name)

    
    def isStarted(self):
        return self.started

    
    def addT(self, t):
        self.finalT = self.finalT + t

    
    def setT(self, t):
        self.finalT = t

    
    def getT(self):
        return self.finalT - self.currT

    
    def __timerTask(self, task):
        t = self.clock.getFrameTime()
        te = t - self.startT
        self.currT = te
        if te >= self.finalT:
            if self.callback != None:
                self.callback()
            else:
                messenger.send(self.name)
            return Task.done
        
        return Task.cont


