# Source Generated with Decompyle++
# File: Transitions.pyo (Python 2.0)

from PandaModules import *
import Task

class Transitions:
    
    def __init__(self, loader):
        self.iris = loader.loadModel('phase_3/models/misc/iris')
        self.iris.setBin('fixed', 1000)
        self.fade = loader.loadModel('phase_3/models/misc/fade')
        self.fade.setBin('fixed', 1000)
        self.iris.setPos(0, 0, 0)
        self.fade.setScale(3)
        self.irisTaskName = 'irisTask'
        self.fadeTaskName = 'fadeTask'

    
    def fadeInLerpDone(self, task):
        self.fade.reparentTo(hidden)
        return Task.done

    
    def fadeIn(self, t = 0.5, block = 0):
        self.noTransitions()
        self.fade.reparentTo(aspect2d)
        if t == 0:
            self.fade.reparentTo(hidden)
        else:
            task = Task.sequence(self.fade.lerpColor(0, 0, 0, 1, 0, 0, 0, 0, t), Task.Task(self.fadeInLerpDone))
            if not block:
                taskMgr.spawnTaskNamed(task, self.fadeTaskName)
            else:
                return task

    
    def fadeInTask(self, task, time = 0.5):
        seq = Task.sequence(self.fadeIn(time, block = 1), task)
        taskMgr.spawnTaskNamed(seq, 'fadeInTaskSeq')

    
    def fadeOut(self, t = 0.5, block = 0):
        self.noTransitions()
        self.fade.reparentTo(aspect2d)
        if t == 0:
            self.fade.setColor(0, 0, 0, 1)
        elif not block:
            self.fade.lerpColor(0, 0, 0, 0, 0, 0, 0, 1, t, task = self.fadeTaskName)
        else:
            return self.fade.lerpColor(0, 0, 0, 0, 0, 0, 0, 1, t)

    
    def fadeScreen(self, alpha = 0.5):
        self.noTransitions()
        self.fade.reparentTo(aspect2d)
        self.fade.setColor(0, 0, 0, alpha)

    
    def fadeOutTask(self, task, time = 0.3, noFade = 1):
        if noFade:
            
            def noFadeTask(task):
                task.noFade()
                return Task.done

            nft = Task.Task(noFadeTask)
            nft.noFade = self.noFade
            seq = Task.sequence(self.fadeOut(time, block = 1), task, nft)
        else:
            seq = Task.sequence(self.fadeOut(time, block = 1), task)
        taskMgr.spawnTaskNamed(seq, 'fadeOutTaskSeq')

    
    def noFade(self):
        taskMgr.removeTasksNamed(self.fadeTaskName)
        self.fade.reparentTo(hidden)

    
    def irisInLerpDone(self, task):
        self.iris.reparentTo(hidden)
        return Task.done

    
    def irisIn(self, t = 0.5, block = 0):
        self.noTransitions()
        if t == 0:
            self.iris.reparentTo(hidden)
        else:
            self.iris.reparentTo(aspect2d)
            self.iris.setScale(0.015)
            task = Task.sequence(self.iris.lerpScale(0.18, 0.18, 0.18, t, blendType = 'noBlend'), Task.Task(self.irisInLerpDone))
            if not block:
                taskMgr.spawnTaskNamed(task, self.irisTaskName)
            else:
                return task

    
    def irisInTask(self, task, time = 0.5):
        seq = Task.sequence(self.irisIn(time, block = 1), task)
        taskMgr.spawnTaskNamed(seq, 'irisInTaskSeq')

    
    def irisOutLerpDone(self, task):
        self.iris.reparentTo(hidden)
        self.fadeOut(0)
        return Task.done

    
    def irisOut(self, t = 0.5, block = 0):
        self.noTransitions()
        if t == 0:
            self.iris.reparentTo(hidden)
        else:
            self.iris.reparentTo(aspect2d)
            self.iris.setScale(0.18)
            task = Task.sequence(self.iris.lerpScale(0.015, 0.015, 0.015, t, blendType = 'noBlend'), Task.Task(self.irisOutLerpDone))
            if not block:
                taskMgr.spawnTaskNamed(task, self.irisTaskName)
            else:
                return task

    
    def irisOutTask(self, task, time = 0.5, noIris = 1):
        if noIris:
            
            def noIrisTask(task):
                task.noIris()
                return Task.done

            nit = Task.Task(noIrisTask)
            nit.noIris = self.noIris
            seq = Task.sequence(self.irisOut(time, block = 1), task, nit)
        else:
            seq = Task.sequence(self.irisOut(time, block = 1), task)
        taskMgr.spawnTaskNamed(seq, 'irisOutTaskSeq')

    
    def noIris(self):
        taskMgr.removeTasksNamed(self.irisTaskName)
        self.iris.reparentTo(hidden)
        self.noFade()

    
    def noTransitions(self):
        self.noFade()
        self.noIris()


