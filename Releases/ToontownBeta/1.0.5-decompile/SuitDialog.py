# Source Generated with Decompyle++
# File: SuitDialog.pyo (Python 2.0)

import whrandom
import DirectNotifyGlobal
notify = DirectNotifyGlobal.directNotify.newCategory('SuitDialog')

class DialogList:
    
    def __init__(self, list):
        self.list = list
        self.index = 0

    
    def get(self):
        dialog = self.list[self.index]
        self.index = (self.index + 1) % len(self.list)
        return dialog


requestBattle = DialogList([
    "It's my day off.",
    "I believe you're in the wrong office.",
    'Have your people call my people.',
    "You're in no position to meet with me.",
    'My assistant will help you.'])

def getBrushOffIndex(suitName):
    if SuitBrushOffs.has_key(suitName):
        brushoffs = SuitBrushOffs[suitName]
    else:
        brushoffs = SuitBrushOffs[None]
    num = len(brushoffs)
    chunk = 100 / num
    randNum = whrandom.randint(0, 99)
    count = chunk
    for i in range(num):
        if randNum < count:
            return i
        
        count += chunk
    
    notify.error('getBrushOffs() - no brush off found!')


def getBrushOffText(suitName, index):
    if SuitBrushOffs.has_key(suitName):
        brushoffs = SuitBrushOffs[suitName]
    else:
        brushoffs = SuitBrushOffs[None]
    return brushoffs[index]

SuitBrushOffs = {
    'f': [
        "I'm late for a meeting"],
    'p': [
        'Push off'],
    'ym': [
        'Yes Man says NO'],
    None: [
        "It's my day off",
        "I believe you're in the wrong office",
        'Have your people call my people',
        "You're in no position to meet with me",
        'Talk to my assistant'] }
