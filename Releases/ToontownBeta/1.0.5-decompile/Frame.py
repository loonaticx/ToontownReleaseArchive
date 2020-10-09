# Source Generated with Decompyle++
# File: Frame.pyo (Python 2.0)

from ShowBaseGlobal import *
from DirectObject import *
from GuiGlobals import *
import GuiFrame
import Vec3

class Frame(DirectObject):
    
    def __init__(self, name):
        self.name = name
        self.managed = 0
        self.offset = 0
        self.frame = GuiFrame.GuiFrame(name)
        self.items = []
        return None

    
    def cleanup(self):
        if self.managed:
            self.frame.unmanage()
        
        self.frame = None
        return None

    
    def __str__(self):
        return 'Frame: %s = %s' % (self.name, self.items)

    
    def getName(self):
        return self.name

    
    def getPos(self):
        return self.frame.getPos()

    
    def setPos(self, x, y):
        v3 = Vec3.Vec3(x, 0.0, y)
        self.frame.setPos(v3)

    
    def setScale(self, scale):
        self.frame.setScale(scale)

    
    def getOffset(self):
        return self.offset

    
    def setOffset(self, offset):
        self.offset = offset

    
    def freeze(self):
        self.frame.freeze()

    
    def thaw(self):
        self.frame.thaw()

    
    def manage(self, nodepath = aspect2d):
        if nodepath:
            self.frame.manage(guiMgr, base.eventMgr.eventHandler, nodepath.node())
        else:
            self.frame.manage(guiMgr, base.eventMgr.eventHandler)
        self.managed = 1

    
    def unmanage(self):
        self.frame.unmanage()
        self.managed = 0

    
    def recompute(self):
        self.frame.recompute()

    
    def clearAllPacking(self):
        self.frame.clearAllPacking()

    
    def addItem(self, item):
        self.frame.addItem(item.getGuiItem())
        self.items.append(item)

    
    def removeItem(self, item):
        self.frame.removeItem(item.getGuiItem())
        self.items.remove(item)

    
    def getGuiItem(self):
        return self.frame

    
    def getItems(self):
        return self.items

    
    def printItems(self):
        print 'frame items: %s' % self.items

    
    def packItem(self, item, relation, otherItem):
        if item in self.items and otherItem in self.items:
            self.frame.packItem(item.getGuiItem(), relation, otherItem.getGuiItem(), self.offset)
        else:
            print "warning: tried to pack item that isn't in frame"

    
    def makeVertical(self):
        for itemNum in range(1, len(self.items)):
            self.packItem(self.items[itemNum], GuiFrame.GuiFrame.UNDER, self.items[itemNum - 1])
            self.packItem(self.items[itemNum], GuiFrame.GuiFrame.ALIGNLEFT, self.items[itemNum - 1])
        
        self.frame.recompute()

    
    def makeHorizontal(self):
        for itemNum in range(1, len(self.items)):
            self.packItem(self.items[itemNum], GuiFrame.GuiFrame.RIGHT, self.items[itemNum - 1])
            self.packItem(self.items[itemNum], GuiFrame.GuiFrame.ALIGNABOVE, self.items[itemNum - 1])
        
        self.frame.recompute()

    
    def makeWideAsWidest(self):
        widestWidth = 0.0
        for item in self.items:
            thisWidth = item.getWidth()
            if thisWidth > widestWidth:
                widestWidth = thisWidth
            
        
        for item in self.items:
            item.setWidth(widestWidth)
        


