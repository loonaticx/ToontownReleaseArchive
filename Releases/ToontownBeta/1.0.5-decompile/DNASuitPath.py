# Source Generated with Decompyle++
# File: DNASuitPath.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Ostream
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

def generateClass_DNASuitPath():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNASuitPath(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libtoontown._inPdt4yozAe()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstDNASuitPath(self, path):
            self.this = libtoontown._inPdt4y0A_i(path.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4yvHel:
                libtoontown._inPdt4yvHel(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPdt4yc0Rl()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getNumPoints(self):
            returnValue = libtoontown._inPdt4yl5vS(self.this)
            return returnValue

        
        def copy(self, path):
            returnValue = libtoontown._inPdt4yaN56(self.this, path.this)
            return returnValue

        
        def getPointIndex(self, i):
            returnValue = libtoontown._inPdt4ys74X(self.this, i)
            return returnValue

        
        def output(self, out):
            returnValue = libtoontown._inPdt4yHk18(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], DNASuitPath):
                    return self.overloaded_constructor_ptrConstDNASuitPath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <DNASuitPath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['DNASuitPath'] = DNASuitPath

