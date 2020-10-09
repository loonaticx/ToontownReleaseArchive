# Source Generated with Decompyle++
# File: NPCToons.pyo (Python 2.0)

import ToontownGlobals
import whrandom
NPCToonDict = {
    2100: ('Questbot 1', ('dll', 'md', 'l', 3, 3, 3, 3, 22, 22, 30), 20, 20, ToontownGlobals.ToontownCentral, 'render', (152, 42, 7.24, 150, 0, 0), 'neutral'),
    2101: ('Questbot 2', ('cll', 'md', 'l', 4, 4, 4, 4, 22, 22, 30), 15, 15, ToontownGlobals.ToontownCentral, 'render', (122, 58, 6.692, -178, 0, 0), 'neutral'),
    2102: ('Questbot 3', ('cll', 'md', 's', 4, 4, 4, 4, 22, 22, 30), 15, 15, ToontownGlobals.ToontownCentral, 'render', (80, -113, 6.692, -11, 0, 0), 'neutral') }

def getNPCName(npcId):
    npc = NPCToonDict.get(npcId)
    if npc:
        return npc[0]
    else:
        return None


def getNPCInSameHood(npcId):
    hoodId = npcId - npcId % 1000
    otherNPCs = []
    for otherNPCId in NPCToonDict.keys():
        zone = otherNPCId - otherNPCId % 1000
        if zone == hoodId and npcId != otherNPCId:
            otherNPCs.append(otherNPCId)
        
    
    if otherNPCs:
        return whrandom.choice(otherNPCs)
    else:
        return None

