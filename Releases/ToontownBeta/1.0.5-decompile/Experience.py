# Source Generated with Decompyle++
# File: Experience.pyo (Python 2.0)

from PandaModules import *
from ToontownBattleGlobals import *
import DirectNotifyGlobal

class Experience:
    notify = DirectNotifyGlobal.directNotify.newCategory('Experience')
    
    def __init__(self, expStr = None):
        if expStr == None:
            self.experience = []
            for track in range(0, len(Tracks)):
                self.experience.append(StartingLevel)
            
        else:
            self.experience = self.makeFromNetString(expStr)

    
    def __str__(self):
        return str(self.experience)

    
    def makeNetString(self):
        dataList = self.experience
        datagram = Datagram()
        for track in range(0, len(Tracks)):
            datagram.addUint16(dataList[track])
        
        dgi = DatagramIterator(datagram)
        return dgi.getRemainingBytes()

    
    def makeFromNetString(self, netString):
        dataList = []
        dg = Datagram(netString)
        dgi = DatagramIterator(dg)
        for track in range(0, len(Tracks)):
            dataList.append(dgi.getUint16())
        
        return dataList

    
    def addExp(self, track, amount = 1):
        if type(track) == type(''):
            track = Tracks.index(track)
        
        self.notify.debug('adding %d exp to track %d' % (amount, track))
        if self.experience[track] + amount <= MaxSkill:
            self.experience[track] += amount
        else:
            self.experience[track] = MaxSkill

    
    def getMaxHp(self):
        hp = BaseHp
        for track in range(0, len(Tracks)):
            lvl = self.getExpLevel(track) + 1
            if lvl > 0:
                for thisLvl in range(1, lvl):
                    hp += thisLvl
                
            
        
        return hp

    
    def maxOutExp(self):
        for track in range(0, len(Tracks)):
            self.experience[track] = MaxSkill
        

    
    def zeroOutExp(self):
        for track in range(0, len(Tracks)):
            self.experience[track] = StartingLevel
        

    
    def setAllExp(self, num):
        for track in range(0, len(Tracks)):
            self.experience[track] = num
        

    
    def getExp(self, track):
        if type(track) == type(''):
            track = Tracks.index(track)
        
        return self.experience[track]

    
    def getExpLevel(self, track):
        if type(track) == type(''):
            track = Tracks.index(track)
        
        level = 0
        for amount in Levels:
            if self.experience[track] >= amount:
                level = Levels.index(amount)
            
        
        return level

    
    def getTotalExp(self):
        total = 0
        for level in self.experience:
            total += level
        
        return total

    
    def getNextExpValue(self, track, curSkill = None):
        if curSkill == None:
            curSkill = self.experience[track]
        
        retVal = Levels[len(Levels) - 1]
        for amount in Levels:
            if curSkill < amount:
                retVal = amount
                return retVal
            
        
        return retVal

    
    def getNewGagIndexList(self, track, extraSkill):
        retList = []
        curSkill = self.experience[track]
        nextExpValue = self.getNextExpValue(track, curSkill)
        finalGagFlag = 0
        while curSkill + extraSkill >= nextExpValue and curSkill < nextExpValue and not finalGagFlag:
            retList.append(Levels.index(nextExpValue))
            newNextExpValue = self.getNextExpValue(track, nextExpValue)
            if newNextExpValue == nextExpValue:
                finalGagFlag = 1
            else:
                nextExpValue = newNextExpValue
        return retList


