# Source Generated with Decompyle++
# File: DCFile.pyo (Python 2.0)

import PandaStatic
import types
import libdirect
import libdirectDowncasts
import FFIExternalObject
import Filename
import Istream
import Ostream
import DCClass
classDefined = 0

def generateClass_DCFile():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DCFile(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libdirectDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libdirect._inP5HfQFOdB()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libdirect and libdirect._inP5HfQjAwv:
                libdirect._inP5HfQjAwv(self.this)
            

        
        def overloaded_read_ptrDCFile_ptrFilename(self, filename):
            returnValue = libdirect._inP5HfQ9cwK(self.this, filename.this)
            return returnValue

        
        def overloaded_read_ptrDCFile_ptrIstream_atomicstring(self, _in, filename):
            returnValue = libdirect._inP5HfQKi_H(self.this, _in.this, filename)
            return returnValue

        
        def overloaded_read_ptrDCFile_ptrIstream(self, _in):
            returnValue = libdirect._inP5HfQmFo_(self.this, _in.this)
            return returnValue

        
        def overloaded_write_ptrConstDCFile_ptrFilename(self, filename):
            returnValue = libdirect._inP5HfQoc95(self.this, filename.this)
            return returnValue

        
        def overloaded_write_ptrConstDCFile_ptrOstream_atomicstring(self, out, filename):
            returnValue = libdirect._inP5HfQo0tc(self.this, out.this, filename)
            return returnValue

        
        def overloaded_write_ptrConstDCFile_ptrOstream(self, out):
            returnValue = libdirect._inP5HfQghi0(self.this, out.this)
            return returnValue

        
        def getNumClasses(self):
            returnValue = libdirect._inP5HfQZnAi(self.this)
            return returnValue

        
        def getClass(self, n):
            returnValue = libdirect._inP5HfQof38(self.this, n)
            returnObject = DCClass.DCClass(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getClassByName(self, name):
            returnValue = libdirect._inP5HfQtnPb(self.this, name)
            returnObject = DCClass.DCClass(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getHash(self):
            returnValue = libdirect._inP5HfQQmzc(self.this)
            return returnValue

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstDCFile_ptrOstream(_args[0])
                elif isinstance(_args[0], Filename.Filename):
                    return self.overloaded_write_ptrConstDCFile_ptrFilename(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> <Filename.Filename> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.StringType):
                        return self.overloaded_write_ptrConstDCFile_ptrOstream_atomicstring(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def read(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Istream.Istream):
                    return self.overloaded_read_ptrDCFile_ptrIstream(_args[0])
                elif isinstance(_args[0], Filename.Filename):
                    return self.overloaded_read_ptrDCFile_ptrFilename(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> <Filename.Filename> '
            elif numArgs == 2:
                if isinstance(_args[0], Istream.Istream):
                    if isinstance(_args[1], types.StringType):
                        return self.overloaded_read_ptrDCFile_ptrIstream_atomicstring(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['DCFile'] = DCFile

