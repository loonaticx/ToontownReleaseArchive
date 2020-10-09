# Source Generated with Decompyle++
# File: OnscreenPanel.pyo (Python 2.0)

from ShowBaseGlobal import *
import GuiGlobals
import PandaObject
import Button
import Label
import OnscreenText
import types

def findPanel(uniqueName):
    if OnscreenPanel.AllPanels.has_key(uniqueName):
        return OnscreenPanel.AllPanels[uniqueName]
    
    return None


def cleanupPanel(uniqueName):
    if OnscreenPanel.AllPanels.has_key(uniqueName):
        OnscreenPanel.AllPanels[uniqueName].cleanup()
    


class OnscreenPanel(PandaObject.PandaObject, NodePath):
    AllPanels = { }
    
    def __init__(self, panelName):
        self.panelName = panelName
        self.panelSetup = 0
        NodePath.__init__(self, aspect2d.attachNewNode(panelName))
        NodePath.hide(self)

    
    def makePanel(self, rect = (-0.5, 0.5, -0.5, 0.5), bg = (1, 1, 1, 1), geom = GuiGlobals.getDefaultPanel(), geomRect = (-0.5, 0.5, -0.5, 0.5), drawOrder = 0, font = GuiGlobals.getDefaultFont(), support3d = 0):
        uniqueName = self.getUniqueName()
        cleanupPanel(uniqueName)
        OnscreenPanel.AllPanels[uniqueName] = self
        self.panelSetup = 1
        self.panelDrawOrder = drawOrder
        self.panelFont = font
        self.panelButtons = []
        self.panelText = []
        if geom == None:
            self.panelGeom = None
        elif isinstance(geom, types.StringType):
            self.panelGeom = loader.loadModelCopy(geom)
            self.panelGeom.reparentTo(self)
        else:
            self.panelGeom = geom.instanceTo(self)
        centerX = (rect[0] + rect[1]) / 2.0
        centerY = (rect[2] + rect[3]) / 2.0
        NodePath.setPos(self, centerX, 0, centerY)
        self.setBin('fixed', self.panelDrawOrder)
        self.panelRegion = None
        if self.panelGeom != None:
            gCenterX = (geomRect[0] + geomRect[1]) / 2.0
            gCenterY = (geomRect[2] + geomRect[3]) / 2.0
            self.panelGeom.setPos(-gCenterX, 0, -gCenterY)
            self.panelGeom.setScale((rect[1] - rect[0]) / (geomRect[1] - geomRect[0]), 1, (rect[3] - rect[2]) / (geomRect[3] - geomRect[2]))
            if bg[3] != 1:
                self.panelGeom.setTransparency(1)
            
            self.panelGeom.setColor(bg[0], bg[1], bg[2], bg[3])
            if support3d:
                dw = DepthWriteTransition()
                self.panelGeom.setY(100)
                self.panelGeom.arc().setTransition(dw, 1)
            
            self.geomRect = geomRect
            self.panelRegion = MouseWatcherRegion(uniqueName, 0, 0, 0, 0)
            self.panelRegion.setRelative(self.panelGeom, geomRect[0], geomRect[1], geomRect[2], geomRect[3])
            self.panelRegion.setSort(self.panelDrawOrder)
        

    
    def cleanup(self):
        if not (self.panelSetup):
            return 0
        
        self.hide()
        for button in self.panelButtons:
            button.cleanup()
        
        del self.panelButtons
        for text in self.panelText:
            text.cleanup()
        
        del self.panelText
        if not self.isEmpty():
            self.removeNode()
        
        uniqueName = self.getUniqueName()
        if OnscreenPanel.AllPanels.has_key(uniqueName):
            del OnscreenPanel.AllPanels[uniqueName]
        
        self.panelSetup = 0
        return 1

    
    def show(self):
        if not (self.panelSetup):
            return 0
        
        NodePath.show(self)
        for button in self.panelButtons:
            if button.panelManage:
                button.manage(self)
            
            if button.func != None:
                if button.event != None:
                    self.accept(button.event, button.func, [
                        button.button])
                else:
                    self.accept(button.button.getDownRolloverEvent(), button.func, [
                        button.button])
                button.startBehavior()
            
        
        if self.panelRegion != None:
            base.mouseWatcherNode.addRegion(self.panelRegion)
        

    
    def hide(self):
        if not (self.panelSetup):
            return 0
        
        NodePath.hide(self)
        for button in self.panelButtons:
            if button.event != None:
                self.ignore(button.event)
            else:
                self.ignore(button.button.getDownRolloverEvent())
            if button.panelManage:
                button.unmanage()
            
        
        if self.panelRegion != None:
            base.mouseWatcherNode.removeRegion(self.panelRegion)
        

    
    def makeButton(self, name, func = None, manage = 1, label = None, labels = None, scale = 0.1, width = None, align = None, drawOrder = None, font = None, pos = (0, 0), geomRect = None, supportInactive = 0, inactive = 0, upStyle = Label.ButtonUp, litStyle = Label.ButtonLit, downStyle = Label.ButtonDown, inactiveStyle = Label.ButtonInactive, event = None):
        if label == None and labels == None:
            label = name
        
        if drawOrder == None:
            drawOrder = self.panelDrawOrder + 10
        
        if font == None:
            font = self.panelFont
        
        buttonName = self.getUniqueName() + '-' + name
        button = Button.Button(buttonName, label = label, labels = labels, scale = scale, width = width, align = align, drawOrder = drawOrder, font = font, pos = pos, geomRect = geomRect, supportInactive = supportInactive, inactive = inactive, upStyle = upStyle, litStyle = litStyle, downStyle = downStyle, inactiveStyle = inactiveStyle, event = event)
        self.panelButtons.append(button)
        button.panelManage = manage
        button.func = func
        return button

    
    def makeText(self, text = '', style = OnscreenText.Plain, pos = (0, 0), scale = None, fg = None, bg = None, shadow = None, frame = None, align = None, wordwrap = None, drawOrder = None, font = None, parent = None, mayChange = 0):
        if drawOrder == None:
            drawOrder = self.panelDrawOrder + 10
        
        if font == None:
            font = self.panelFont
        
        if parent == None:
            parent = self
        
        text = OnscreenText.OnscreenText(text, style = style, pos = pos, scale = scale, fg = fg, bg = bg, shadow = shadow, frame = frame, align = align, wordwrap = wordwrap, drawOrder = drawOrder, font = font, parent = parent, mayChange = mayChange)
        self.panelText.append(text)
        return text

    
    def getUniqueName(self):
        return self.panelName

    
    def setPos(self, x, y, z):
        NodePath.setPos(self, x, y, z)
        for button in self.panelButtons:
            if button.managed:
                button.unmanage()
                button.manage(self)
            
        
        if self.panelRegion != None:
            self.panelRegion.setRelative(self.panelGeom, self.geomRect[0], self.geomRect[1], self.geomRect[2], self.geomRect[3])
        


