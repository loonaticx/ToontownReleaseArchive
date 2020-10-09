# Source Generated with Decompyle++
# File: DNAStorage.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import FFIExternalObject
import Texture
import NodePath
import DNASuitPoint
import Point3
import DNABattleCell
import DNASuitEdge
import NodeRelation
import DNAGroup
import PosHpr
import DNAVisGroup
import DNASuitPath
import Ostream
classDefined = 0

def generateClass_DNAStorage():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNAStorage(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libtoontown._inPdt4yuzFR()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4yUEE8:
                libtoontown._inPdt4yUEE8(self.this)
            

        
        def printNodeStorage(self):
            returnValue = libtoontown._inPdt4ynNxk(self.this)
            return returnValue

        
        def printTextureStorage(self):
            returnValue = libtoontown._inPdt4yk8Ya(self.this)
            return returnValue

        
        def printSuitPointStorage(self):
            returnValue = libtoontown._inPdt4y_FN_(self.this)
            return returnValue

        
        def printBattleCellStorage(self):
            returnValue = libtoontown._inPdt4ySh2Z(self.this)
            return returnValue

        
        def storeTexture(self, codeString, texture):
            returnValue = libtoontown._inPdt4y3XPk(self.this, codeString, texture.this)
            return returnValue

        
        def storeNode(self, codeString, node):
            returnValue = libtoontown._inPdt4y6Gl7(self.this, codeString, node.this)
            return returnValue

        
        def storeHoodNode(self, codeString, node):
            returnValue = libtoontown._inPdt4yIOuW(self.this, codeString, node.this)
            return returnValue

        
        def storePlaceNode(self, codeString, node):
            returnValue = libtoontown._inPdt4y4bg6(self.this, codeString, node.this)
            return returnValue

        
        def overloaded_storeSuitPoint_ptrDNAStorage___enum__DNASuitPointType_ptrLPoint3f(self, type, pos):
            returnValue = libtoontown._inPdt4yhPlA(self.this, type, pos.this)
            returnObject = DNASuitPoint.DNASuitPoint(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_storeSuitPoint_ptrDNAStorage_ptrDNASuitPoint(self, parameter1):
            returnValue = libtoontown._inPdt4y96Ar(self.this, parameter1.this)
            return returnValue

        
        def getHighestSuitPointIndex(self):
            returnValue = libtoontown._inPdt4ynKbV(self.this)
            return returnValue

        
        def removeSuitPoint(self, parameter1):
            returnValue = libtoontown._inPdt4yuuVm(self.this, parameter1.this)
            return returnValue

        
        def storeBlockNumber(self, block, zoneId):
            returnValue = libtoontown._inPdt4yYh3h(self.this, block, zoneId)
            return returnValue

        
        def storeBlockPosHpr(self, block, pos, hpr):
            returnValue = libtoontown._inPdt4y3liP(self.this, block, pos.this, hpr.this)
            return returnValue

        
        def storeBattleCell(self, parameter1):
            returnValue = libtoontown._inPdt4yG_Dh(self.this, parameter1.this)
            return returnValue

        
        def removeBattleCell(self, parameter1):
            returnValue = libtoontown._inPdt4yDBuo(self.this, parameter1.this)
            return returnValue

        
        def overloaded_storeSuitEdge_ptrDNAStorage_int_int_atomicstring(self, startIndex, endIndex, zoneId):
            returnValue = libtoontown._inPdt4yNqZ8(self.this, startIndex, endIndex, zoneId)
            returnObject = DNASuitEdge.DNASuitEdge(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_storeSuitEdge_ptrDNAStorage_ptrDNASuitEdge(self, parameter1):
            returnValue = libtoontown._inPdt4yOerq(self.this, parameter1.this)
            returnObject = DNASuitEdge.DNASuitEdge(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def removeSuitEdge(self, parameter1):
            returnValue = libtoontown._inPdt4ynwHb(self.this, parameter1.this)
            return returnValue

        
        def deleteUnusedSuitPoints(self):
            returnValue = libtoontown._inPdt4ysni7(self.this)
            return returnValue

        
        def fixCoincidentSuitPoints(self):
            returnValue = libtoontown._inPdt4ydzjO(self.this)
            return returnValue

        
        def resetNodes(self):
            returnValue = libtoontown._inPdt4yR44o(self.this)
            return returnValue

        
        def resetTextures(self):
            returnValue = libtoontown._inPdt4yUejQ(self.this)
            return returnValue

        
        def resetHood(self):
            returnValue = libtoontown._inPdt4yZo48(self.this)
            return returnValue

        
        def resetHoodNodes(self):
            returnValue = libtoontown._inPdt4yPGos(self.this)
            return returnValue

        
        def resetPlaceNodes(self):
            returnValue = libtoontown._inPdt4yncLk(self.this)
            return returnValue

        
        def resetSuitPoints(self):
            returnValue = libtoontown._inPdt4yU_05(self.this)
            return returnValue

        
        def resetBattleCells(self):
            returnValue = libtoontown._inPdt4yft1N(self.this)
            return returnValue

        
        def resetBlockNumbers(self):
            returnValue = libtoontown._inPdt4y3j6Q(self.this)
            return returnValue

        
        def resetBlockPosHprs(self):
            returnValue = libtoontown._inPdt4yju_J(self.this)
            return returnValue

        
        def findTexture(self, dnaString):
            returnValue = libtoontown._inPdt4yl6Ky(self.this, dnaString)
            returnObject = Texture.Texture(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def findNode(self, dnaString):
            returnValue = libtoontown._inPdt4ypVLg(self.this, dnaString)
            returnObject = NodePath.NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getNumCatalogCodes(self, catalogString):
            returnValue = libtoontown._inPdt4ytESV(self.this, catalogString)
            return returnValue

        
        def getCatalogCode(self, catalogString, i):
            returnValue = libtoontown._inPdt4yatPT(self.this, catalogString, i)
            return returnValue

        
        def storeCatalogString(self, catalogString, dnaString):
            returnValue = libtoontown._inPdt4ytXiu(self.this, catalogString, dnaString)
            return returnValue

        
        def printCatalog(self):
            returnValue = libtoontown._inPdt4yXzRO(self.this)
            return returnValue

        
        def storeDNAGroup(self, parameter1, parameter2):
            returnValue = libtoontown._inPdt4y3c_S(self.this, parameter1.this, parameter2.this)
            return returnValue

        
        def overloaded_removeDNAGroup_ptrDNAStorage_ptrNodeRelation(self, parameter1):
            returnValue = libtoontown._inPdt4yS0zN(self.this, parameter1.this)
            return returnValue

        
        def overloaded_removeDNAGroup_ptrDNAStorage_ptrDNAGroup(self, parameter1):
            returnValue = libtoontown._inPdt4yY6Ha(self.this, parameter1.this)
            return returnValue

        
        def findDNAGroup(self, parameter1):
            returnValue = libtoontown._inPdt4yvag3(self.this, parameter1.this)
            returnObject = DNAGroup.DNAGroup(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def findNodeRelation(self, parameter1):
            returnValue = libtoontown._inPdt4yJGHY(self.this, parameter1.this)
            returnObject = NodeRelation.NodeRelation(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getZoneFromBlockNumber(self, blockNumber):
            returnValue = libtoontown._inPdt4yw4C0(self.this, blockNumber)
            return returnValue

        
        def getBlockNumberAt(self, index):
            returnValue = libtoontown._inPdt4yPB30(self.this, index)
            return returnValue

        
        def getNumBlockNumbers(self):
            returnValue = libtoontown._inPdt4ytQbC(self.this)
            return returnValue

        
        def getPosHprFromBlockNumber(self, blockNumber):
            returnValue = libtoontown._inPdt4y2lEp(self.this, blockNumber)
            returnObject = PosHpr.PosHpr(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getPosHprBlockAt(self, index):
            returnValue = libtoontown._inPdt4ySPHU(self.this, index)
            return returnValue

        
        def getNumBlockPosHprs(self):
            returnValue = libtoontown._inPdt4yPlYW(self.this)
            return returnValue

        
        def resetDNAGroups(self):
            returnValue = libtoontown._inPdt4ySdEH(self.this)
            return returnValue

        
        def storeDNAVisGroup(self, parameter1, parameter2):
            returnValue = libtoontown._inPdt4ysjJX(self.this, parameter1.this, parameter2.this)
            return returnValue

        
        def removeDNAVisGroup(self, parameter1):
            returnValue = libtoontown._inPdt4yVKl8(self.this, parameter1.this)
            return returnValue

        
        def findDNAVisGroup(self, parameter1):
            returnValue = libtoontown._inPdt4yhiGw(self.this, parameter1.this)
            returnObject = DNAVisGroup.DNAVisGroup(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def resetDNAVisGroups(self):
            returnValue = libtoontown._inPdt4yYvv1(self.this)
            return returnValue

        
        def getNumDNAVisGroups(self):
            returnValue = libtoontown._inPdt4yotr_(self.this)
            return returnValue

        
        def getDNAVisGroup(self, i):
            returnValue = libtoontown._inPdt4y9mmU(self.this, i)
            returnObject = DNAVisGroup.DNAVisGroup(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getNumVisiblesInDNAVisGroup(self, i):
            returnValue = libtoontown._inPdt4ycpwk(self.this, i)
            return returnValue

        
        def getDNAVisGroupName(self, i):
            returnValue = libtoontown._inPdt4y9be3(self.this, i)
            return returnValue

        
        def getVisibleName(self, visgroupIndex, visibleIndex):
            returnValue = libtoontown._inPdt4yE_mc(self.this, visgroupIndex, visibleIndex)
            return returnValue

        
        def storeDNAVisGroupAI(self, parameter1):
            returnValue = libtoontown._inPdt4yn11T(self.this, parameter1.this)
            return returnValue

        
        def getNumDNAVisGroupsAI(self):
            returnValue = libtoontown._inPdt4yH5P2(self.this)
            return returnValue

        
        def getDNAVisGroupAI(self, i):
            returnValue = libtoontown._inPdt4yz_uo(self.this, i)
            returnObject = DNAVisGroup.DNAVisGroup(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def resetDNAVisGroupsAI(self):
            returnValue = libtoontown._inPdt4yL0G0(self.this)
            return returnValue

        
        def getNumNodeRelations(self):
            returnValue = libtoontown._inPdt4y0KsH(self.this)
            return returnValue

        
        def getNodeRelationAt(self, i):
            returnValue = libtoontown._inPdt4yWVKJ(self.this, i)
            returnObject = NodeRelation.NodeRelation(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def printNodeRelations(self):
            returnValue = libtoontown._inPdt4ycY3c(self.this)
            return returnValue

        
        def getSuitEdgeZone(self, startIndex, endIndex):
            returnValue = libtoontown._inPdt4yMh_i(self.this, startIndex, endIndex)
            return returnValue

        
        def getSuitEdgeTravelTime(self, startIndex, endIndex, rate):
            returnValue = libtoontown._inPdt4y3Jpk(self.this, startIndex, endIndex, rate)
            return returnValue

        
        def getNumSuitPoints(self):
            returnValue = libtoontown._inPdt4yDX52(self.this)
            return returnValue

        
        def getSuitPointAtIndex(self, index):
            returnValue = libtoontown._inPdt4ycJ4i(self.this, index)
            returnObject = DNASuitPoint.DNASuitPoint(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getSuitPointWithIndex(self, index):
            returnValue = libtoontown._inPdt4ypR8H(self.this, index)
            returnObject = DNASuitPoint.DNASuitPoint(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getSuitPath(self, startPoint, endPoint):
            returnValue = libtoontown._inPdt4yFhHg(self.this, startPoint.this, endPoint.this)
            returnObject = DNASuitPath.DNASuitPath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def fixup(self):
            returnValue = libtoontown._inPdt4yeMsU(self.this)
            return returnValue

        
        def write(self, out, indentLevel):
            returnValue = libtoontown._inPdt4yr7F4(self.this, out.this, indentLevel)
            return returnValue

        
        def storeSuitPoint(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], DNASuitPoint.DNASuitPoint):
                    return self.overloaded_storeSuitPoint_ptrDNAStorage_ptrDNASuitPoint(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <DNASuitPoint.DNASuitPoint> '
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], Point3.Point3):
                        return self.overloaded_storeSuitPoint_ptrDNAStorage___enum__DNASuitPointType_ptrLPoint3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def storeSuitEdge(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], DNASuitEdge.DNASuitEdge):
                    return self.overloaded_storeSuitEdge_ptrDNAStorage_ptrDNASuitEdge(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <DNASuitEdge.DNASuitEdge> '
            elif numArgs == 3:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.StringType):
                            return self.overloaded_storeSuitEdge_ptrDNAStorage_int_int_atomicstring(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.StringType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

        
        def removeDNAGroup(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], NodeRelation.NodeRelation):
                    return self.overloaded_removeDNAGroup_ptrDNAStorage_ptrNodeRelation(_args[0])
                elif isinstance(_args[0], DNAGroup.DNAGroup):
                    return self.overloaded_removeDNAGroup_ptrDNAStorage_ptrDNAGroup(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodeRelation.NodeRelation> <DNAGroup.DNAGroup> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['DNAStorage'] = DNAStorage

