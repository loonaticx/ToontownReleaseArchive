# Source Generated with Decompyle++
# File: ToontownClientRepository.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from ToontownMsgTypes import *
from DownloadForceAcknowledge import *
from ClockDelta import *
from ToontownGlobals import *
from DCSubatomicType import *
import sys
import AvatarDNA
import DirectNotifyGlobal
import ClientRepository
import PotentialAvatar
import PotentialShard
import FSM
import State
import LocalToon
import LoginScreen
import AvatarChooser
import ShardChooser
import HoodChooser
import MakeAToon
import HoodMgr
import PlayGame
import FriendHandle
import Task
import DialogBox
import types

class ToontownClientRepository(ClientRepository.ClientRepository):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownClientRepository')
    avatarLimit = 6
    defaultServerPort = 5150
    
    def __init__(self, dcFileName, serverVersion, launcher = None):
        ClientRepository.ClientRepository.__init__(self, dcFileName)
        self.launcher = launcher
        base.launcher = launcher
        self.name2nodePath = { }
        self.name2nodePath['render'] = base.render
        self.name2nodePath['hidden'] = base.hidden
        self.friendManager = None
        self.friendsMap = { }
        self.friendsOnline = { }
        self.friendsMapPending = 0
        self._ToontownClientRepository__queryAvatarMap = { }
        self._ToontownClientRepository__shards = { }
        self.serverVersion = serverVersion
        self.loginFSM = FSM.FSM('ClientRepositoryLogin', [
            State.State('loginOff', self.enterLoginOff, self.exitLoginOff, [
                'login']),
            State.State('login', self.enterLogin, self.exitLogin, [
                'waitForLoginResponse',
                'failedToConnect',
                'shutdown',
                'noConnection']),
            State.State('failedToConnect', self.enterFailedToConnect, self.exitFailedToConnect, [
                'shutdown',
                'login']),
            State.State('shutdown', self.enterShutdown, self.exitShutdown, [
                'loginOff']),
            State.State('waitForLoginResponse', self.enterWaitForLoginResponse, self.exitWaitForLoginResponse, [
                'reject',
                'waitForShardList',
                'noConnection']),
            State.State('waitForShardList', self.enterWaitForShardList, self.exitWaitForShardList, [
                'waitForAvatarList',
                'noShards',
                'noConnection']),
            State.State('noShards', self.enterNoShards, self.exitNoShards, [
                'waitForShardList',
                'noConnection',
                'shutdown']),
            State.State('reject', self.enterReject, self.exitReject, [
                'shutdown']),
            State.State('noConnection', self.enterNoConnection, self.exitNoConnection, [
                'login']),
            State.State('waitForAvatarList', self.enterWaitForAvatarList, self.exitWaitForAvatarList, [
                'chooseAvatar',
                'createAvatar',
                'noConnection']),
            State.State('chooseAvatar', self.enterChooseAvatar, self.exitChooseAvatar, [
                'createAvatar',
                'waitForSetAvatarResponse',
                'waitForDeleteAvatarResponse',
                'noConnection']),
            State.State('createAvatar', self.enterCreateAvatar, self.exitCreateAvatar, [
                'chooseAvatar',
                'waitForSetAvatarResponse',
                'waitForCreateAvatarResponse',
                'noConnection']),
            State.State('waitForCreateAvatarResponse', self.enterWaitForCreateAvatarResponse, self.exitWaitForCreateAvatarResponse, [
                'waitForSetAvatarResponse',
                'chooseAvatar',
                'noConnection']),
            State.State('waitForDeleteAvatarResponse', self.enterWaitForDeleteAvatarResponse, self.exitWaitForDeleteAvatarResponse, [
                'chooseAvatar',
                'createAvatar',
                'noConnection']),
            State.State('waitForSetAvatarResponse', self.enterWaitForSetAvatarResponse, self.exitWaitForSetAvatarResponse, [
                'chooseAvatar',
                'noConnection'])], 'loginOff', 'loginOff')
        self.gameFSM = FSM.FSM('ClientRepository', [
            State.State('gameOff', self.enterGameOff, self.exitGameOff, [
                'waitOnEnterResponses']),
            State.State('waitOnEnterResponses', self.enterWaitOnEnterResponses, self.exitWaitOnEnterResponses, [
                'playGame',
                'waitForTutorial',
                'gameOff']),
            State.State('waitForTutorial', self.enterWaitForTutorial, self.exitWaitForTutorial, [
                'tutorialQuestion',
                'gameOff']),
            State.State('tutorialQuestion', self.enterTutorialQuestion, self.exitTutorialQuestion, [
                'playGame',
                'gameOff']),
            State.State('playGame', self.enterPlayGame, self.exitPlayGame, [
                'gameOff',
                'waitOnEnterResponses'])], 'gameOff', 'gameOff')
        self.loginFSM.getStateNamed('waitForSetAvatarResponse').addChild(self.gameFSM)
        self.loginFSM.enterInitialState()
        self.loginScreen = None
        self.music = None
        self.hoodMgr = HoodMgr.HoodMgr(self)
        self.playGame = PlayGame.PlayGame(self.gameFSM, 'donePlayingGame')
        return None

    
    def getServerVersion(self):
        return self.serverVersion

    
    def enterLoginOff(self):
        self.handler = self.handleLoginOff
        return None

    
    def exitLoginOff(self):
        self.handler = None
        return None

    
    def handleLoginOff(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def enterLogin(self, serverName = 'localhost', serverPort = defaultServerPort):
        self.connectingBox = DialogBox.DialogBox(message = 'Connecting...')
        self.connectingBox.show()
        base.win.update()
        self.serverName = serverName
        self.serverPort = serverPort
        self.loginScreen = None
        self.handler = self.handleLogin
        if self.launcher and self.launcher.hasProxy():
            self.proxyServerName = self.launcher.getProxyServer()
            self.proxyServerPort = self.launcher.getProxyPort()
            self.notify.info('Connecting to game server through proxy: %s, port: %s' % (self.proxyServerName, self.proxyServerPort))
            retVal = self.connect(self.proxyServerName, self.proxyServerPort)
            self.stopReaderPollTask()
        else:
            retVal = self.connect(self.serverName, self.serverPort)
        self.connectingBox.cleanup()
        del self.connectingBox
        if retVal:
            if self.launcher and self.launcher.hasProxy():
                realGameServer = self.serverName + ':' + str(self.serverPort)
                connectString = 'CONNECT ' + realGameServer + ' HTTP/1.0\n\n'
                datagram = Datagram()
                datagram.appendData(connectString)
                self.notify.info('Sending CONNECT string: ' + connectString)
                self.cw.setRawMode(1)
                self.qcr.setRawMode(1)
                self.notify.info('done set raw mode')
                self.send(datagram)
                self.notify.info('done send datagram')
                self.findRawString([
                    '\r\n',
                    '\r\r'], self.finishLogin)
                self.notify.info('done find raw string')
                self.startRawReaderPollTask()
                self.notify.info('done start raw reader poll task')
            else:
                self.finishLogin()
        else:
            self.loginFSM.request('failedToConnect')
        return None

    
    def finishLogin(self):
        self.cw.setRawMode(0)
        self.qcr.setRawMode(0)
        self.startReaderPollTask()
        self.startHeartbeat()
        if self.launcher:
            green = self.launcher.getGreen()
            self.launcher.deleteGreen()
        else:
            green = None
        if green:
            self.loginFSM.request('waitForLoginResponse', [
                1,
                green])
        elif base.config.GetBool('require-green', 1):
            print 'You must have a green to log in, or set dconfig require-green to 0'
            self.loginFSM.request('shutdown')
        else:
            self.loginScreen = LoginScreen.LoginScreen('loginEntered')
            self.accept('loginEntered', self._ToontownClientRepository__handleLoginEntered)
            self.loginScreen.load()
            self.loginScreen.enter()
        return None

    
    def __handleLoginEntered(self):
        loginName = self.loginScreen.getLoginName()
        self.loginFSM.request('waitForLoginResponse', [
            0,
            loginName])

    
    def exitLogin(self):
        if self.loginScreen:
            self.loginScreen.unload()
            del self.loginScreen
        
        self.ignore('loginEntered')
        self.handler = None
        return None

    
    def handleLogin(self, msgType, di):
        if msgType == CLIENT_SERVER_UP:
            self._ToontownClientRepository__handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self._ToontownClientRepository__handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def enterFailedToConnect(self):
        self.handler = self.handleFailedToConnect
        self.failedToConnectBox = DialogBox.DialogBox(message = 'Could not connect to ' + self.serverName + ':' + str(self.serverPort) + '. Try again?', doneEvent = 'failedToConnectAck', style = DialogBox.TwoChoice)
        self.failedToConnectBox.show()
        self.accept('failedToConnectAck', self._ToontownClientRepository__handleFailedToConnectAck)
        self.notify.warning('Failed to connect to ' + self.serverName + ':' + str(self.serverPort) + '. Notifying user.')
        return None

    
    def __handleFailedToConnectAck(self):
        doneStatus = self.failedToConnectBox.doneStatus
        if doneStatus == 'ok':
            self.loginFSM.request('login', [
                self.serverName,
                self.serverPort])
        elif doneStatus == 'cancel':
            self.loginFSM.request('shutdown')
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))
        return None

    
    def handleFailedToConnect(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def exitFailedToConnect(self):
        self.handler = None
        self.ignore('failedToConnectAck')
        self.failedToConnectBox.cleanup()
        del self.failedToConnectBox
        return None

    
    def enterShutdown(self):
        self.handler = self.handleShutdown
        self.notify.info('Exiting Toontown cleanly')
        sys.exit()
        return None

    
    def exitShutdown(self):
        self.handler = None
        return None

    
    def handleShutdown(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def enterWaitForLoginResponse(self, hasGreen, login):
        self.handler = self.handleWaitForLoginResponse
        if hasGreen:
            self.sendGreenMsg(login)
        else:
            self.sendLoginMsg(login)
        return None

    
    def sendLoginMsg(self, loginName):
        datagram = Datagram()
        datagram.addUint16(CLIENT_LOGIN)
        datagram.addString(loginName)
        datagram.addUint32(self.tcpConn.getAddress().getIp())
        datagram.addUint16(5150)
        datagram.addString(self.serverVersion)
        datagram.addUint32(self.hashVal)
        self.send(datagram)
        return None

    
    def sendGreenMsg(self, green):
        datagram = Datagram()
        datagram.addUint16(CLIENT_LOGIN_2)
        datagram.addString(green)
        datagram.addString(self.serverVersion)
        datagram.addUint32(self.hashVal)
        self.send(datagram)
        return None

    
    def exitWaitForLoginResponse(self):
        self.handler = None
        return None

    
    def handleWaitForLoginResponse(self, msgType, di):
        if msgType == CLIENT_LOGIN_RESP:
            self.handleLoginResponseMsg(di)
        elif msgType == CLIENT_LOGIN_2_RESP:
            self.handleLogin2ResponseMsg(di)
        elif msgType == CLIENT_SERVER_UP:
            self._ToontownClientRepository__handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self._ToontownClientRepository__handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def handleLoginResponseMsg(self, di):
        returnCode = di.getInt8()
        self.notify.info('Login response return code: ' + str(returnCode))
        if returnCode == 0:
            if launcher:
                self.notify.info('Setting user name to unknown and chat to 1')
                launcher.setGoUserName('Unknown')
                launcher.setChatPermission(1)
            
            accountCode = di.getUint32()
            commentString = di.getString()
            if wantTimestamps:
                sec = di.getUint32()
                usec = di.getUint32()
                initClockDelta(sec, usec)
            
            self.loginFSM.request('waitForShardList')
        else:
            accountCode = di.getUint32()
            errorString = di.getString()
            self.notify.warning(errorString)
            self.loginFSM.request('reject')
        return None

    
    def handleLogin2ResponseMsg(self, di):
        returnCode = di.getInt8()
        errorString = di.getString()
        self.notify.info('Login2 response return code: ' + str(returnCode))
        if returnCode == 0:
            goUserName = di.getString()
            self.notify.info('Login2 goUserName: ' + str(goUserName))
            if launcher:
                launcher.setGoUserName(goUserName)
            
            chatCode = di.getUint8()
            self.notify.info('Login2 chatCode: ' + str(chatCode))
            if launcher:
                launcher.setChatPermission(not chatCode)
            
            if wantTimestamps:
                sec = di.getUint32()
                usec = di.getUint32()
                initClockDelta(sec, usec)
            
            self.loginFSM.request('waitForShardList')
        else:
            self.notify.warning(errorString)
            self.loginFSM.request('reject')
        return None

    
    def enterWaitForShardList(self):
        self.handler = self.handleWaitForGetShardListResponse
        self.sendGetShardListMsg()
        return None

    
    def sendGetShardListMsg(self):
        datagram = Datagram()
        datagram.addUint16(CLIENT_GET_SHARD_LIST)
        self.send(datagram)
        return None

    
    def exitWaitForShardList(self):
        self.handler = None
        return None

    
    def handleWaitForGetShardListResponse(self, msgType, di):
        if msgType == CLIENT_GET_SHARD_LIST_RESP:
            self.handleGetShardListResponseMsg(di)
        elif msgType == CLIENT_SERVER_UP:
            self._ToontownClientRepository__handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self._ToontownClientRepository__handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def handleGetShardListResponseMsg(self, di):
        numberOfShards = di.getUint16()
        shardList = []
        if numberOfShards == 0:
            self.loginFSM.request('noShards')
        else:
            for i in range(numberOfShards):
                shardId = di.getUint32()
                shardName = di.getString()
                shardPop = di.getUint32()
                potShard = PotentialShard.PotentialShard(shardId, shardName, shardPop)
                shardList.append(potShard)
                potShard.available = 1
                self._ToontownClientRepository__shards[shardId] = potShard
            
            self.loginFSM.request('waitForAvatarList')
        return None

    
    def enterNoShards(self):
        self.handler = self.handleNoShards
        self.noShardsBox = DialogBox.DialogBox(message = 'No Toontown Districts are available. Try again?', doneEvent = 'noShardsAck', style = DialogBox.TwoChoice)
        self.noShardsBox.show()
        self.accept('noShardsAck', self._ToontownClientRepository__handleNoShardsAck)
        self.notify.warning('No shards are available.')
        return None

    
    def __handleNoShardsAck(self):
        doneStatus = self.noShardsBox.doneStatus
        print doneStatus
        if doneStatus == 'ok':
            self.loginFSM.request('waitForShardList')
        elif doneStatus == 'cancel':
            self.loginFSM.request('shutdown')
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))
        return None

    
    def handleNoShards(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def exitNoShards(self):
        self.handler = None
        self.ignore('noShardsAck')
        self.noShardsBox.cleanup()
        del self.noShardsBox
        return None

    
    def enterReject(self):
        self.handler = self.handleReject
        self.notify.warning('Connection Rejected')
        self.loginFSM.request('shutdown')
        return None

    
    def exitReject(self):
        self.handler = None
        return None

    
    def handleReject(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def enterNoConnection(self):
        self.handler = self.handleNoConnection
        self.stopHeartbeat()
        self.stopReaderPollTask()
        self.lostConnectionBox = DialogBox.DialogBox(doneEvent = 'lostConnectionOk', message = 'Lost Connection', style = DialogBox.Acknowledge)
        self.lostConnectionBox.show()
        self.accept('lostConnectionOk', self._ToontownClientRepository__handleLostConnectionOk)
        self.notify.warning('Lost connection to server. Notifying user.')
        return None

    
    def __handleLostConnectionOk(self):
        self.loginFSM.request('login', [
            self.serverName,
            self.serverPort])
        return None

    
    def handleNoConnection(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def exitNoConnection(self):
        self.handler = None
        self.ignore('lostConnectionOk')
        self.lostConnectionBox.cleanup()
        return None

    
    def enterWaitForAvatarList(self):
        self.handler = self.handleWaitForAvatarList
        self.sendGetAvatarsMsg()
        return None

    
    def sendGetAvatarsMsg(self):
        datagram = Datagram()
        datagram.addUint16(CLIENT_GET_AVATARS)
        self.send(datagram)
        return None

    
    def exitWaitForAvatarList(self):
        self.handler = None
        return None

    
    def handleWaitForAvatarList(self, msgType, di):
        if msgType == CLIENT_GET_AVATARS_RESP:
            self.handleGetAvatarsRespMsg(di)
        elif msgType == CLIENT_SERVER_UP:
            self._ToontownClientRepository__handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self._ToontownClientRepository__handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def handleGetAvatarsRespMsg(self, di):
        returnCode = di.getUint8()
        if returnCode == 0:
            avatarTotal = di.getUint16()
            avList = []
            for i in range(0, avatarTotal):
                avNum = di.getUint32()
                avName = di.getString()
                avDNA = di.getString()
                avPosition = di.getUint8()
                potAv = PotentialAvatar.PotentialAvatar(avNum, avName, avDNA, avPosition)
                avList.append(potAv)
            
            self.avList = avList
            self.loginFSM.request('chooseAvatar', [
                self.avList])
        else:
            self.notify.error('Bad avatar list return code: ' + str(returnCode))
            self.loginFSM.request('off')
        return None

    
    def enterChooseAvatar(self, avList):
        self.sendSetAvatarIdMsg(0)
        base.playMusic(self.music, looping = 1, volume = 0.9, interupt = None)
        self.handler = self.handleChooseAvatar
        self.avChoice = AvatarChooser.AvatarChooser(avList, self.loginFSM, 'avatarChooserDone')
        self.avChoice.load()
        self.avChoice.enter()
        self.accept('avatarChooserDone', self._ToontownClientRepository__handleAvatarChooserDone, [
            avList])
        return None

    
    def __handleAvatarChooserDone(self, avList, doneStatus):
        done = doneStatus['mode']
        index = self.avChoice.getChoice()
        for av in avList:
            if av.position == index:
                avatarChoice = av
            
        
        if done == 'chose':
            self.avChoice.exit()
            self.loginFSM.request('waitForSetAvatarResponse', [
                avatarChoice])
        elif done == 'create':
            self.avChoice.exit()
            self.loginFSM.request('createAvatar', [
                avList,
                index])
        elif done == 'delete':
            self.avChoice.exit()
            self.loginFSM.request('waitForDeleteAvatarResponse', [
                avatarChoice])
        
        return None

    
    def handleChooseAvatar(self, msgType, di):
        if msgType == CLIENT_SERVER_UP:
            self._ToontownClientRepository__handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self._ToontownClientRepository__handleServerDown(di)
        elif msgType == CLIENT_GET_STATE_RESP:
            pass
        else:
            self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def exitChooseAvatar(self):
        self.handler = None
        self.avChoice.exit()
        self.avChoice.unload()
        self.avChoice = None
        self.ignore('avatarChooserDone')
        return None

    
    def enterCreateAvatar(self, avList, index):
        base.stopMusic(self.music)
        base.unloadMusic(self.music)
        self.handler = self.handleCreateAvatar
        base.transitions.noFade()
        self.avCreate = MakeAToon.MakeAToon(self.loginFSM, 'makeAToonComplete')
        self.avCreate.load()
        self.avCreate.enter()
        self.accept('makeAToonComplete', self._ToontownClientRepository__handleMakeAToon, [
            avList,
            index])
        return None

    
    def __handleMakeAToon(self, avList, index):
        done = self.avCreate.getDoneStatus()
        avDNA = self.avCreate.getDNA()
        avName = self.avCreate.getName()
        avPosition = index
        if done == 'check':
            self.handler = self.handleWaitForCreateAvatarResponse
            self.sendCreateAvatarMsg(avDNA, avName, avPosition)
        elif done == 'cancel':
            self.avCreate.exit()
            self.loginFSM.request('chooseAvatar', [
                avList])
        else:
            self.avCreate.exit()
            self.loginFSM.request('chooseAvatar', [
                avList])
        return None

    
    def exitCreateAvatar(self):
        self.ignore('makeAToonComplete')
        self.avCreate.unload()
        self.avCreate = None
        self.handler = None
        return None

    
    def handleCreateAvatar(self, msgType, di):
        if msgType == CLIENT_SERVER_UP:
            self._ToontownClientRepository__handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self._ToontownClientRepository__handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def enterWaitForCreateAvatarResponse(self, avDNA, avName, avPosition):
        self.handler = self.handleWaitForCreateAvatarResponse
        self.sendCreateAvatarMsg(avDNA, avName, avPosition)
        return None

    
    def sendCreateAvatarMsg(self, avDNA, avName, avPosition):
        datagram = Datagram()
        datagram.addUint16(CLIENT_CREATE_AVATAR)
        datagram.addUint16(0)
        datagram.addString(avName)
        datagram.addString(avDNA)
        datagram.addUint8(avPosition)
        self.newName = avName
        self.newDNA = avDNA
        self.newPosition = avPosition
        self.send(datagram)
        return None

    
    def exitWaitForCreateAvatarResponse(self):
        self.handler = None
        return None

    
    def handleWaitForCreateAvatarResponse(self, msgType, di):
        if msgType == CLIENT_CREATE_AVATAR_RESP:
            self.handleCreateAvatarResponseMsg(di)
        elif msgType == CLIENT_SERVER_UP:
            self._ToontownClientRepository__handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self._ToontownClientRepository__handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def handleCreateAvatarResponseMsg(self, di):
        echoContext = di.getUint16()
        returnCode = di.getUint8()
        if returnCode == 0:
            self.notify.debug('name accepted')
            self.avCreate.acceptName()
            self.avId = di.getUint32()
            newPotAv = PotentialAvatar.PotentialAvatar(self.avId, self.newName, self.newDNA, self.newPosition)
            self.avList.append(newPotAv)
        else:
            self.notify.debug('name rejected')
            self.handler = self.handleCreateAvatar
            self.avCreate.rejectName()
        return None

    
    def enterWaitForDeleteAvatarResponse(self, potAv):
        self.handler = self.handleWaitForDeleteAvatarResponse
        self.sendDeleteAvatarMsg(potAv.id)
        return None

    
    def sendDeleteAvatarMsg(self, avId):
        datagram = Datagram()
        datagram.addUint16(CLIENT_DELETE_AVATAR)
        datagram.addUint32(avId)
        self.send(datagram)
        return None

    
    def exitWaitForDeleteAvatarResponse(self):
        self.handler = None
        return None

    
    def handleWaitForDeleteAvatarResponse(self, msgType, di):
        if msgType == CLIENT_DELETE_AVATAR_RESP:
            self.handleGetAvatarsRespMsg(di)
        elif msgType == CLIENT_SERVER_UP:
            self._ToontownClientRepository__handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self._ToontownClientRepository__handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def enterWaitForSetAvatarResponse(self, potAv):
        self.handler = self.handleWaitForSetAvatarResponse
        self.sendSetAvatarMsg(potAv)
        return None

    
    def sendSetAvatarIdMsg(self, avId):
        datagram = Datagram()
        datagram.addUint16(CLIENT_SET_AVATAR)
        datagram.addUint32(avId)
        self.send(datagram)
        return None

    
    def sendSetAvatarMsg(self, potAv):
        self.sendSetAvatarIdMsg(potAv.id)
        self.avData = potAv
        return None

    
    def handleWaitForSetAvatarResponse(self, msgType, di):
        if msgType == CLIENT_GET_AVATAR_DETAILS_RESP:
            self.handleAvatarResponseMsg(di)
        elif msgType == CLIENT_GET_FRIEND_LIST_RESP:
            self._ToontownClientRepository__handleGetFriendsList(di)
        elif msgType == CLIENT_FRIEND_ONLINE:
            self._ToontownClientRepository__handleFriendOnline(di)
        elif msgType == CLIENT_FRIEND_OFFLINE:
            self._ToontownClientRepository__handleFriendOffline(di)
        elif msgType == CLIENT_SERVER_UP:
            self._ToontownClientRepository__handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self._ToontownClientRepository__handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def handleAvatarResponseMsg(self, di):
        avatarId = di.getUint32()
        returnCode = di.getUint8()
        if returnCode == 0:
            if self.notify.getDebug():
                self.notify.debug('name2cdc: ' + str(self.name2cdc))
            
            cdc = self.name2cdc['DistributedToon']
            loader.beginBulkLoad('localToonPlayGame', 79)
            localToon = LocalToon.LocalToon(self)
            toonbase.localToon = localToon
            NametagGlobals.setToonNode(toonbase.localToon.node())
            localToon.updateAllRequiredFields(cdc, di)
            localToon.doId = avatarId
            self.doId2do[avatarId] = localToon
            self.doId2cdc[avatarId] = cdc
            localToon.generate()
            self._ToontownClientRepository__sendGetFriendsListRequest()
            self.gameFSM.request('waitOnEnterResponses', [
                localToon.defaultShard,
                localToon.defaultZone,
                localToon.defaultZone,
                -1])
        else:
            self.notify.error('Gee, bad avatar.')
        return None

    
    def exitWaitForSetAvatarResponse(self):
        self.handler = None
        if hasattr(toonbase, 'localToon'):
            camera.reparentTo(render)
            camera.setPos(0, 0, 0)
            camera.setHpr(0, 0, 0)
            del self.doId2do[toonbase.localToon.getDoId()]
            del self.doId2cdc[toonbase.localToon.getDoId()]
            toonbase.localToon.disable()
            toonbase.localToon.delete()
            NametagGlobals.setToonNode(base.camNode)
            del toonbase.localToon
        
        for task in taskMgr.taskList:
            if task.name in [
                'dataloop',
                'eventManager',
                'readerPollTask',
                'heartBeat',
                'igloop',
                'downloadSequence',
                'patchAndHash',
                'launcher-download',
                'launcher-download-multifile',
                'launcher-decompressFile',
                'launcher-decompressMultifile',
                'launcher-extract',
                'launcher-patch',
                'tkloop',
                'manager-update',
                'downloadStallTask']:
                pass
            1
            print taskMgr
            self.notify.error("You can't leave toontown until you clean up your tasks.")
        
        for hook in messenger.dict.keys():
            if hook in [
                'f9-up',
                'launcherAllPhasesComplete',
                'launcherPercentPhaseComplete',
                'phaseComplete-3',
                'page_down',
                'page_up',
                'PandaPaused',
                'PandaRestarted']:
                pass
            1
            print messenger
            self.notify.error("You can't leave toontown until you clean up your hooks.")
        
        return None

    
    def enterGameOff(self):
        self.handler = self.handleGameOff
        return None

    
    def exitGameOff(self):
        self.handler = None
        return None

    
    def handleGameOff(self, msgType, di):
        self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def enterWaitOnEnterResponses(self, shardId, hoodId, zoneId, avId):
        self.handler = self.handleWaitOnEnterResponses
        self.handlerArgs = {
            'hoodId': hoodId,
            'zoneId': zoneId,
            'avId': avId }
        self.sendSetShardMsg(shardId)
        return None

    
    def handleWaitOnEnterResponses(self, msgType, di):
        if msgType == CLIENT_GET_STATE_RESP:
            self.handleSetShardResponse(di)
        elif msgType == CLIENT_GET_FRIEND_LIST_RESP:
            self._ToontownClientRepository__handleGetFriendsList(di)
        elif msgType == CLIENT_FRIEND_ONLINE:
            self._ToontownClientRepository__handleFriendOnline(di)
        elif msgType == CLIENT_FRIEND_OFFLINE:
            self._ToontownClientRepository__handleFriendOffline(di)
        elif msgType == CLIENT_SERVER_UP:
            self._ToontownClientRepository__handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self._ToontownClientRepository__handleServerDown(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def handleSetShardResponse(self, di):
        hoodId = self.handlerArgs['hoodId']
        zoneId = self.handlerArgs['zoneId']
        avId = self.handlerArgs['avId']
        if toonbase.localToon.tutorialAck:
            if base.config.GetBool('force-tutorial', 0):
                self.gameFSM.request('waitForTutorial', [
                    hoodId,
                    zoneId,
                    avId])
            else:
                self.gameFSM.request('playGame', [
                    hoodId,
                    zoneId,
                    avId])
        else:
            self.gameFSM.request('waitForTutorial', [
                hoodId,
                zoneId,
                avId])
        return None

    
    def exitWaitOnEnterResponses(self):
        self.handler = None
        self.handlerArgs = None
        return None

    
    def enterWaitForTutorial(self, hoodId, zoneId, avId):
        self.handler = self.handleWaitForTutorial
        self.handlerArgs = {
            'hoodId': hoodId,
            'zoneId': zoneId,
            'avId': avId }
        self.sendSetZoneMsg(QuietZone)
        return None

    
    def handleWaitForTutorial(self, msgType, di):
        if msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            self.handleGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            self.handleGenerateWithRequiredOther(di)
        elif msgType == CLIENT_OBJECT_UPDATE_FIELD:
            self.handleUpdateField(di)
        elif msgType == CLIENT_OBJECT_DISABLE_RESP:
            self.handleDisable(di)
        elif msgType == CLIENT_OBJECT_DELETE_RESP:
            self.handleDelete(di)
        elif msgType == CLIENT_GET_FRIEND_LIST_RESP:
            self._ToontownClientRepository__handleGetFriendsList(di)
        elif msgType == CLIENT_FRIEND_ONLINE:
            self._ToontownClientRepository__handleFriendOnline(di)
        elif msgType == CLIENT_FRIEND_OFFLINE:
            self._ToontownClientRepository__handleFriendOffline(di)
        elif msgType == CLIENT_GET_AVATAR_DETAILS_RESP:
            self._ToontownClientRepository__handleGetAvatarDetailsResp(di)
        elif msgType == CLIENT_SERVER_UP:
            self._ToontownClientRepository__handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self._ToontownClientRepository__handleServerDown(di)
        elif msgType == CLIENT_GET_STATE_RESP:
            pass
        elif msgType == CLIENT_DONE_SET_ZONE_RESP:
            self.handleTmGenerate()
        else:
            self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def handleTmGenerate(self):
        hoodId = self.handlerArgs['hoodId']
        zoneId = self.handlerArgs['zoneId']
        avId = self.handlerArgs['avId']
        self.gameFSM.request('tutorialQuestion', [
            hoodId,
            zoneId,
            avId])
        return None

    
    def exitWaitForTutorial(self):
        self.handler = None
        self.handlerArgs = None
        self.ignore('tmGenerate')
        return None

    
    def enterTutorialQuestion(self, hoodId, zoneId, avId):
        self.handler = self.handleTutorialQuestion
        self.handlerArgs = {
            'hoodId': hoodId,
            'zoneId': zoneId,
            'avId': avId }
        doneEvent = 'tutorialQuestionAck'
        self.tutorialQuestionBox = DialogBox.DialogBox(message = toonbase.localToon.getName() + ' is new to Toontown.\n\n Would you' + ' like Mickey to show you around?', doneEvent = doneEvent, style = DialogBox.TwoChoice, okButtonText = 'Yes', cancelButtonText = 'No')
        self.tutorialQuestionBox.show()
        if toonbase.loader.gui:
            toonbase.loader.gui.hide()
        
        self.acceptOnce(doneEvent, self._ToontownClientRepository__handleTutorialQuestionAck)
        return None

    
    def handleTutorialQuestion(self, msgType, di):
        if msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            self.handleGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            self.handleGenerateWithRequiredOther(di)
        elif msgType == CLIENT_OBJECT_UPDATE_FIELD:
            self.handleUpdateField(di)
        elif msgType == CLIENT_OBJECT_DISABLE_RESP:
            self.handleDisable(di)
        elif msgType == CLIENT_OBJECT_DELETE_RESP:
            self.handleDelete(di)
        elif msgType == CLIENT_GET_FRIEND_LIST_RESP:
            self._ToontownClientRepository__handleGetFriendsList(di)
        elif msgType == CLIENT_FRIEND_ONLINE:
            self._ToontownClientRepository__handleFriendOnline(di)
        elif msgType == CLIENT_FRIEND_OFFLINE:
            self._ToontownClientRepository__handleFriendOffline(di)
        elif msgType == CLIENT_GET_AVATAR_DETAILS_RESP:
            self._ToontownClientRepository__handleGetAvatarDetailsResp(di)
        elif msgType == CLIENT_SERVER_UP:
            self._ToontownClientRepository__handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self._ToontownClientRepository__handleServerDown(di)
        elif msgType == CLIENT_GET_STATE_RESP:
            pass
        elif msgType == CLIENT_DONE_SET_ZONE_RESP:
            pass
        else:
            self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def __handleTutorialQuestionAck(self):
        doneStatus = self.tutorialQuestionBox.doneStatus
        hoodId = self.handlerArgs['hoodId']
        zoneId = self.handlerArgs['zoneId']
        avId = self.handlerArgs['avId']
        if doneStatus == 'ok':
            self.acceptOnce('startTutorial', self._ToontownClientRepository__handleStartTutorial, [
                avId])
            messenger.send('requestTutorial')
        elif doneStatus == 'cancel':
            messenger.send('rejectTutorial')
            self.gameFSM.request('playGame', [
                hoodId,
                zoneId,
                avId])
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))
        return None

    
    def __handleStartTutorial(self, avId, zoneId):
        self.gameFSM.request('playGame', [
            Tutorial,
            zoneId,
            avId])
        return None

    
    def exitTutorialQuestion(self):
        self.handler = None
        self.handlerArgs = None
        self.tutorialQuestionBox.cleanup()
        del self.tutorialQuestionBox
        self.ignore('tutorialQuestionAck')
        self.ignore('startTutorial')
        if toonbase.loader.gui:
            toonbase.loader.gui.show()
        
        return None

    
    def enterPlayGame(self, hoodId, zoneId, avId):
        base.stopMusic(self.music)
        base.unloadMusic(self.music)
        self.music = None
        self.handler = self.handlePlayGame
        self.accept('donePlayingGame', self.exitPlayGame)
        base.transitions.noFade()
        self.playGame.load()
        loader.endBulkLoad('localToonPlayGame')
        self.playGame.enter(hoodId, zoneId, avId)
        return None

    
    def exitPlayGame(self):
        self.handler = None
        self.playGame.exit()
        self.playGame.unload()
        self.disableAllBetweenShards()
        self.ignore('donePlayingGame')
        return None

    
    def handlePlayGame(self, msgType, di):
        if self.notify.getDebug():
            self.notify.debug('handle play game got message type: ' + `msgType`)
        
        if msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            self.handleGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            self.handleGenerateWithRequiredOther(di)
        elif msgType == CLIENT_OBJECT_UPDATE_FIELD:
            self.handleUpdateField(di)
        elif msgType == CLIENT_OBJECT_DISABLE_RESP:
            self.handleDisable(di)
        elif msgType == CLIENT_OBJECT_DELETE_RESP:
            self.handleDelete(di)
        elif msgType == CLIENT_GET_FRIEND_LIST_RESP:
            self._ToontownClientRepository__handleGetFriendsList(di)
        elif msgType == CLIENT_FRIEND_ONLINE:
            self._ToontownClientRepository__handleFriendOnline(di)
        elif msgType == CLIENT_FRIEND_OFFLINE:
            self._ToontownClientRepository__handleFriendOffline(di)
        elif msgType == CLIENT_GET_AVATAR_DETAILS_RESP:
            self._ToontownClientRepository__handleGetAvatarDetailsResp(di)
        elif msgType == CLIENT_SERVER_UP:
            self._ToontownClientRepository__handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self._ToontownClientRepository__handleServerDown(di)
        elif msgType == CLIENT_GET_STATE_RESP:
            pass
        elif msgType == CLIENT_DONE_SET_ZONE_RESP:
            pass
        else:
            self.handleUnexpectedMsgType(msgType, di)
        return None

    
    def sendQuietZoneRequest(self):
        self.disableAll()
        datagram = Datagram()
        datagram.addUint16(CLIENT_SET_ZONE)
        datagram.addUint16(QuietZone)
        self.send(datagram)
        return None

    
    def disableAll(self):
        distObjs = self.doId2do.values()
        for distObj in distObjs:
            if distObj.neverDisable:
                pass
            1
            self.disableDoId(distObj.doId)
        

    
    def disableAllBetweenShards(self):
        distObjs = self.doId2do.values()
        for distObj in distObjs:
            if distObj.doId == toonbase.localToon.doId:
                pass
            1
            self.disableDoId(distObj.doId)
        

    
    def fillUpFriendsMap(self):
        if self.isFriendsMapComplete():
            return 1
        
        if not (self.friendsMapPending):
            self.notify.warning('Friends list stale; fetching new list.')
            self._ToontownClientRepository__sendGetFriendsListRequest()
        
        return 0

    
    def isFriend(self, doId):
        if doId in toonbase.localToon.friendsList:
            self.identifyFriend(doId)
            return 1
        
        return 0

    
    def isFriendOnline(self, doId):
        return self.friendsOnline.has_key(doId)

    
    def identifyFriend(self, doId):
        if self.friendsMap.has_key(doId):
            return self.friendsMap[doId]
        
        avatar = None
        if self.doId2do.has_key(doId):
            avatar = self.doId2do[doId]
        elif self.cache.contains(doId):
            avatar = self.cache.dict[doId]
        else:
            self.notify.warning("Don't know who friend %d is." % doId)
            return None
        handle = FriendHandle.FriendHandle(doId, avatar.getName(), avatar.style)
        self.friendsMap[doId] = handle
        return handle

    
    def isFriendsMapComplete(self):
        for friendId in toonbase.localToon.friendsList:
            if self.identifyFriend(friendId) == None:
                return 0
            
        
        return 1

    
    def removeFriend(self, avatarId):
        datagram = Datagram()
        datagram.addUint16(CLIENT_REMOVE_FRIEND)
        datagram.addUint32(avatarId)
        self.send(datagram)
        
        try:
            toonbase.localToon.friendsList.remove(avatarId)
        except:
            pass


    
    def __sendGetFriendsListRequest(self):
        self.friendsMapPending = 1
        datagram = Datagram()
        datagram.addUint16(CLIENT_GET_FRIEND_LIST)
        self.send(datagram)
        return None

    
    def __handleGetFriendsList(self, di):
        error = di.getUint8()
        if error:
            self.notify.warning('Got error return from friends list.')
        else:
            count = di.getUint16()
            for i in range(0, count):
                doId = di.getUint32()
                name = di.getString()
                dnaString = di.getString()
                dna = AvatarDNA.AvatarDNA()
                dna.makeFromNetString(dnaString)
                handle = FriendHandle.FriendHandle(doId, name, dna)
                self.friendsMap[doId] = handle
                if self.friendsOnline.has_key(doId):
                    self.friendsOnline[doId] = handle
                
            
        self.friendsMapPending = 0
        messenger.send('friendsMapComplete')

    
    def __handleFriendOnline(self, di):
        doId = di.getUint32()
        self.notify.debug('Friend %d now online.' % doId)
        if not self.friendsOnline.has_key(doId):
            self.friendsOnline[doId] = self.identifyFriend(doId)
            messenger.send('friendOnline', [
                doId])
        

    
    def __handleFriendOffline(self, di):
        doId = di.getUint32()
        self.notify.debug('Friend %d now offline.' % doId)
        
        try:
            del self.friendsOnline[doId]
            messenger.send('friendOffline', [
                doId])
        except:
            pass


    
    def getAvatarDetails(self, avatar, func, *args):
        task = Task.Task(func)
        task.args = args
        task.avatar = avatar
        avId = avatar.doId
        self._ToontownClientRepository__queryAvatarMap[avId] = task
        self._ToontownClientRepository__sendGetAvatarDetails(avId)

    
    def __sendGetAvatarDetails(self, avId):
        datagram = Datagram()
        datagram.addUint16(CLIENT_GET_AVATAR_DETAILS)
        datagram.addUint32(avId)
        self.send(datagram)

    
    def __handleGetAvatarDetailsResp(self, di):
        avId = di.getUint32()
        returnCode = di.getUint8()
        self.notify.info('Got query response for avatar %d, code = %d.' % (avId, returnCode))
        
        try:
            task = self._ToontownClientRepository__queryAvatarMap[avId]
        except:
            self.notify.warning('Received unexpected details for avatar %d.' % avId)
            return None

        del self._ToontownClientRepository__queryAvatarMap[avId]
        gotData = 0
        if returnCode != 0:
            self.notify.warning('No information available for avatar %d.' % avId)
        else:
            cdc = self.name2cdc['DistributedToon']
            task.avatar.updateAllRequiredFields(cdc, di)
            gotData = 1
        if isinstance(task.__call__, types.StringType):
            messenger.send(task.__call__, list((gotData, task.avatar) + task.args))
        else:
            apply(task.__call__, (gotData, task.avatar) + task.args)

    
    def getShardName(self, shardId):
        
        try:
            return self._ToontownClientRepository__shards[shardId].name
        except:
            return None


    
    def isShardAvailable(self, shardId):
        
        try:
            return self._ToontownClientRepository__shards[shardId].available
        except:
            return 0


    
    def listAvailableShards(self):
        list = []
        for s in self._ToontownClientRepository__shards.values():
            if s.available:
                list.append((s.id, s.name))
            
        
        return list

    
    def __handleServerUp(self, di):
        shardId = di.getUint32()
        shardName = di.getString()
        potShard = PotentialShard.PotentialShard(shardId, shardName, 0)
        potShard.available = 1
        self._ToontownClientRepository__shards[shardId] = potShard
        self.notify.info('%s is now available.' % shardName)

    
    def __handleServerDown(self, di):
        shardId = di.getUint32()
        
        try:
            potShard = self._ToontownClientRepository__shards[shardId]
            potShard.available = 0
            self.notify.info('%s is no longer available.' % potShard.name)
        except:
            self.notify.info('Unknown shard %d is no longer available.' % shardId)


    
    def handleDatagram(self, datagram):
        di = DatagramIterator(datagram)
        msgType = di.getUint16()
        if self.notify.getDebug():
            self.notify.debug('handleDatagram: msgType: ' + `msgType`)
        
        self.handler(msgType, di)
        return None

    
    def findRawString(self, matchList, callback):
        self.currentRawString = ''
        self.rawStringMatchList = matchList
        self.rawStringCallback = callback

    
    def handleRawString(self, str):
        self.notify.info('handleRawString: str = <%s>' % str)
        self.currentRawString += str
        self.notify.info('currentRawString = <%s>' % self.currentRawString)
        for matchString in self.rawStringMatchList:
            if self.currentRawString.find(matchString) >= 0:
                self.rawStringCallback()
                return None
            
        

    
    def sendHeartbeat(self):
        datagram = Datagram()
        datagram.addUint16(CLIENT_HEARTBEAT)
        self.send(datagram)
        return None

    
    def stopHeartbeat(self):
        taskMgr.removeTasksNamed('heartBeat')
        return None

    
    def startHeartbeat(self):
        self.stopHeartbeat()
        newTask = Task.loop(Task.pause(10), Task.Task(self.sendHeartbeatTask))
        taskMgr.spawnTaskNamed(newTask, 'heartBeat')
        return None

    
    def sendHeartbeatTask(self, task):
        self.sendHeartbeat()
        return Task.done


