# Source Generated with Decompyle++
# File: DistributedAnimatedProp.pyo (Python 2.0)

from ShowBaseGlobal import *
from ClockDelta import *
import DirectNotifyGlobal
import FSM
import DistributedObject

class DistributedAnimatedProp(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.fsm = FSM.FSM('DistributedAnimatedProp', [
            State.State('off', self.enterOff, self.exitOff, [
                'playing']),
            State.State('playing', self.enterPlaying, self.exitPlaying, [
                'off'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)

    
    def disable(self):
        self.fsm.request('off')
        self.ignoreAll()
        del self.propNodePath
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        DistributedObject.DistributedObject.delete(self)

    
    def setBlock(self, prop):
        self.propID = prop
        self.accept('enter_prop_trigger_' + self.propID, self.propIDTrigger)

    
    def setState(self, state, sec, usec):
        self.fsm.request(state, [
            localElapsedTime(sec, usec)])

    
    def __getPropNodePath(self):
        if not self.__dict__.has_key('propNodePath'):
            self.propNodePath = self.cr.playGame.hood.loader.geom.find('**/prop' + self.propID + ':*_DNARoot')
        
        return self.propNodePath

    
    def propTrigger(self, args):
        print '\n\n', self.propID, ': DistributedAnimatedProp.propTrigger()', args, '\n\n'
        self.accept('enter_exit_trigger_' + self.propID, self.propIDTrigger)

    
    def exitTrigger(self, args):
        print '\n\n', self.propID, ': DistributedAnimatedProp.exitTrigger()', args, '\n\n'

    
    def rejectInteract(self):
        pass

    
    def toonInteract(self, avatarID):
        pass

    
    def toonExit(self):
        pass

    
    def enterOff(self):
        if self.isAnimationPlaying():
            zzzzzzzzzzz
        

    
    def exitOff(self):
        pass

    
    def enterPlaying(self, ts):
        zzzzzzzzzzzzzz

    
    def exitPlaying(self):
        pass


