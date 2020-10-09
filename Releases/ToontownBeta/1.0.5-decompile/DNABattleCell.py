# Source Generated with Decompyle++
# File: DNABattleCell.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Point3
import Ostream
import NodePath
import DNAStorage
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
classDefined = 0

def generateClass_DNABattleCell():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNABattleCell(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, width, height, pos):
            self.this = libtoontown._inPdt4yaZyl(width, height, pos.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4yydYV:
                libtoontown._inPdt4yydYV(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPdt4yLL2s()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setWidthHeight(self, width, height):
            returnValue = libtoontown._inPdt4yynZM(self.this, width, height)
            return returnValue

        
        def getWidth(self):
            returnValue = libtoontown._inPdt4yDzCb(self.this)
            return returnValue

        
        def getHeight(self):
            returnValue = libtoontown._inPdt4yLTrA(self.this)
            return returnValue

        
        def setPos(self, pos):
            returnValue = libtoontown._inPdt4yR5Pn(self.this, pos.this)
            return returnValue

        
        def getPos(self):
            returnValue = libtoontown._inPdt4ymFER(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def output(self, out):
            returnValue = libtoontown._inPdt4y3pDC(self.this, out.this)
            return returnValue

        
        def overloaded_traverse_ptrDNABattleCell_ptrNodePath_ptrDNAStorage_int(self, parent, store, editing):
            returnValue = libtoontown._inPdt4yKekl(self.this, parent.this, store.this, editing)
            returnObject = NodePath.NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_traverse_ptrDNABattleCell_ptrNodePath_ptrDNAStorage(self, parent, store):
            returnValue = libtoontown._inPdt4y6ird(self.this, parent.this, store.this)
            returnObject = NodePath.NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_write_ptrConstDNABattleCell_ptrOstream_ptrDNAStorage_int(self, out, store, indentLevel):
            returnValue = libtoontown._inPdt4y_woo(self.this, out.this, store.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstDNABattleCell_ptrOstream_ptrDNAStorage(self, out, store):
            returnValue = libtoontown._inPdt4yln1q(self.this, out.this, store.this)
            return returnValue

        
        def traverse(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], NodePath.NodePath):
                    if isinstance(_args[1], DNAStorage.DNAStorage):
                        return self.overloaded_traverse_ptrDNABattleCell_ptrNodePath_ptrDNAStorage(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
            elif numArgs == 3:
                if isinstance(_args[0], NodePath.NodePath):
                    if isinstance(_args[1], DNAStorage.DNAStorage):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_traverse_ptrDNABattleCell_ptrNodePath_ptrDNAStorage_int(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], DNAStorage.DNAStorage):
                        return self.overloaded_write_ptrConstDNABattleCell_ptrOstream_ptrDNAStorage(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 3:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], DNAStorage.DNAStorage):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_write_ptrConstDNABattleCell_ptrOstream_ptrDNAStorage_int(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


    globals()['DNABattleCell'] = DNABattleCell

