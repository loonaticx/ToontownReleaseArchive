# Source Generated with Decompyle++
# File: DirectScrolledList.pyo (Python 2.0)

from DirectFrame import *
from DirectButton import *
import GuiGlobals
import Task

class DirectScrolledList(DirectFrame):
    
    def __init__(self, parent = guiTop, **kw):
        self.index = 0
        optiondefs = (('items', [], None), ('command', None, None), ('extraArgs', [], None), ('numItemsVisible', 1, self.setNumItemsVisible), ('scrollSpeed', 8, self.setScrollSpeed))
        self.defineoptions(kw, optiondefs, dynamicGroups = ('items',))
        DirectFrame.__init__(self, parent)
        self.incButton = self.createcomponent('incButton', (), 'incButton', DirectButton, (), parent = self)
        self.incButton.bind(B1PRESS, self._DirectScrolledList__incButtonDown)
        self.incButton.bind(B1RELEASE, self._DirectScrolledList__buttonUp)
        self.decButton = self.createcomponent('decButton', (), 'decButton', DirectButton, (), parent = self)
        self.decButton.bind(B1PRESS, self._DirectScrolledList__decButtonDown)
        self.decButton.bind(B1RELEASE, self._DirectScrolledList__buttonUp)
        self.itemFrame = self.createcomponent('itemFrame', (), 'itemFrame', DirectFrame, (), parent = self)
        for item in self['items']:
            item.reparentTo(self.itemFrame)
        
        self.initialiseoptions(DirectScrolledList)
        self.recordMaxHeight()
        self.scrollTo(0)

    
    def recordMaxHeight(self):
        self.maxHeight = 0.0
        for item in self['items']:
            self.maxHeight = max(self.maxHeight, item.getHeight())
        

    
    def setScrollSpeed(self):
        self.scrollSpeed = self['scrollSpeed']
        if self.scrollSpeed <= 0:
            self.scrollSpeed = 1
        

    
    def setNumItemsVisible(self):
        self.numItemsVisible = self['numItemsVisible']

    
    def destroy(self):
        taskMgr.removeTasksNamed(self.taskName('scroll'))
        DirectFrame.destroy(self)

    
    def scrollBy(self, delta):
        return self.scrollTo(self.index + delta)

    
    def scrollTo(self, index):
        self.index = index
        if len(self['items']) <= self['numItemsVisible']:
            self.incButton['state'] = DISABLED
            self.decButton['state'] = DISABLED
            self.index = 0
            ret = 0
        elif self.index <= 0:
            self.index = 0
            self.decButton['state'] = DISABLED
            self.incButton['state'] = NORMAL
            ret = 0
        elif self.index >= len(self['items']) - self['numItemsVisible']:
            self.index = len(self['items']) - self['numItemsVisible']
            self.incButton['state'] = DISABLED
            self.decButton['state'] = NORMAL
            ret = 0
        else:
            self.incButton['state'] = NORMAL
            self.decButton['state'] = NORMAL
            ret = 1
        for item in self['items']:
            item.hide()
        
        upperRange = min(len(self['items']), self['numItemsVisible'])
        for i in range(self.index, self.index + upperRange):
            item = self['items'][i]
            item.show()
            item.setPos(0, 0, -(i - self.index) * self.maxHeight)
        
        return ret

    
    def __scrollByTask(self, task):
        if task.time - task.prevTime < task.delayTime:
            return Task.cont
        else:
            ret = self.scrollBy(task.delta)
            task.prevTime = task.time
            if ret:
                return Task.cont
            else:
                return Task.done

    
    def __incButtonDown(self, event):
        task = Task.Task(self._DirectScrolledList__scrollByTask)
        task.delayTime = 1.0 / self.scrollSpeed
        task.prevTime = 0.0
        task.delta = 1
        self.scrollBy(task.delta)
        taskMgr.spawnTaskNamed(task, self.taskName('scroll'))

    
    def __decButtonDown(self, event):
        task = Task.Task(self._DirectScrolledList__scrollByTask)
        task.delayTime = 1.0 / self.scrollSpeed
        task.prevTime = 0.0
        task.delta = -1
        self.scrollBy(task.delta)
        taskMgr.spawnTaskNamed(task, self.taskName('scroll'))

    
    def __buttonUp(self, event):
        taskMgr.removeTasksNamed(self.taskName('scroll'))

    
    def addItem(self, item):
        self['items'].append(item)
        item.reparentTo(self.itemFrame)
        self.refresh()

    
    def removeItem(self, item):
        if item in self['items']:
            self['items'].remove(item)
            item.reparentTo(hidden)
            self.refresh()
            return 1
        else:
            return 0

    
    def refresh(self):
        self.recordMaxHeight()
        self.scrollTo(self.index)


