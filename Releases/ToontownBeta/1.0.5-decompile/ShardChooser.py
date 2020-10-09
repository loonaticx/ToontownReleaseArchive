# Source Generated with Decompyle++
# File: ShardChooser.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
from TaskManagerGlobal import *
import PandaObject
import OnscreenText
import PotentialShard
import PickList
import StateData

class ShardChooser(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, shardList, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.shardList = shardList
        self.choice = None

    
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
            self.accept('shard-picker', self._ShardChooser__makeChoice)
        

    
    def exit(self):
        if self.isLoaded == 0:
            return None
        
        self.ignore('shard-picker')
        self.title.reparentTo(hidden)
        self.prompt.reparentTo(hidden)
        self.bg.reparentTo(hidden)
        self.pickList.unmanage()

    
    def load(self):
        if self.isLoaded == 1:
            return None
        
        self.title = OnscreenText.OnscreenText('ToonTown District List', parent = hidden, style = OnscreenText.ScreenTitle, pos = (0.0, 0.8))
        promptText = 'Please choose a district to enter'
        self.prompt = OnscreenText.OnscreenText(promptText, parent = hidden, style = OnscreenText.ScreenPrompt, pos = (0.0, 0.5))
        self.list = []
        for shard in self.shardList:
            self.list.append(shard.name + ' (' + str(shard.population) + ' players)')
        
        self.pickList = PickList.PickList('shard-picker', self.list)
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

    
    def getChoice(self):
        return self.choice

    
    def __makeChoice(self, choice):
        self.choice = choice
        
        def sendDoneTask(self):
            messenger.send(self.doneEvent)
            return Task.done

        sdt = Task.Task(sendDoneTask)
        sdt.doneEvent = self.doneEvent
        base.transitions.fadeOutTask(sdt)


