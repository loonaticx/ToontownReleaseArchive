# Source Generated with Decompyle++
# File: DDHood.pyo (Python 2.0)

from ShowBaseGlobal import *
import Hood
import DDTownLoader
import DDSafeZoneLoader
from ToontownGlobals import *

class DDHood(Hood.Hood):
    
    def __init__(self, parentFSM, doneEvent, dnaStore):
        Hood.Hood.__init__(self, parentFSM, doneEvent, dnaStore)
        self.id = DonaldsDock
        self.townLoaderClass = DDTownLoader.DDTownLoader
        self.safeZoneLoaderClass = DDSafeZoneLoader.DDSafeZoneLoader
        self.storageDNAFile = 'phase_6/dna/storage_DD.dna'
        self.skyFile = 'phase_6/models/props/BR_sky'
        self.titleColor = (0.8, 0.6, 0.5, 1.0)

    
    def load(self):
        Hood.Hood.load(self)
        self.parentFSM.getStateNamed('DDHood').addChild(self.fsm)
        self.fog = Fog(Fog.MLinear)

    
    def unload(self):
        self.parentFSM.getStateNamed('DDHood').removeChild(self.fsm)
        Hood.Hood.unload(self)
        self.fog = None

    
    def enter(self, *args):
        Hood.Hood.enter(self, *args)

    
    def exit(self):
        Hood.Hood.exit(self)

    
    def setUnderwaterFog(self):
        if base.wantFog:
            self.fog.setColor(Vec4(0.0, 0.0, 0.6, 1.0))
            self.fog.setRange(0.1, 100.0)
            render.setFog(self.fog)
        

    
    def setWhiteFog(self):
        if base.wantFog:
            self.fog.setColor(Vec4(0.8, 0.8, 0.8, 1.0))
            self.fog.setRange(0, 400)
            render.setFog(self.fog)
        

    
    def setNoFog(self):
        if base.wantFog:
            render.clearFog()
        


