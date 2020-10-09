# Source Generated with Decompyle++
# File: DistributedChar.pyo (Python 2.0)

import DistributedAvatar
import Char

class DistributedChar(DistributedAvatar.DistributedAvatar, Char.Char):
    
    def __init__(self, cr):
        
        try:
            self.DistributedChar_initialized
        except:
            self.DistributedChar_initialized = 1
            DistributedAvatar.DistributedAvatar.__init__(self, cr)

        return None

    
    def setHp(self, hp):
        self.hp = hp
        return None


