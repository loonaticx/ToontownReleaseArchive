# Source Generated with Decompyle++
# File: DDSafeZoneLoader.pyo (Python 2.0)

from PandaObject import *
from ShowBaseGlobal import *
import SafeZoneLoader
import DDPlayground
import State
import Actor

class DDSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = DDPlayground.DDPlayground
        self.musicFile = 'phase_6/audio/bgm/DD_nbrhood.mid'
        self.activityMusicFile = 'phase_6/audio/bgm/DD_SZ_activity.mid'
        self.dnaFile = 'phase_6/dna/donalds_dock_sz.dna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_DD_sz.dna'

    
    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.seagullSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_Seagull.mp3')
        self.underwaterSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_Underwater.mp3')
        self.swimSound = base.loadSfx('phase_6/audio/sfx/AV_swimming.mp3')
        boat = self.geom.find('**/donalds_boat')
        if boat.isEmpty():
            self.notify.error('Boat not found')
        else:
            toonbase.tcr.name2nodePath['donalds_boat'] = boat
        wheel = boat.find('**/wheel')
        if wheel.isEmpty():
            self.notify.error('Wheel not found')
        else:
            wheel.hide()
        self.donald = Actor.Actor()
        self.donald.loadModel('phase_6/models/char/donald-wheel-mod')
        self.donald.loadAnims({
            'steer': 'phase_6/models/char/donald-wheel-chan' })
        self.dockSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_dockcreak.mp3')
        self.foghornSound = base.loadSfx('phase_5/audio/sfx/SZ_DD_foghorn.mp3')
        self.bellSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_shipbell.mp3')
        self.waterSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_waterlap.mp3')

    
    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        base.unloadSfx(self.seagullSound)
        base.unloadSfx(self.underwaterSound)
        base.unloadSfx(self.swimSound)
        base.unloadSfx(self.dockSound)
        base.unloadSfx(self.foghornSound)
        base.unloadSfx(self.bellSound)
        base.unloadSfx(self.waterSound)
        del self.seagullSound
        del self.underwaterSound
        del self.swimSound
        del self.dockSound
        del self.foghornSound
        del self.bellSound
        del self.waterSound
        del toonbase.tcr.name2nodePath['donalds_boat']
        del self.donald

    
    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    
    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)


