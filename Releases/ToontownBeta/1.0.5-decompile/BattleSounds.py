# Source Generated with Decompyle++
# File: BattleSounds.pyo (Python 2.0)

from PandaModules import *
import DirectNotifyGlobal
SoundFilePrefix = 'phase_5/audio/sfx/'

class SoundCache:
    notify = DirectNotifyGlobal.directNotify.newCategory('SoundCache')
    
    def __init__(self):
        self.sounds = { }
        self.cache = []
        self.maxSize = base.config.GetInt('sound-cache-size', 12)

    
    def delSound(self, sound):
        base.unloadSfx(sound)
        del sound

    
    def unloadSounds(self):
        for sound in self.sounds.values():
            self.delSound(sound)
        
        self.sounds = { }
        self.cache = []

    
    def getSound(self, name):
        if not self.sounds.has_key(name):
            sound = base.loadSfx(SoundFilePrefix + name)
            if sound == None:
                return None
            
            sound.name = name
            self.sounds[name] = sound
            self.cache.append(sound)
            if len(self.sounds) > self.maxSize:
                lru = self.cache.pop(0)
                del self.sounds[lru.name]
                self.delSound(lru)
            
        
        return self.sounds[name]


globalSoundCache = SoundCache()
