# Source Generated with Decompyle++
# File: NodePathCollection.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import NodePath
import TypeHandle
import Ostream
classDefined = 0

def generateClass_NodePathCollection():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class NodePathCollection(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPbPIPw8Xv()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstNodePathCollection(self, copy):
            self.this = libpanda._inPbPIPvC_H(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPbPIPbpHD:
                libpanda._inPbPIPbpHD(self.this)
            

        
        def assign(self, copy):
            returnValue = libpanda._inPbPIPagif(self.this, copy.this)
            returnObject = NodePathCollection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def addPath(self, nodePath):
            returnValue = libpanda._inPbPIPh97i(self.this, nodePath.this)
            return returnValue

        
        def removePath(self, nodePath):
            returnValue = libpanda._inPbPIP4Saw(self.this, nodePath.this)
            return returnValue

        
        def addPathsFrom(self, other):
            returnValue = libpanda._inPbPIP8O7c(self.this, other.this)
            return returnValue

        
        def removePathsFrom(self, other):
            returnValue = libpanda._inPbPIPI6sC(self.this, other.this)
            return returnValue

        
        def removeDuplicatePaths(self):
            returnValue = libpanda._inPbPIPYbHO(self.this)
            return returnValue

        
        def hasPath(self, path):
            returnValue = libpanda._inPbPIPPTrJ(self.this, path.this)
            return returnValue

        
        def clear(self):
            returnValue = libpanda._inPbPIPHMgl(self.this)
            return returnValue

        
        def isEmpty(self):
            returnValue = libpanda._inPbPIPRtzI(self.this)
            return returnValue

        
        def getNumPaths(self):
            returnValue = libpanda._inPbPIPzkKi(self.this)
            return returnValue

        
        def getPath(self, index):
            returnValue = libpanda._inPbPIPtQQJ(self.this, index)
            returnObject = NodePath.NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __getitem__(self, index):
            returnValue = libpanda._inPbPIPr8Il(self.this, index)
            returnObject = NodePath.NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getGraphType(self):
            returnValue = libpanda._inPbPIPwNxN(self.this)
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_ls_ptrConstNodePathCollection(self):
            returnValue = libpanda._inPbPIPwqA8(self.this)
            return returnValue

        
        def overloaded_ls_ptrConstNodePathCollection_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPbPIPKHri(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_ls_ptrConstNodePathCollection_ptrOstream(self, out):
            returnValue = libpanda._inPbPIPu3_6(self.this, out.this)
            return returnValue

        
        def findAllMatches(self, path):
            returnValue = libpanda._inPbPIPQ4NM(self.this, path)
            returnObject = NodePathCollection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def reparentTo(self, other):
            returnValue = libpanda._inPbPIPUPkO(self.this, other.this)
            return returnValue

        
        def wrtReparentTo(self, other):
            returnValue = libpanda._inPbPIPjrqE(self.this, other.this)
            return returnValue

        
        def instanceTo(self, other):
            returnValue = libpanda._inPbPIPfycc(self.this, other.this)
            returnObject = NodePathCollection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def show(self):
            returnValue = libpanda._inPbPIP0uQK(self.this)
            return returnValue

        
        def hide(self):
            returnValue = libpanda._inPbPIPyW4n(self.this)
            return returnValue

        
        def stash(self):
            returnValue = libpanda._inPbPIPbpiS(self.this)
            return returnValue

        
        def unstash(self):
            returnValue = libpanda._inPbPIPEtV5(self.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPbPIPnsFB(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstNodePathCollection_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPbPIPVB_H(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstNodePathCollection_ptrOstream(self, out):
            returnValue = libpanda._inPbPIP4BKZ(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], NodePathCollection):
                    return self.overloaded_constructor_ptrConstNodePathCollection(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePathCollection> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def ls(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_ls_ptrConstNodePathCollection()
            elif numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_ls_ptrConstNodePathCollection_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_ls_ptrConstNodePathCollection_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstNodePathCollection_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstNodePathCollection_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['NodePathCollection'] = NodePathCollection

