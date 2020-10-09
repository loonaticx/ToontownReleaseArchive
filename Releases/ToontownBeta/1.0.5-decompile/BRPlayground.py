# Source Generated with Decompyle++
# File: BRPlayground.pyo (Python 2.0)

from ShowBaseGlobal import *
import Playground
import whrandom

class BRPlayground(Playground.Playground):
    
    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)

    
    def load(self):
        Playground.Playground.load(self)

    
    def unload(self):
        Playground.Playground.unload(self)

    
    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)
        self.nextWindTime = 0
        taskMgr.spawnMethodNamed(self._BRPlayground__wind, 'br-wind')

    
    def exit(self):
        Playground.Playground.exit(self)
        taskMgr.removeTasksNamed('br-wind')

    
    def __wind(self, task):
        now = globalClock.getFrameTime()
        if now < self.nextWindTime:
            return Task.cont
        
        randNum = whrandom.random()
        wind = int(randNum * 100) % 3 + 1
        if wind == 1:
            base.playSfx(self.loader.wind1Sound)
        elif wind == 2:
            base.playSfx(self.loader.wind2Sound)
        elif wind == 3:
            base.playSfx(self.loader.wind3Sound)
        
        self.nextWindTime = now + randNum * 8.0
        return Task.cont


