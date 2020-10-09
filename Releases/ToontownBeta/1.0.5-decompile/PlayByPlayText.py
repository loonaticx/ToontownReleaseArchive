# Source Generated with Decompyle++
# File: PlayByPlayText.pyo (Python 2.0)

from DirectObject import *
from ShowBaseGlobal import *
from GuiGlobals import *
from ToontownBattleGlobals import *
from ToontownGlobals import *
from SuitBattleGlobals import *
from IntervalGlobal import *
import DirectNotifyGlobal
import string
import OnscreenText
import BattleBase

class PlayByPlayText(OnscreenText.OnscreenText):
    notify = DirectNotifyGlobal.directNotify.newCategory('PlayByPlayText')
    
    def __init__(self):
        OnscreenText.OnscreenText.__init__(self, mayChange = 1, pos = (0.0, 0.75), scale = 0.2, fg = (1, 0, 0, 1), font = getSignFont())
        return None

    
    def getShowInterval(self, text, duration, suitText = 0):
        if suitText:
            prettyText = self._PlayByPlayText__prettify(text)
        else:
            prettyText = text
        intervalList = [
            FunctionInterval(self.hide),
            WaitInterval(duration * 0.3),
            FunctionInterval(self.setText, extraArgs = [
                prettyText]),
            FunctionInterval(self.show),
            WaitInterval(duration * 0.7),
            FunctionInterval(self.hide)]
        track = Track(intervalList)
        return track

    
    def getToonsDiedInterval(self, textList, duration):
        intervalList = [
            FunctionInterval(self.hide),
            WaitInterval(duration * 0.3)]
        waitGap = (0.6 / len(textList)) * duration
        for text in textList:
            newList = [
                FunctionInterval(self.setText, extraArgs = [
                    text]),
                FunctionInterval(self.show),
                WaitInterval(waitGap),
                FunctionInterval(self.hide)]
            intervalList += newList
        
        intervalList.append(WaitInterval(duration * 0.1))
        track = Track(intervalList)
        return track

    
    def __prettify(self, text):
        retStr = ''
        counter = 0
        for char in text:
            if self._PlayByPlayText__isUpper(char):
                if counter > 0:
                    retStr += ' '
                
            
            retStr += char
            counter += 1
        
        retStr += '!'
        return retStr

    
    def __isUpper(self, char):
        if char >= 'A' and char <= 'Z':
            return 1
        else:
            return 0


