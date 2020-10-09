# Source Generated with Decompyle++
# File: InventoryPage.pyo (Python 2.0)

import ShtikerPage
from DirectGui import *

class InventoryPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    
    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.title = DirectLabel(parent = self, relief = None, text = 'Gags', text_scale = 0.12, pos = (0, 0, 0.6))

    
    def unload(self):
        del self.title
        ShtikerPage.ShtikerPage.unload(self)

    
    def enter(self):
        ShtikerPage.ShtikerPage.enter(self)
        toonbase.localToon.inventory.show()
        toonbase.localToon.inventory.reparentTo(self)
        toonbase.localToon.inventory.setActivateMode('book')
        self.accept('enterBookDelete', self.enterDeleteMode)
        self.accept('exitBookDelete', self.exitDeleteMode)

    
    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)
        self.ignore('enterBookDelete')
        self.ignore('exitBookDelete')
        self.makePageWhite(None)
        toonbase.localToon.inventory.hide()
        toonbase.localToon.inventory.reparentTo(hidden)
        self.exitDeleteMode()

    
    def enterDeleteMode(self):
        self.title['text'] = 'DELETE GAGS'
        self.title['text_fg'] = (0, 0, 0, 1)
        self.book['image_color'] = Vec4(1, 1, 0, 1)

    
    def exitDeleteMode(self):
        self.title['text'] = 'Gags'
        self.title['text_fg'] = (0, 0, 0, 1)
        self.book['image_color'] = Vec4(1, 1, 1, 1)


