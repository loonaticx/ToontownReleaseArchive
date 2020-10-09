# Source Generated with Decompyle++
# File: TutorialManagerAI.pyo (Python 2.0)

from AIBaseGlobal import *
from PandaModules import *
import DistributedObjectAI
import DirectNotifyGlobal
import DistributedTutorialAI

class TutorialManagerAI(DistributedObjectAI.DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('TutorialManagerAI')
    
    def __init__(self, air):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        return None

    
    def requestTutorial(self):
        avId = self.air.msgSender
        av = self.air.doId2do.get(avId)
        if av:
            tutorialZone = self.air.allocateZone()
            self.d_enterTutorial(avId, tutorialZone)
            tutorial = DistributedTutorialAI.DistributedTutorialAI(self.air, avId)
            tutorial.generateWithRequired(tutorialZone)
        else:
            self.notify.warning('Toon ' + str(avId) + " isn't here, but just requested a tutorial. " + 'I will ignore this.')
        return None

    
    def rejectTutorial(self):
        avId = self.air.msgSender
        av = self.air.doId2do.get(avId)
        if av:
            av.b_setTutorialAck(1)
        else:
            self.notify.warning('Toon ' + str(avId) + " isn't here, but just rejected a tutorial. " + 'I will ignore this.')
        return None

    
    def d_enterTutorial(self, avId, zoneId):
        self.sendUpdateToAvatarId(avId, 'enterTutorial', [
            zoneId])
        return None


