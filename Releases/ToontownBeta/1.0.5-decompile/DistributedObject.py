# Source Generated with Decompyle++
# File: DistributedObject.pyo (Python 2.0)

from PandaObject import *
from DirectNotifyGlobal import *

class DistributedObject(PandaObject):
    notify = directNotify.newCategory('DistributedObject')
    
    def __init__(self, cr):
        
        try:
            self.DistributedObject_initialized
        except:
            self.DistributedObject_initialized = 1
            self.cr = cr
            self.setNeverDisable(0)
            self.setCacheable(0)
            self.delayDeleteFlag = 0
            self.deleteImminent = 0

        return None

    
    def setNeverDisable(self, bool):
        self.neverDisable = bool
        return None

    
    def getNeverDisable(self):
        return self.neverDisable

    
    def setCacheable(self, bool):
        self.cacheable = bool
        return None

    
    def getCacheable(self):
        return self.cacheable

    
    def deleteOrDelay(self):
        if self.delayDeleteFlag:
            self.deleteImminent = 1
        else:
            self.disableAnnounceAndDelete()
        return None

    
    def delayDelete(self, flag):
        if self.delayDeleteFlag:
            if flag:
                self.notify.warning('Object: ' + str(self.getDoId()) + ' is already in delayDelete mode')
            else:
                self.delayDeleteFlag = 0
                if self.deleteImminent:
                    self.disableAnnounceAndDelete()
                
        elif flag:
            self.delayDeleteFlag = 1
        else:
            self.notify.warning('Object: ' + str(self.getDoId()) + ' is not in delayDelete mode')
        return None

    
    def disableAnnounceAndDelete(self):
        self.disableAndAnnounce()
        self.delete()
        return None

    
    def disableAndAnnounce(self):
        self.disable()
        messenger.send(self.uniqueName('disable'))
        return None

    
    def announceGenerate(self):
        messenger.send(self.uniqueName('generate'), [
            self])

    
    def disable(self):
        pass

    
    def delete(self):
        
        try:
            self.DistributedObject_deleted
        except:
            self.DistributedObject_deleted = 1
            del self.cr
            return None


    
    def generate(self):
        pass

    
    def generateInit(self):
        pass

    
    def getDoId(self):
        return self.doId

    
    def updateRequiredFields(self, cdc, di):
        for i in cdc.broadcastRequiredCDU:
            i.updateField(cdc, self, di)
        

    
    def updateAllRequiredFields(self, cdc, di):
        for i in cdc.allRequiredCDU:
            i.updateField(cdc, self, di)
        

    
    def updateRequiredOtherFields(self, cdc, di):
        for i in cdc.broadcastRequiredCDU:
            i.updateField(cdc, self, di)
        
        numberOfOtherFields = di.getArg(STUint16)
        for i in range(numberOfOtherFields):
            cdc.updateField(self, di)
        
        return None

    
    def sendUpdate(self, fieldName, args = [], sendToId = None):
        self.cr.sendUpdate(self, fieldName, args, sendToId)

    
    def taskName(self, taskString):
        return taskString + '-' + str(self.getDoId())

    
    def uniqueName(self, idString):
        return idString + '-' + str(self.getDoId())


