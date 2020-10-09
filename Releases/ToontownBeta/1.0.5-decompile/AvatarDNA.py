# Source Generated with Decompyle++
# File: AvatarDNA.pyo (Python 2.0)

import whrandom
from PandaModules import *
from DirectNotifyGlobal import *
notify = directNotify.newCategory('AvatarDNA')
classTypes = [
    't',
    's',
    'c']
toonType = classTypes[0]
suitType = classTypes[1]
charType = classTypes[2]
toonHeadTypes = [
    'dls',
    'dss',
    'dsl',
    'dll',
    'cls',
    'css',
    'csl',
    'cll',
    'hls',
    'hss',
    'hsl',
    'hll',
    'mls',
    'mss',
    'rls',
    'rss',
    'rsl',
    'rll',
    'fls',
    'fss',
    'fsl',
    'fll']
toonTorsoTypes = [
    'ss',
    'ms',
    'ls',
    'sd',
    'md',
    'ld']
toonLegTypes = [
    's',
    'm',
    'l']
numToonShirtTypes = 69
numToonShortTypes = 52
numToonSkirtTypes = 33
charTypes = [
    'mk',
    'mn',
    'g',
    'd']
suitHeadTypes = [
    'f',
    'p',
    'ym',
    'mm',
    'ds',
    'hh',
    'cr',
    'tbc',
    'bf',
    'b',
    'dt',
    'ac',
    'bs',
    'sd',
    'le',
    'bw',
    'sc',
    'pp',
    'tw',
    'bc',
    'nc',
    'mb',
    'ls',
    'rb',
    'cc',
    'tm',
    'nd',
    'gh',
    'ms',
    'tf',
    'm',
    'mh']
suitATypes = [
    'ym',
    'hh',
    'tbc',
    'dt',
    'bs',
    'le',
    'bw',
    'pp',
    'nc',
    'rb',
    'nd',
    'tf',
    'm',
    'mh']
suitBTypes = [
    'p',
    'ds',
    'b',
    'ac',
    'sd',
    'bc',
    'ls',
    'tm',
    'ms']
suitCTypes = [
    'f',
    'mm',
    'cr',
    'bf',
    'sc',
    'tw',
    'mb',
    'cc',
    'gh']
suitDepts = [
    'c',
    'l',
    'm',
    's']
corpPolyColor = VBase4(0.95, 0.75, 0.75, 1.0)
legalPolyColor = VBase4(0.75, 0.75, 0.95, 1.0)
moneyPolyColor = VBase4(0.65, 0.95, 0.85, 1.0)
salesPolyColor = VBase4(0.95, 0.75, 0.95, 1.0)
suitsPerLevel = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1]
suitsPerDept = 8

def getSuitBodyType(name):
    if name in suitATypes:
        return 'a'
    elif name in suitBTypes:
        return 'b'
    elif name in suitCTypes:
        return 'c'
    else:
        print 'Unknown body type for suit name: ', name


def getSuitDept(name):
    index = suitHeadTypes.index(name)
    if index < 8:
        return suitDepts[0]
    elif index < 16:
        return suitDepts[1]
    elif index < 24:
        return suitDepts[2]
    elif index < 32:
        return suitDepts[3]
    else:
        print 'Unknown dept for suit name: ', name

allColorsList = [
    VBase4(1.0, 1.0, 1.0, 1.0),
    VBase4(0.96875, 0.691406, 0.699219, 1.0),
    VBase4(0.933594, 0.265625, 0.28125, 1.0),
    VBase4(0.863281, 0.40625, 0.417969, 1.0),
    VBase4(0.710938, 0.234375, 0.4375, 1.0),
    VBase4(0.570312, 0.449219, 0.164062, 1.0),
    VBase4(0.640625, 0.355469, 0.269531, 1.0),
    VBase4(0.996094, 0.695312, 0.511719, 1.0),
    VBase4(0.832031, 0.5, 0.296875, 1.0),
    VBase4(0.992188, 0.480469, 0.167969, 1.0),
    VBase4(0.996094, 0.898438, 0.320312, 1.0),
    VBase4(0.996094, 0.957031, 0.597656, 1.0),
    VBase4(0.855469, 0.933594, 0.492188, 1.0),
    VBase4(0.550781, 0.824219, 0.324219, 1.0),
    VBase4(0.242188, 0.742188, 0.515625, 1.0),
    VBase4(0.304688, 0.96875, 0.402344, 1.0),
    VBase4(0.433594, 0.90625, 0.835938, 1.0),
    VBase4(0.347656, 0.820312, 0.953125, 1.0),
    VBase4(0.191406, 0.5625, 0.773438, 1.0),
    VBase4(0.558594, 0.589844, 0.875, 1.0),
    VBase4(0.285156, 0.328125, 0.726562, 1.0),
    VBase4(0.460938, 0.378906, 0.824219, 1.0),
    VBase4(0.546875, 0.28125, 0.75, 1.0),
    VBase4(0.726562, 0.472656, 0.859375, 1.0),
    VBase4(0.898438, 0.617188, 0.90625, 1.0)]
