# Source Generated with Decompyle++
# File: Button.pyo (Python 2.0)

from ShowBaseGlobal import *
from DirectObject import *
from GuiGlobals import *
import GuiButton
import Label

class Button(DirectObject):
    
    def __init__(self, name, label = None, labels = None, scale = 0.1, width = None, align = None, drawOrder = getDefaultDrawOrder(), font = getDefaultFont(), pos = (0, 0), geomRect = None, supportInactive = 0, inactive = 0, upStyle = Label.ButtonUp, litStyle = Label.ButtonLit, downStyle = Label.ButtonDown, inactiveStyle = Label.ButtonInactive, event = None, rolloverSound = None, clickSound = None):
        self.name = name
        self.width = width
        if label == None and labels == None:
            label = self.name
        
        self.inactive = inactive
        if inactive:
            supportInactive = 1
        
        if type(label) == type(''):
            self.label = label
            self.lUp = Label.textLabel(self.label, upStyle, scale, width, drawOrder, font)
            if width == None:
                width = self.lUp.getWidth() / scale
                self.width = width
            
            self.lLit = Label.textLabel(self.label, litStyle, scale, width, drawOrder, font)
            self.lDown = Label.textLabel(self.label, downStyle, scale, width, drawOrder, font)
            if supportInactive:
                self.lInactive = Label.textLabel(self.label, inactiveStyle, scale, width, drawOrder, font)
            
        elif isinstance(label, NodePath):
            self.lUp = Label.modelLabel(label, geomRect = geomRect, style = upStyle, scale = (scale, scale), drawOrder = drawOrder)
            if width == None:
                width = self.lUp.getWidth() / scale
                self.width = width
            
            self.lLit = Label.modelLabel(label, geomRect = geomRect, style = litStyle, scale = (scale, scale), drawOrder = drawOrder)
            self.lDown = Label.modelLabel(label, geomRect = geomRect, style = downStyle, scale = (scale, scale), drawOrder = drawOrder)
            if supportInactive:
                self.lInactive = Label.modelLabel(label, geomRect = geomRect, style = inactiveStyle, scale = (scale, scale), drawOrder = drawOrder)
            
        elif labels:
            (self.lUp, self.lLit, self.lDown, self.lInactive) = labels
        else:
            self.lUp = label
            self.lLit = label
            self.lDown = label
            self.lInactive = label
        if width == None:
            width = self.lUp.getWidth()
        
        if not supportInactive:
            self.lInactive = self.lUp
        
        self.button = GuiButton.GuiButton(self.name, self.lUp, self.lLit, self.lDown, self.lDown, self.lInactive)
        self.button.setDrawOrder(drawOrder)
        self.button.setRolloverFunctor(getNewRolloverFunctor(rolloverSound))
        self.button.setBehaviorFunctor(getNewClickFunctor(clickSound))
        if event != None:
            self.button.setBehaviorEvent(event)
        
        self.event = event
        if align == TMALIGNLEFT:
            self.xoffset = (width / 2.0) * scale
        elif align == TMALIGNRIGHT:
            self.xoffset = (-width / 2.0) * scale
        else:
            self.xoffset = 0
        self.setPos(pos[0], pos[1])
        self.managed = 0
        return None

    
    def cleanup(self):
        if self.managed:
            self.unmanage()
        
        del self.lUp
        del self.lLit
        del self.lDown
        del self.lInactive
        del self.button
        return None

    
    def __str__(self):
        return 'Button: %s' % self.name

    
    def getName(self):
        return self.name

    
    def getLabel(self):
        return self.label

    
    def getGuiItem(self):
        return self.button

    
    def getWidth(self):
        return self.width

    
    def setWidth(self, width):
        self.lUp.setWidth(width)
        self.lLit.setWidth(width)
        self.lDown.setWidth(width)
        self.lInactive.setWidth(width)

    
    def setInactive(self, inactive):
        self.inactive = inactive
        if self.managed:
            self.button.exit()
            if self.inactive:
                self.button.inactive()
            else:
                self.button.up()
                if self.event != None:
                    self.button.startBehavior()
                
        

    
    def manage(self, nodepath = aspect2d):
        if not (self.managed):
            if nodepath:
                self.button.manage(guiMgr, base.eventMgr.eventHandler, nodepath.node())
            else:
                self.button.manage(guiMgr, base.eventMgr.eventHandler)
            if self.event != None:
                self.button.startBehavior()
            
            if self.inactive:
                self.button.exit()
                self.button.inactive()
            
            self.managed = 1
        

    
    def unmanage(self):
        if self.managed:
            self.button.unmanage()
            self.managed = 0
        

    
    def getPos(self):
        v = self.button.getPos()
        return Vec3(v[0] - self.xoffset, v[1], v[2])

    
    def setPos(self, x, y, node = None):
        if node == None:
            v3 = Vec3(x + self.xoffset, 0.0, y)
        else:
            mat = node.getMat(base.render2d)
            v3 = Vec3(mat.xformPoint(Point3(x + self.xoffset, 0.0, y)))
        self.button.setPos(v3)

    
    def setBehaviorEvent(self, eventName):
        self.button.setBehaviorEvent(eventName)
        self.event = eventName

    
    def setBehaviorEventParameter(self, param):
        self.button.setBehaviorEventParameter(param)

    
    def startBehavior(self):
        self.button.startBehavior()

    
    def stopBehavior(self):
        self.button.stopBehavior()

    
    def setRolloverEvent(self, eventName):
        self.button.setUpRolloverEvent(eventName)

    
    def setDownRolloverEvent(self, eventName):
        self.button.setDownRolloverEvent(eventName)

    
    def setUpRolloverEvent(self, eventName):
        self.button.setUpRolloverEvent(eventName)

    
    def setDownEvent(self, eventName):
        self.button.setDownEvent(eventName)

    
    def setUpEvent(self, eventName):
        self.button.setUpEvent(eventName)


