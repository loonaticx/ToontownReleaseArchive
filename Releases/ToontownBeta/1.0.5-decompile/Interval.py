# Source Generated with Decompyle++
# File: Interval.pyo (Python 2.0)

from DirectObject import *
from IntervalGlobal import *
import ClockObject
import Task
IVAL_NONE = 0
IVAL_INIT = 1
IVAL_DONE = 2

class Interval(DirectObject):
    notify = directNotify.newCategory('Interval')
    playbackCounter = 0
    clock = ClockObject.ClockObject.getGlobalClock()
    
    def __init__(self, name, duration, openEnded = 1, reverse = 0):
        self.name = name
        self.duration = duration
        self.curr_t = 0.0
        self.prev_t = 0.0
        self.stopEventList = []
        self.setTHooks = []
        self.fOpenEnded = openEnded
        self.reverse = reverse

    
    def getName(self):
        return self.name

    
    def getDuration(self):
        return self.duration

    
    def setfOpenEnded(self, openEnded):
        self.fOpenEnded = openEnded

    
    def getfOpenEnded(self):
        return self.fOpenEnded

    
    def setT(self, t, event = IVAL_NONE):
        self.curr_t = t
        self.updateFunc(t, event)
        for func in self.setTHooks:
            func(t)
        
        self.prev_t = self.curr_t

    
    def updateFunc(self, t, event = IVAL_NONE):
        pass

    
    def setTHook(self, t):
        pass

    
    def setFinalT(self):
        self.setT(self.getDuration(), event = IVAL_DONE)

    
    def play(self, t0 = 0.0, duration = 0.0, scale = 1.0):
        if t0 > self.duration:
            t0 = self.duration
        
        taskMgr.removeTasksNamed(self.name + '-play')
        self.offset = t0
        self.startT = self.clock.getFrameTime()
        self.scale = scale
        self.firstTime = 1
        if duration == 0.0:
            self.endTime = self.duration
        else:
            self.endTime = min(self.duration, self.offset + duration)
        taskMgr.spawnMethodNamed(self._Interval__playTask, self.name + '-play')

    
    def loop(self, t0 = 0.0, duration = 0.0, scale = 1.0):
        self.accept(self.name + '-loop', self.play, extraArgs = [
            t0,
            duration,
            scale])
        self.play(t0, duration, scale)
        return None

    
    def stop(self):
        for stopEvent in self.stopEventList:
            messenger.send(stopEvent)
        
        taskMgr.removeTasksNamed(self.name + '-play')
        self.ignore(self.name + '-loop')
        return self.curr_t

    
    def isPlaying(self):
        return taskMgr.hasTaskNamed(self.name + '-play')

    
    def __playTask(self, task):
        t = self.clock.getFrameTime()
        te = self.offset + (t - self.startT) * self.scale
        if te < self.endTime:
            if self.firstTime:
                self.setT(te, event = IVAL_INIT)
                self.firstTime = 0
            else:
                self.setT(te)
            return Task.cont
        else:
            te = self.endTime
            if self.firstTime:
                self.setT(te, event = IVAL_INIT)
                self.firstTime = 0
            else:
                self.setT(te, IVAL_DONE)
            messenger.send(self.name + '-loop')
            return Task.done

    
    def __repr__(self, indent = 0):
        space = ''
        for l in range(indent):
            space = space + ' '
        
        return space + self.name + ' dur: %.2f' % self.duration

    
    def popupControls(self, tl = None):
        base.wantTk = 1
        import TkGlobal
        import fpformat
        import string
        from Tkinter import *
        import Pmw
        import EntryScale
        if tl == None:
            tl = Toplevel()
            tl.title('Interval Controls')
        
        outerFrame = Frame(tl)
        self.es = EntryScale.EntryScale(outerFrame, text = self.getName(), min = 0, max = string.atof(fpformat.fix(self.duration, 2)), command = (lambda t, s = self: s.setT(t)))
        es = EntryScale.EntryScale(outerFrame, text = self.getName(), min = 0, max = string.atof(fpformat.fix(self.duration, 2)), command = (lambda t, s = self: s.setT(t)))
        
        def onPress(s = self, es = es):
            taskMgr.removeTasksNamed(s.name + '-play')
            s.setT(es.get(), event = IVAL_INIT)

        es.onPress = onPress
        
        es.onRelease = lambda s = self: s.stop()
        
        def onReturn(s = self, es = es):
            s.setT(es.get(), event = IVAL_INIT)
            s.stop()

        es.onReturnRelease = onReturn
        es.pack(expand = 1, fill = X)
        bf = Frame(outerFrame)
        
        def toStart(s = self, es = es):
            s.setT(0.0, event = IVAL_INIT)
            s.stop()

        
        def toEnd(s = self):
            s.setT(s.getDuration(), event = IVAL_INIT)
            s.stop()

        jumpToStart = Button(bf, text = '<<', command = toStart)
        stop = Button(bf, text = 'Stop', command = (lambda s = self: s.stop()))
        play = Button(bf, text = 'Play', command = (lambda s = self, es = es: s.play(es.get())))
        jumpToEnd = Button(bf, text = '>>', command = toEnd)
        jumpToStart.pack(side = LEFT, expand = 1, fill = X)
        play.pack(side = LEFT, expand = 1, fill = X)
        stop.pack(side = LEFT, expand = 1, fill = X)
        jumpToEnd.pack(side = LEFT, expand = 1, fill = X)
        bf.pack(expand = 1, fill = X)
        outerFrame.pack(expand = 1, fill = X)
        
        def update(t, es = es):
            es.set(t, fCommand = 0)

        self.setTHooks.append(update)
        
        def onDestroy(e, s = self, u = update):
            if u in s.setTHooks:
                s.setTHooks.remove(u)
            

        tl.bind('<Destroy>', onDestroy)


