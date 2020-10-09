# Source Generated with Decompyle++
# File: TTHood.pyo (Python 2.0)

from ShowBaseGlobal import *
import Hood
import TTTownLoader
import TTSafeZoneLoader
from ToontownGlobals import *

class TTHood(Hood.Hood):
    
    def __init__(self, parentFSM, doneEvent, dnaStore):
        Hood.Hood.__init__(self, parentFSM, doneEvent, dnaStore)
        self.id = ToontownCentral
        self.townLoaderClass = TTTownLoader.TTTownLoader
        self.safeZoneLoaderClass = TTSafeZoneLoader.TTSafeZoneLoader
        self.storageDNAFile = 'phase_4/dna/storage_TT.dna'
        self.skyFile = 'phase_4/models/props/TT_sky'
        self.titleColor = (1.0, 0.5, 0.4, 1.0)

    
    def load(self):
        Hood.Hood.load(self)
        self.parentFSM.getStateNamed('TTHood').addChild(self.fsm)

    
    def unload(self):
        self.parentFSM.getStateNamed('TTHood').removeChild(self.fsm)
        Hood.Hood.unload(self)

    
    def enter(self, *args):
        Hood.Hood.enter(self, *args)

    
    def exit(self):
        Hood.Hood.exit(self)


