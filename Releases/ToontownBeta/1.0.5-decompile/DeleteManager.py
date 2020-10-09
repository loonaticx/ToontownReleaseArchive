# Source Generated with Decompyle++
# File: DeleteManager.pyo (Python 2.0)

from ShowBaseGlobal import *
import DistributedObject
import DirectNotifyGlobal

class DeleteManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DeleteManager')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.setNeverDisable(1)
        return None

    
    def generate(self):
        self.accept('deleteItems', self.d_setInventory)
        return None

    
    def disable(self):
        self.ignore('deleteItems')
        return None

    
    def d_setInventory(self, newInventoryString):
        self.sendUpdate('setInventory', [
            newInventoryString])
        return None


