# Source Generated with Decompyle++
# File: libtoontownGlobals.pyo (Python 2.0)

import types
import libtoontown
import Node
import DNAStorage

def loadDNAFile(dnaStore, filename, cs, editing):
    returnValue = libtoontown._inPdt4yjYV1(dnaStore.this, filename, cs, editing)
    returnObject = Node.Node(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()


def loadDNAFileAI(dnaStore, filename, cs):
    returnValue = libtoontown._inPdt4yqGgU(dnaStore.this, filename, cs)
    return returnValue

HCCUT = 1
HCFREE = 2
HCG1 = 3
HCSMOOTH = 4
PCTHPR = 2
PCTNONE = 0
PCTT = 3
PCTXYZ = 1
TMALIGNCENTER = 3
TMALIGNLEFT = 1
TMALIGNRIGHT = 2
