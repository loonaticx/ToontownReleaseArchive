# Source Generated with Decompyle++
# File: Ring.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
import NodePath
import RingTrack

class Ring(NodePath.NodePath):
    
    def __init__(self, moveTrack, period, startT, tOffset = 0.0):
        NodePath.NodePath.__init__(self)
        self.assign(hidden.attachNewNode(toonbase.localToon.uniqueName('ring')))
        self.setMoveTrack(moveTrack)
        self.setPeriod(period)
        self.setStartT(startT)
        self.setTOffset(tOffset)
        self.setT(0.0)

    
    def setMoveTrack(self, moveTrack):
        self._Ring__moveTrack = moveTrack

    
    def setPeriod(self, period):
        self._Ring__period = float(period)

    
    def setStartT(self, startT):
        self._Ring__startT = float(startT)

    
    def setTOffset(self, tOffset):
        self._Ring__tOffset = float(tOffset)

    
    def setT(self, t):
        pos = RingTrack.Eval(self._Ring__moveTrack, ((t - self._Ring__startT) / self._Ring__period + self._Ring__tOffset) % 1.0)
        self.setPos(pos[0], pos[1], 0)


