# Source Generated with Decompyle++
# File: ScrollingLabel.pyo (Python 2.0)

from ShowBaseGlobal import *
from GuiGlobals import *
import PandaObject
import Frame
import GuiFrame
import Button
import GuiLabel
import Sign
import Label

class ScrollingLabel(PandaObject.PandaObject):
    
    def __init__(self, name, itemList, label = None, scale = 0.1, width = None, drawOrder = getDefaultDrawOrder(), font = getDefaultFont(), showLabels = 1, leftLabels = None, rightLabels = None):
        self.name = name
        if label == None:
            self.label = self.name
        else:
            self.label = label
        self.eventName = self.name
        self.frame = Frame.Frame(name)
        self.frame.setOffset(0.015)
        self.item = 0
        self.items = itemList
        self.showLabels = showLabels
        if showLabels:
            itemString = ' '
        else:
            itemString = ''
        self.keyFocus = 1
        if width == None:
            width = 0
            text = TextNode()
            text.setFont(font)
            for item in itemList:
                w = text.calcWidth(item) + 0.2
                width = max(width, w)
            
        
        self.title = Sign.Sign(self.name, self.label, Label.ScrollTitle, scale, width, drawOrder, font)
        self.frame.addItem(self.title)
        self.itemSign = Sign.Sign('item', itemString, Label.ScrollItem, scale, width, drawOrder, font)
        self.frame.addItem(self.itemSign)
        self.frame.packItem(self.itemSign, GuiFrame.GuiFrame.UNDER, self.title)
        self.frame.packItem(self.itemSign, GuiFrame.GuiFrame.ALIGNLEFT, self.title)
        if leftLabels:
            self.leftButton = Button.Button(self.eventName + '-left', labels = leftLabels, scale = scale, drawOrder = drawOrder, font = font, event = 'left-button')
        else:
            self.leftButton = Button.Button(self.eventName + '-left', label = ' < ', scale = scale, drawOrder = drawOrder, font = font, event = 'left-button')
        self.leftButton.getGuiItem().setUpRolloverEvent(self.eventName + '-rollover')
        self.frame.addItem(self.leftButton)
        self.frame.packItem(self.leftButton, GuiFrame.GuiFrame.UNDER, self.title)
        self.frame.packItem(self.leftButton, GuiFrame.GuiFrame.LEFT, self.title)
        if rightLabels:
            self.rightButton = Button.Button(self.eventName + '-right', labels = rightLabels, scale = scale, drawOrder = drawOrder, font = font, event = 'right-button')
        else:
            self.rightButton = Button.Button(self.eventName + '-right', label = ' > ', scale = scale, drawOrder = drawOrder, font = font, event = 'right-button')
        self.rightButton.getGuiItem().setUpRolloverEvent(self.eventName + '-rollover')
        self.frame.addItem(self.rightButton)
        self.frame.packItem(self.rightButton, GuiFrame.GuiFrame.UNDER, self.title)
        self.frame.packItem(self.rightButton, GuiFrame.GuiFrame.RIGHT, self.title)
        self.setItem(self.item)
        self.frame.recompute()
        return None

    
    def cleanup(self):
        self.ignore('left-button')
        self.ignore('right-button')
        self.ignore(self.eventName + '-rollover')
        self.setKeyFocus(0)
        self.frame.cleanup()
        self.frame = None
        self.items = None
        self.label = None
        self.title.cleanup()
        self.title = None
        self.itemSign.cleanup()
        self.itemSign = None
        self.leftButton.cleanup()
        self.leftButton = None
        self.rightButton.cleanup()
        self.rightButton = None
        return None

    
    def getTitle(self):
        return self.name

    
    def setTitle(self, name):
        self.name = name
        if self.showLabels:
            self.title.setText(name)
            self.frame.recompute()
        

    
    def getItemSign(self):
        return self.itemSign

    
    def getItem(self):
        return self.items[self.item]

    
    def setItem(self, item):
        self.item = item
        if self.showLabels:
            self.itemSign.setText(self.items[self.item])
        

    
    def getEventName(self):
        return self.eventName

    
    def setEventName(self, eventName):
        self.eventName = eventName

    
    def getPos(self):
        return self.frame.getPos()

    
    def setPos(self, x, y):
        self.frame.freeze()
        self.frame.setPos(x, y)
        self.frame.recompute()
        self.frame.thaw()

    
    def setScale(self, scale):
        self.frame.freeze()
        self.frame.setScale(scale)
        self.frame.recompute()
        self.frame.thaw()

    
    def setWidth(self, width):
        self.frame.freeze()
        self.itemSign.setWidth(width)
        self.frame.recompute()
        self.frame.thaw()

    
    def getKeyFocus(self):
        return self.keyFocus

    
    def setKeyFocus(self, focus):
        self.keyFocus = focus
        if focus == 1:
            self.ignore('left-up')
            self.ignore('right-up')
            self.accept('left-up', self.handleLeftArrow)
            self.accept('right-up', self.handleRightArrow)
        else:
            self.ignore('left-up')
            self.ignore('right-up')

    
    def recompute(self):
        self.frame.recompute()

    
    def manage(self):
        self.accept('left-button', self.handleLeftButton)
        self.accept('right-button', self.handleRightButton)
        self.frame.manage()
        self.setKeyFocus(0)
        self.leftButton.startBehavior()
        self.rightButton.startBehavior()
        return None

    
    def unmanage(self):
        self.ignore('left-up')
        self.ignore('right-up')
        self.ignore('left-button')
        self.ignore('right-button')
        self.ignore(self.eventName + '-rollover')
        self.setKeyFocus(0)
        self.frame.unmanage()
        return None

    
    def handleLeftButton(self, item):
        if self.leftButton.button == item:
            self.item = self.item - 1
            if self.item < 0:
                self.item = len(self.items) - 1
            
            self.setItem(self.item)
            messenger.send(self.eventName, [
                self.item])
        

    
    def handleRightButton(self, item):
        if self.rightButton.button == item:
            self.item = self.item + 1
            if self.item >= len(self.items):
                self.item = 0
            
            self.setItem(self.item)
            messenger.send(self.eventName, [
                self.item])
        

    
    def handleLeftArrow(self):
        self.leftButton.getGuiItem().down()
        self.spawnButtonUpTask(self.leftButton)

    
    def handleRightArrow(self):
        self.rightButton.getGuiItem().down()
        self.spawnButtonUpTask(self.rightButton)

    
    def spawnButtonUpTask(self, button):
        
        def buttonUp(state):
            state.button.getGuiItem().up()
            return Task.done

        task = Task.Task(buttonUp)
        task.button = button
        taskMgr.spawnTaskNamed(Task.doLater(0.035, task, 'buttonUp-later'), 'doLater-buttonUp-later')


