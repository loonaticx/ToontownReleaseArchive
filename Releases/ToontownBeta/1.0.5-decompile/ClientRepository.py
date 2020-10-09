# Source Generated with Decompyle++
# File: ClientRepository.pyo (Python 2.0)

from PandaModules import *
from TaskManagerGlobal import *
from MsgTypes import *
from ShowBaseGlobal import *
import Task
import DirectNotifyGlobal
import ClientDistClass
import CRCache
import Datagram
import DirectObject

class ClientRepository(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('ClientRepository')
    
    def __init__(self, dcFileName):
        self.number2cdc = { }
        self.name2cdc = { }
        self.doId2do = { }
        self.doId2cdc = { }
        self.parseDcFile(dcFileName)
        self.cache = CRCache.CRCache()
        return None

    
    def parseDcFile(self, dcFileName):
        self.dcFile = DCFile()
        fname = Filename(dcFileName)
        readResult = self.dcFile.read(fname)
        if not readResult:
            self.notify.error('Could not read dcfile: ' + dcFileName)
        
        self.hashVal = self.dcFile.getHash()
        return self.parseDcClasses(self.dcFile)

    
    def parseDcClasses(self, dcFile):
        numClasses = dcFile.getNumClasses()
        for i in range(0, numClasses):
            dcClass = dcFile.getClass(i)
            clientDistClass = ClientDistClass.ClientDistClass(dcClass)
            self.number2cdc[dcClass.getNumber()] = clientDistClass
            self.name2cdc[dcClass.getName()] = clientDistClass
        
        return None

    
    def connect(self, serverName, serverPort):
        self.qcm = QueuedConnectionManager()
        gameServerTimeoutMs = base.config.GetInt('game-server-timeout-ms', 20000)
        self.tcpConn = self.qcm.openTCPClientConnection(serverName, serverPort, gameServerTimeoutMs)
        if self.tcpConn == None:
            return None
        else:
            self.tcpConn.setNoDelay(1)
            self.qcr = QueuedConnectionReader(self.qcm, 0)
            self.qcr.addConnection(self.tcpConn)
            self.cw = ConnectionWriter(self.qcm, 0)
            self.startReaderPollTask()
            return self.tcpConn

    
    def startRawReaderPollTask(self):
        self.stopRawReaderPollTask()
        self.stopReaderPollTask()
        task = Task.Task(self.rawReaderPollUntilEmpty)
        task.currentRawString = ''
        taskMgr.spawnTaskNamed(task, 'rawReaderPollTask')
        return None

    
    def stopRawReaderPollTask(self):
        taskMgr.removeTasksNamed('rawReaderPollTask')
        return None

    
    def rawReaderPollUntilEmpty(self, task):
        while self.rawReaderPollOnce():
            pass
        return Task.cont

    
    def rawReaderPollOnce(self):
        self.notify.debug('rawReaderPollOnce')
        self.ensureValidConnection()
        availGetVal = self.qcr.dataAvailable()
        if availGetVal:
            datagram = NetDatagram()
            readRetVal = self.qcr.getData(datagram)
            if readRetVal:
                str = datagram.getMessage()
                self.notify.debug('rawReaderPollOnce: found str: ' + str)
                self.handleRawString(str)
            else:
                ClientRepository.notify.warning('getData returned false')
        
        return availGetVal

    
    def handleRawString(self, str):
        pass

    
    def startReaderPollTask(self):
        self.stopRawReaderPollTask()
        self.stopReaderPollTask()
        task = Task.Task(self.readerPollUntilEmpty)
        taskMgr.spawnTaskNamed(task, 'readerPollTask')
        return None

    
    def stopReaderPollTask(self):
        taskMgr.removeTasksNamed('readerPollTask')
        return None

    
    def readerPollUntilEmpty(self, task):
        while self.readerPollOnce():
            pass
        return Task.cont

    
    def readerPollOnce(self):
        self.ensureValidConnection()
        availGetVal = self.qcr.dataAvailable()
        if availGetVal:
            datagram = NetDatagram()
            readRetVal = self.qcr.getData(datagram)
            if readRetVal:
                self.handleDatagram(datagram)
            else:
                ClientRepository.notify.warning('getData returned false')
        
        return availGetVal

    
    def ensureValidConnection(self):
        if self.qcm.resetConnectionAvailable():
            resetConnectionPointer = PointerToConnection()
            if self.qcm.getResetConnection(resetConnectionPointer):
                self.loginFSM.request('noConnection')
            
        
        return None

    
    def handleDatagram(self, datagram):
        pass

    
    def handleGenerateWithRequired(self, di):
        classId = di.getArg(STUint16)
        doId = di.getArg(STUint32)
        cdc = self.number2cdc[classId]
        distObj = self.generateWithRequiredFields(cdc, doId, di)
        return None

    
    def handleGenerateWithRequiredOther(self, di):
        classId = di.getArg(STUint16)
        doId = di.getArg(STUint32)
        cdc = self.number2cdc[classId]
        distObj = self.generateWithRequiredOtherFields(cdc, doId, di)
        return None

    
    def generateWithRequiredFields(self, cdc, doId, di):
        if self.doId2do.has_key(doId):
            distObj = self.doId2do[doId]
            distObj.generate()
            distObj.updateRequiredFields(cdc, di)
            distObj.announceGenerate()
        elif self.cache.contains(doId):
            distObj = self.cache.retrieve(doId)
            self.doId2do[doId] = distObj
            self.doId2cdc[doId] = cdc
            distObj.generate()
            distObj.updateRequiredFields(cdc, di)
            distObj.announceGenerate()
        else:
            distObj = cdc.constructor(self)
            distObj.doId = doId
            self.doId2do[doId] = distObj
            self.doId2cdc[doId] = cdc
            distObj.generateInit()
            distObj.generate()
            distObj.updateRequiredFields(cdc, di)
            distObj.announceGenerate()
        return distObj

    
    def generateWithRequiredOtherFields(self, cdc, doId, di):
        if self.doId2do.has_key(doId):
            distObj = self.doId2do[doId]
            distObj.generate()
            distObj.updateRequiredOtherFields(cdc, di)
            distObj.announceGenerate()
        elif self.cache.contains(doId):
            distObj = self.cache.retrieve(doId)
            self.doId2do[doId] = distObj
            self.doId2cdc[doId] = cdc
            distObj.generate()
            distObj.updateRequiredOtherFields(cdc, di)
            distObj.announceGenerate()
        else:
            distObj = cdc.constructor(self)
            distObj.doId = doId
            self.doId2do[doId] = distObj
            self.doId2cdc[doId] = cdc
            distObj.generateInit()
            distObj.generate()
            distObj.updateRequiredOtherFields(cdc, di)
            distObj.announceGenerate()
        return distObj

    
    def handleDisable(self, di):
        doId = di.getArg(STUint32)
        self.disableDoId(doId)
        return None

    
    def disableDoId(self, doId):
        if self.doId2do.has_key(doId):
            distObj = self.doId2do[doId]
            del self.doId2do[doId]
            del self.doId2cdc[doId]
            if distObj.getCacheable():
                self.cache.cache(distObj)
            else:
                distObj.deleteOrDelay()
        else:
            ClientRepository.notify.warning('Disable failed. DistObj ' + str(doId) + ' is not in dictionary')
        return None

    
    def handleDelete(self, di):
        doId = di.getArg(STUint32)
        if self.doId2do.has_key(doId):
            obj = self.doId2do[doId]
            del self.doId2do[doId]
            del self.doId2cdc[doId]
            obj.deleteOrDelay()
        elif self.cache.contains(doId):
            self.cache.delete(doId)
        else:
            ClientRepository.notify.warning('Asked to delete non-existent DistObj ' + str(doId))
        return None

    
    def handleUpdateField(self, di):
        doId = di.getArg(STUint32)
        do = self.doId2do.get(doId)
        cdc = self.doId2cdc.get(doId)
        if do != None and cdc != None:
            cdc.updateField(do, di)
        else:
            ClientRepository.notify.warning('Asked to update non-existent DistObj ' + str(doId))
        return None

    
    def handleUnexpectedMsgType(self, msgType, di):
        currentLoginState = self.loginFSM.getCurrentState()
        if currentLoginState:
            currentLoginStateName = currentLoginState.getName()
        else:
            currentLoginStateName = 'None'
        currentGameState = self.gameFSM.getCurrentState()
        if currentGameState:
            currentGameStateName = currentGameState.getName()
        else:
            currentGameStateName = 'None'
        ClientRepository.notify.warning('Ignoring unexpected message type: ' + str(msgType) + ' login state: ' + currentLoginStateName + ' game state: ' + currentGameStateName)
        return None

    
    def sendSetShardMsg(self, shardId):
        datagram = Datagram.Datagram()
        datagram.addUint16(CLIENT_SET_SHARD)
        datagram.addUint32(shardId)
        self.send(datagram)
        return None

    
    def sendSetZoneMsg(self, zoneId):
        datagram = Datagram.Datagram()
        datagram.addUint16(CLIENT_SET_ZONE)
        datagram.addUint16(zoneId)
        self.send(datagram)
        return None

    
    def sendUpdate(self, do, fieldName, args, sendToId = None):
        doId = do.doId
        cdc = self.doId2cdc[doId]
        cdc.sendUpdate(self, do, fieldName, args, sendToId)

    
    def send(self, datagram):
        self.cw.send(datagram, self.tcpConn)
        return None

    
    def replaceMethod(self, oldMethod, newFunction):
        foundIt = 0
        import new
        for cdc in self.number2cdc.values():
            for cdu in cdc.allCDU:
                method = cdu.func
                if method and method.im_func == oldMethod:
                    newMethod = new.instancemethod(newFunction, method.im_self, method.im_class)
                    cdu.func = newMethod
                    foundIt = 1
                
            
        
        return foundIt


