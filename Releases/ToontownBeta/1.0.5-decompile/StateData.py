# Source Generated with Decompyle++
# File: StateData.pyo (Python 2.0)

from DirectObject import *
import DirectNotifyGlobal

class StateData(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('StateData')
    
    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        self.doneStatus = None
        self.isLoaded = 0
        self.isEntered = 0
        return None

    
    def cleanup(self):
        self.unload()
        return None

    
    def enter(self):
        if self.isEntered == 1:
            return None
        
        self.isEntered = 1
        if self.isLoaded == 0:
            self.load()
        
        self.notify.debug('enter()')
        return None

    
    def exit(self):
        if self.isEntered == 0:
            return None
        
        self.isEntered = 0
        self.notify.debug('exit()')
        return None

    
    def load(self):
        if self.isLoaded == 1:
            return None
        
        self.isLoaded = 1
        self.notify.debug('load()')
        return None

    
    def unload(self):
        if self.isLoaded == 0:
            return None
        
        self.isLoaded = 0
        self.exit()
        self.notify.debug('unload()')
        return None

    
    def getDoneStatus(self):
        return self.doneStatus


