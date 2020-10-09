# Source Generated with Decompyle++
# File: PickList.pyo (Python 2.0)

from ShowBaseGlobal import *
from GuiGlobals import *
import PandaObject
import Frame
import Button

class PickList(PandaObject.PandaObject):
    
    def __init__(self, name, choiceList, scale = 0.1, width = None, drawOrder = getDefaultDrawOrder(), font = getDefaultFont()):
        self.name = name
        self.frame = Frame.Frame(name)
        self.choice = -1
        self.choiceList = []
        self.eventName = self.name
        self.frame.setOffset(0.015)
        self._PickList__displayChoices(choiceList, scale, width, drawOrder, font)
        self.isClean = 0
        return None

    
    def owns(self, item):
        for x in self.choiceList:
            if x.button == item:
                return 1
            
        
        return None

    
    def cleanup(self):
        if self.isClean == 0:
            self.isClean = 1
            self.disable()
            self.frame.unmanage()
            self.frame = None
            self.choiceList = []
        
        return None

    
    def getName(self):
        return self.name

    
    def getEventName(self):
        return self.eventName

    
    def setEventName(self, eventName):
        self.eventName = eventName

    
    def __displayChoices(self, choiceList, scale, width, drawOrder, font):
        if width == None:
            width = 0
            text = TextNode()
            text.setFont(font)
            for choice in choiceList:
                w = text.calcWidth(choice) + 0.2
                width = max(width, w)
            
        
        for choice in choiceList:
            button = Button.Button(choice, scale = scale, width = width, drawOrder = drawOrder, font = font, event = 'choose')
            choiceIndex = choiceList.index(choice)
            button.setBehaviorEventParameter(choiceIndex)
            eventName = self.name + '-up'
            button.button.setUpRolloverEvent(eventName)
            eventName = self.name + '-exit'
            button.button.setUpEvent(eventName)
            self.frame.addItem(button)
            self.choiceList.append(button)
        
        self.frame.makeVertical()
        return None

    
    def manage(self):
        self.enable()
        self.frame.manage()
        for x in self.choiceList:
            x.startBehavior()
        
        return None

    
    def unmanage(self):
        self.disable()
        self.frame.unmanage()
        return None

    
    def enable(self):
        self.activate()
        self.accept('up-up', self._PickList__decrementChoice)
        self.accept('down-up', self._PickList__incrementChoice)
        self.accept('enter-up', self._PickList__makeChoice, [
            1,
            None,
            None])
        self.accept(self.name + '-up', self._PickList__updateButtonChoice)
        self.accept(self.name + '-exit', self._PickList__exitChoice)
        self.accept('choose', self._PickList__makeChoice, [
            0])

    
    def disable(self, button = None):
        self.deactivate(button)
        self.ignore('up-up')
        self.ignore('down-up')
        self.ignore('enter-up')
        self.ignore(self.name + '-up')
        self.ignore(self.name + '-exit')
        self.ignore('choose')

    
    def activate(self):
        for choice in self.choiceList:
            choice.getGuiItem().up()
        

    
    def deactivate(self, button = None):
        for choice in self.choiceList:
            if choice.getGuiItem().isActive():
                if not (button == None):
                    if not (self.choiceList.index(choice) == button):
                        choice.getGuiItem().inactive()
                    
                else:
                    choice.getGuiItem().inactive()
            
        

    
    def recompute(self):
        self.frame.recompute()

    
    def setPos(self, x, y):
        self.frame.setPos(x, y)

    
    def __incrementChoice(self):
        choice = self.choice + 1
        if choice > len(self.choiceList) - 1:
            choice = 0
        
        self.choiceList[choice].getGuiItem().enter()

    
    def __decrementChoice(self):
        choice = self.choice - 1
        if choice < 0:
            choice = len(self.choiceList) - 1
        
        self.choiceList[choice].getGuiItem().enter()

    
    def __updateButtonChoice(self, item):
        if self.owns(item):
            if self.choice == -1:
                self.choice = item.getBehaviorEventParameter()
            
            if self.choice != item.getBehaviorEventParameter():
                self.choice = item.getBehaviorEventParameter()
                for choice in self.choiceList:
                    if choice.button != item:
                        choice.getGuiItem().exit()
                    
                
                messenger.send(self.name + '-rollover')
            
        

    
    def __exitChoice(self, item):
        if self.owns(item):
            if self.choice == item.getBehaviorEventParameter():
                self.choice = -1
            
        

    
    def __makeChoice(self, button, item, whichOne):
        if self.choice == -1:
            return None
        elif button:
            self.choiceList[self.choice].getGuiItem().down()
            
            def buttonUp(state):
                state.choice.getGuiItem().up()
                return Task.done

            task = Task.Task(buttonUp)
            task.choice = self.choiceList[self.choice]
            taskMgr.spawnTaskNamed(Task.doLater(0.035, task, 'buttonUp-later'), 'doLater-buttonUp-later')
        elif self.owns(item):
            messenger.send(self.eventName, [
                self.choice])
            self.disable(self.choice)
        


