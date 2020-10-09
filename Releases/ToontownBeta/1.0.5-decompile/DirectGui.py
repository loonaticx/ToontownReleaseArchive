# Source Generated with Decompyle++
# File: DirectGui.pyo (Python 2.0)

from DirectGuiGlobals import *
import __builtin__
__builtin__.guiTop = aspect2d.attachNewNode(PGTop('DirectGuiTop'))
guiTop.node().setMouseWatcher(base.mouseWatcherNode)
base.mouseWatcherNode.addRegion(PGMouseWatcherBackground())
PGItem.getTextNode().setFont(getDefaultFont())
from DirectFrame import *
from DirectButton import *
from DirectEntry import *
from DirectLabel import *
from DirectScrolledList import *
