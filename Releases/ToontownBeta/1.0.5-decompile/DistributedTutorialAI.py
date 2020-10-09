# Source Generated with Decompyle++
# File: DistributedTutorialAI.pyo (Python 2.0)

from AIBaseGlobal import *
from PandaModules import *
import DistributedObjectAI
import DirectNotifyGlobal
import DistributedTrolleyAI

class DistributedTutorialAI(DistributedObjectAI.DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTutorialAI')
    
    def __init__(self, air, avId):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.avId = avId
        self.acceptOnce(self.air.getAvatarExitEvent(avId), self._DistributedTutorialAI__handleUnexpectedExit, extraArgs = [
            avId])
        return None

    
    def generate(self):
        self.trolley = DistributedTrolleyAI.DistributedTrolleyAI(self.air)
        self.trolley.generateWithRequired(self.zoneId)
        self.trolley.start()
        return None

    
    def allDone(self):
        if self.air.msgSender == self.avId:
            taskMgr.doMethodLater(20, self.endTutorialTask, self.uniqueName('endTutorial-timer'))
            av = self.air.doId2do.get(self.avId)
            av.b_setTutorialAck(1)
        else:
            self.notify.warning('%s tried to end tutorial for %s' % [
                self.air.msgSender,
                self.avId])
        return None

    
    def endTutorialTask(self, task):
        self.endTutorial()
        return Task.done

    
    def endTutorial(self):
        self.air.deallocateZone(self.zoneId)
        self.requestDelete()
        self.trolley.requestDelete()

    
    def delete(self):
        taskMgr.removeTasksNamed('endTutorial-timer')
        self.ignoreAll()
        return None

    
    def __handleUnexpectedExit(self, avId):
        self.notify.warning('Avatar: ' + str(avId) + ' has exited unexpectedly')
        self.endTutorial()
        return None


