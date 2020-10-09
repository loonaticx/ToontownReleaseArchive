# Source Generated with Decompyle++
# File: HoodChooser.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
from TaskManagerGlobal import *
import PandaObject
import OnscreenText
import PickList
import StateData

class HoodChooser(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, hoodList, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.hoodList = hoodList

    
    def cleanup(self):
        self.unload()

    
    def enter(self):
        if self.isLoaded == 0:
            self.load()
        
        base.disableMouse()
        if self.title:
            self.title.reparentTo(aspect2d)
        
        if self.prompt:
            self.prompt.reparentTo(aspect2d)
        
        self.bg.reparentTo(render2d)
        self.bg.setPos(0.0, 0.0, 0.0)
        self.bg.setScale(1.01)
        self.bg.setBin('background', 0)
        if self.pickList:
            self.pickList.manage()
            self.accept('hood-picker', self._HoodChooser__makeChoice)
        

    
    def exit(self):
        if self.isLoaded == 0:
            return None
        
        self.ignore('hood-picker')
        self.title.reparentTo(hidden)
        self.prompt.reparentTo(hidden)
        self.bg.reparentTo(hidden)
        self.pickList.unmanage()

    
    def load(self):
        if self.isLoaded == 1:
            return None
        
        self.title = OnscreenText.OnscreenText("ToonTown 'Map'", parent = hidden, style = OnscreenText.ScreenTitle, pos = (0.0, 0.8))
        promptText = 'Please choose a neighborhood to enter'
        self.prompt = OnscreenText.OnscreenText(promptText, parent = hidden, style = OnscreenText.ScreenPrompt, pos = (0.0, 0.5))
        self.list = []
        for hood in self.hoodList:
            self.list.append(toonbase.tcr.hoodMgr.getFullnameFromId(hood))
        
        self.pickList = PickList.PickList('hood-picker', self.list)
        self.pickList.unmanage()
        self.bg = loader.loadModel('phase_3/models/gui/hotel-room-background')
        self.isLoaded = 1

    
    def unload(self):
        if self.isLoaded == 0:
            return None
        
        self.exit()
        self.bg.removeNode()
        self.pickList.cleanup()
        self.pickList = None
        self.isLoaded = 0

    
    def __makeChoice(self, choice):
        self.choice = choice
        
        def sendDoneTask(self):
            messenger.send(self.doneEvent)
            return Task.done

        sdt = Task.Task(sendDoneTask)
        sdt.doneEvent = self.doneEvent
        base.transitions.fadeOutTask(sdt)

    
    def getChoice(self):
        return self.choice


