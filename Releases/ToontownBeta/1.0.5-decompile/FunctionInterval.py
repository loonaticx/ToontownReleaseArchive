# Source Generated with Decompyle++
# File: FunctionInterval.pyo (Python 2.0)

from PandaModules import *
from Interval import *
from MessengerGlobal import *

class FunctionInterval(Interval):
    functionIntervalNum = 1
    notify = directNotify.newCategory('FunctionInterval')
    
    def __init__(self, function, name = None, openEnded = 1, extraArgs = []):
        self.function = function
        if name == None:
            name = 'FunctionInterval-%d' % FunctionInterval.functionIntervalNum
            FunctionInterval.functionIntervalNum += 1
        
        self.extraArgs = extraArgs
        Interval.__init__(self, name, duration = 0.0, openEnded = openEnded)

    
    def updateFunc(self, t, event = IVAL_NONE):
        apply(self.function, self.extraArgs)
        self.notify.debug('updateFunc() - %s: executing Function' % self.name)



class EventInterval(FunctionInterval):
    
    def __init__(self, event, sentArgs = []):
        
        def sendFunc(event = event, sentArgs = sentArgs):
            messenger.send(event, sentArgs)

        FunctionInterval.__init__(self, sendFunc, name = event, openEnded = 0)



class AcceptInterval(FunctionInterval):
    
    def __init__(self, dirObj, event, function, name = None):
        
        def acceptFunc(dirObj = dirObj, event = event, function = function):
            dirObj.accept(event, function)

        if name == None:
            name = 'Accept-' + event
        
        FunctionInterval.__init__(self, acceptFunc, name = name, openEnded = 0)



class IgnoreInterval(FunctionInterval):
    
    def __init__(self, dirObj, event, name = None):
        
        def ignoreFunc(dirObj = dirObj, event = event):
            dirObj.ignore(event)

        if name == None:
            name = 'Ignore-' + event
        
        FunctionInterval.__init__(self, ignoreFunc, name = name, openEnded = 0)



class ParentInterval(FunctionInterval):
    parentIntervalNum = 1
    
    def __init__(self, nodePath, parent, name = None):
        
        def reparentFunc(nodePath = nodePath, parent = parent):
            nodePath.reparentTo(parent)

        if name == None:
            name = 'ParentInterval-%d' % ParentInterval.parentIntervalNum
            ParentInterval.parentIntervalNum += 1
        
        FunctionInterval.__init__(self, reparentFunc, name = name)



class WrtParentInterval(FunctionInterval):
    wrtParentIntervalNum = 1
    
    def __init__(self, nodePath, parent, name = None):
        
        def wrtReparentFunc(nodePath = nodePath, parent = parent):
            nodePath.wrtReparentTo(parent)

        if name == None:
            name = 'WrtParentInterval-%d' % WrtParentInterval.wrtParentIntervalNum
            WrtParentInterval.wrtParentIntervalNum += 1
        
        FunctionInterval.__init__(self, wrtReparentFunc, name = name)



class PosInterval(FunctionInterval):
    posIntervalNum = 1
    
    def __init__(self, nodePath, pos, duration = 0.0, name = None, other = None):
        
        def posFunc(np = nodePath, pos = pos, other = other):
            if other:
                np.setPos(other, pos)
            else:
                np.setPos(pos)

        if name == None:
            name = 'PosInterval-%d' % PosInterval.posIntervalNum
            PosInterval.posIntervalNum += 1
        
        FunctionInterval.__init__(self, posFunc, name = name)



class HprInterval(FunctionInterval):
    hprIntervalNum = 1
    
    def __init__(self, nodePath, hpr, duration = 0.0, name = None, other = None):
        
        def hprFunc(np = nodePath, hpr = hpr, other = other):
            if other:
                np.setHpr(other, hpr)
            else:
                np.setHpr(hpr)

        if name == None:
            name = 'HprInterval-%d' % HprInterval.hprIntervalNum
            HprInterval.hprIntervalNum += 1
        
        FunctionInterval.__init__(self, hprFunc, name = name)



class ScaleInterval(FunctionInterval):
    scaleIntervalNum = 1
    
    def __init__(self, nodePath, scale, duration = 0.0, name = None, other = None):
        
        def scaleFunc(np = nodePath, scale = scale, other = other):
            if other:
                np.setScale(other, scale)
            else:
                np.setScale(scale)

        if name == None:
            name = 'ScaleInterval-%d' % ScaleInterval.scaleIntervalNum
            ScaleInterval.scaleIntervalNum += 1
        
        FunctionInterval.__init__(self, scaleFunc, name = name)



class PosHprInterval(FunctionInterval):
    posHprIntervalNum = 1
    
    def __init__(self, nodePath, pos, hpr, duration = 0.0, name = None, other = None):
        
        def posHprFunc(np = nodePath, pos = pos, hpr = hpr, other = other):
            if other:
                np.setPosHpr(other, pos, hpr)
            else:
                np.setPosHpr(pos, hpr)

        if name == None:
            name = 'PosHprInterval-%d' % PosHprInterval.posHprIntervalNum
            PosHprInterval.posHprIntervalNum += 1
        
        FunctionInterval.__init__(self, posHprFunc, name = name)



class PosHprScaleInterval(FunctionInterval):
    posHprScaleIntervalNum = 1
    
    def __init__(self, nodePath, pos, hpr, scale, duration = 0.0, name = None, other = None):
        
        def posHprScaleFunc(np = nodePath, pos = pos, hpr = hpr, scale = scale, other = other):
            if other:
                np.setPosHprScale(other, pos, hpr, scale)
            else:
                np.setPosHprScale(pos, hpr, scale)

        if name == None:
            name = 'PosHprScale-%d' % PosHprScaleInterval.posHprScaleIntervalNum
            PosHprScaleInterval.posHprScaleIntervalNum += 1
        
        FunctionInterval.__init__(self, posHprScaleFunc, name = name)

