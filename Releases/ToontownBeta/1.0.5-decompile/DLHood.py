# Source Generated with Decompyle++
# File: DLHood.pyo (Python 2.0)

from ShowBaseGlobal import *
import Hood
import DLTownLoader
import DLSafeZoneLoader
from ToontownGlobals import *

class DLHood(Hood.Hood):
    
    def __init__(self, parentFSM, doneEvent, dnaStore):
        Hood.Hood.__init__(self, parentFSM, doneEvent, dnaStore)
        self.id = DonaldsDreamland
        self.townLoaderClass = DLTownLoader.DLTownLoader
        self.safeZoneLoaderClass = DLSafeZoneLoader.DLSafeZoneLoader
        self.storageDNAFile = 'phase_8/dna/storage_DL.dna'
        self.skyFile = 'phase_8/models/props/DL_sky'
        self.titleColor = (1.0, 0.9, 0.5, 1.0)

    
    def load(self):
        Hood.Hood.load(self)
        self.parentFSM.getStateNamed('DLHood').addChild(self.fsm)

    
    def unload(self):
        self.parentFSM.getStateNamed('DLHood').removeChild(self.fsm)
        Hood.Hood.unload(self)

    
    def enter(self, *args):
        Hood.Hood.enter(self, *args)

    
    def exit(self):
        Hood.Hood.exit(self)


