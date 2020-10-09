# Source Generated with Decompyle++
# File: Trajectory.pyo (Python 2.0)

import DirectNotifyGlobal
from PandaModules import *
from math import *

class Trajectory:
    notify = DirectNotifyGlobal.directNotify.newCategory('Trajectory')
    notify.setDebug(1)
    __gravity = 32.0
    __radius = 2.0
    
    def __init__(self, startTime, startPos, startVel, gravMult = 1.0):
        self._Trajectory__setStartTime(startTime)
        self._Trajectory__setStartPos(startPos)
        self._Trajectory__setStartVel(startVel)
        self._Trajectory__setGravityMult(gravMult)

    
    def __setStartTime(self, t):
        self._Trajectory__startTime = t

    
    def __setStartPos(self, sp):
        self._Trajectory__startPos = sp

    
    def __setStartVel(self, sv):
        self._Trajectory__startVel = sv

    
    def __setGravityMult(self, mult):
        self._Trajectory__zAcc = mult * -(Trajectory._Trajectory__gravity)

    
    def __calcTimeOfHighestPoint(self):
        t = -self._Trajectory__startVel[2] / self._Trajectory__zAcc
        if t < 0:
            t = 0
        
        return t + self._Trajectory__startTime

    
    def __calcTimeOfImpactOnPlane(self, height = 0):
        a = self._Trajectory__zAcc * 0.5
        b = self._Trajectory__startVel[2]
        c = self._Trajectory__startPos[2] - height
        D = b * b - 4.0 * a * c
        if D < 0:
            return -1.0
        elif D == 0:
            t = -b / 2.0 * a
        else:
            t = (-b - sqrt(D)) / 2.0 * a
        if t < 0:
            return -1.0
        
        return t + self._Trajectory__startTime

    
    def __calcZ(self, t):
        tt = t - self._Trajectory__startTime
        return self._Trajectory__startPos[2] + self._Trajectory__startVel[2] * tt + 0.5 * self._Trajectory__zAcc * tt * tt

    
    def __reachesHeight(self, height):
        if self._Trajectory__calcZ(self._Trajectory__calcTimeOfHighestPoint()) < height:
            return 0
        
        return 1

    
    def getPos(self, t):
        tt = t - self._Trajectory__startTime
        return Point3(self._Trajectory__startPos[0] + self._Trajectory__startVel[0] * tt, self._Trajectory__startPos[1] + self._Trajectory__startVel[1] * tt, self._Trajectory__calcZ(t))

    
    def getVel(self, t):
        tt = t - self._Trajectory__startTime
        return Vec3(self._Trajectory__startVel[0], self._Trajectory__startVel[1], self._Trajectory__startVel[2] + self._Trajectory__zAcc * tt)

    
    def getStartTime(self):
        return self._Trajectory__startTime

    
    def checkCollisionWithGround(self, height = 0):
        return self._Trajectory__calcTimeOfImpactOnPlane(height)

    
    def checkCollisionWithDisc(self, discCenter, discRadius):
        if self._Trajectory__reachesHeight(discCenter[2]) == 0:
            return -1.0
        
        t_atDiscHeight = self._Trajectory__calcTimeOfImpactOnPlane(discCenter[2])
        if t_atDiscHeight < 0:
            return -1.0
        
        p_atDiscHeight = self.getPos(t_atDiscHeight)
        offset_x = p_atDiscHeight[0] - discCenter[0]
        offset_y = p_atDiscHeight[1] - discCenter[1]
        offset_from_center_SQUARED = offset_x * offset_x + offset_y * offset_y
        max_offset = discRadius
        max_offset_SQUARED = max_offset * max_offset
        if offset_from_center_SQUARED < max_offset_SQUARED:
            return t_atDiscHeight
        else:
            return -1.0

    
    def calcEnterAndLeaveCylinderXY(self, cylBottomCenter, cylRadius):
        v = Vec2(cylBottomCenter[0], cylBottomCenter[1])
        o = Vec2(self._Trajectory__startPos[0], self._Trajectory__startPos[1])
        d = Vec2(self._Trajectory__startVel[0], self._Trajectory__startVel[1])
        d.normalize()
        b = d.dot(o - v)
        c = (o - v).dot(o - v) - cylRadius * cylRadius
        bsmc = b * b - c
        if bsmc <= 0.0:
            return (-1.0, -1.0)
        
        sqrt_bsmc = sqrt(bsmc)
        t1 = -b - sqrt_bsmc
        t2 = -b + sqrt_bsmc
        if t1 > t2:
            self.notify.debug('calcEnterAndLeaveCylinderXY: t1 > t2??')
        
        mag = Vec2(self._Trajectory__startVel[0], self._Trajectory__startVel[1]).length()
        t1 = t1 / mag
        t2 = t2 / mag
        return (t1 + self._Trajectory__startTime, t2 + self._Trajectory__startTime)

    
    def checkCollisionWithCylinderSides(self, cylBottomCenter, cylRadius, cylHeight):
        if self._Trajectory__reachesHeight(cylBottomCenter[2]) == 0:
            return -1.0
        
        (t1, t2) = self.calcEnterAndLeaveCylinderXY(cylBottomCenter, cylRadius)
        p1 = self.getPos(t1)
        p2 = self.getPos(t2)
        cylTopHeight = cylBottomCenter[2] + cylHeight
        if p1[2] > cylTopHeight and p2[2] > cylTopHeight:
            return -1.0
        
        if p1[2] < cylTopHeight and p1[2] > cylBottomCenter[2]:
            if t1 > self._Trajectory__startTime:
                return t1
            
        
        return -1.0

    
    def checkCollisionWithProjectile(self, projectile):
        return -1.0


