# Source Generated with Decompyle++
# File: RewardPanel.pyo (Python 2.0)

from DirectObject import *
from ShowBaseGlobal import *
from GuiGlobals import *
from ToontownBattleGlobals import *
from IntervalGlobal import *
from BattleBase import *
import DirectNotifyGlobal
import whrandom
import string
import OnscreenText
import OnscreenPanel

class RewardPanel(OnscreenPanel.OnscreenPanel):
    notify = DirectNotifyGlobal.directNotify.newCategory('RewardPanel')
    
    def __init__(self, name):
        OnscreenPanel.OnscreenPanel.__init__(self, name)
        self.panel = self.makePanel(rect = (-0.8, 0.8, 0.55, 0.95), bg = (1, 1, 1, 0.8))
        self.trackText = self.makeText(pos = (0, 0.1), scale = 0.1, text = '', mayChange = 1)
        self.skillText = self.makeText(pos = (-0.3, -0.15), scale = 0.07, text = 'Skill:0', mayChange = 1)
        self.nextText = self.makeText(pos = (0.3, -0.15), scale = 0.07, text = 'Next:0', mayChange = 1)
        self.gagText = self.makeText(pos = (0, -0.16), scale = 0.07, text = '', mayChange = 1)
        self.congratsLeft = self.makeText(pos = (-0.4, -0.03), scale = 0.07, text = '', mayChange = 1)
        self.congratsRight = self.makeText(pos = (0.4, -0.03), scale = 0.07, text = '', mayChange = 1)
        self.gagList = []
        self.skill = None
        return None

    
    def clearGags(self):
        for gag in self.gagList:
            gag.removeNode()
        
        self.gagList = []
        return None

    
    def incrementSkill(self, increment):
        if self.skill == None:
            self.notify.warning('Skill is set to None. Setting to zero.')
            self.skill = 0
        else:
            self.setSkill(self.skill + increment)

    
    def setSkill(self, skill):
        self.skill = skill
        self.skillText.setText('Skill: %s' % skill)
        return None

    
    def setNext(self, next):
        self.nextText.setText('Next: %s' % next)
        return None

    
    def setTrack(self, toon, track, curSkill):
        self.gagText.setText('')
        self.congratsLeft.setText('')
        self.congratsRight.setText('')
        self.trackText.setText(Tracks[track].capitalize() + 's for ' + toon.getName())
        self.panelGeom.setColor(TrackColors[track][0], TrackColors[track][1], TrackColors[track][2], 0.8)
        self.clearGags()
        self.setSkill(curSkill)
        self.setNext(self.getNextExpValue(track, curSkill))
        return None

    
    def addGag(self, track, level, i, n):
        separation = 0.125
        xOrigin = (n - 1) * -0.5 * separation
        gagOriginal = toonbase.localToon.inventory.buttonLookup(track, level)
        gag = gagOriginal.instanceTo(self)
        gag.setPos(xOrigin + i * separation, 0, 0)
        gag.setScale(0.9)
        gag.setBin('fixed', 10)
        self.gagList.append(gag)
        self.incrementSkill(level + 1)
        return None

    
    def getRandomCongratsPair(self, toon):
        congratsStrings = [
            'Yeah!',
            'Congratulations!',
            'Wow!',
            'Cool!',
            'Go ' + toon.getName() + '!',
            toon.getName() + ' rules!',
            'Awesome!',
            'Toon-tastic!']
        numStrings = len(congratsStrings)
        indexList = range(numStrings)
        index1 = whrandom.choice(indexList)
        indexList.remove(index1)
        index2 = whrandom.choice(indexList)
        string1 = congratsStrings[index1]
        string2 = congratsStrings[index2]
        return (string1, string2)

    
    def newGag(self, toon, track, level):
        self.trackText.setText('New ' + Tracks[track].capitalize() + ' gag for ' + toon.getName() + '!')
        self.skillText.setText('')
        self.nextText.setText('')
        self.congratsLeft.setText('')
        self.congratsRight.setText('')
        self.gagText.setText(AvPropStrings[track][level])
        self.clearGags()
        gagOriginal = toonbase.localToon.inventory.buttonLookup(track, level)
        gag = gagOriginal.instanceTo(self)
        gag.setPos(0, 0, -0.02)
        gag.setScale(1.2)
        gag.setBin('fixed', 10)
        self.gagList.append(gag)
        return None

    
    def getNewGagIntervalList(self, toon, track, level):
        leftCongratsAnticipate = 1.0
        rightCongratsAnticipate = 1.0
        finalDelay = 1.5
        (leftString, rightString) = self.getRandomCongratsPair(toon)
        intervalList = []
        intervalList.append(FunctionInterval(self.newGag, extraArgs = [
            toon,
            track,
            level]))
        intervalList.append(WaitInterval(leftCongratsAnticipate))
        intervalList.append(FunctionInterval(self.congratsLeft.setText, extraArgs = [
            leftString]))
        intervalList.append(WaitInterval(rightCongratsAnticipate))
        intervalList.append(FunctionInterval(self.congratsRight.setText, extraArgs = [
            rightString]))
        intervalList.append(WaitInterval(finalDelay))
        return intervalList

    
    def getNextExpValue(self, track, curSkill):
        retVal = Levels[len(Levels) - 1]
        for amount in Levels:
            if curSkill < amount:
                retVal = amount
                return retVal
            
        
        return retVal

    
    def getTrackIntervalList(self, toon, track, curSkill, levelList):
        intervalList = []
        trackStartDelay = 0.5
        trackEndDelay = 2.5
        gagSwitchDelay = 0.25
        intervalList.append(FunctionInterval(self.setTrack, extraArgs = [
            toon,
            track,
            curSkill]))
        intervalList.append(WaitInterval(trackStartDelay))
        maxGags = 12
        i = 0
        screenClears = 0
        extraSkill = 0
        for level in levelList:
            if i % maxGags == 0 and i > 0:
                intervalList.append(FunctionInterval(self.clearGags))
                screenClears += 1
            
            intervalList.append(FunctionInterval(self.addGag, extraArgs = [
                track,
                level,
                i % maxGags,
                min(len(levelList) - screenClears * maxGags, maxGags)]))
            intervalList.append(WaitInterval(gagSwitchDelay))
            i += 1
            extraSkill += level + 1
        
        intervalList.append(WaitInterval(trackEndDelay))
        nextExpValue = self.getNextExpValue(track, curSkill)
        finalGagFlag = 0
        while curSkill + extraSkill >= nextExpValue and curSkill < nextExpValue and not finalGagFlag:
            intervalList += self.getNewGagIntervalList(toon, track, Levels.index(nextExpValue))
            newNextExpValue = self.getNextExpValue(track, nextExpValue)
            if newNextExpValue == nextExpValue:
                finalGagFlag = 1
            else:
                nextExpValue = newNextExpValue
            continue
            0
        return intervalList

    
    def getExpIntervalList(self, toon, expList, invArray):
        movieIntervalList = []
        for track in range(len(Tracks)):
            levelList = []
            for level in range(len(Levels)):
                count = invArray[track][level]
                for i in range(count):
                    levelList.append(level)
                
            
            if len(levelList) > 0:
                movieIntervalList += self.getTrackIntervalList(toon, track, expList[track], levelList)
            
        
        return movieIntervalList

    
    def getExpTrack(self, toon, expList, invArray):
        trackList = self.getExpIntervalList(toon, expList, invArray)
        if len(trackList) > 0:
            return Track(trackList)
        else:
            return None
        return track

    
    def testMovie(self):
        trackList = self.getExpIntervalList(toonbase.localToon, [
            500,
            10,
            20,
            30,
            40,
            50,
            60], [
            [
                0,
                0,
                0,
                0,
                10,
                0],
            [
                0,
                0,
                0,
                0,
                0,
                0],
            [
                0,
                0,
                0,
                0,
                0,
                0],
            [
                0,
                1,
                0,
                0,
                0,
                0],
            [
                0,
                0,
                0,
                0,
                0,
                0],
            [
                0,
                0,
                0,
                0,
                0,
                0],
            [
                2,
                3,
                0,
                0,
                0,
                0]])
        if len(trackList) > 0:
            trackList.insert(0, FunctionInterval(self.show))
            trackList.append(FunctionInterval(self.hide))
            trackList.append(FunctionInterval(toonbase.localToon.loop, extraArgs = [
                'neutral']))
            trackList.append(FunctionInterval(toonbase.localToon.startUpdateSmartCamera))
            track = Track(trackList)
            track.play()
            toonbase.localToon.loop('victory')
            toonbase.localToon.stopUpdateSmartCamera()
            camera.setPosHpr(0, 8, toonbase.localToon.getHeight(), 179, -10, 0)
        else:
            self.notify.debug('no experience, no movie.')
        return None

    
    def cleanup(self):
        self.clearGags()
        OnscreenPanel.OnscreenPanel.cleanup(self)
        return None


