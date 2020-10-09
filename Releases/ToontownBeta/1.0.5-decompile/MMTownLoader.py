# Source Generated with Decompyle++
# File: MMTownLoader.pyo (Python 2.0)

import TownLoader
import MMStreet
import Suit

class MMTownLoader(TownLoader.TownLoader):
    
    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self, hood, parentFSM, doneEvent)
        self.streetClass = MMStreet.MMStreet
        self.musicFile = 'phase_6/audio/bgm/MM_SZ.mid'
        self.townStorageDNAFile = 'phase_6/dna/storage_MM_town.dna'

    
    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        Suit.loadSuits(2)
        dnaFile = 'phase_6/dna/minnies_melody_land_' + str(self.branchZone) + '.dna'
        self.createHood(dnaFile)

    
    def unload(self):
        Suit.unloadSuits(2)
        TownLoader.TownLoader.unload(self)


