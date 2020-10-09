# Source Generated with Decompyle++
# File: DNAGroup.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import NodePath
import DNAStorage
import Ostream
import Namable
import TypeHandle
import ReferenceCount
import TypedReferenceCount
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
classDefined = 0

def generateClass_DNAGroup():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNAGroup(TypedReferenceCount.TypedReferenceCount, Namable.Namable, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, initialName):
            self.this = libtoontown._inPdt4yBsCp(initialName)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libtoontown._inPdt4yoz75()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstDNAGroup(self, group):
            self.this = libtoontown._inPdt4yJtN4(group.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4y239M:
                libtoontown._inPdt4y239M(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPdt4yYv_Z()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_traverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage_int(self, parent, store, editing):
            returnValue = libtoontown._inPdt4yraUW(self.this, parent.this, store.this, editing)
            returnObject = NodePath.NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_traverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage(self, parent, store):
            returnValue = libtoontown._inPdt4yX4XS(self.this, parent.this, store.this)
            returnObject = NodePath.NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_topLevelTraverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage_int(self, parent, store, editing):
            returnValue = libtoontown._inPdt4ylxhv(self.this, parent.this, store.this, editing)
            returnObject = NodePath.NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_topLevelTraverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage(self, parent, store):
            returnValue = libtoontown._inPdt4yOBvf(self.this, parent.this, store.this)
            returnObject = NodePath.NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def add(self, group):
            returnValue = libtoontown._inPdt4yY_Zo(self.this, group.this)
            return returnValue

        
        def remove(self, group):
            returnValue = libtoontown._inPdt4yng_w(self.this, group.this)
            return returnValue

        
        def at(self, index):
            returnValue = libtoontown._inPdt4yyR9n(self.this, index)
            returnObject = DNAGroup(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def current(self):
            returnValue = libtoontown._inPdt4ygrHn(self.this)
            returnObject = DNAGroup(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getNumChildren(self):
            returnValue = libtoontown._inPdt4yTta8(self.this)
            return returnValue

        
        def getParent(self):
            returnValue = libtoontown._inPdt4yi91A(self.this)
            returnObject = DNAGroup(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_write_ptrConstDNAGroup_ptrOstream_ptrDNAStorage_int(self, out, store, indentLevel):
            returnValue = libtoontown._inPdt4ysq3X(self.this, out.this, store.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstDNAGroup_ptrOstream_ptrDNAStorage(self, out, store):
            returnValue = libtoontown._inPdt4ydm94(self.this, out.this, store.this)
            return returnValue

        
        def ls(self):
            returnValue = libtoontown._inPdt4yydWD(self.this)
            return returnValue

        
        def upcastToNamable(self):
            returnValue = libtoontown._inPdt4y5I2q(self.this)
            returnObject = Namable.Namable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def upcastToReferenceCount(self):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxtDe8f(upcastSelf.this)
            returnObject = ReferenceCount.ReferenceCount(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getType(self):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxtuIyI(upcastSelf.this)
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getTypeIndex(self):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxtfVBU(upcastSelf.this)
            return returnValue

        
        def isOfType(self, handle):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxtgfKt(upcastSelf.this, handle.this)
            return returnValue

        
        def isExactType(self, handle):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxt0xzz(upcastSelf.this, handle.this)
            return returnValue

        
        def getRefCount(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtIP2_(upcastSelf.this)
            return returnValue

        
        def ref(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtTs5_(upcastSelf.this)
            return returnValue

        
        def unref(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtpMWy(upcastSelf.this)
            return returnValue

        
        def testRefCountIntegrity(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtoDk2(upcastSelf.this)
            return returnValue

        
        def assign(self, other):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtiPcI(upcastSelf.this, other.this)
            returnObject = Namable.Namable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setName(self, name):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtEnBW(upcastSelf.this, name)
            return returnValue

        
        def clearName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtSJVl(upcastSelf.this)
            return returnValue

        
        def hasName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtR9hC(upcastSelf.this)
            return returnValue

        
        def getName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtYaRN(upcastSelf.this)
            return returnValue

        
        def output(self, out):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxthN8q(upcastSelf.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                elif isinstance(_args[0], DNAGroup):
                    return self.overloaded_constructor_ptrConstDNAGroup(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAGroup> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def topLevelTraverse(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], NodePath.NodePath):
                    if isinstance(_args[1], DNAStorage.DNAStorage):
                        return self.overloaded_topLevelTraverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
            elif numArgs == 3:
                if isinstance(_args[0], NodePath.NodePath):
                    if isinstance(_args[1], DNAStorage.DNAStorage):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_topLevelTraverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage_int(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

        
        def traverse(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], NodePath.NodePath):
                    if isinstance(_args[1], DNAStorage.DNAStorage):
                        return self.overloaded_traverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
            elif numArgs == 3:
                if isinstance(_args[0], NodePath.NodePath):
                    if isinstance(_args[1], DNAStorage.DNAStorage):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_traverse_ptrDNAGroup_ptrNodePath_ptrDNAStorage_int(_args[0], _args[1], _args[2])
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
                        return self.overloaded_write_ptrConstDNAGroup_ptrOstream_ptrDNAStorage(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 3:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], DNAStorage.DNAStorage):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_write_ptrConstDNAGroup_ptrOstream_ptrDNAStorage_int(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


    globals()['DNAGroup'] = DNAGroup

