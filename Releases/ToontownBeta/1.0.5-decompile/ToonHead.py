# Source Generated with Decompyle++
# File: ToonHead.pyo (Python 2.0)

import Actor
import Task
import FSM
import State
import string
import whrandom
from ShowBaseGlobal import *
HeadDict = {
    'dls': '/models/char/dogMM_Shorts-head-',
    'dss': '/models/char/dogMM_Skirt-head-',
    'dsl': '/models/char/dogSS_Shorts-head-',
    'dll': '/models/char/dogLL_Shorts-head-',
    'c': '/models/char/cat-heads-',
    'h': '/models/char/horse-heads-',
    'm': '/models/char/mouse-heads-',
    'r': '/models/char/rabbit-heads-',
    'f': '/models/char/duck-heads-' }

class ToonHead(Actor.Actor):
    EyesOpen = loader.loadTexture('phase_3/maps/eyes.jpg', 'phase_3/maps/eyes_a.rgb')
    EyesOpen.setMinfilter(Texture.FTLinear)
    EyesOpen.setMagfilter(Texture.FTLinear)
    EyesClosed = loader.loadTexture('phase_3/maps/eyesClosed.jpg', 'phase_3/maps/eyesClosed_a.rgb')
    EyesClosed.setMinfilter(Texture.FTLinear)
    EyesClosed.setMagfilter(Texture.FTLinear)
    
    def __init__(self):
        
        try:
            self.ToonHead_initialized
        except:
            self.ToonHead_initialized = 1
            Actor.Actor.__init__(self)
            self.toonName = 'ToonHead-' + str(self.this)
            self._ToonHead__blinkName = 'blink-' + self.toonName
            self._ToonHead__stareAtName = 'stareAt-' + self.toonName
            self._ToonHead__lookName = 'look-' + self.toonName
            self._ToonHead__eyes = None
            self._ToonHead__lpupil = None
            self._ToonHead__rpupil = None
            self._ToonHead__nextBlinkTime = 0
            self._ToonHead__nextLookTime = 0
            self.eyelids = FSM.FSM('eyelids', [
                State.State('open', self.enterEyelidsOpen, self.exitEyelidsOpen, [
                    'closed']),
                State.State('closed', self.enterEyelidsClosed, self.exitEyelidsClosed, [
                    'open'])], 'open', 'open')
            self.eyelids.enterInitialState()
            self._ToonHead__stareAtNode = NodePath()
            self._ToonHead__stareAtPoint = Point3(0, 0, 0)
            self._ToonHead__stareAtTime = 0

        return None

    
    def delete(self):
        
        try:
            self.ToonHead_deleted
        except:
            self.ToonHead_deleted = 1
            del self.eyelids
            del self._ToonHead__stareAtNode
            del self._ToonHead__stareAtPoint
            if self._ToonHead__eyes:
                del self._ToonHead__eyes
            
            if self._ToonHead__lpupil:
                del self._ToonHead__lpupil
            
            if self._ToonHead__rpupil:
                del self._ToonHead__rpupil
            
            Actor.Actor.delete(self)


    
    def setupHead(self, dna, forGui = 0):
        self.generateToonHead(1, dna, ('1000',), forGui)
        self.generateToonColor(dna)
        if forGui:
            dw = DepthWriteTransition()
            dt = DepthTestTransition(DepthTestProperty.MLess)
            geomArc = self.getGeomNode().arc()
            geomArc.setTransition(dw, 1)
            geomArc.setTransition(dt, 1)
        
        if dna.getAnimal() == 'dog':
            self.loop('neutral')
        

    
    def findSomethingToLookAt(self):
        neutral = whrandom.random() < 0.25
        if neutral:
            x = 0
            y = 0
        else:
            x = whrandom.choice((-0.8, -0.5, 0, 0.5, 0.8))
            y = whrandom.choice((-0.5, 0, 0.5, 0.8))
        self.lerpLookAt(Point3(x, 1.5, y))

    
    def generateToonHead(self, copy, style, lods, forGui = 0):
        headStyle = style.head
        fix = None
        if headStyle == 'dls':
            filePrefix = HeadDict['dls']
            headHeight = 0.75
        elif headStyle == 'dss':
            filePrefix = HeadDict['dss']
            headHeight = 0.5
        elif headStyle == 'dsl':
            filePrefix = HeadDict['dsl']
            headHeight = 0.5
        elif headStyle == 'dll':
            filePrefix = HeadDict['dll']
            headHeight = 0.75
        elif headStyle == 'cls':
            filePrefix = HeadDict['c']
            fix = self._ToonHead__fixHeadLongShort
            headHeight = 0.75
        elif headStyle == 'css':
            filePrefix = HeadDict['c']
            fix = self._ToonHead__fixHeadShortShort
            headHeight = 0.5
        elif headStyle == 'csl':
            filePrefix = HeadDict['c']
            fix = self._ToonHead__fixHeadShortLong
            headHeight = 0.5
        elif headStyle == 'cll':
            filePrefix = HeadDict['c']
            fix = self._ToonHead__fixHeadLongLong
            headHeight = 0.75
        elif headStyle == 'hls':
            filePrefix = HeadDict['h']
            fix = self._ToonHead__fixHeadLongShort
            headHeight = 0.75
        elif headStyle == 'hss':
            filePrefix = HeadDict['h']
            fix = self._ToonHead__fixHeadShortShort
            headHeight = 0.5
        elif headStyle == 'hsl':
            filePrefix = HeadDict['h']
            fix = self._ToonHead__fixHeadShortLong
            headHeight = 0.5
        elif headStyle == 'hll':
            filePrefix = HeadDict['h']
            fix = self._ToonHead__fixHeadLongLong
            headHeight = 0.75
        elif headStyle == 'mls':
            filePrefix = HeadDict['m']
            fix = self._ToonHead__fixHeadLongLong
            headHeight = 0.75
        elif headStyle == 'mss':
            filePrefix = HeadDict['m']
            fix = self._ToonHead__fixHeadShortShort
            headHeight = 0.5
        elif headStyle == 'rls':
            filePrefix = HeadDict['r']
            fix = self._ToonHead__fixHeadLongShort
            headHeight = 0.75
        elif headStyle == 'rss':
            filePrefix = HeadDict['r']
            fix = self._ToonHead__fixHeadShortShort
            headHeight = 0.5
        elif headStyle == 'rsl':
            filePrefix = HeadDict['r']
            fix = self._ToonHead__fixHeadShortLong
            headHeight = 0.5
        elif headStyle == 'rll':
            filePrefix = HeadDict['r']
            fix = self._ToonHead__fixHeadLongLong
            headHeight = 0.75
        elif headStyle == 'fls':
            filePrefix = HeadDict['f']
            fix = self._ToonHead__fixHeadLongShort
            headHeight = 0.75
        elif headStyle == 'fss':
            filePrefix = HeadDict['f']
            fix = self._ToonHead__fixHeadShortShort
            headHeight = 0.5
        elif headStyle == 'fsl':
            filePrefix = HeadDict['f']
            fix = self._ToonHead__fixHeadShortLong
            headHeight = 0.5
        elif headStyle == 'fll':
            filePrefix = HeadDict['f']
            fix = self._ToonHead__fixHeadLongLong
            headHeight = 0.75
        else:
            ToonHead.notify.error('unknown head style: %s' % headStyle)
        animalType = style.getAnimal()
        if len(lods) == 1:
            self.loadModel('phase_3' + filePrefix + lods[0], 'head', 'lodRoot', copy)
            if not copy:
                self.showAllParts('head')
            
            if fix != None:
                fix(style, None, copy)
            
        else:
            for lod in lods:
                self.loadModel('phase_3' + filePrefix + lod, 'head', lod, copy)
                if not copy:
                    self.showAllParts('head', lod)
                
                if fix != None:
                    fix(style, lod, copy)
                
            
        self._ToonHead__fixEyes(style, forGui)
        return headHeight

    
    def generateToonColor(self, style):
        parts = self.findAllMatches('**/head*')
        for partNum in range(0, parts.getNumPaths()):
            parts.getPath(partNum).setColor(style.getHeadColor())
        
        animalType = style.getAnimal()
        if animalType == 'cat' and animalType == 'rabbit' or animalType == 'mouse':
            parts = self.findAllMatches('**/ear?-*')
            for partNum in range(0, parts.getNumPaths()):
                parts.getPath(partNum).setColor(style.getHeadColor())
            
        

    
    def __fixEyes(self, style, forGui = 0):
        mode = -3
        if forGui:
            mode = -2
        
        if self.hasLOD():
            for lodName in self.getLODNames():
                self.drawInFront('eyes*', 'head-front*', mode, lodName = lodName)
                self.drawInFront('joint-pupil?', 'eyes*', mode, lodName = lodName)
            
        else:
            self.drawInFront('eyes*', 'head-front*', mode)
            self.drawInFront('joint-pupil?', 'eyes*', mode)
        allEyes = self.findAllMatches('**/eyes*')
        for i in range(0, allEyes.getNumPaths()):
            allEyes.getPath(i).setColorOff()
        
        if self.hasLOD():
            self._ToonHead__eyes = self.find('**/' + self.getLODNames()[0] + '/**/eyes*')
        else:
            self._ToonHead__eyes = self.find('**/eyes*')
        if not self._ToonHead__eyes.isEmpty():
            self._ToonHead__lpupil = None
            self._ToonHead__rpupil = None
            lp = self._ToonHead__eyes.find('**/joint-pupilL')
            rp = self._ToonHead__eyes.find('**/joint-pupilR')
            if lp.isEmpty() or rp.isEmpty():
                print 'Unable to locate pupils.'
            else:
                leye = self._ToonHead__eyes.attachNewNode('leye')
                reye = self._ToonHead__eyes.attachNewNode('reye')
                lmat = Mat4(0.802174, 0.59709, 0, 0, -0.586191, 0.787531, 0.190197, 0, 0.113565, -0.152571, 0.981746, 0, -0.233634, 0.418062, 0.0196875, 1)
                leye.setMat(lmat)
                rmat = Mat4(0.786788, -0.617224, 0, 0, 0.602836, 0.768447, 0.214658, 0, -0.132492, -0.16889, 0.976689, 0, 0.233634, 0.418062, 0.0196875, 1)
                reye.setMat(rmat)
                self._ToonHead__lpupil = leye.attachNewNode('lpupil')
                self._ToonHead__rpupil = reye.attachNewNode('rpupil')
                lpt = self._ToonHead__eyes.attachNewNode('')
                rpt = self._ToonHead__eyes.attachNewNode('')
                lpt.wrtReparentTo(self._ToonHead__lpupil)
                rpt.wrtReparentTo(self._ToonHead__rpupil)
                lp.reparentTo(lpt)
                rp.reparentTo(rpt)
                animalType = style.getAnimal()
                if animalType != 'dog':
                    leye.flattenStrong()
                    reye.flattenStrong()
                
        

    
    def __setPupilDirection(self, x, y):
        LeftA = Point3(0.06, 0.0, 0.14)
        LeftB = Point3(-0.13, 0.0, 0.1)
        LeftC = Point3(-0.05, 0.0, 0.0)
        LeftD = Point3(0.06, 0.0, 0.0)
        RightA = Point3(0.13, 0.0, 0.1)
        RightB = Point3(-0.06, 0.0, 0.14)
        RightC = Point3(-0.06, 0.0, 0.0)
        RightD = Point3(0.05, 0.0, 0.0)
        LeftAD = Point3(LeftA[0] - LeftA[2] * (LeftD[0] - LeftA[0]) / (LeftD[2] - LeftA[2]), 0.0, 0.0)
        LeftBC = Point3(LeftB[0] - LeftB[2] * (LeftC[0] - LeftB[0]) / (LeftC[2] - LeftB[2]), 0.0, 0.0)
        RightAD = Point3(RightA[0] - RightA[2] * (RightD[0] - RightA[0]) / (RightD[2] - RightA[2]), 0.0, 0.0)
        RightBC = Point3(RightB[0] - RightB[2] * (RightC[0] - RightB[0]) / (RightC[2] - RightB[2]), 0.0, 0.0)
        if y < 0.0:
            y2 = -y
            left1 = LeftAD + (LeftD - LeftAD) * y2
            left2 = LeftBC + (LeftC - LeftBC) * y2
            right1 = RightAD + (RightD - RightAD) * y2
            right2 = RightBC + (RightC - RightBC) * y2
        else:
            y2 = y
            left1 = LeftAD + (LeftA - LeftAD) * y2
            left2 = LeftBC + (LeftB - LeftBC) * y2
            right1 = RightAD + (RightA - RightAD) * y2
            right2 = RightBC + (RightB - RightBC) * y2
        left0 = Point3(0.0, 0.0, left1[2] - left1[0] * (left2[2] - left1[2]) / (left2[0] - left1[0]))
        right0 = Point3(0.0, 0.0, right1[2] - right1[0] * (right2[2] - right1[2]) / (right2[0] - right1[0]))
        if x < 0.0:
            x2 = -x
            left = left0 + (left2 - left0) * x2
            right = right0 + (right2 - right0) * x2
        else:
            x2 = x
            left = left0 + (left1 - left0) * x2
            right = right0 + (right1 - right0) * x2
        self._ToonHead__lpupil.setPos(left)
        self._ToonHead__rpupil.setPos(right)

    
    def __lookPupilsAt(self, node, point):
        if node != None:
            mat = node.getMat(self._ToonHead__eyes)
            point = mat.xformPoint(point)
        
        distance = 1.0
        z = max(0.1, point[1])
        x = distance * point[0] / z
        y = distance * point[2] / z
        x = min(max(x, -1), 1)
        y = min(max(y, -1), 1)
        self._ToonHead__setPupilDirection(x, y)

    
    def __lookHeadAt(self, node, point, frac = 1):
        reachedTarget = 1
        lodName = self.getLODNames()[0]
        head = self.getPart('head', lodName)
        if node != None:
            headParent = NodePath(head)
            headParent.shorten(1)
            mat = node.getMat(headParent)
            point = mat.xformPoint(point)
        
        rot = Mat3()
        lookAt(rot, Vec3(point), Vec3(0, 0, 1), CSDefault)
        scale = VBase3()
        hpr = VBase3()
        if decomposeMatrix(rot, scale, hpr, 0.0, CSDefault):
            hpr = VBase3(min(max(hpr[0], -60), 60), min(max(hpr[1], -20), 30), 0)
            if frac != 1:
                currentHpr = head.getHpr()
                if abs(hpr[0] - currentHpr[0]) < 1:
                    pass
                reachedTarget = abs(hpr[1] - currentHpr[1]) < 1
                hpr = currentHpr + (hpr - currentHpr) * frac
            
            for lodName in self.getLODNames():
                head = self.getPart('head', lodName)
                head.setHpr(hpr)
            
        
        return reachedTarget

    
    def __fixHeadLongLong(self, style, lodName = None, copy = 1):
        if lodName == None:
            searchRoot = self
        else:
            searchRoot = self.find('**/' + str(lodName))
        otherParts = searchRoot.findAllMatches('**/*short')
        for partNum in range(0, otherParts.getNumPaths()):
            if copy:
                otherParts.getPath(partNum).removeNode()
            else:
                otherParts.getPath(partNum).hide()
        

    
    def __fixHeadLongShort(self, style, lodName = None, copy = 1):
        animalType = style.getAnimal()
        headStyle = style.head
        if lodName == None:
            searchRoot = self
        else:
            searchRoot = self.find('**/' + str(lodName))
        if animalType != 'fowl' and animalType != 'horse':
            if animalType == 'rabbit':
                if copy:
                    searchRoot.find('**/ears-long').removeNode()
                else:
                    searchRoot.find('**/ears-long').hide()
            elif copy:
                searchRoot.find('**/ears-short').removeNode()
            else:
                searchRoot.find('**/ears-short').hide()
        
        if animalType != 'rabbit':
            if copy:
                searchRoot.find('**/eyes-short').removeNode()
            else:
                searchRoot.find('**/eyes-short').hide()
        
        if copy:
            self.find('**/head-short').removeNode()
            self.find('**/head-front-short').removeNode()
        else:
            self.find('**/head-short').hide()
            self.find('**/head-front-short').hide()
        if animalType != 'rabbit':
            if copy:
                searchRoot.find('**/muzzle-long').removeNode()
            else:
                searchRoot.find('**/muzzle-long').hide()
        elif copy:
            searchRoot.find('**/muzzle-short').removeNode()
        else:
            searchRoot.find('**/muzzle-short').hide()

    
    def __fixHeadShortLong(self, style, lodName = None, copy = 1):
        animalType = style.getAnimal()
        headStyle = style.head
        if lodName == None:
            searchRoot = self
        else:
            searchRoot = self.find('**/' + str(lodName))
        if animalType != 'fowl' and animalType != 'horse':
            if animalType == 'rabbit':
                if copy:
                    searchRoot.find('**/ears-short').removeNode()
                else:
                    searchRoot.find('**/ears-short').hide()
            elif copy:
                searchRoot.find('**/ears-long').removeNode()
            else:
                searchRoot.find('**/ears-long').hide()
        
        if animalType != 'rabbit':
            if copy:
                searchRoot.find('**/eyes-long').removeNode()
            else:
                searchRoot.find('**/eyes-long').hide()
        
        if copy:
            searchRoot.find('**/head-long').removeNode()
            searchRoot.find('**/head-front-long').removeNode()
        else:
            searchRoot.find('**/head-long').hide()
            searchRoot.find('**/head-front-long').hide()
        if animalType != 'rabbit':
            if copy:
                searchRoot.find('**/muzzle-short').removeNode()
            else:
                searchRoot.find('**/muzzle-short').hide()
        elif copy:
            searchRoot.find('**/muzzle-long').removeNode()
        else:
            searchRoot.find('**/muzzle-long').hide()

    
    def __fixHeadShortShort(self, style, lodName = None, copy = 1):
        if lodName == None:
            searchRoot = self
        else:
            searchRoot = self.find('**/' + str(lodName))
        otherParts = searchRoot.findAllMatches('**/*long')
        for partNum in range(0, otherParts.getNumPaths()):
            if copy:
                otherParts.getPath(partNum).removeNode()
            else:
                otherParts.getPath(partNum).hide()
        

    
    def __blinkEyes(self, task):
        now = globalClock.getFrameTime()
        if now < self._ToonHead__nextBlinkTime:
            return Task.cont
        
        if self.eyelids.getCurrentState().getName() == 'closed' or self._ToonHead__nextBlinkTime == 0:
            self.eyelids.request('open')
            self._ToonHead__nextBlinkTime = now + whrandom.random() * 4.0 + 1.0
        else:
            self.eyelids.request('closed')
            self._ToonHead__nextBlinkTime = now + 0.1
        return Task.cont

    
    def startBlink(self):
        taskMgr.removeTasksNamed(self._ToonHead__blinkName)
        self._ToonHead__nextBlinkTime = 0
        task = Task.Task(self._ToonHead__blinkEyes)
        taskMgr.spawnTaskNamed(task, self._ToonHead__blinkName)

    
    def stopBlink(self):
        taskMgr.removeTasksNamed(self._ToonHead__blinkName)
        self.eyelids.request('open')

    
    def closeEyes(self):
        self.eyelids.request('closed')

    
    def openEyes(self):
        self.eyelids.request('open')

    
    def __stareAt(self, task):
        frac = 0.2
        reachedTarget = self._ToonHead__lookHeadAt(self._ToonHead__stareAtNode, self._ToonHead__stareAtPoint, frac)
        self._ToonHead__lookPupilsAt(self._ToonHead__stareAtNode, self._ToonHead__stareAtPoint)
        if reachedTarget and self._ToonHead__stareAtNode == None:
            return Task.done
        else:
            return Task.cont

    
    def startStareAt(self, node, point):
        taskMgr.removeTasksNamed(self._ToonHead__stareAtName)
        self._ToonHead__stareAtNode = node
        self._ToonHead__stareAtPoint = point
        self._ToonHead__stareAtTime = globalClock.getFrameTime()
        task = Task.Task(self._ToonHead__stareAt)
        taskMgr.spawnTaskNamed(task, self._ToonHead__stareAtName)

    
    def lerpLookAt(self, point, time = 1.5):
        taskMgr.removeTasksNamed(self._ToonHead__stareAtName)
        lodName = self.getLODNames()[0]
        head = self.getPart('head', lodName)
        startHpr = head.getHpr()
        startLpupil = self._ToonHead__lpupil.getPos()
        startRpupil = self._ToonHead__rpupil.getPos()
        self._ToonHead__lookHeadAt(None, point)
        self._ToonHead__lookPupilsAt(None, point)
        endHpr = head.getHpr()
        endLpupil = self._ToonHead__lpupil.getPos()
        endRpupil = self._ToonHead__rpupil.getPos()
        head.setHpr(startHpr)
        self._ToonHead__lpupil.setPos(startLpupil)
        self._ToonHead__rpupil.setPos(startRpupil)
        head.lerpHpr(endHpr, time, blendType = 'easeInOut', task = self._ToonHead__stareAtName)
        self._ToonHead__lpupil.lerpPos(endLpupil, time * 0.5, blendType = 'easeInOut', task = self._ToonHead__stareAtName)
        self._ToonHead__rpupil.lerpPos(endRpupil, time * 0.5, blendType = 'easeInOut', task = self._ToonHead__stareAtName)

    
    def stopStareAt(self):
        self.lerpLookAt(Vec3.forward())

    
    def stopStareAtNow(self):
        taskMgr.removeTasksNamed(self._ToonHead__stareAtName)
        self._ToonHead__setPupilDirection(0, 0)
        for lodName in self.getLODNames():
            head = self.getPart('head', lodName)
            head.setHpr(0, 0, 0)
        

    
    def __lookAround(self, task):
        now = globalClock.getFrameTime()
        if now < self._ToonHead__nextLookTime:
            return Task.cont
        
        if whrandom.random() < 0.25:
            self.stopStareAt()
        else:
            self.findSomethingToLookAt()
        self._ToonHead__nextLookTime = now + whrandom.random() * 8.0 + 4.0
        return Task.cont

    
    def startLookAround(self):
        taskMgr.removeTasksNamed(self._ToonHead__lookName)
        now = globalClock.getFrameTime()
        self._ToonHead__nextLookTime = now + whrandom.random() * 8.0 + 4.0
        task = Task.Task(self._ToonHead__lookAround)
        taskMgr.spawnTaskNamed(task, self._ToonHead__lookName)

    
    def stopLookAround(self):
        taskMgr.removeTasksNamed(self._ToonHead__lookName)
        self.stopStareAt()

    
    def stopLookAroundNow(self):
        taskMgr.removeTasksNamed(self._ToonHead__lookName)
        self.stopStareAtNow()

    
    def enterEyelidsOpen(self):
        pass

    
    def exitEyelidsOpen(self):
        pass

    
    def enterEyelidsClosed(self):
        if not self._ToonHead__eyes.isEmpty() and ToonHead.EyesClosed:
            self._ToonHead__eyes.setTexture(ToonHead.EyesClosed)
            if self._ToonHead__lpupil:
                self._ToonHead__lpupil.hide()
                self._ToonHead__rpupil.hide()
            
        

    
    def exitEyelidsClosed(self):
        if not self._ToonHead__eyes.isEmpty() and ToonHead.EyesOpen:
            self._ToonHead__eyes.setTexture(ToonHead.EyesOpen)
            if self._ToonHead__lpupil:
                self._ToonHead__lpupil.show()
                self._ToonHead__rpupil.show()
            
        


