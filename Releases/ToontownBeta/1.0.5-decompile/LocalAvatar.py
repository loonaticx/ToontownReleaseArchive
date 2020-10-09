# Source Generated with Decompyle++
# File: LocalAvatar.pyo (Python 2.0)

from ShowBaseGlobal import *
import Avatar
import DistributedAvatar
import Task
import PositionExaminer
import ToontownGlobals
import ChatManager
import math
import string
import whrandom
import DirectNotifyGlobal
from DirectGui import *
import ToontownGlobals
from PythonUtil import *
import GuiGlobals
RUN_FORWARD_MODE = 1
WALK_FORWARD_MODE = 2
NEUTRAL_MODE = 3
SPIN_IN_PLACE_MODE = 4
WALK_BACKWARD_MODE = 5

class LocalAvatar(DistributedAvatar.DistributedAvatar):
    notify = DirectNotifyGlobal.directNotify.newCategory('LocalAvatar')
    wantMouse = base.config.GetBool('want-mouse', 0)
    __enableMarkerPlacement = base.config.GetBool('place-markers', 0)
    
    def __init__(self, cr):
        
        try:
            self.LocalAvatar_initialized
        except:
            self.LocalAvatar_initialized = 1
            DistributedAvatar.DistributedAvatar.__init__(self, cr)
            self.initializeCollisions()
            self.initializeSmartCamera()
            self.animMultiplier = 1.0
            self.soundRun = base.loadSfx('phase_4/audio/sfx/AV_footstep_runloop.wav')
            self.soundWalk = base.loadSfx('phase_4/audio/sfx/AV_footstep_walkloop.wav')
            self.soundWalkCollision = base.loadSfx('phase_4/audio/sfx/AV_collision.mp3')
            self.positionExaminer = PositionExaminer.PositionExaminer()
            friendsGui = loader.loadModel('phase_4/models/gui/friendslist_gui')
            friendsButtonNormal = friendsGui.find('**/FriendsBox_Closed')
            friendsButtonPressed = friendsGui.find('**/FriendsBox_Rollover')
            friendsButtonRollover = friendsGui.find('**/FriendsBox_Rollover')
            self.bFriendsList = DirectButton(image = (friendsButtonNormal, friendsButtonPressed, friendsButtonRollover), relief = None, pos = (1.192, 0, 0.875), scale = 0.8, text = ('', 'Friends', 'Friends'), text_scale = 0.09, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -0.18), text_font = ToontownGlobals.getInterfaceFont(), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self.sendFriendsListEvent)
            self.bFriendsList.hide()
            self.friendsListButtonActive = 0
            self.friendsListButtonObscured = 0
            self.chatMgr = ChatManager.ChatManager()
            self.isShift = 0
            self.isPageUp = 0
            self.isPageDown = 0

        return None

    
    def sendFriendsListEvent(self):
        messenger.send('friendsList')

    
    def delete(self):
        
        try:
            self.LocalAvatar_deleted
        except:
            self.LocalAvatar_deleted = 1
            self.deleteCollisions()
            self.positionExaminer.delete()
            del self.positionExaminer
            self.bFriendsList.destroy()
            del self.bFriendsList
            self.chatMgr.delete()
            del self.chatMgr
            base.unloadSfx(self.soundRun)
            del self.soundRun
            base.unloadSfx(self.soundWalk)
            del self.soundWalk
            base.unloadSfx(self.soundWalkCollision)
            del self.soundWalkCollision
            self.ignoreAll()
            DistributedAvatar.DistributedAvatar.delete(self)

        return None

    
    def initializeCollisions(self):
        self.cSphere = CollisionSphere(0.0, 0.0, 0.0, 1.5)
        self.cSphereNode = CollisionNode('cSphereNode')
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.attachNewNode(self.cSphereNode)
        self.cSphereNodePath.hide()
        self.cSphereBitMask = ToontownGlobals.WallBitmask
        self.cSphereNode.setFromCollideMask(self.cSphereBitMask)
        self.cSphereNode.setIntoCollideMask(BitMask32.allOff())
        self.cRay = CollisionRay(0.0, 0.0, 6.0, 0.0, 0.0, -1.0)
        self.cRayNode = CollisionNode('cRayNode')
        self.cRayNode.addSolid(self.cRay)
        self.cRayNodePath = self.attachNewNode(self.cRayNode)
        self.cRayNodePath.hide()
        self.cRayBitMask = ToontownGlobals.FloorBitmask
        self.cRayNode.setFromCollideMask(self.cRayBitMask)
        self.cRayNode.setIntoCollideMask(BitMask32.allOff())
        self.pusher = CollisionHandlerPusher()
        self.pusher.setInPattern('enter%in')
        self.pusher.setOutPattern('exit%in')
        self.lifter = CollisionHandlerFloor()
        self.lifter.setInPattern('on-floor')
        self.lifter.setOutPattern('off-floor')
        self.floorOffset = 0.025
        self.lifter.setOffset(self.floorOffset)
        self.lifter.setMaxVelocity(16.0)
        self.cTrav = CollisionTraverser()
        base.cTrav = self.cTrav
        self.collisionsOn()
        self.pusher.addCollider(self.cSphereNode, base.drive.node())
        self.lifter.addCollider(self.cRayNode, base.drive.node())
        self.ccTrav = CollisionTraverser()
        self.ccLine = CollisionSegment(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.ccLineNode = CollisionNode('ccLineNode')
        self.ccLineNode.addSolid(self.ccLine)
        self.ccLineNodePath = self.attachNewNode(self.ccLineNode)
        self.ccLineNodePath.hide()
        self.ccLineBitMask = ToontownGlobals.CameraBitmask
        self.ccLineNode.setFromCollideMask(self.ccLineBitMask)
        self.ccLineNode.setIntoCollideMask(BitMask32.allOff())
        self.camCollisionQueue = CollisionHandlerQueue()
        self.ccTrav.addCollider(self.ccLineNode, self.camCollisionQueue)
        self.ccRay = CollisionRay(0.0, 0.0, 6.0, 0.0, 0.0, -1.0)
        self.ccRayNode = CollisionNode('ccRayNode')
        self.ccRayNode.addSolid(self.ccRay)
        self.ccRayNodePath = base.camera.attachNewNode(self.ccRayNode)
        self.ccRayNodePath.hide()
        self.ccRayBitMask = ToontownGlobals.FloorBitmask
        self.ccRayNode.setFromCollideMask(self.ccRayBitMask)
        self.ccRayNode.setIntoCollideMask(BitMask32.allOff())
        self.ccTravFloor = CollisionTraverser()
        self.camFloorCollisionQueue = CollisionHandlerQueue()
        self.ccTravFloor.addCollider(self.ccRayNode, self.camFloorCollisionQueue)
        cam = base.cam.node()
        nearPlaneDist = cam.getNear()
        hFov = cam.getHfov()
        vFov = cam.getVfov()
        hOff = nearPlaneDist * math.tan(deg2Rad(hFov / 2))
        vOff = nearPlaneDist * math.tan(deg2Rad(vFov / 2))
        camPnts = [
            Point3(hOff, nearPlaneDist, vOff),
            Point3(-hOff, nearPlaneDist, vOff),
            Point3(hOff, nearPlaneDist, -vOff),
            Point3(-hOff, nearPlaneDist, -vOff),
            Point3(0.0, 0.0, 0.0)]
        avgPnt = Point3(0.0, 0.0, 0.0)
        for camPnt in camPnts:
            avgPnt = avgPnt + camPnt
        
        avgPnt = avgPnt / len(camPnts)
        sphereRadius = 0.0
        for camPnt in camPnts:
            dist = Vec3(camPnt - avgPnt).length()
            if dist > sphereRadius:
                sphereRadius = dist
            
        
        sphereRadius *= 1.15
        self.ccSphere = CollisionSphere(avgPnt[0], avgPnt[1], avgPnt[2], sphereRadius)
        self.ccSphereNode = CollisionNode('ccSphereNode')
        self.ccSphereNode.addSolid(self.ccSphere)
        self.ccSphereNodePath = base.camera.attachNewNode(self.ccSphereNode)
        self.ccSphereNodePath.hide()
        self.ccSphereBitMask = ToontownGlobals.CameraBitmask
        self.ccSphereNode.setFromCollideMask(self.ccSphereBitMask)
        self.ccSphereNode.setIntoCollideMask(BitMask32.allOff())
        self.camPusher = CollisionHandlerPusher()
        self.camPusher.addCollider(self.ccSphereNode, base.camera.arc())
        self.ccPusherTrav = CollisionTraverser()
        self.ccSphere2 = self.ccSphere
        self.ccSphereNode2 = CollisionNode('ccSphereNode2')
        self.ccSphereNode2.addSolid(self.ccSphere2)
        self.ccSphereNodePath2 = base.camera.attachNewNode(self.ccSphereNode2)
        self.ccSphereNodePath2.hide()
        self.ccSphereBitMask2 = ToontownGlobals.CameraBitmask
        self.ccSphereNode2.setFromCollideMask(self.ccSphereBitMask2)
        self.ccSphereNode2.setIntoCollideMask(BitMask32(0))
        self.camPusher2 = CollisionHandlerPusher()
        self.ccPusherTrav.addCollider(self.ccSphereNode2, self.camPusher2)
        self.camPusher2.addCollider(self.ccSphereNode2, base.camera.arc())
        return None

    
    def deleteCollisions(self):
        del self.cSphere
        del self.cSphereNode
        self.cSphereNodePath.removeNode()
        del self.cSphereNodePath
        del self.cRay
        del self.cRayNode
        self.cRayNodePath.removeNode()
        del self.cRayNodePath
        del self.pusher
        self.ignore('entero157')
        del self.lifter
        del self.cTrav
        del self.ccTrav
        del self.ccLine
        del self.ccLineNode
        self.ccLineNodePath.removeNode()
        del self.ccLineNodePath
        del self.camCollisionQueue
        del self.ccRay
        del self.ccRayNode
        self.ccRayNodePath.removeNode()
        del self.ccRayNodePath
        del self.ccTravFloor
        del self.camFloorCollisionQueue
        del self.ccSphere
        del self.ccSphereNode
        self.ccSphereNodePath.removeNode()
        del self.ccSphereNodePath
        del self.camPusher
        del self.ccPusherTrav
        del self.ccSphere2
        del self.ccSphereNode2
        self.ccSphereNodePath2.removeNode()
        del self.ccSphereNodePath2
        del self.camPusher2

    
    def collisionsOff(self):
        self.cTrav.removeCollider(self.cSphereNode)
        self.cTrav.removeCollider(self.cRayNode)
        return None

    
    def collisionsOn(self):
        self.collisionsOff()
        self.cTrav.addCollider(self.cSphereNode, self.pusher)
        self.cTrav.addCollider(self.cRayNode, self.lifter)
        return None

    
    def collidedWithWall(self, collisionEntry):
        base.playSfx(self.soundWalkCollision)

    
    def attachCamera(self):
        pos = self.getPos()
        hpr = self.getHpr()
        base.enableMouse()
        camera.reparentTo(self)
        base.setMouseOnArc(self.arc())
        if self.wantMouse:
            base.mouseInterfaceNode.setIgnoreMouse(0)
        else:
            base.mouseInterfaceNode.setIgnoreMouse(1)
        base.mouseInterfaceNode.setPos(pos)
        base.mouseInterfaceNode.setHpr(hpr)
        self.setWalkSpeedNormal()

    
    def setWalkSpeedNormal(self):
        base.mouseInterfaceNode.setForwardSpeed(ToontownGlobals.ToonForwardSpeed)
        base.mouseInterfaceNode.setReverseSpeed(ToontownGlobals.ToonReverseSpeed)
        base.mouseInterfaceNode.setRotateSpeed(ToontownGlobals.ToonRotateSpeed)
        return None

    
    def setWalkSpeedSlow(self):
        base.mouseInterfaceNode.setForwardSpeed(ToontownGlobals.ToonForwardSlowSpeed)
        base.mouseInterfaceNode.setReverseSpeed(ToontownGlobals.ToonReverseSlowSpeed)
        base.mouseInterfaceNode.setRotateSpeed(ToontownGlobals.ToonRotateSlowSpeed)
        return None

    
    def detachCamera(self):
        base.disableMouse()

    
    def addTabHook(self):
        self.accept('tab', self.nextCameraPos)
        self.accept('shift', self.setShift, [
            1])
        self.accept('shift-up', self.setShift, [
            0])
        self.accept('page_up', self.pageUp, [
            1])
        self.accept('page_up-up', self.pageUp, [
            0])
        self.accept('page_down', self.pageDown, [
            1])
        self.accept('page_down-up', self.pageDown, [
            0])

    
    def removeTabHook(self):
        self.ignore('tab')
        self.ignore('shift')
        self.ignore('shift-up')
        self.ignore('up')

    
    def setShift(self, shift):
        self.isShift = shift

    
    def pageUp(self, pageUp):
        if self.isPageUp != pageUp:
            self.isPageUp = pageUp
            self.setIdealCameraPosByIndex(self.cameraIndex)
        

    
    def pageDown(self, pageDown):
        if self.isPageDown != pageDown:
            self.isPageDown = pageDown
            self.setIdealCameraPosByIndex(self.cameraIndex)
        

    
    def nextCameraPos(self):
        self._LocalAvatar__filthyHack = 1
        if self.isShift:
            self.cameraIndex -= 1
            if self.cameraIndex < 0:
                self.cameraIndex = len(self.cameraPositions) - 1
            
        else:
            self.cameraIndex += 1
            if self.cameraIndex > len(self.cameraPositions) - 1:
                self.cameraIndex = 0
            
        self.setIdealCameraPosByIndex(self.cameraIndex)

    
    def initCameraPositions(self):
        camHeight = self.getClampedAvatarHeight()
        heightScaleFactor = camHeight * 0.3333333333
        defLookAt = Point3(0.0, 1.5, camHeight)
        qtXoffset = 3.0
        qtPosition = (Point3(qtXoffset - 1, -10.0, camHeight + 5.0), Point3(qtXoffset, 2.0, camHeight))
        self.cameraPositions = ((Point3(0.0, -9.0 * heightScaleFactor, camHeight), defLookAt, Point3(0.0, camHeight, camHeight * 4.0), Point3(0.0, camHeight, camHeight * -1.0)), (Point3(0.0, 0.5, camHeight), defLookAt, Point3(0.0, camHeight, camHeight * 1.33), Point3(0.0, camHeight, camHeight * 0.66)), (Point3(5.7 * heightScaleFactor, 7.65 * heightScaleFactor, camHeight + 2.0), Point3(0.0, 1.0, camHeight), Point3(0.0, 1.0, camHeight * 4.0), Point3(0.0, 1.0, camHeight * -1.0)), (Point3(0.0, -60, 60), defLookAt + Point3(0, 15, 0), defLookAt + Point3(0, 15, 0), defLookAt + Point3(0, 15, 0)), (Point3(0.0, -24.0 * heightScaleFactor, camHeight + 4.0), defLookAt, Point3(0.0, 1.5, camHeight * 4.0), Point3(0.0, 1.5, camHeight * -1.0)), (Point3(0.0, -12.0 * heightScaleFactor, camHeight + 4.0), defLookAt, Point3(0.0, 1.5, camHeight * 4.0), Point3(0.0, 1.5, camHeight * -1.0)))
        return None

    
    def posCamera(self, lerp, time):
        if not lerp:
            self.positionCameraWithPusher(self.getCompromiseCameraPos(), self.getLookAtPoint())
        else:
            camPos = self.getCompromiseCameraPos()
            savePos = camera.getPos()
            saveHpr = camera.getHpr()
            self.positionCameraWithPusher(camPos, self.getLookAtPoint())
            x = camPos[0]
            y = camPos[1]
            z = camPos[2]
            destHpr = camera.getHpr()
            h = destHpr[0]
            p = destHpr[1]
            r = destHpr[2]
            camera.setPos(savePos)
            camera.setHpr(saveHpr)
            taskMgr.removeTasksNamed('posCamera')
            camera.lerpPosHpr(x, y, z, h, p, r, time, task = 'posCamera')

    
    def getClampedAvatarHeight(self):
        return max(self.getHeight(), 3.0)

    
    def getVisibilityPoint(self):
        return Point3(0.0, 0.0, self.getHeight())

    
    def setLookAtPoint(self, la):
        self._LocalAvatar__curLookAt = Point3(la)

    
    def getLookAtPoint(self):
        return Point3(self._LocalAvatar__curLookAt)

    
    def setIdealCameraPos(self, pos):
        self._LocalAvatar__idealCameraPos = Point3(pos)
        self.updateSmartCameraCollisionLineSegment()

    
    def getIdealCameraPos(self):
        return Point3(self._LocalAvatar__idealCameraPos)

    
    def setIdealCameraPosByIndex(self, index):
        self.setIdealCameraPos(self.cameraPositions[index][0])
        if self.isPageUp and self.isPageDown and not (self.isPageUp) and not (self.isPageDown):
            self._LocalAvatar__filthyHack = 1
            self.setLookAtPoint(self.cameraPositions[index][1])
        elif self.isPageUp:
            self._LocalAvatar__filthyHack = 1
            self.setLookAtPoint(self.cameraPositions[index][2])
        elif self.isPageDown:
            self._LocalAvatar__filthyHack = 1
            self.setLookAtPoint(self.cameraPositions[index][3])
        else:
            self.notify.error('This case should be impossible.')

    
    def getCompromiseCameraPos(self):
        if self._LocalAvatar__idealCameraObstructed == 0:
            compromisePos = self.getIdealCameraPos()
        else:
            visPnt = self.getVisibilityPoint()
            idealPos = self.getIdealCameraPos()
            distance = Vec3(idealPos - visPnt).length()
            ratio = self.closestObstructionDistance / distance
            compromisePos = idealPos * ratio + visPnt * (1 - ratio)
            liftMult = 1.0 - ratio * ratio
            compromisePos = Point3(compromisePos[0], compromisePos[1], compromisePos[2] + self.getHeight() * 0.4 * liftMult)
        compromisePos.setZ(compromisePos[2] + self.cameraZOffset)
        return compromisePos

    
    def updateSmartCameraCollisionLineSegment(self):
        fudgeDist = 0.5
        self.ccLine.setPointB(self.getIdealCameraPos())
        pointA = self.getVisibilityPoint()
        fudgeVector = Vec3(self.ccLine.getPointB() - pointA)
        fudgeVector.normalize()
        fudgeVector = fudgeVector * fudgeDist
        pointA = Point3(pointA + Point3(fudgeVector))
        self.ccLine.setPointA(pointA)

    
    def initializeSmartCamera(self):
        self._LocalAvatar__idealCameraObstructed = 0
        self.closestObstructionDistance = 0.0
        self.cameraIndex = 0
        self.cameraZOffset = 0.0
        self._LocalAvatar__onLevelGround = 0
        self._LocalAvatar__geom = render

    
    def setOnLevelGround(self, flag):
        self._LocalAvatar__onLevelGround = flag

    
    def setGeom(self, geom):
        self._LocalAvatar__geom = geom

    
    def startUpdateSmartCamera(self):
        self._LocalAvatar__floorDetected = 0
        self._LocalAvatar__filthyHack = 0
        self.initCameraPositions()
        self.setIdealCameraPosByIndex(self.cameraIndex)
        self.posCamera(0, 0.0)
        self._LocalAvatar__instantaneousCamPos = camera.getPos()
        self.cTrav.addCollider(self.ccSphereNode, self.camPusher)
        self._LocalAvatar__lastPosWrtRender = camera.getPos(render)
        self._LocalAvatar__lastHprWrtRender = camera.getHpr(render)
        taskName = self.taskName('updateSmartCamera')
        taskMgr.removeTasksNamed(taskName)
        taskMgr.spawnMethodNamed(self.updateSmartCamera, taskName)

    
    def stopUpdateSmartCamera(self):
        self.cTrav.removeCollider(self.ccSphereNode)
        taskName = self.taskName('updateSmartCamera')
        taskMgr.removeTasksNamed(taskName)

    
    def updateSmartCamera(self, task):
        if not (self._LocalAvatar__filthyHack):
            if self._LocalAvatar__lastPosWrtRender == camera.getPos(render):
                if self._LocalAvatar__lastHprWrtRender == camera.getHpr(render):
                    return Task.cont
                
            
        
        self._LocalAvatar__filthyHack = 0
        self._LocalAvatar__lastPosWrtRender = camera.getPos(render)
        self._LocalAvatar__lastHprWrtRender = camera.getHpr(render)
        camWasObstructed = self._LocalAvatar__idealCameraObstructed
        self._LocalAvatar__idealCameraObstructed = 0
        self.ccTrav.traverse(self._LocalAvatar__geom)
        if self.camCollisionQueue.getNumEntries() > 0:
            self.camCollisionQueue.sortEntries()
            self.handleCameraObstruction(self.camCollisionQueue.getEntry(0), camWasObstructed)
        
        if not (self._LocalAvatar__onLevelGround):
            self.handleCameraFloorInteraction()
        
        self.nudgeCamera()
        return Task.cont

    
    def positionCameraWithPusher(self, pos, lookAt):
        camera.setPos(pos)
        self.ccPusherTrav.traverse(self._LocalAvatar__geom)
        camera.lookAt(lookAt)

    
    def nudgeCamera(self):
        CLOSE_ENOUGH = 0.1
        curCamPos = self._LocalAvatar__instantaneousCamPos
        curCamHpr = camera.getHpr()
        targetCamPos = self.getCompromiseCameraPos()
        targetCamLookAt = self.getLookAtPoint()
        posDone = 0
        if Vec3(curCamPos - targetCamPos).length() <= CLOSE_ENOUGH:
            camera.setPos(targetCamPos)
            posDone = 1
        
        camera.setPos(targetCamPos)
        camera.lookAt(targetCamLookAt)
        targetCamHpr = camera.getHpr()
        hprDone = 0
        if Vec3(curCamHpr - targetCamHpr).length() <= CLOSE_ENOUGH:
            hprDone = 1
        
        if posDone and hprDone:
            return None
        
        lerpRatio = 0.15
        lerpRatio = 1 - pow(1 - lerpRatio, globalClock.getDt() * 30.0)
        self._LocalAvatar__instantaneousCamPos = targetCamPos * lerpRatio + curCamPos * (1 - lerpRatio)
        camera.setPos(self._LocalAvatar__instantaneousCamPos)
        camera.setHpr(targetCamHpr * lerpRatio + curCamHpr * (1 - lerpRatio))

    
    def popCameraToDest(self):
        newCamPos = self.getCompromiseCameraPos()
        newCamLookAt = self.getLookAtPoint()
        self.positionCameraWithPusher(newCamPos, newCamLookAt)
        self._LocalAvatar__instantaneousCamPos = camera.getPos()

    
    def handleCameraObstruction(self, camObstrCollisionEntry, camWasObstructed):
        collisionPoint = camObstrCollisionEntry.getFromIntersectionPoint()
        collisionVec = Vec3(collisionPoint - self.ccLine.getPointA())
        distance = collisionVec.length()
        if not camWasObstructed and camWasObstructed and self.closestObstructionDistance > distance:
            popCameraUp = 1
        else:
            popCameraUp = 0
        self._LocalAvatar__idealCameraObstructed = 1
        self.closestObstructionDistance = distance
        if popCameraUp:
            self.popCameraToDest()
        

    
    def handleCameraFloorInteraction(self):
        self.ccTravFloor.traverse(self._LocalAvatar__geom)
        if self.camFloorCollisionQueue.getNumEntries() == 0:
            return None
        
        self.camFloorCollisionQueue.sortEntries()
        camObstrCollisionEntry = self.camFloorCollisionQueue.getEntry(0)
        camHeightFromFloor = camObstrCollisionEntry.getFromIntersectionPoint()[2]
        heightOfFloorUnderCamera = (camera.getPos()[2] - self.floorOffset) + camHeightFromFloor
        camIdealHeightFromFloor = self.getIdealCameraPos()[2]
        camTargetHeight = heightOfFloorUnderCamera + camIdealHeightFromFloor
        self.cameraZOffset = camTargetHeight - camIdealHeightFromFloor
        if self.cameraZOffset < 0.0:
            self.cameraZOffset = self.cameraZOffset * 0.3333333333
            if self.cameraZOffset < -(self.getClampedAvatarHeight() * 0.5):
                if self.cameraZOffset < -self.getClampedAvatarHeight():
                    self.cameraZOffset = 0.0
                else:
                    self.cameraZOffset = -(self.getClampedAvatarHeight() * 0.5)
            
        
        if self._LocalAvatar__floorDetected == 0:
            self._LocalAvatar__floorDetected = 1
            self.popCameraToDest()
        

    
    def lerpCameraFov(self, fov, time):
        from IntervalGlobal import *
        oldFov = base.cam.node().getHfov()
        if abs(fov - oldFov) > 0.1:
            
            def setCamFov(fov):
                base.cam.node().setFov(fov)

            self.camLerpInterval = LerpFunctionInterval(setCamFov, fromData = oldFov, toData = fov, duration = time, name = 'cam-fov-lerp')
            self.camLerpInterval.play()
        

    
    def gotoNode(self, node):
        possiblePoints = (Point3(3, 6, 0), Point3(-3, 6, 0), Point3(6, 6, 0), Point3(-6, 6, 0), Point3(3, 9, 0), Point3(-3, 9, 0), Point3(6, 9, 0), Point3(-6, 9, 0), Point3(9, 9, 0), Point3(-9, 9, 0), Point3(6, 0, 0), Point3(-6, 0, 0), Point3(6, 3, 0), Point3(-6, 3, 0), Point3(9, 9, 0), Point3(-9, 9, 0), Point3(0, 12, 0), Point3(3, 12, 0), Point3(-3, 12, 0), Point3(6, 12, 0), Point3(-6, 12, 0), Point3(9, 12, 0), Point3(-9, 12, 0), Point3(0, -6, 0), Point3(-3, -6, 0), Point3(0, -9, 0), Point3(-6, -9, 0))
        for point in possiblePoints:
            pos = self.positionExaminer.consider(node, point)
            if pos:
                self.setPos(node, pos)
                self.lookAt(node)
                self.setHpr(self.getH() + whrandom.choice((-10, 10)), 0, 0)
                base.drive.node().setPos(self.getPos())
                base.drive.node().setHpr(self.getHpr())
                return None
            
        
        self.setPos(node, 0, 0, 0)
        base.drive.node().setPos(self.getPos())
        base.drive.node().setHpr(self.getHpr())

    
    def displayWhisper(self, chatString):
        whisper = WhisperPopup(chatString, ToontownGlobals.getInterfaceFont())
        whisper.manage(toonbase.marginManager)

    
    def setAnimMultiplier(self, value):
        self.animMultiplier = value

    
    def getAnimMultiplier(self):
        return self.animMultiplier

    
    def runSound(self):
        base.stopSfx(self.soundWalk)
        base.playSfx(self.soundRun, looping = 1)

    
    def walkSound(self):
        base.stopSfx(self.soundRun)
        base.playSfx(self.soundWalk, looping = 1)

    
    def stopSound(self):
        base.stopSfx(self.soundRun)
        base.stopSfx(self.soundWalk)

    
    def trackAnimToSpeed(self, task):
        speed = base.mouseInterfaceNode.getSpeed()
        if speed >= task.runCutOff:
            if task.animMode != RUN_FORWARD_MODE:
                task.animMode = RUN_FORWARD_MODE
                if self.hp > 0:
                    self.b_setAnimState('run', self.animMultiplier)
                else:
                    self.b_setAnimState('sad-walk', self.animMultiplier)
                self.runSound()
            
        elif speed > 0.0 and speed < task.runCutOff:
            if task.animMode != WALK_FORWARD_MODE:
                task.animMode = WALK_FORWARD_MODE
                if self.hp > 0:
                    self.b_setAnimState('walk', self.animMultiplier)
                else:
                    self.b_setAnimState('sad-walk', self.animMultiplier)
                self.walkSound()
            
        elif speed == 0.0:
            rotSpeed = base.mouseInterfaceNode.getRotSpeed()
            if rotSpeed == 0.0:
                if task.animMode != NEUTRAL_MODE:
                    task.animMode = NEUTRAL_MODE
                    if self.hp > 0:
                        self.b_setAnimState('neutral', self.animMultiplier)
                    else:
                        self.b_setAnimState('sad-neutral', self.animMultiplier)
                    self.stopSound()
                
            elif task.animMode != SPIN_IN_PLACE_MODE:
                task.animMode = SPIN_IN_PLACE_MODE
                if self.hp > 0:
                    self.b_setAnimState('walk', self.animMultiplier)
                else:
                    self.b_setAnimState('sad-walk', self.animMultiplier)
                self.walkSound()
            
        elif speed < 0.0:
            if task.animMode != WALK_BACKWARD_MODE:
                task.animMode = WALK_BACKWARD_MODE
                if self.hp > 0:
                    self.b_setAnimState('walk', -(self.animMultiplier))
                else:
                    self.b_setAnimState('sad-walk', -(self.animMultiplier))
                self.walkSound()
            
        
        return Task.cont

    
    def startTrackAnimToSpeed(self):
        taskName = self.taskName('trackAnimToSpeed')
        taskMgr.removeTasksNamed(taskName)
        task = Task.Task(self.trackAnimToSpeed)
        task.runCutOff = 8.0
        task.animMode = NEUTRAL_MODE
        if self.hp > 0:
            self.b_setAnimState('neutral', self.animMultiplier)
        else:
            self.b_setAnimState('sad-neutral', self.animMultiplier)
        taskMgr.spawnTaskNamed(task, taskName)

    
    def stopTrackAnimToSpeed(self):
        taskName = self.taskName('trackAnimToSpeed')
        taskMgr.removeTasksNamed(taskName)
        self.stopSound()

    
    def startChat(self):
        self.chatMgr.start()
        self.accept('chatUpdate', self.b_setChat)
        self.accept('chatUpdateQT', self.b_setQT)
        self.accept(ToontownGlobals.ThinkPosHotkey, self.thinkPos)
        if self._LocalAvatar__enableMarkerPlacement:
            self.accept(ToontownGlobals.PlaceMarkerHotkey, self._LocalAvatar__placeMarker)
        
        self.b_setParentalControl(self.chatMgr.chatPermission())
        return None

    
    def stopChat(self):
        self.chatMgr.stop()
        self.ignore('chatUpdate')
        self.ignore('chatUpdateQT')
        self.ignore(ToontownGlobals.ThinkPosHotkey)
        if self._LocalAvatar__enableMarkerPlacement:
            self.ignore(ToontownGlobals.PlaceMarkerHotkey)
        
        return None

    
    def thinkPos(self):
        pos = self.getPos()
        hpr = self.getHpr()
        serverVersion = toonbase.tcr.getServerVersion()
        if hasattr(toonbase.tcr.playGame.hood, 'loader') and hasattr(toonbase.tcr.playGame.hood.loader, 'place') and toonbase.tcr.playGame.hood.loader.place != None:
            zoneId = toonbase.tcr.playGame.hood.loader.place.getZoneId()
        else:
            zoneId = '?'
        self.b_setChat('X: %.3f' % pos[0] + '\nY: %.3f' % pos[1] + '\nZ: %.3f' % pos[2] + '\nH: %.3f' % hpr[0] + '\nP: %.3f' % hpr[1] + '\nR: %.3f' % hpr[2] + '\nZone: %s' % str(zoneId) + '\nVer: %s' % serverVersion, CFThought)

    
    def __placeMarker(self):
        pos = self.getPos()
        hpr = self.getHpr()
        print '(%d, %d, %0.1f),' % (pos[0], pos[1], pos[2])
        print '(%0.1f, %0.1f, %0.1f, %0.1f, %0.1f, %0.1f),' % (pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2])
        chest = loader.loadModelOnce('phase_4/models/props/coffin')
        chest.reparentTo(render)
        chest.setColor(1, 0, 0, 1)
        chest.setPosHpr(pos, hpr)
        chest.setScale(0.5)

    
    def stopPosHprBroadcast(self):
        taskName = self.taskName('sendPosHpr')
        taskMgr.removeTasksNamed(taskName)

    
    def startPosHprBroadcast(self):
        taskName = self.taskName('sendPosHpr')
        xyz = self.getPos()
        hpr = self.getHpr(0)
        self.storeX = xyz[0]
        self.storeY = xyz[1]
        self.storeZ = xyz[2]
        self.storeH = hpr[0]
        self.storeP = hpr[1]
        self.storeR = hpr[2]
        self.epsilon = 0.001
        self.d_setPosHpr(self.storeX, self.storeY, self.storeZ, self.storeH, self.storeP, self.storeR)
        taskMgr.removeTasksNamed(taskName)
        task = Task.Task(self.posHprBroadcast)
        task.loopTime = 0.0
        taskMgr.spawnTaskNamed(task, taskName)

    
    def posHprBroadcast(self, task):
        if task.time - task.loopTime < 0.2:
            return Task.cont
        else:
            task.loopTime = task.time
            self.d_broadcastDRPosHpr()
            return Task.cont
        return None

    
    def d_broadcastDRPosHpr(self):
        xyz = self.getPos()
        hpr = self.getHpr(0)
        if abs(self.storeX - xyz[0]) > self.epsilon:
            newX = xyz[0]
        else:
            newX = None
        if abs(self.storeY - xyz[1]) > self.epsilon:
            newY = xyz[1]
        else:
            newY = None
        if abs(self.storeZ - xyz[2]) > self.epsilon:
            newZ = xyz[2]
        else:
            newZ = None
        if abs(self.storeH - hpr[0]) > self.epsilon:
            newH = hpr[0]
        else:
            newH = None
        if abs(self.storeP - hpr[1]) > self.epsilon:
            newP = hpr[1]
        else:
            newP = None
        if abs(self.storeR - hpr[2]) > self.epsilon:
            newR = hpr[2]
        else:
            newR = None
        if not newX and newY and newZ and newH and newP:
            pass
        if not newR:
            pass
        1
        if newH:
            if not newX and newY and newZ and newP:
                pass
            if not newR:
                if newH:
                    self.storeH = newH
                
                self.d_setH(self.storeH)
            elif newX or newY:
                if not newZ and newH and newP:
                    pass
                if not newR:
                    if newX:
                        self.storeX = newX
                    
                    if newY:
                        self.storeY = newY
                    
                    self.d_setXY(self.storeX, self.storeY)
                elif newX and newY or newZ:
                    if not newH and newP:
                        pass
                    if not newR:
                        oldStoreX = self.storeX
                        oldStoreY = self.storeY
                        oldStoreZ = self.storeZ
                        if newX:
                            self.storeX = newX
                        
                        if newY:
                            self.storeY = newY
                        
                        if newZ:
                            self.storeZ = newZ
                        
                        self.d_setPos(self.storeX, self.storeY, self.storeZ)
                    elif newX and newY or newH:
                        if not newZ and newP:
                            pass
                        if not newR:
                            if newX:
                                self.storeX = newX
                            
                            if newY:
                                self.storeY = newY
                            
                            if newH:
                                self.storeH = newH
                            
                            self.d_setXYH(self.storeX, self.storeY, self.storeH)
                        elif newX and newY and newZ or newH:
                            if not newP:
                                pass
                            if not newR:
                                if newX:
                                    self.storeX = newX
                                
                                if newY:
                                    self.storeY = newY
                                
                                if newZ:
                                    self.storeZ = newZ
                                
                                if newH:
                                    self.storeH = newH
                                
                                self.d_setXYZH(self.storeX, self.storeY, self.storeZ, self.storeH)
                            elif newX:
                                self.storeX = newX
                            
        if newY:
            self.storeY = newY
        
        if newZ:
            self.storeZ = newZ
        
        if newH:
            self.storeH = newH
        
        if newP:
            self.storeP = newP
        
        if newR:
            self.storeR = newR
        
        self.d_setPosHpr(self.storeX, self.storeY, self.storeZ, self.storeH, self.storeP, self.storeR)

    
    def tunnelOut(self, hoodId, zoneId, tunnelOrigin, callback):
        
        def irisOut(task):
            base.transitions.irisOut(0.4)
            return Task.done

        
        def callCallback(task):
            task.localToon.stopSound()
            apply(task.callback, [
                task.hoodId,
                task.zoneId])
            return Task.done

        callbackTask = Task.Task(callCallback)
        callbackTask.callback = callback
        callbackTask.localToon = self
        callbackTask.hoodId = hoodId
        callbackTask.zoneId = zoneId
        callbackTask.tunnelOrigin = tunnelOrigin
        self.b_setAnimState('run', self.animMultiplier)
        self.runSound()
        camera.wrtReparentTo(render)
        reducedCamH = shortestDestAngle(camera.getH(tunnelOrigin), 179)
        reducedAvH = shortestDestAngle(self.getH(tunnelOrigin), 179)
        camera.lerpPosHpr(0, 20, 12, reducedCamH, -20, 0, 1, other = tunnelOrigin, blendType = 'easeInOut', task = 'tunnelOutLerpCamera')
        seq = Task.sequence(self.lerpPosHpr(0, -16, 0.1, reducedAvH, 0, 0, 2, other = tunnelOrigin), Task.Task(irisOut), Task.pause(0.5), callbackTask)
        taskMgr.spawnTaskNamed(seq, 'tunnelOutSequence')

    
    def tunnelIn(self, hoodId, zoneId, tunnelOrigin, callback):
        
        def irisIn(task):
            base.transitions.irisIn(0.4)
            return Task.done

        
        def callCallback(task):
            task.localToon.stopSound()
            apply(task.callback, [
                task.hoodId,
                task.zoneId])
            return Task.done

        callbackTask = Task.Task(callCallback)
        callbackTask.callback = callback
        callbackTask.localToon = self
        callbackTask.hoodId = hoodId
        callbackTask.zoneId = zoneId
        callbackTask.tunnelOrigin = tunnelOrigin
        self.b_setAnimState('run', self.animMultiplier)
        self.runSound()
        camera.reparentTo(render)
        camera.setPosHpr(tunnelOrigin, 0, 20, 12, 180, -20, 0)
        self.setPosHpr(tunnelOrigin, 0, -16, 0.1, 0, 0, 0)
        seq = Task.sequence(Task.Task(irisIn), self.lerpPosHpr(0, 5, 0.1, 0, 0, 0, 2, other = tunnelOrigin), callbackTask)
        taskMgr.spawnTaskNamed(seq, 'tunnelInSequence')

    
    def skyTrack(self, task):
        sky = task.sky
        sky.overloaded_setZ_ptrNodePath_ptrConstNodePath_float(render, 0.0)
        sky.overloaded_setHpr_ptrNodePath_ptrConstNodePath_float_float_float(render, 0.0, 0.0, 0.0)
        return Task.cont

    
    def startSky(self, sky):
        sky.reparentTo(camera)
        sky.setZ(render, 0.0)
        sky.setHpr(render, 0.0, 0.0, 0.0)
        skyTrackTask = Task.Task(self.skyTrack, 40)
        skyTrackTask.sky = sky
        skyTrackTask.h = 0
        taskMgr.spawnTaskNamed(skyTrackTask, 'skyTrack')

    
    def stopSky(self, sky):
        taskMgr.removeTasksNamed('skyTrack')
        sky.reparentTo(hidden)

    
    def setFriendsListButtonActive(self, active):
        self.friendsListButtonActive = active
        self._LocalAvatar__doFriendsListButton()

    
    def obscureFriendsListButton(self, increment):
        self.friendsListButtonObscured += increment
        self._LocalAvatar__doFriendsListButton()

    
    def __doFriendsListButton(self):
        if self.friendsListButtonActive and self.friendsListButtonObscured <= 0:
            self.bFriendsList.show()
        else:
            self.bFriendsList.hide()

    
    def travCollisionsLOS(self, n = None):
        if n == None:
            n = self._LocalAvatar__geom
        
        self.ccTrav.traverse(n)

    
    def travCollisionsFloor(self, n = None):
        if n == None:
            n = self._LocalAvatar__geom
        
        self.ccTravFloor.traverse(n)

    
    def travCollisionsPusher(self, n = None):
        if n == None:
            n = self._LocalAvatar__geom
        
        self.ccPusherTrav.traverse(n)


