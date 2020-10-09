# Source Generated with Decompyle++
# File: LerpInterval.pyo (Python 2.0)

from Interval import *
from PandaModules import *
import LerpBlendHelpers

class LerpInterval(Interval):
    notify = directNotify.newCategory('LerpInterval')
    
    def __init__(self, name, duration, functorFunc, blendType = 'noBlend'):
        self.lerp = None
        self.functorFunc = functorFunc
        self.blendType = self.getBlend(blendType)
        Interval.__init__(self, name, duration)

    
    def updateFunc(self, t, event = IVAL_NONE):
        if event == IVAL_INIT:
            self.lerp = Lerp(self.functorFunc(), self.duration, self.blendType)
        
        if not (self.lerp):
            self.lerp = Lerp(self.functorFunc(), self.duration, self.blendType)
        
        self.lerp.setT(t)
        self.notify.debug('updateFunc() - %s: t = %f' % (self.name, t))

    
    def getBlend(self, blendType):
        if blendType == 'easeIn':
            return LerpBlendHelpers.easeIn
        elif blendType == 'easeOut':
            return LerpBlendHelpers.easeOut
        elif blendType == 'easeInOut':
            return LerpBlendHelpers.easeInOut
        elif blendType == 'noBlend':
            return LerpBlendHelpers.noBlend
        else:
            raise Exception('Error: LerpInterval.__getBlend: Unknown blend type')



class LerpPosInterval(LerpInterval):
    lerpPosNum = 1
    
    def __init__(self, node, duration, pos, startPos = None, other = None, blendType = 'noBlend', name = None):
        
        def functorFunc(node = node, pos = pos, startPos = startPos, other = other):
            if callable(pos):
                pos = pos()
            
            if other != None:
                if startPos == None:
                    startPos = node.getPos(other)
                
                functor = PosLerpFunctor(node, startPos, pos, other)
            elif startPos == None:
                startPos = node.getPos()
            
            functor = PosLerpFunctor(node, startPos, pos)
            return functor

        if name == None:
            name = 'LerpPosInterval-%d' % LerpPosInterval.lerpPosNum
            LerpPosInterval.lerpPosNum += 1
        
        LerpInterval.__init__(self, name, duration, functorFunc, blendType)



class LerpHprInterval(LerpInterval):
    lerpHprNum = 1
    
    def __init__(self, node, duration, hpr, startHpr = None, other = None, blendType = 'noBlend', name = None):
        
        def functorFunc(node = node, hpr = hpr, startHpr = startHpr, other = other):
            if callable(hpr):
                hpr = hpr()
            
            if other != None:
                if startHpr == None:
                    startHpr = node.getHpr(other)
                
                functor = HprLerpFunctor(node, startHpr, hpr, other)
            elif startHpr == None:
                startHpr = node.getHpr()
            
            functor = HprLerpFunctor(node, startHpr, hpr)
            return functor

        if name == None:
            name = 'LerpHprInterval-%d' % LerpHprInterval.lerpHprNum
            LerpHprInterval.lerpHprNum += 1
        
        LerpInterval.__init__(self, name, duration, functorFunc, blendType)



class LerpScaleInterval(LerpInterval):
    lerpScaleNum = 1
    
    def __init__(self, node, duration, scale, startScale = None, other = None, blendType = 'noBlend', name = None):
        
        def functorFunc(node = node, scale = scale, startScale = startScale, other = other):
            if callable(scale):
                scale = scale()
            
            if other != None:
                if startScale == None:
                    startScale = node.getScale(other)
                
                functor = ScaleLerpFunctor(node, startScale, scale, other)
            elif startScale == None:
                startScale = node.getScale()
            
            functor = ScaleLerpFunctor(node, startScale, scale)
            return functor

        if name == None:
            name = 'LerpScaleInterval-%d' % LerpScaleInterval.lerpScaleNum
            LerpScaleInterval.lerpScaleNum += 1
        
        LerpInterval.__init__(self, name, duration, functorFunc, blendType)



