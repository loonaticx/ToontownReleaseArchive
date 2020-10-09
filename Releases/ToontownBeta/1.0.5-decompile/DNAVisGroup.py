# Source Generated with Decompyle++
# File: DNAVisGroup.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DNASuitEdge
import DNABattleCell
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import Namable
import Ostream
import TypeHandle
import DNAGroup
import NodePath
import DNAStorage
import Ostream
import Namable
import TypeHandle
import ReferenceCount
import TypedReferenceCount
classDefined = 0

def generateClass_DNAVisGroup():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNAVisGroup(DNAGroup.DNAGroup, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, initialName):
            self.this = libtoontown._inPdt4yv_mR(initialName)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libtoontown._inPdt4yXGKI()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstDNAVisGroup(self, group):
            self.this = libtoontown._inPdt4yCyfu(group.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4yYGxV:
                libtoontown._inPdt4yYGxV(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPdt4yqlTy()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def addVisible(self, visGroupName):
            returnValue = libtoontown._inPdt4ykaIa(self.this, visGroupName)
            return returnValue

        
        def removeVisible(self, visGroupName):
            returnValue = libtoontown._inPdt4yyv81(self.this, visGroupName)
            return returnValue

        
        def getNumVisibles(self):
            returnValue = libtoontown._inPdt4yjBUT(self.this)
            return returnValue

        
        def getVisibleName(self, i):
            returnValue = libtoontown._inPdt4y9iX6(self.this, i)
            return returnValue

        
        def addSuitEdge(self, edge):
            returnValue = libtoontown._inPdt4yxQIm(self.this, edge.this)
            return returnValue

        
        def removeSuitEdge(self, edge):
            returnValue = libtoontown._inPdt4yll9U(self.this, edge.this)
            return returnValue

        
        def getNumSuitEdges(self):
            returnValue = libtoontown._inPdt4y8jQf(self.this)
            return returnValue

        
        def getSuitEdge(self, i):
            returnValue = libtoontown._inPdt4y_5TQ(self.this, i)
            returnObject = DNASuitEdge.DNASuitEdge(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def addBattleCell(self, cell):
            returnValue = libtoontown._inPdt4yGpzx(self.this, cell.this)
            return returnValue

        
        def removeBattleCell(self, cell):
            returnValue = libtoontown._inPdt4ygKgH(self.this, cell.this)
            return returnValue

        
        def getNumBattleCells(self):
            returnValue = libtoontown._inPdt4y8eHg(self.this)
            return returnValue

        
        def getBattleCell(self, i):
            returnValue = libtoontown._inPdt4yd5de(self.this, i)
            returnObject = DNABattleCell.DNABattleCell(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                elif isinstance(_args[0], DNAVisGroup):
                    return self.overloaded_constructor_ptrConstDNAVisGroup(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAVisGroup> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['DNAVisGroup'] = DNAVisGroup

