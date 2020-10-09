# Source Generated with Decompyle++
# File: TTTownLoader.pyo (Python 2.0)

import TownLoader
import TTStreet
import Suit

class TTTownLoader(TownLoader.TownLoader):
    
    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self, hood, parentFSM, doneEvent)
        self.streetClass = TTStreet.TTStreet
        self.musicFile = 'phase_4/audio/bgm/TC_SZ.mid'
        self.townStorageDNAFile = 'phase_5/dna/storage_TT_town.dna'

    
    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        Suit.loadSuits(1)
        dnaFile = 'phase_5/dna/toontown_central_' + str(self.branchZone) + '.dna'
        self.createHood(dnaFile)

    
    def unload(self):
        Suit.unloadSuits(1)
        TownLoader.TownLoader.unload(self)


