# Source Generated with Decompyle++
# File: Walk.pyo (Python 2.0)

from ShowBaseGlobal import *
import DirectNotifyGlobal
import PandaObject
import StateData
import FSM
import State

class Walk(PandaObject.PandaObject, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('Walk')
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.fsm = FSM.FSM('Walk', [
            State.State('off', self.enterOff, self.exitOff, [
                'walking',
                'swimming',
                'slowWalking']),
            State.State('walking', self.enterWalking, self.exitWalking, [
                'swimming',
                'slowWalking']),
            State.State('swimming', self.enterSwimming, self.exitSwimming, [
                'walking',
                'slowWalking']),
            State.State('slowWalking', self.enterSlowWalking, self.exitSlowWalking, [
                'walking',
                'swimming'])], 'off', 'off')
        self.fsm.enterInitialState()
        return None

    
    def load(self):
        return None

    
    def unload(self):
        del self.fsm
        return None

    
    def enter(self, slowWalk = 0):
        toonbase.localToon.lifter.clear()
        toonbase.localToon.startUpdateSmartCamera()
        toonbase.localToon.startPosHprBroadcast()
        toonbase.localToon.startBlink()
        toonbase.localToon.attachCamera()
        toonbase.localToon.addTabHook()
        toonbase.localToon.showName()
        toonbase.localToon.collisionsOn()
        return None

    
    def exit(self):
        self.fsm.request('off')
        toonbase.localToon.stopUpdateSmartCamera()
        toonbase.localToon.stopPosHprBroadcast()
        toonbase.localToon.stopBlink()
        toonbase.localToon.detachCamera()
        toonbase.localToon.removeTabHook()
        toonbase.localToon.collisionsOff()
        return None

    
    def enterOff(self):
        return None

    
    def exitOff(self):
        return None

    
    def enterWalking(self):
        if toonbase.localToon.hp > 0:
            toonbase.localToon.startTrackAnimToSpeed()
            toonbase.localToon.setWalkSpeedNormal()
        else:
            self.fsm.request('slowWalking')
        return None

    
    def exitWalking(self):
        toonbase.localToon.stopTrackAnimToSpeed()
        return None

    
    def enterSwimming(self, swimSound):
        toonbase.localToon.setWalkSpeedNormal()
        self.swimSound = swimSound
        self.swimSoundPlaying = 0
        toonbase.localToon.b_setAnimState('swim', toonbase.localToon.animMultiplier)
        taskMgr.spawnMethodNamed(self._Walk__swim, 'localToonSwimming')
        return None

    
    def exitSwimming(self):
        taskMgr.removeTasksNamed('localToonSwimming')
        base.stopSfx(self.swimSound)
        del self.swimSound
        del self.swimSoundPlaying
        return None

    
    def __swim(self, task):
        speed = base.mouseInterfaceNode.getSpeed()
        if speed == 0 and self.swimSoundPlaying:
            self.swimSoundPlaying = 0
            base.stopSfx(self.swimSound)
        elif speed > 0 and self.swimSoundPlaying == 0:
            self.swimSoundPlaying = 1
            base.playSfx(self.swimSound, looping = 1)
        
        return Task.cont

    
    def enterSlowWalking(self):
        self.accept(toonbase.localToon.uniqueName('positiveHP'), self._Walk__handlePositiveHP)
        toonbase.localToon.startTrackAnimToSpeed()
        toonbase.localToon.setWalkSpeedSlow()
        return None

    
    def __handlePositiveHP(self):
        self.fsm.request('walking')
        return None

    
    def exitSlowWalking(self):
        toonbase.localToon.stopTrackAnimToSpeed()
        self.ignore(toonbase.localToon.uniqueName('positiveHP'))
        return None


