# Source Generated with Decompyle++
# File: Place.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from ToontownGlobals import *
import PandaObject
import DirectNotifyGlobal
import StateData
import PublicWalk
import DownloadForceAcknowledge

class Place(PandaObject.PandaObject, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('Place')
    
    def __init__(self, loader, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.loader = loader
        self.dfaDoneEvent = 'dfaDoneEvent'
        return None

    
    def load(self):
        self.walkDoneEvent = 'walkDone'
        self.walkStateData = PublicWalk.PublicWalk(self.fsm, self.walkDoneEvent)
        self.walkStateData.load()
        return None

    
    def unload(self):
        del self.walkDoneEvent
        self.walkStateData.unload()
        del self.walkStateData
        del self.loader
        return None

    
    def getZoneId(self):
        return None

    
    def handleTeleportQuery(self, fromAvatar, toAvatar):
        fromAvatar.d_teleportResponse(toAvatar.doId, 1, toAvatar.defaultShard, self.loader.hood.id, self.getZoneId())

    
    def enterWalk(self, teleportIn = 0):
        self.walkStateData.enter()
        if teleportIn == 0:
            self.walkStateData.fsm.request('walking')
        
        self.acceptOnce(self.walkDoneEvent, self._Place__handleWalkDone)
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        return None

    
    def exitWalk(self):
        self.walkStateData.exit()
        self.ignore(self.walkDoneEvent)
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        self.loader.hood.hideTitleText()
        return None

    
    def __handleWalkDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'StickerBook':
            self.last = self.fsm.getCurrentState().getName()
            self.fsm.request('stickerBook')
        elif mode == 'Options':
            self.last = self.fsm.getCurrentState().getName()
            self.fsm.request('stickerBook', [
                toonbase.localToon.optionsPage])
        else:
            self.notify.error('Invalid mode: %s' % mode)
        return None

    
    def enterStickerBook(self, page = None):
        toonbase.localToon.laffMeter.start()
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        if page:
            toonbase.localToon.book.setPage(page)
        
        toonbase.localToon.b_setAnimState('OpenBook', 1, self._Place__enterStickerBookGUI)

    
    def __enterStickerBookGUI(self):
        toonbase.localToon.collisionsOn()
        toonbase.localToon.book.showButton()
        toonbase.localToon.book.enter()
        self.accept('bookDone', self._Place__handleBook)
        self.accept('escape-up', self._Place__escCloseBook)
        toonbase.localToon.b_setAnimState('ReadBook', 1)

    
    def __escCloseBook(self):
        toonbase.localToon.book.exit()
        toonbase.localToon.b_setAnimState('CloseBook', 1, callback = self.handleBookClose)
        return None

    
    def exitStickerBook(self):
        toonbase.localToon.laffMeter.stop()
        toonbase.localToon.setFriendsListButtonActive(0)
        toonbase.localToon.book.exit()
        toonbase.localToon.book.hideButton()
        toonbase.localToon.collisionsOff()
        self.ignore('bookDone')
        self.ignore('escape-up')
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')

    
    def __handleBook(self):
        toonbase.localToon.book.exit()
        bookStatus = toonbase.localToon.book.getDoneStatus()
        if bookStatus['mode'] == 'close':
            toonbase.localToon.b_setAnimState('CloseBook', 1, callback = self.handleBookClose)
            return None
        elif bookStatus['mode'] == 'teleport':
            zoneId = bookStatus['hood']
            toonbase.localToon.b_setAnimState('CloseBook', 1, callback = self._Place__handleBookCloseTeleport, extraArgs = [
                zoneId,
                zoneId])
            return None
        elif bookStatus['mode'] == 'exit':
            toonbase.localToon.b_setAnimState('CloseBook', 1, callback = self._Place__handleBookCloseExit)
            return None
        

    
    def __handleBookCloseTeleport(self, hoodId, zoneId):
        self.fsm.request('DFA', [
            {
                'mode': 'teleportOut',
                'hoodId': hoodId,
                'zoneId': zoneId,
                'avId': -1 }])
        return None

    
    def __handleBookCloseExit(self):
        toonbase.localToon.b_setAnimState('TeleportOut', 1, self._Place__handleBookExitTeleport, [
            0])
        return None

    
    def __handleBookExitTeleport(self, requestStatus):
        toonbase.tcr.loginFSM.request('chooseAvatar', [
            toonbase.tcr.avList])
        return None

    
    def handleBookClose(self):
        self.fsm.request('walk')
        toonbase.localToon.b_setAnimState('neutral', 1)
        return None

    
    def enterDFA(self, requestStatus):
        self.acceptOnce(self.dfaDoneEvent, self.enterDFACallback, [
            requestStatus])
        self.dfa = DownloadForceAcknowledge.DownloadForceAcknowledge(self.dfaDoneEvent)
        self.dfa.enter(toonbase.tcr.hoodMgr.getPhaseFromHood(requestStatus['hoodId']))

    
    def exitDFA(self):
        self.ignore(self.dfaDoneEvent)

    
    def handleEnterTunnel(self, requestStatus, collEntry):
        self.fsm.request('DFA', [
            requestStatus])

    
    def enterDFACallback(self, requestStatus, doneStatus):
        self.dfa.exit()
        del self.dfa
        if doneStatus['mode'] == 'complete':
            self.fsm.request(requestStatus['mode'], [
                requestStatus])
        elif doneStatus['mode'] == 'incomplete':
            self.fsm.request('DFAReject')
        else:
            self.notify.error('Unknown done status for DownloadForceAcknowledge: ' + `doneStatus`)
        return None

    
    def enterDFAReject(self):
        self.fsm.request('walk')

    
    def exitDFAReject(self):
        pass

    
    def enterDoorIn(self, requestStatus):
        door = toonbase.tcr.doId2do.get(requestStatus['doorDOID'])
        door.readyToExit()

    
    def exitDoorIn(self):
        pass

    
    def enterDoorOut(self, requestStatus):
        pass

    
    def exitDoorOut(self):
        pass

    
    def enterTunnelIn(self, requestStatus):
        tunnelOrigin = base.render.find(requestStatus['tunnelName'])
        toonbase.localToon.tunnelIn(requestStatus['hoodId'], requestStatus['zoneId'], tunnelOrigin, self.tunnelInMovieCallback)

    
    def tunnelInMovieCallback(self, hood, zoneId):
        self.fsm.request('walk')

    
    def exitTunnelIn(self):
        pass

    
    def enterTunnelOut(self, requestStatus):
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        tunnelOrigin = requestStatus['tunnelOrigin']
        toonbase.localToon.tunnelOut(hoodId, zoneId, tunnelOrigin, self.tunnelOutMovieCallback)

    
    def tunnelOutMovieCallback(self, hoodId, zoneId):
        tunnelName = toonbase.tcr.hoodMgr.makeLinkTunnelName(self.loader.hood.id, self.getZoneId())
        self.doneStatus = {
            'mode': 'tunnelOut',
            'hoodId': hoodId,
            'zoneId': zoneId,
            'tunnelName': tunnelName }
        messenger.send(self.doneEvent)

    
    def exitTunnelOut(self):
        pass

    
    def enterTeleportOut(self, requestStatus, callback):
        toonbase.localToon.b_setAnimState('TeleportOut', 1, callback, [
            requestStatus])

    
    def exitTeleportOut(self):
        pass

    
    def enterTeleportIn(self, requestStatus):
        avId = requestStatus['avId']
        if avId != -1:
            if toonbase.tcr.doId2do.has_key(avId):
                avatar = toonbase.tcr.doId2do[avId]
                toonbase.localToon.gotoNode(avatar)
                toonbase.localToon.b_setChat('Hi, %s.' % avatar.getName(), CFSpeech | CFTimeout)
            else:
                friend = toonbase.tcr.identifyFriend(avId)
                if friend == None:
                    toonbase.localToon.setWhisper('The toon you were coming to visit is gone!')
                else:
                    toonbase.localToon.setWhisper('%s has gone somewhere else.' % friend.getName())
        
        base.transitions.irisIn()
        self.fsm.request('walk', [
            1])
        toonbase.localToon.b_setAnimState('TeleportIn', 1, callback = self.teleportInDone)

    
    def teleportInDone(self):
        self.walkStateData.fsm.request('walking')

    
    def exitTeleportIn(self):
        pass

    
    def requestTeleport(self, hoodId, zoneId, avId):
        pass


