# Source Generated with Decompyle++
# File: DirectLabel.pyo (Python 2.0)

from DirectFrame import *

class DirectLabel(DirectFrame):
    
    def __init__(self, parent = guiTop, **kw):
        optiondefs = (('pgFunc', PGItem, None), ('numStates', 1, None), ('activeState', 0, self.setActiveState))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.initialiseoptions(DirectLabel)

    
    def setActiveState(self):
        self.guiItem.setState(self['activeState'])


