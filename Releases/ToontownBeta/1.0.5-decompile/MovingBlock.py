# Source Generated with Decompyle++
# File: MovingBlock.pyo (Python 2.0)

from ShowBaseGlobal import *
from ClockDelta import *
from IntervalGlobal import *
import DirectObject

class MovingBlock(DirectObject.DirectObject, NodePath):
    
    def __init__(self, name, model):
        self.name = name
        NodePath.__init__(self, hidden.attachNewNode(self.name))
        self.model = model.copyTo(self)
        self.model.find('**/floor').setName(self.name)
        toonbase.tcr.name2nodePath[self.name] = self
        self.accept('on-floor', self._MovingBlock__handleOnFloor)
        self.accept('off-floor', self._MovingBlock__handleOffFloor)
        return None

    
    def delete(self):
        del toonbase.tcr.name2nodePath[self.name]
        self.model.removeNode()
        del self.model
        self.ignore('on-floor')
        self.ignore('off-floor')
        return None

    
    def __handleOnFloor(self, collEntry):
        if collEntry.getIntoNode().getName() == self.name:
            print 'on floor %s' % self.name
            toonbase.localToon.wrtReparentTo(self)
            toonbase.localToon.d_setParent(self.name)
            base.drive.node().setPos(toonbase.localToon.getPos())
            base.drive.node().setHpr(toonbase.localToon.getHpr())
        
        return None

    
    def __handleOffFloor(self, collEntry):
        if collEntry.getIntoNode().getName() == self.name:
            print 'off floor %s' % self.name
            toonbase.localToon.wrtReparentTo(render)
            toonbase.localToon.d_setParent('render')
            base.drive.node().setPos(toonbase.localToon.getPos())
            base.drive.node().setHpr(toonbase.localToon.getHpr())
        
        return None


