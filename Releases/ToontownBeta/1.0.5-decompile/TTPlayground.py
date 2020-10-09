# Source Generated with Decompyle++
# File: TTPlayground.pyo (Python 2.0)

from ShowBaseGlobal import *
import Playground
import whrandom
import DownloadForceAcknowledge

class TTPlayground(Playground.Playground):
    
    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)

    
    def load(self):
        Playground.Playground.load(self)

    
    def unload(self):
        Playground.Playground.unload(self)

    
    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)
        self.nextBirdTime = 0
        taskMgr.spawnMethodNamed(self._TTPlayground__birds, 'TT-birds')

    
    def exit(self):
        Playground.Playground.exit(self)
        taskMgr.removeTasksNamed('TT-birds')

    
    def __birds(self, task):
        if task.time < self.nextBirdTime:
            return Task.cont
        
        base.playSfx(whrandom.choice(self.loader.birdSound))
        randNum = whrandom.random()
        self.nextBirdTime = task.time + randNum * 20.0
        return Task.cont

    
    def enterDFA(self, requestStatus):
        doneEvent = 'dfaDoneEvent'
        self.accept(doneEvent, self.enterDFACallback, [
            requestStatus])
        self.dfa = DownloadForceAcknowledge.DownloadForceAcknowledge(doneEvent)
        self.dfa.enter(5)


