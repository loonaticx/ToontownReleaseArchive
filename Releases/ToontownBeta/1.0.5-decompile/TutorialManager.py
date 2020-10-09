# Source Generated with Decompyle++
# File: TutorialManager.pyo (Python 2.0)

from ShowBaseGlobal import *
from PandaObject import *
import DistributedObject
import DirectNotifyGlobal

class TutorialManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('TutorialManager')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.setNeverDisable(1)
        return None

    
    def generate(self):
        messenger.send('tmGenerate')
        self.accept('requestTutorial', self.d_requestTutorial)
        self.accept('rejectTutorial', self.d_rejectTutorial)
        return None

    
    def disable(self):
        self.ignoreAll()
        return None

    
    def d_requestTutorial(self):
        self.sendUpdate('requestTutorial', [])
        return None

    
    def d_rejectTutorial(self):
        self.sendUpdate('rejectTutorial', [])
        return None

    
    def enterTutorial(self, zoneId):
        messenger.send('startTutorial', [
            zoneId])