class LerpPosHprInterval(LerpInterval):
    lerpPosHprNum = 1
    
    def __init__(self, node, duration, pos, hpr, startPos = None, startHpr = None, other = None, blendType = 'noBlend', name = None):
        
        def functorFunc(node = node, pos = pos, hpr = hpr, startPos = startPos, startHpr = startHpr, other = other):
            if callable(pos):
                pos = pos()
            
            if callable(hpr):
                hpr = hpr()
            
            if other != None:
                if startPos == None:
                    startPos = node.getPos(other)
                
                if startHpr == None:
                    startHpr = node.getHpr(other)
                
                functor = PosHprLerpFunctor(node, startPos, pos, startHpr, hpr, other)
            elif startPos == None:
                startPos = node.getPos()
            
            if startHpr == None:
                startHpr = node.getHpr()
            
            functor = PosHprLerpFunctor(node, startPos, pos, startHpr, hpr)
            return functor

        if name == None:
            name = 'LerpPosHpr-%d' % LerpPosHprInterval.lerpPosHprNum
            LerpPosHprInterval.lerpPosHprNum += 1
        
        LerpInterval.__init__(self, name, duration, functorFunc, blendType)



class LerpPosHprScaleInterval(LerpInterval):
    lerpPosHprScaleNum = 1
    
    def __init__(self, node, duration, pos, hpr, scale, startPos = None, startHpr = None, startScale = None, other = None, blendType = 'noBlend', name = None):
        
        def functorFunc(node = node, pos = pos, hpr = hpr, scale = scale, startPos = startPos, startHpr = startHpr, startScale = startScale, other = other):
            if callable(pos):
                pos = pos()
            
            if callable(hpr):
                hpr = hpr()
            
            if callable(scale):
                scale = scale()
            
            if other != None:
                if startPos == None:
                    startPos = node.getPos(other)
                
                if startHpr == None:
                    startHpr = node.getHpr(other)
                
                if startScale == None:
                    startScale = node.getScale(other)
                
                functor = PosHprScaleLerpFunctor(node, startPos, pos, startHpr, hpr, startScale, scale, other)
            elif startPos == None:
                startPos = node.getPos()
            
            if startHpr == None:
                startHpr = node.getHpr()
            
            if startScale == None:
                startScale = node.getScale()
            
            functor = PosHprScaleLerpFunctor(node, startPos, pos, startHpr, hpr, startScale, scale)
            return functor

        if name == None:
            name = 'LerpPosHprScale-%d' % LerpPosHprScaleInterval.lerpPosHprScaleNum
            LerpPosHprScaleInterval.lerpPosHprScaleNum += 1
        
        LerpInterval.__init__(self, name, duration, functorFunc, blendType)



class LerpFunctionInterval(Interval):
    lerpFunctionIntervalNum = 1
    notify = directNotify.newCategory('LerpFunctionInterval')
    
    def __init__(self, function, fromData = 0, toData = 1, duration = 0.0, blendType = 'noBlend', extraArgs = [], name = None):
        self.function = function
        self.fromData = fromData
        self.toData = toData
        self.blendType = self.getBlend(blendType)
        self.extraArgs = extraArgs
        if name == None:
            name = 'LerpFunctionInterval-%d' % LerpFunctionInterval.lerpFunctionIntervalNum
            LerpFunctionInterval.lerpFunctionIntervalNum += 1
        
        Interval.__init__(self, name, duration)

    
    def updateFunc(self, t, event = IVAL_NONE):
        if t >= self.duration:
            apply(self.function, [
                self.toData] + self.extraArgs)
        elif self.duration == 0.0:
            apply(self.function, [
                self.toData] + self.extraArgs)
        else:
            bt = self.blendType(t / self.duration)
            data = self.fromData * (1 - bt) + self.toData * bt
            apply(self.function, [
                data] + self.extraArgs)
        self.notify.debug('updateFunc() - %s: t = %f' % (self.name, t))

    
    def getBlend(self, blendType):
        if blendType == 'easeIn':
            return LerpBlendHelpers.easeIn
        elif blendType == 'easeOut':
            return LerpBlendHelpers.easeOut
        elif blendType == 'easeInOut':
            return LerpBlendHelpers.easeInOut
        elif blendType == 'noBlend':
            return LerpBlendHelpers.noBlend
        else:
            raise Exception('Error: LerpInterval.__getBlend: Unknown blend type')


