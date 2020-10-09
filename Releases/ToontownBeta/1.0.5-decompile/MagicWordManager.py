# Source Generated with Decompyle++
# File: MagicWordManager.pyo (Python 2.0)

from ShowBaseGlobal import *
import DistributedObject
import DirectNotifyGlobal

class MagicWordManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('MagicWordManager')
    wantMagicWords = base.config.GetBool('want-magic-words', 0)
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.setNeverDisable(1)
        return None

    
    def generate(self):
        self.accept('magicWord', self.b_setMagicWord)
        return None

    
    def disable(self):
        self.ignore('magicWord')
        return None

    
    def setMagicWord(self, magicWord):
        if magicWord == '~endgame':
            print 'Requesting minigame abort...'
            messenger.send('minigameAbort')
        
        return None

    
    def d_setMagicWord(self, magicWord):
        self.sendUpdate('setMagicWord', [
            magicWord])
        return None

    
    def b_setMagicWord(self, magicWord):
        if self.wantMagicWords:
            self.setMagicWord(magicWord)
            self.d_setMagicWord(magicWord)
        
        return None


