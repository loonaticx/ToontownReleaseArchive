# Source Generated with Decompyle++
# File: Mopath.pyo (Python 2.0)

from PandaObject import *
from DirectGeometry import *
import NodePath

class Mopath(PandaObject):
    nameIndex = 1
    
    def __init__(self, name = None):
        if name == None:
            name = 'mopath%d' % self.nameIndex
            self.nameIndex = self.nameIndex + 1
        
        self.name = name
        self.reset()

    
    def getMaxT(self):
        return self.maxT

    
    def loadFile(self, filename):
        nodePath = loader.loadModel(filename)
        if nodePath:
            self._Mopath__extractCurves(nodePath)
            if self.xyzNurbsCurve != None:
                self.maxT = self.xyzNurbsCurve.getMaxT()
            elif self.hprNurbsCurve != None:
                self.maxT = self.hprNurbsCurve.getMaxT()
            elif self.tNurbsCurve != None:
                self.maxT = self.tNurbsCurve.getMaxT()
            else:
                print 'Mopath: no valid curves in file: %s' % filename
            nodePath.removeNode()
        else:
            print 'Mopath: no data in file: %s' % filename

    
    def reset(self):
        self.maxT = 0.0
        self.loop = 0
        self.xyzNurbsCurve = None
        self.hprNurbsCurve = None
        self.tNurbsCurve = None
        self.node = None

    
    def __extractCurves(self, nodePath):
        node = nodePath.node()
        if isinstance(node, ParametricCurve):
            if node.getCurveType() == PCTXYZ:
                self.xyzNurbsCurve = node
            elif node.getCurveType() == PCTHPR:
                self.hprNurbsCurve = node
            elif node.getCurveType() == PCTNONE:
                if self.xyzNurbsCurve == None:
                    self.xyzNurbsCurve = node
                else:
                    print 'Mopath: got a PCT_NONE curve and an XYZ Curve!'
            elif node.getCurveType() == PCTT:
                self.tNurbsCurve = node
            
        else:
            for child in nodePath.getChildrenAsList():
                self._Mopath__extractCurves(child)
            

    
    def getFinalState(self):
        pos = Point3(0)
        if self.xyzNurbsCurve != None:
            self.xyzNurbsCurve.getPoint(self.maxT, pos)
        
        hpr = Point3(0)
        if self.hprNurbsCurve != None:
            self.hprNurbsCurve.getPoint(self.maxT, hpr)
        
        return (pos, hpr)

    
    def goTo(self, node, time):
        if self.xyzNurbsCurve == None and self.hprNurbsCurve == None:
            print 'Mopath: Mopath has no curves'
            return None
        
        self.playbackTime = CLAMP(time, 0.0, self.maxT)
        if self.xyzNurbsCurve != None:
            pos = Point3(0)
            self.xyzNurbsCurve.getPoint(self.playbackTime, pos)
            node.setPos(pos)
        
        if self.hprNurbsCurve != None:
            hpr = Point3(0)
            self.hprNurbsCurve.getPoint(self.playbackTime, hpr)
            node.setHpr(hpr)
        

    
    def play(self, node, time = 0.0, loop = 0):
        if self.xyzNurbsCurve == None and self.hprNurbsCurve == None:
            print 'Mopath: Mopath has no curves'
            return None
        
        self.node = node
        self.loop = loop
        self.stop()
        t = taskMgr.spawnMethodNamed(self._Mopath__playTask, self.name + '-play')
        t.currentTime = time
        t.lastTime = globalClock.getFrameTime()

    
    def stop(self):
        taskMgr.removeTasksNamed(self.name + '-play')

    
    def __playTask(self, state):
        time = globalClock.getFrameTime()
        dTime = time - state.lastTime
        state.lastTime = time
        if self.loop:
            cTime = (state.currentTime + dTime) % self.maxT
        else:
            cTime = state.currentTime + dTime
        if self.loop == 0 and cTime > self.maxT:
            self.stop()
            messenger.send(self.name + '-done')
            self.node = None
            return Task.done
        
        self.goTo(self.node, cTime)
        state.currentTime = cTime
        return Task.cont


