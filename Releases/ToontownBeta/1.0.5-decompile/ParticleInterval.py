# Source Generated with Decompyle++
# File: ParticleInterval.pyo (Python 2.0)

from PandaModules import *
from Interval import *
import BattleParticles

class ParticleInterval(Interval):
    particleNum = 1
    notify = directNotify.newCategory('ParticleInterval')
    
    def __init__(self, particleEffect, parent, worldRelative = 1, loop = 0, duration = 0.0, name = None):
        id = 'Particle-%d' % ParticleInterval.particleNum
        ParticleInterval.particleNum += 1
        if name == None:
            name = id
        
        self.particleEffect = particleEffect
        self.parent = parent
        self.worldRelative = worldRelative
        self.loop = loop
        Interval.__init__(self, name, duration)
        self.stopEvent = id + '_stopEvent'
        self.stopEventList = [
            self.stopEvent]

    
    def updateFunc(self, t, event = IVAL_NONE):
        if t >= self.getDuration():
            BattleParticles.cleanupParticleEffect(self.particleEffect)
            self.ignore(self.stopEvent)
        elif event == IVAL_INIT:
            BattleParticles.startParticleEffect(self.particleEffect, self.parent, self.worldRelative)
            self.acceptOnce(self.stopEvent, (lambda s = self: BattleParticles.cleanupParticleEffect(s.particleEffect)))
        
        self.notify.debug('updateFunc() - %s: t = %f' % (self.name, t))


