# Source Generated with Decompyle++
# File: SuitPage.pyo (Python 2.0)

import ShtikerPage
from DirectGui import *

class SuitPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    
    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.title = DirectLabel(parent = self, relief = None, text = 'Cogs Defeated\n(Coming Soon)', text_scale = 0.12, pos = (0, 0, 0.6))

    
    def unload(self):
        del self.title
        ShtikerPage.ShtikerPage.unload(self)


