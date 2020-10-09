# Source Generated with Decompyle++
# File: SoundInterval.pyo (Python 2.0)

from PandaModules import *
from Interval import *

class SoundInterval(Interval):
    soundNum = 1
    notify = directNotify.newCategory('SoundInterval')
    
    def __init__(self, sound, loop = 0, duration = 0.0, name = None):
        id = 'Sound-%d' % SoundInterval.soundNum
        SoundInterval.soundNum += 1
        self.sound = sound
        self.loop = loop
        self.wantSound = base.wantSfx
        if duration == 0.0:
            if self.wantSound:
                duration = self.sound.length()
                if duration == 0:
                    self.notify.warning('zero length duration!')
                
                duration += 1.5
            else:
                print 'SoundInterval: Warning, want-sound #f,' + ' zero sound duration assumed'
                duration = 0.0
        
        if name == None:
            name = id
        
        Interval.__init__(self, name, duration)
        self.stopEvent = id + '_stopEvent'
        if self.wantSound:
            self.stopEventList = [
                self.stopEvent]
        

    
    def updateFunc(self, t, event = IVAL_NONE):
        if not (self.wantSound):
            return None
        
        if t >= self.getDuration():
            self.sound.stop()
            self.ignore(self.stopEvent)
        elif event == IVAL_INIT:
            if t < 0.1:
                t = 0.0
            
            self.sound.setTime(t)
            self.sound.setLoop(self.loop)
            self.sound.play()
            self.acceptOnce(self.stopEvent, (lambda s = self: s.sound.stop()))
        
        self.notify.debug('updateFunc() - %s: t = %f' % (self.name, t))