defaultColorList = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24]

class AvatarDNA:
    
    def __init__(self, str = None, type = None, dna = None, r = None, b = None, g = None):
        if str != None:
            self.makeFromNetString(str)
        elif type != None:
            if type == 't':
                if dna == None:
                    self.newToonRandom(r, g, b)
                else:
                    self.newToon(dna, r, g, b)
            elif type == 's':
                self.newSuit()
            elif type == 'c':
                self.newChar(dna)
            
        else:
            self.type = 'u'

    
    def makeToonFromProperties(self, head, torso, legs, armColor, gloveColor, legColor, headColor, topTexture, sleeveTexture, bottomTexture):
        self.type = 't'
        self.head = head
        self.torso = torso
        self.legs = legs
        self.armColor = armColor
        self.gloveColor = gloveColor
        self.legColor = legColor
        self.headColor = headColor
        self.topTex = topTexture
        self.sleeveTex = sleeveTexture
        self.botTex = bottomTexture
        return None

    
    def __str__(self):
        if self.type == 't':
            string = 'type = toon\n'
            string = string + 'head = %s, torso = %s, legs = %s\n' % (self.head, self.torso, self.legs)
            string = string + 'arm color = %d\n' % self.armColor
            string = string + 'glove color = %d\n' % self.gloveColor
            string = string + 'leg color = %d\n' % self.legColor
            string = string + 'head color = %d\n' % self.headColor
            string = string + 'top texture = %d\n' % self.topTex
            string = string + 'sleeve texture = %d\n' % self.topTex
            if self.torso[1] == 's':
                string = string + 'bottom texture = %d\n' % self.botTex
            else:
                string = string + 'bottom texture = %d\n' % self.botTex
            return string
        elif self.type == 's':
            return 'type = %s\nbody = %s, dept = %s, name = %s' % ('suit', self.body, self.dept, self.name)
        elif self.type == 'c':
            return 'type = char, name = %s' % self.name
        else:
            return 'type undefined'

    
    def makeNetString(self):
        dg = Datagram()
        dg.addFixedString(self.type, 1)
        if self.type == 't':
            headIndex = toonHeadTypes.index(self.head)
            torsoIndex = toonTorsoTypes.index(self.torso)
            legsIndex = toonLegTypes.index(self.legs)
            dg.addUint8(headIndex)
            dg.addUint8(torsoIndex)
            dg.addUint8(legsIndex)
            dg.addUint8(self.topTex)
            dg.addUint8(self.botTex)
            dg.addUint8(self.armColor)
            dg.addUint8(self.gloveColor)
            dg.addUint8(self.legColor)
            dg.addUint8(self.headColor)
        elif self.type == 's':
            dg.addFixedString(self.name, 3)
            dg.addFixedString(self.dept, 1)
        elif self.type == 'c':
            dg.addFixedString(self.name, 2)
        elif self.type == 'u':
            notify.error('undefined avatar')
        else:
            notify.error('unknown avatar type: ', self.type)
        return dg.getMessage()

    
    def printNetString(self):
        string = self.makeNetString()
        dg = Datagram(string)
        dg.dumpHex(ostream)

    
    def makeFromNetString(self, string):
        dg = Datagram(string)
        dgi = DatagramIterator(dg)
        self.type = dgi.getFixedString(1)
        if self.type == 't':
            headIndex = dgi.getUint8()
            torsoIndex = dgi.getUint8()
            legsIndex = dgi.getUint8()
            self.head = toonHeadTypes[headIndex]
            self.torso = toonTorsoTypes[torsoIndex]
            self.legs = toonLegTypes[legsIndex]
            self.topTex = dgi.getUint8()
            self.botTex = dgi.getUint8()
            self.armColor = dgi.getUint8()
            self.gloveColor = dgi.getUint8()
            self.legColor = dgi.getUint8()
            self.headColor = dgi.getUint8()
        elif self.type == 's':
            self.name = dgi.getFixedString(3)
            self.dept = dgi.getFixedString(1)
            self.body = getSuitBodyType(self.name)
        elif self.type == 'c':
            self.name = sgi.getFixedString(2)
        else:
            notify.error('unknown avatar type: ', self.type)
        return None

    
    def defaultColor(self):
        return 0

    
    def __defaultColors(self):
        color = self.defaultColor()
        self.armColor = color
        self.gloveColor = color
        self.legColor = color
        self.headColor = color

    
    def __defaultChar(self):
        self.type = 'c'
        self.name = charTypes[0]

    
    def __defaultSuit(self):
        self.type = 's'
        self.name = 'ds'
        self.dept = getSuitDept(self.name)
        self.body = getSuitBodyType(self.name)

    
    def newChar(self, name = None):
        if name == None:
            self._AvatarDNA__defaultChar()
        else:
            self.type = 'c'
            if name in charTypes:
                self.name = name
            else:
                notify.error('unknown avatar type: ', name)

    
    def newSuit(self, name = None):
        if name == None:
            self._AvatarDNA__defaultSuit()
        else:
            self.type = 's'
            self.name = name
            self.dept = getSuitDept(self.name)
            self.body = getSuitBodyType(self.name)

    
    def newSuitRandom(self, level = None, dept = None):
        self.type = 's'
        if level == None:
            level = whrandom.choice(range(1, len(suitsPerLevel)))
        elif level < 0 or level > len(suitsPerLevel):
            notify.error('Invalid suit level: %d' % level)
        
        if dept == None:
            dept = whrandom.choice(suitDepts)
        elif not (dept in suitDepts):
            notify.error('Invalid suit dept: ', dept)
        
        self.dept = dept
        index = suitDepts.index(dept)
        base = index * suitsPerDept
        offset = 0
        if level > 1:
            for i in range(1, level):
                offset = offset + suitsPerLevel[i - 1]
            
        
        bottom = base + offset
        top = bottom + suitsPerLevel[level - 1]
        self.name = suitHeadTypes[whrandom.choice(range(bottom, top))]
        self.body = getSuitBodyType(self.name)

    
    def newToon(self, dna, color = None):
        if len(dna) == 3:
            self.type = 't'
            self.head = dna[0]
            self.torso = dna[1]
            self.legs = dna[2]
            self.topTex = 0
            self.botTex = 0
            if color == None:
                color = self.defaultColor()
            
            self.armColor = color
            self.legColor = color
            self.headColor = color
            self.gloveColor = self.defaultColor()
        else:
            notify.error("tuple must be in format ('%s', '%s', '%s')")

    
    def newToonRandom(self):
        self.type = 't'
        self.legs = whrandom.choice(toonLegTypes)
        self.torso = whrandom.choice(toonTorsoTypes)
        self.head = whrandom.choice(toonHeadTypes)
        self.topTex = whrandom.randint(0, numToonShirtTypes - 1)
        if self.torso[1] == 's':
            self.botTex = whrandom.randint(0, numToonShortTypes - 1)
        else:
            self.botTex = whrandom.randint(0, numToonSkirtTypes - 1)
        self.armColor = whrandom.choice(defaultColorList)
        self.legColor = whrandom.choice(defaultColorList)
        self.headColor = whrandom.choice(defaultColorList)
        self.gloveColor = self.defaultColor()

    
    def getType(self):
        if self.type == 't':
            type = self.getAnimal()
        elif self.type == 's':
            type = 'suit'
        elif self.type == 'c':
            type = self.getCharName()
        else:
            notify.error('Invalid DNA type: ', self.type)
        return type

    
    def getAnimal(self):
        if self.head[0] == 'd':
            return 'dog'
        elif self.head[0] == 'c':
            return 'cat'
        elif self.head[0] == 'm':
            return 'mouse'
        elif self.head[0] == 'h':
            return 'horse'
        elif self.head[0] == 'r':
            return 'rabbit'
        elif self.head[0] == 'f':
            return 'fowl'
        else:
            notify.error('unknown headStyle: ', self.head[0])

    
    def getHeadSize(self):
        if self.head[1] == 'l':
            return 'long'
        elif self.head[1] == 's':
            return 'short'
        else:
            notify.error('unknown head size: ', self.head[1])

    
    def getMuzzleSize(self):
        if self.head[2] == 'l':
            return 'long'
        elif self.head[2] == 's':
            return 'short'
        else:
            notify.error('unknown muzzle size: ', self.head[2])

    
    def getTorsoSize(self):
        if self.torso[0] == 'l':
            return 'long'
        elif self.torso[0] == 'm':
            return 'medium'
        elif self.torso[0] == 's':
            return 'short'
        else:
            notify.error('unknown torso size: ', self.torso[0])

    
    def getLegSize(self):
        if self.legs == 'l':
            return 'long'
        elif self.legs == 'm':
            return 'medium'
        elif self.legs == 's':
            return 'short'
        else:
            notify.error('unknown leg size: ', self.legs)

    
    def getClothes(self):
        if self.torso[1] == 's':
            return 'shorts'
        elif self.torso[1] == 'd':
            return 'dress'
        else:
            notify.error('unknown clothing type: ', self.torso[1])

    
    def getArmColor(self):
        return allColorsList[self.armColor]

    
    def getLegColor(self):
        return allColorsList[self.legColor]

    
    def getHeadColor(self):
        return allColorsList[self.headColor]

    
    def getGloveColor(self):
        return allColorsList[self.gloveColor]

    
    def getCharName(self):
        if self.name == 'mk':
            return 'mickey'
        elif self.name == 'mn':
            return 'minnie'
        elif self.name == 'g':
            return 'goofy'
        elif self.name == 'd':
            return 'donald'
        else:
            notify.error('unknown char type: ', self.name)


