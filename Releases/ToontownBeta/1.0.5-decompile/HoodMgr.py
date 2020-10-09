# Source Generated with Decompyle++
# File: HoodMgr.pyo (Python 2.0)

from ShowBaseGlobal import *
import DirectObject
import DirectNotifyGlobal
import DownloadForceAcknowledge
import string
import whrandom
from ToontownGlobals import *

class HoodMgr(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('HoodMgr')
    
    def __init__(self, tcr):
        self.tcr = tcr
        return None

    
    def getAvailableZones(self):
        if base.launcher == None:
            return self.getZonesInPhase(4) + self.getZonesInPhase(6) + self.getZonesInPhase(8)
        else:
            first = base.launcher.firstPhase
            final = base.launcher.finalPhase
            zones = []
            for phase in range(first, final + 1):
                if base.launcher.getPhaseComplete(phase):
                    zones = zones + self.getZonesInPhase(phase)
                
            
            return zones

    
    def getZonesInPhase(self, phase):
        p = []
        for i in phaseMap.items():
            if i[1] == phase:
                p.append(i[0])
            
        
        return p

    
    def getPhaseFromHood(self, hoodId):
        return phaseMap[hoodId]

    
    def getPlaygroundCenterFromId(self, hoodId):
        if hoodId == DonaldsDock:
            return whrandom.choice(([
                -28.0,
                -2.5,
                5.8,
                120.0,
                0.0,
                0.0], [
                -22,
                13,
                5.8,
                155.6,
                0.0,
                0.0], [
                67,
                47,
                5.7,
                134.7,
                0.0,
                0.0], [
                62,
                19,
                5.7,
                97.0,
                0.0,
                0.0], [
                66,
                -27,
                5.7,
                80.5,
                0.0,
                0.0], [
                -114,
                -7,
                5.7,
                -97.0,
                -0.0,
                0.0], [
                -108,
                36,
                5.7,
                -153.8,
                -0.0,
                0.0], [
                -116,
                -46,
                5.7,
                -70.1,
                -0.0,
                0.0], [
                -63,
                -79,
                5.7,
                -41.2,
                -0.0,
                0.0], [
                -2,
                -79,
                5.7,
                57.4,
                -0.0,
                0.0], [
                -38,
                -78,
                5.7,
                9.1,
                -0.0,
                0.0]))
        elif hoodId == ToontownCentral:
            return whrandom.choice(([
                111.0,
                -29.0,
                2.0,
                90,
                0,
                0], [
                105,
                17,
                -1.3,
                -160.2,
                0.0,
                0.0], [
                145,
                -4,
                -1.3,
                135.9,
                0.0,
                0.0], [
                146,
                -53,
                -1.3,
                56.5,
                0.0,
                0.0], [
                105,
                -55,
                -1.3,
                -54.4,
                0.0,
                0.0], [
                189,
                -19,
                6.4,
                101.0,
                0.0,
                0.0], [
                135,
                -104,
                6.5,
                63.3,
                0.0,
                0.0], [
                45,
                -69,
                6.6,
                31.2,
                0.0,
                0.0], [
                104,
                57,
                6.7,
                164.0,
                0.0,
                0.0], [
                73,
                -16,
                -3.3,
                -122.0,
                0.0,
                0.0]))
        elif hoodId == TheBrrrgh:
            return whrandom.choice(([
                -109,
                -39,
                8.7,
                -78.0,
                0.0,
                0.0], [
                -60,
                65,
                6.2,
                179.3,
                0.0,
                0.0], [
                20,
                8,
                6.2,
                169.1,
                0.0,
                0.0], [
                -5,
                -53,
                6.2,
                -43.0,
                0.0,
                0.0], [
                -52,
                -111,
                6.2,
                25.0,
                0.0,
                0.0], [
                -101,
                -111,
                6.2,
                -20.2,
                0.0,
                0.0], [
                53,
                9,
                6.2,
                87.0,
                0.0,
                0.0], [
                -28,
                59,
                6.2,
                -117.4,
                0.0,
                0.0], [
                -109,
                61,
                6.2,
                -130.4,
                0.0,
                0.0], [
                -86,
                -5,
                3.0,
                -72.6,
                0.0,
                0.0]))
        elif hoodId == MinniesMelodyland:
            return whrandom.choice(([
                86,
                44,
                -13.5,
                121.1,
                0.0,
                0.0], [
                88,
                -16,
                -13.5,
                91.3,
                0.0,
                0.0], [
                92,
                -76,
                -13.5,
                62.5,
                0.0,
                0.0], [
                53,
                -112,
                6.5,
                65.8,
                0.0,
                0.0], [
                -18,
                -110,
                6.5,
                7.4,
                0.0,
                0.0], [
                -69,
                -71,
                6.5,
                -67.2,
                0.0,
                0.0], [
                -75,
                21,
                6.5,
                -100.9,
                0.0,
                0.0], [
                -21,
                72,
                6.5,
                -129.5,
                0.0,
                0.0], [
                56,
                72,
                6.5,
                138.2,
                0.0,
                0.0], [
                -41,
                47,
                6.5,
                -98.9,
                0.0,
                0.0]))
        elif hoodId == DaisyGardens:
            return whrandom.choice(([
                0,
                0,
                0,
                0,
                0,
                0], [
                76,
                35,
                1.1,
                -12.9,
                0.0,
                0.0], [
                97,
                106,
                0.0,
                51.4,
                0.0,
                0.0], [
                51,
                180,
                10.0,
                22.6,
                0.0,
                0.0], [
                -14,
                203,
                10.0,
                85.6,
                0.0,
                0.0], [
                -58,
                158,
                10.0,
                -146.9,
                0.0,
                0.0], [
                -86,
                128,
                0.0,
                -178.9,
                0.0,
                0.0], [
                -64,
                65,
                0.0,
                17.7,
                0.0,
                0.0], [
                -13,
                39,
                0.0,
                -15.7,
                0.0,
                0.0], [
                -12,
                193,
                0.0,
                -112.4,
                0.0,
                0.0], [
                87,
                128,
                0.0,
                45.4,
                0.0,
                0.0]))
        elif hoodId == ConstructionZone:
            return whrandom.choice(([
                0,
                0,
                0,
                0,
                0,
                0],))
        elif hoodId == FunnyFarm:
            return whrandom.choice(([
                0,
                0,
                0,
                0,
                0,
                0],))
        elif hoodId == GoofyStadium:
            return whrandom.choice(([
                0,
                0,
                0,
                0,
                0,
                0],))
        elif hoodId == DonaldsDreamland:
            return whrandom.choice(([
                77,
                91,
                0.0,
                124.4,
                0.0,
                0.0], [
                29,
                92,
                0.0,
                -154.5,
                0.0,
                0.0], [
                -28,
                49,
                -16.4,
                -142.0,
                0.0,
                0.0], [
                21,
                40,
                -16.0,
                -65.1,
                0.0,
                0.0], [
                48,
                27,
                -15.4,
                -161.0,
                0.0,
                0.0], [
                -2,
                -22,
                -15.2,
                -132.1,
                0.0,
                0.0], [
                -92,
                -88,
                0.0,
                -116.3,
                0.0,
                0.0], [
                -56,
                -93,
                0.0,
                -21.5,
                0.0,
                0.0], [
                20,
                -88,
                0.0,
                -123.4,
                0.0,
                0.0], [
                76,
                -90,
                0.0,
                11.0,
                0.0,
                0.0]))
        elif hoodId == BossbotHQ:
            return whrandom.choice(([
                0,
                0,
                0,
                0,
                0,
                0],))
        elif hoodId == SellbotHQ:
            return whrandom.choice(([
                0,
                0,
                0,
                0,
                0,
                0],))
        elif hoodId == CashbotHQ:
            return whrandom.choice(([
                0,
                0,
                0,
                0,
                0,
                0],))
        elif hoodId == LawbotHQ:
            return whrandom.choice(([
                0,
                0,
                0,
                0,
                0,
                0],))
        elif hoodId == Tutorial:
            return whrandom.choice(([
                130.9,
                -8.6,
                -1.3,
                105.5,
                0,
                0],))
        else:
            self.notify.error('getSafeZoneCenterFromId: No such hood name as: ' + str(hoodId))

    
    def getBranchZone(self, zoneId):
        return zoneId - zoneId % 100

    
    def getSafeZone(self, zoneId):
        return zoneId - zoneId % 1000

    
    def getIdFromName(self, hoodName):
        if hoodName == 'dd':
            return DonaldsDock
        elif hoodName == 'tt':
            return ToontownCentral
        elif hoodName == 'br':
            return TheBrrrgh
        elif hoodName == 'mm':
            return MinniesMelodyland
        elif hoodName == 'dg':
            return DaisyGardens
        elif hoodName == 'cz':
            return ConstructionZone
        elif hoodName == 'ff':
            return FunnyFarm
        elif hoodName == 'gs':
            return GoofyStadium
        elif hoodName == 'dl':
            return DonaldsDreamland
        elif hoodName == 'bh':
            return BossbotHQ
        elif hoodName == 'sh':
            return SellbotHQ
        elif hoodName == 'ch':
            return CashbotHQ
        elif hoodName == 'lh':
            return LawbotHQ
        else:
            self.notify.error('No such hood name as: ' + hoodName)
            return None
        return None

    
    def getNameFromId(self, hoodId):
        if hoodId == DonaldsDock:
            return 'dd'
        elif hoodId == ToontownCentral:
            return 'tt'
        elif hoodId == TheBrrrgh:
            return 'br'
        elif hoodId == MinniesMelodyland:
            return 'mm'
        elif hoodId == DaisyGardens:
            return 'dg'
        elif hoodId == ConstructionZone:
            return 'cz'
        elif hoodId == FunnyFarm:
            return 'ff'
        elif hoodId == GoofyStadium:
            return 'gs'
        elif hoodId == DonaldsDreamland:
            return 'dl'
        elif hoodId == BossbotHQ:
            return 'bh'
        elif hoodId == SellbotHQ:
            return 'sh'
        elif hoodId == CashbotHQ:
            return 'ch'
        elif hoodId == LawbotHQ:
            return 'lh'
        else:
            self.notify.error('No such hood id as: ' + str(hoodId))
            return None

    
    def getFullnameFromId(self, hoodId):
        if hoodId == DonaldsDock:
            return "Donald's Dock"
        elif hoodId == ToontownCentral:
            return 'Toontown Central'
        elif hoodId == TheBrrrgh:
            return 'The Brrrgh'
        elif hoodId == MinniesMelodyland:
            return "Minnie's Melodyland"
        elif hoodId == DaisyGardens:
            return 'Daisy Gardens'
        elif hoodId == ConstructionZone:
            return 'Construction Zone'
        elif hoodId == FunnyFarm:
            return 'Funny Farm'
        elif hoodId == GoofyStadium:
            return 'Goofy Stadium'
        elif hoodId == DonaldsDreamland:
            return "Donald's Dreamland"
        elif hoodId == BossbotHQ:
            return 'Bossbot HQ'
        elif hoodId == SellbotHQ:
            return 'Sellbot HQ'
        elif hoodId == CashbotHQ:
            return 'Cashbot HQ'
        elif hoodId == LawbotHQ:
            return 'Lawbot HQ'
        elif hoodId == Tutorial:
            return 'Toon-torial'
        else:
            print 'No such hood id as: ', str(hoodId)

    
    def addLinkTunnelHooks(self, hoodPart, nodeList):
        tunnelOriginList = []
        for i in nodeList:
            linkTunnelNPC = i.findAllMatches('**/linktunnel*')
            for p in range(linkTunnelNPC.getNumPaths()):
                linkTunnel = linkTunnelNPC.getPath(p)
                name = linkTunnel.getName()
                hoodStr = name[11:13]
                zoneStr = name[14:18]
                hoodId = self.getIdFromName(hoodStr)
                zoneId = int(zoneStr)
                linkSphere = linkTunnel.find('**/tunnel_trigger')
                if linkSphere.isEmpty():
                    self.notify.error('tunnel_trigger not found')
                
                linkSphere.node().setName('tunnel_trigger_' + hoodStr + '_' + zoneStr)
                tunnelOrigin = linkTunnel.find('**/tunnel_origin')
                if tunnelOrigin.isEmpty():
                    self.notify.error('tunnel_origin not found')
                
                tunnelOriginPlaceHolder = render.attachNewNode('toph_' + hoodStr + '_' + zoneStr)
                tunnelOriginList.append(tunnelOriginPlaceHolder)
                tunnelOriginPlaceHolder.setPos(tunnelOrigin.getPos(render))
                tunnelOriginPlaceHolder.setHpr(tunnelOrigin.getHpr(render))
                hoodPart.accept('enter' + linkSphere.getName(), hoodPart.handleEnterTunnel, [
                    {
                        'mode': 'tunnelOut',
                        'hoodId': hoodId,
                        'zoneId': zoneId,
                        'tunnelOrigin': tunnelOriginPlaceHolder,
                        'tutorial': 0 }])
            
        
        return tunnelOriginList

    
    def extractGroupName(self, groupFullName):
        return string.split(groupFullName, ':', 1)[0]

    
    def makeLinkTunnelName(self, hoodId, currentZone):
        return '**/toph_' + self.getNameFromId(hoodId) + '_' + str(currentZone)


