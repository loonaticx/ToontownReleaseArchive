# Source Generated with Decompyle++
# File: RingGroup.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
import NodePath
import Ring
import RingTrack
import ClockObject
import ClockDelta

class RingGroup(NodePath.NodePath):
    ringColors = (Vec4(1, 0, 0, 1), Vec4(0, 1, 0, 1), Vec4(0, 0, 1, 1), Vec4(1, 1, 0, 1))
    
    def __init__(self, numRings, ringModel, tracks, xyScale):
        NodePath.NodePath.__init__(self)
        self.assign(hidden.attachNewNode(toonbase.localToon.uniqueName('ring-group')))
        self._RingGroup__numRings = numRings
        self._RingGroup__rings = []
        self._RingGroup__ringModels = []
        for i in range(0, self._RingGroup__numRings):
            ring = Ring.Ring(tracks[i], 2, 0, float(i) * 0.25)
            ring.reparentTo(self)
            ring.setScale(xyScale, xyScale, 1.0)
            ring.setColor(self.ringColors[i])
            model = ringModel.instanceTo(ring)
            self._RingGroup__rings.append(ring)
            self._RingGroup__ringModels.append(model)
        

    
    def __del__(self):
        for model in self._RingGroup__ringModels:
            model.removeNode()
            del model
        
        del self._RingGroup__rings

    
    def getRing(self, index):
        return self._RingGroup__rings[index]

    
    def setT(self, t):
        for ring in self._RingGroup__rings:
            ring.setT(t)
        


