# Source Generated with Decompyle++
# File: DDPlayground.pyo (Python 2.0)

from PandaObject import *
from ShowBaseGlobal import *
import Playground
import whrandom
import State
import Actor

class DDPlayground(Playground.Playground):
    
    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)
        self.submerged = 0
        self.activityFsm = FSM.FSM('Activity', [
            State.State('off', self.enterOff, self.exitOff, [
                'OnBoat']),
            State.State('OnBoat', self.enterOnBoat, self.exitOnBoat, [
                'off'])], 'off', 'off')
        self.activityFsm.enterInitialState()

    
    def load(self):
        Playground.Playground.load(self)

    
    def unload(self):
        del self.activityFsm
        Playground.Playground.unload(self)

    
    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)
        taskMgr.spawnMethodNamed(self._DDPlayground__checkForUnderwater, 'dd-check-underwater')
        self.nextSeagullTime = 0
        taskMgr.spawnMethodNamed(self._DDPlayground__seagulls, 'dd-seagulls')
        self.loader.hood.setWhiteFog()
        donald = self.loader.donald
        donald.loop('steer')
        donald.setZ(3.95)
        donald.setY(-0.5)
        donald.reparentTo(toonbase.tcr.name2nodePath['donalds_boat'])

    
    def exit(self):
        Playground.Playground.exit(self)
        taskMgr.removeTasksNamed('dd-check-underwater')
        taskMgr.removeTasksNamed('dd-seagulls')
        self.loader.hood.setNoFog()
        donald = self.loader.donald
        donald.stop()
        donald.reparentTo(hidden)

    
    def __checkForUnderwater(self, task):
        if camera.getZ(render) < 1.0:
            self._DDPlayground__submerge()
        else:
            self._DDPlayground__emerge()
        return Task.cont

    
    def __submerge(self):
        if self.submerged:
            return None
        
        self.loader.hood.setUnderwaterFog()
        base.playSfx(self.loader.underwaterSound, looping = 1)
        base.stopSfx(self.loader.seagullSound)
        taskMgr.removeTasksNamed('dd-seagulls')
        self.walkStateData.fsm.request('swimming', [
            self.loader.swimSound])
        self.submerged = 1

    
    def __emerge(self):
        if self.submerged == 0:
            return None
        
        self.loader.hood.setWhiteFog()
        base.stopSfx(self.loader.underwaterSound)
        self.nextSeagullTime = 0
        taskMgr.spawnMethodNamed(self._DDPlayground__seagulls, 'dd-seagulls')
        self.walkStateData.fsm.request('walking')
        self.submerged = 0

    
    def __seagulls(self, task):
        if task.time < self.nextSeagullTime:
            return Task.cont
        
        base.playSfx(self.loader.seagullSound)
        self.nextSeagullTime = task.time + whrandom.random() * 4.0 + 8.0
        return Task.cont

    
    def handleBookClose(self):
        Playground.Playground.handleBookClose(self)
        if self.submerged:
            self.walkStateData.fsm.request('swimming', [
                self.loader.swimSound])
        

    
    def teleportInDone(self):
        if self.submerged:
            self.walkStateData.fsm.request('swimming', [
                self.loader.swimSound])
        else:
            self.walkStateData.fsm.request('walking')

    
    def enterOff(self):
        return None

    
    def exitOff(self):
        return None

    
    def enterOnBoat(self):
        boat = toonbase.tcr.name2nodePath['donalds_boat']
        toonbase.localToon.wrtReparentTo(boat)
        toonbase.localToon.d_setParent('donalds_boat')
        base.drive.node().setPos(toonbase.localToon.getPos())
        base.drive.node().setHpr(toonbase.localToon.getHpr())
        base.playSfx(self.loader.waterSound, looping = 1)

    
    def exitOnBoat(self):
        toonbase.localToon.wrtReparentTo(render)
        toonbase.localToon.d_setParent('render')
        base.drive.node().setPos(toonbase.localToon.getPos())
        base.drive.node().setHpr(toonbase.localToon.getHpr())
        base.stopSfx(self.loader.waterSound)


