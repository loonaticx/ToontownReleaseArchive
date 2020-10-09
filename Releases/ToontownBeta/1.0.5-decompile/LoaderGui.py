# Source Generated with Decompyle++
# File: LoaderGui.pyo (Python 2.0)

from PandaModules import *
from ShowBaseGlobal import *
import GuiGlobals

class LoaderGui:
    
    def __init__(self, size, name, pos = None, namePos = None):
        self.size = size
        self.count = 0
        base.render.stash()
        self.width = base.config.GetFloat('loader-bar-width', 1.0)
        self.height = base.config.GetFloat('loader-bar-height', 0.1)
        doneRed = base.config.GetFloat('loader-bar-done-red', 1.0)
        doneGreen = base.config.GetFloat('loader-bar-done-green', 0.0)
        doneBlue = base.config.GetFloat('loader-bar-done-blue', 0.0)
        doneAlpha = base.config.GetFloat('loader-bar-done-alpha', 1.0)
        undoneRed = base.config.GetFloat('loader-bar-undone-red', 1.0)
        undoneGreen = base.config.GetFloat('loader-bar-undone-green', 1.0)
        undoneBlue = base.config.GetFloat('loader-bar-undone-blue', 1.0)
        undoneAlpha = base.config.GetFloat('loader-bar-undone-alpha', 1.0)
        self.doneLabel = GuiLabel.makeSimpleCardLabel()
        self.undoneLabel = GuiLabel.makeSimpleCardLabel()
        self.doneLabel.setDrawOrder(100000)
        self.undoneLabel.setDrawOrder(100000)
        self.doneLabel.setForegroundColor(doneRed, doneGreen, doneBlue, doneAlpha)
        self.undoneLabel.setForegroundColor(undoneRed, undoneGreen, undoneBlue, undoneAlpha)
        self.doneLabel.setWidth(0.0001)
        self.doneLabel.setHeight(self.height)
        self.undoneLabel.setWidth(self.width)
        self.undoneLabel.setHeight(self.height)
        self.doneSign = GuiSign('done', self.doneLabel)
        self.undoneSign = GuiSign('undone', self.undoneLabel)
        self.name = 'Loading...'
        self.nameSign = self._LoaderGui__makeSign(self.name, 'loading')
        if pos:
            self.pos = pos
        else:
            self.pos = Vec3(0.0, 0.0, 0.0)
        if namePos:
            self.namePos = namePos
        else:
            self.namePos = Vec3(0.0, 0.0, self.height)
        self.adjustBars()
        self.nameSign.freeze()
        self.nameSign.setDrawOrder(100000)
        self.nameSign.setPos(Vec3(self.pos[0] + self.namePos[0], self.pos[1] + self.namePos[1], self.pos[2] + self.namePos[2]))
        self.nameSign.setScale(self.height)
        self.nameSign.thaw()
        self.doneSign.manage(GuiGlobals.guiMgr, base.eventMgr.eventHandler)
        self.undoneSign.manage(GuiGlobals.guiMgr, base.eventMgr.eventHandler)
        self.nameSign.manage(GuiGlobals.guiMgr, base.eventMgr.eventHandler)

    
    def show(self):
        self.doneSign.manage(GuiGlobals.guiMgr, base.eventMgr.eventHandler)
        self.undoneSign.manage(GuiGlobals.guiMgr, base.eventMgr.eventHandler)
        self.nameSign.manage(GuiGlobals.guiMgr, base.eventMgr.eventHandler)
        return None

    
    def hide(self):
        self.doneSign.unmanage()
        self.undoneSign.unmanage()
        self.nameSign.unmanage()
        return None

    
    def __del__(self):
        base.render.unstash()
        self.doneSign.unmanage()
        self.undoneSign.unmanage()
        self.nameSign.unmanage()
        del self.doneSign
        del self.undoneSign
        del self.nameSign
        del self.doneLabel
        del self.undoneLabel
        del self.pos
        del self.namePos
        base.win.update()

    
    def __makeLabel(self, txt):
        label = GuiLabel.makeSimpleTextLabel(txt, GuiGlobals.getDefaultFont())
        label.setForegroundColor(1.0, 1.0, 1.0, 1.0)
        label.setBackgroundColor(1.0, 1.0, 1.0, 0.0)
        label.setScale(0.75, 1.0, 1.0)
        label.thaw()
        return label

    
    def __makeSign(self, txt, name):
        label = self._LoaderGui__makeLabel(txt)
        sign = GuiSign(name, label)
        return sign

    
    def adjustBars(self):
        frac = float(self.count) / float(self.size)
        fracRecip = 1.0 - frac
        if fracRecip < 0.0:
            fracRecip = 0.0
        
        if frac > 1.0:
            frac = 1.0
        
        doneFrac = self.width * frac
        undoneFrac = self.width * fracRecip
        if doneFrac < 0.0001:
            self.doneLabel.setWidth(0.0001)
        else:
            self.doneLabel.setWidth(doneFrac)
        if undoneFrac < 0.0001:
            undoneFrac = 0.0
            self.undoneLabel.setWidth(0.0001)
        else:
            self.undoneLabel.setWidth(undoneFrac)
        donePos = (doneFrac - self.width) * 0.5
        undonePos = (self.width - undoneFrac) * 0.5
        donePos = Vec3(self.pos[0] + donePos, self.pos[1], self.pos[2])
        undonePos = Vec3(self.pos[0] + undonePos, self.pos[1], self.pos[2])
        self.doneSign.setPos(donePos)
        self.undoneSign.setPos(undonePos)

    
    def update(self, count):
        self.count = count
        self.adjustBars()
        base.win.update()
        while not base.eventMgr.eventQueue.isQueueEmpty():
            event = base.eventMgr.eventQueue.dequeueEvent()
            base.eventMgr.processEvent(event)

    
    def finish(self):
        N = 10
        remaining = self.size - self.count
        if remaining:
            step = max(1, int(remaining / N))
            while self.count != self.size:
                self.count += step
                if self.count > self.size:
                    self.count = self.size
                
                self.update(self.count)
        
        return None


