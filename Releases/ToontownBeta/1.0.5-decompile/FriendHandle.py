# Source Generated with Decompyle++
# File: FriendHandle.pyo (Python 2.0)

from ToontownGlobals import *

class FriendHandle:
    
    def __init__(self, doId, name, style):
        self.doId = doId
        self.name = name
        self.style = style

    
    def getDoId(self):
        return self.doId

    
    def getName(self):
        return self.name

    
    def getFont(self):
        return getToonFont()

    
    def uniqueName(self, idString):
        return idString + '-' + str(self.getDoId())

    
    def d_setWhisper(self, chatString):
        toonbase.localToon.sendUpdate('setWhisper', [
            chatString], sendToId = self.doId)

    
    def d_teleportQuery(self, requesterId):
        toonbase.localToon.sendUpdate('teleportQuery', [
            requesterId], sendToId = self.doId)

    
    def d_teleportResponse(self, avId, available, shardId, hoodId, zoneId):
        toonbase.localToon.sendUpdate('teleportResponse', [
            avId,
            available,
            shardId,
            hoodId,
            zoneId], sendToId = self.doId)


