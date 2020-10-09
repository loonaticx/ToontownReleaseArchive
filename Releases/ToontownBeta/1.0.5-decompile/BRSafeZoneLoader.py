# Source Generated with Decompyle++
# File: BRSafeZoneLoader.pyo (Python 2.0)

from ShowBaseGlobal import *
import SafeZoneLoader
import BRPlayground

class BRSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = BRPlayground.BRPlayground
        self.musicFile = 'phase_8/audio/bgm/TB_nbrhood.mid'
        self.activityMusicFile = 'phase_8/audio/bgm/TB_SZ_activity.mid'
        self.dnaFile = 'phase_8/dna/the_burrrgh_sz.dna'
        self.safeZoneStorageDNAFile = 'phase_8/dna/storage_BR_sz.dna'

    
    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.wind1Sound = base.loadSfx('phase_8/audio/sfx/SZ_TB_wind_1.mp3')
        self.wind2Sound = base.loadSfx('phase_8/audio/sfx/SZ_TB_wind_2.mp3')
        self.wind3Sound = base.loadSfx('phase_8/audio/sfx/SZ_TB_wind_3.mp3')

    
    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        base.unloadSfx(self.wind1Sound)
        base.unloadSfx(self.wind2Sound)
        base.unloadSfx(self.wind3Sound)

    
    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    
    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)


