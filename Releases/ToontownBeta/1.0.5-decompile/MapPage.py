# Source Generated with Decompyle++
# File: MapPage.pyo (Python 2.0)

import ShtikerPage
import ToontownGlobals
import PythonUtil
from DirectGui import *

class MapPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    
    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.mapModel = loader.loadModel('phase_4/models/gui/toontown_map')
        self.map = DirectFrame(parent = self, relief = None, image = self.mapModel.find('**/toontown_map'), image_scale = (1.8, 1, 1.35), scale = 0.97, pos = (0, 0, 0.04))
        self.cloudModel = loader.loadModel('phase_4/models/gui/cloud')
        self.cloud = self.cloudModel.find('**/cloud')
        self.allZones = [
            ToontownGlobals.DonaldsDock,
            ToontownGlobals.ToontownCentral,
            ToontownGlobals.TheBrrrgh,
            ToontownGlobals.MinniesMelodyland,
            ToontownGlobals.DaisyGardens,
            ToontownGlobals.ConstructionZone,
            ToontownGlobals.FunnyFarm,
            ToontownGlobals.GoofyStadium,
            ToontownGlobals.DonaldsDreamland,
            ToontownGlobals.BossbotHQ,
            ToontownGlobals.SellbotHQ,
            ToontownGlobals.CashbotHQ,
            ToontownGlobals.LawbotHQ]
        self.cloudScaleList = ((-0.5,), (), (0.4, 0.5), (0.65,), (0.6, -0.45), (0.5, 0.4), (-0.45, -0.6), (0.55,), (0.6,), (0.4,), (0.4,), (-0.4,), (-0.45,))
        self.cloudSquishList = ((1,), (), (1, 1), (0.7,), (0.5, 0.8), (0.85, 0.8), (0.7, 0.85), (1,), (0.65,), (1,), (1,), (1,), (1,))
        self.cloudPosList = (((0.47, 0.0, -0.07),), (), ((0.3, 0.0, 0.4), (0.45, 0.0, 0.3)), ((-0.05, 0.0, 0.23),), ((-0.25, 0.0, -0.5), (-0.33, 0.0, -0.4)), ((0.28, 0.0, -0.45), (0.15, 0.0, -0.45)), ((-0.5, 0.0, 0.15), (-0.45, 0.0, 0.32)), ((-0.45, 0.0, -0.1),), ((-0.1, 0.0, 0.5),), ((-0.55, 0.0, 0.5),), ((0.55, 0.0, 0.5),), ((-0.55, 0.0, -0.5),), ((0.55, 0.0, -0.43),))
        self.buttonPosList = ((0.594, 0.0, -0.075), (0.0, 0.0, -0.2), (0.475, 0.0, 0.25), (0.063, 0.0, 0.15), (-0.25, 0.0, -0.475), (0.313, 0.0, -0.475), (-0.438, 0.0, 0.22), (-0.55, 0.0, -0.125), (-0.088, 0.0, 0.47), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
        self.buttonScaleList = ((0.35, 1, 0.2), (0.4, 1, 0.3), (0.35, 1, 0.3), (0.25, 1, 0.25), (0.25, 1, 0.25), (0.275, 1, 0.25), (0.3, 1, 0.25), (0.3, 1, 0.25), (0.35, 1, 0.25), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1))
        self.buttons = []
        self.clouds = []
        for hood in self.allZones:
            abbrev = toonbase.tcr.hoodMgr.getNameFromId(hood)
            fullname = toonbase.tcr.hoodMgr.getFullnameFromId(hood)
            hoodIndex = self.allZones.index(hood)
            button = DirectButton(parent = self.map, relief = None, pos = self.buttonPosList[hoodIndex], pad = (0.2, 0.16), text = ('', fullname, fullname), text_bg = Vec4(1, 1, 1, 0.4), text_scale = 0.055, command = self._MapPage__buttonCallback, extraArgs = [
                hood])
            button.resetFrameSize()
            self.buttons.append(button)
            hoodClouds = []
            for cloudScale, cloudPos, cloudSquish in zip(self.cloudScaleList[hoodIndex], self.cloudPosList[hoodIndex], self.cloudSquishList[hoodIndex]):
                cloud = DirectFrame(parent = self.map, relief = None, state = DISABLED, image = self.cloud, scale = (cloudScale * 1.333, abs(cloudScale), abs(cloudScale) * cloudSquish), pos = (cloudPos[0] * 1.25, cloudPos[1], cloudPos[2]))
                cloud.hide()
                hoodClouds.append(cloud)
            
            self.clouds.append(hoodClouds)
        
        self.resetFrameSize()
        return None

    
    def unload(self):
        self.mapModel.removeNode()
        del self.mapModel
        self.cloudModel.removeNode()
        del self.cloudModel
        self.cloud.removeNode()
        del self.cloud
        del self.buttons
        del self.clouds
        ShtikerPage.ShtikerPage.unload(self)

    
    def enter(self):
        ShtikerPage.ShtikerPage.enter(self)
        if toonbase.localToon.teleportCheat:
            safeZonesVisited = ToontownGlobals.Hoods
        else:
            safeZonesVisited = toonbase.localToon.safeZonesVisited
        hoodsAvailable = toonbase.tcr.hoodMgr.getAvailableZones()
        hoodList = PythonUtil.intersection(safeZonesVisited, hoodsAvailable)
        for hood in self.allZones:
            button = self.buttons[self.allZones.index(hood)]
            clouds = self.clouds[self.allZones.index(hood)]
            if hood in hoodList:
                button.show()
                for cloud in clouds:
                    cloud.hide()
                
            else:
                button.hide()
                for cloud in clouds:
                    cloud.show()
                
        
        return None

    
    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)

    
    def __buttonCallback(self, hood):
        self.doneStatus = {
            'mode': 'teleport',
            'hood': hood }
        messenger.send(self.doneEvent)


