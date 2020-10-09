# Source Generated with Decompyle++
# File: InventoryBase.pyo (Python 2.0)

from PandaModules import *
from ToontownBattleGlobals import *
import DirectObject
import DirectNotifyGlobal

class InventoryBase(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('InventoryBase')
    
    def __init__(self, toon, invStr = None):
        self.toon = toon
        if invStr == None:
            self.inventory = []
            for track in range(0, len(Tracks)):
                level = []
                for thisLevel in range(0, len(Levels)):
                    level.append(0)
                
                self.inventory.append(level)
            
        else:
            self.inventory = self.makeFromNetString(invStr)
        self.calcTotalProps()

    
    def __str__(self):
        retStr = 'maxProps: %d, totalProps: %d\n' % (self.getMaxTotalProps(), self.totalProps)
        for track in range(0, len(Tracks)):
            retStr += Tracks[track] + ' = ' + str(self.inventory[track]) + '\n'
        
        return retStr

    
    def updateInvString(self, invString):
        inventory = self.makeFromNetString(invString)
        self.updateInventory(inventory)
        return None

    
    def updateInventory(self, inv):
        self.inventory = inv
        self.calcTotalProps()

    
    def makeNetString(self):
        dataList = self.inventory
        datagram = Datagram()
        for track in range(0, len(Tracks)):
            for level in range(0, len(Levels)):
                datagram.addUint8(dataList[track][level])
            
        
        dgi = DatagramIterator(datagram)
        return dgi.getRemainingBytes()

    
    def makeFromNetString(self, netString):
        dataList = []
        dg = Datagram(netString)
        dgi = DatagramIterator(dg)
        for track in range(0, len(Tracks)):
            subList = []
            for level in range(0, len(Levels)):
                subList.append(dgi.getUint8())
            
            dataList.append(subList)
        
        return dataList

    
    def addItem(self, track, level):
        return self.addItems(track, level, 1)

    
    def addItems(self, track, level, amount):
        if type(track) == type(''):
            track = Tracks.index(track)
        
        max = self.getMax(track, level)
        if self.toon.experience.getExpLevel(track) >= level:
            if self.numItem(track, level) <= max - amount:
                if self.totalProps + amount <= self.getMaxTotalProps():
                    self.inventory[track][level] += amount
                    self.totalProps += amount
                    return self.inventory[track][level]
                else:
                    return -2
            else:
                return -1
        else:
            return 0

    
    def addItemWithList(self, track, levelList):
        for level in levelList:
            self.addItem(track, level)
        

    
    def numItem(self, track, level):
        if type(track) == type(''):
            track = Tracks.index(track)
        
        return self.inventory[track][level]

    
    def useItem(self, track, level):
        if type(track) == type(''):
            track = Tracks.index(track)
        
        if self.numItem(track, level):
            self.inventory[track][level] -= 1
            self.calcTotalProps()
        

    
    def getMax(self, track, level):
        if type(track) == type(''):
            track = Tracks.index(track)
        
        maxList = CarryLimits[track]
        return maxList[self.toon.experience.getExpLevel(track)][level]

    
    def getTrackAndLevel(self, propName):
        for track in range(0, len(Tracks)):
            if AvProps[track].count(propName):
                return (tracks, AvProps[track].index(propName))
            
        
        return (-1, -1)

    
    def calcTotalProps(self):
        self.totalProps = 0
        for track in range(0, len(Tracks)):
            for level in range(0, len(Levels)):
                self.totalProps += self.numItem(track, level)
            
        
        return None

    
    def countPropsInList(self, invList):
        totalProps = 0
        for track in range(len(Tracks)):
            for level in range(len(Levels)):
                totalProps += invList[track][level]
            
        
        return totalProps

    
    def getMaxTotalProps(self):
        maxTotalProps = 0
        for level in range(0, len(MaxProps)):
            if self.toon.maxHp >= MaxProps[level][0]:
                maxTotalProps = MaxProps[level][1]
            
        
        return maxTotalProps

    
    def setToMin(self, newInventory):
        for track in range(len(Tracks)):
            for level in range(len(Levels)):
                self.inventory[track][level] = min(self.inventory[track][level], newInventory[track][level])
            
        
        self.calcTotalProps()
        return None

    
    def validateItemsBasedOnExp(self, newInventory):
        for track in range(len(Tracks)):
            for level in range(len(Levels)):
                if newInventory[track][level] > self.getMax(track, level):
                    return 0
                
            
        
        return 1

    
    def validatePurchase(self, newInventory, newItemMax):
        newItemTotal = self.countPropsInList(newInventory)
        oldItemTotal = self.totalProps
        if newItemTotal > oldItemTotal + newItemMax:
            self.notify.warning('Somebody overspent! Rejecting purchase.')
            return 0
        
        if self.validateItemsBasedOnExp(newInventory):
            self.updateInventory(newInventory)
            return 1
        else:
            self.notify.warning('Somebody is trying to buy forbidden items! ' + 'Rejecting purchase.')
            return 0

    
    def maxOutInv(self):
        while self.totalProps < self.getMaxTotalProps():
            totalPropsBefore = self.totalProps
            for track in range(len(Tracks)):
                for level in range(len(Levels)):
                    self.addItem(track, level)
                
            
            if self.totalProps == totalPropsBefore:
                self.notify.error('This should never happen')
            
            continue
            0
        self.calcTotalProps()
        return None

    
    def zeroInv(self):
        for track in range(len(Tracks)):
            for level in range(len(Levels)):
                self.inventory[track][level] = 0
            
        
        self.calcTotalProps()
        return None


