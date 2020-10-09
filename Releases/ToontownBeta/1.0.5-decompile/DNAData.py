# Source Generated with Decompyle++
# File: DNAData.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Filename
import Ostream
import Istream
import DNAStorage
import DSearchPath
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

def generateClass_DNAData():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNAData(DNAGroup.DNAGroup, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, initialName):
            self.this = libtoontown._inPdt4ygL_q(initialName)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libtoontown._inPdt4yWmjm()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstDNAData(self, copy):
            self.this = libtoontown._inPdt4yXogM(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4yr2rx:
                libtoontown._inPdt4yr2rx(self.this)
            

        
        def overloaded_resolveDnaFilename_ptrFilename_ptrConstDSearchPath(dnaFilename, searchpath):
            returnValue = libtoontown._inPdt4ySpNG(dnaFilename.this, searchpath.this)
            return returnValue

        overloaded_resolveDnaFilename_ptrFilename_ptrConstDSearchPath = PandaStatic.PandaStatic(overloaded_resolveDnaFilename_ptrFilename_ptrConstDSearchPath)
        
        def overloaded_resolveDnaFilename_ptrFilename(dnaFilename):
            returnValue = libtoontown._inPdt4yAr01(dnaFilename.this)
            return returnValue

        overloaded_resolveDnaFilename_ptrFilename = PandaStatic.PandaStatic(overloaded_resolveDnaFilename_ptrFilename)
        
        def getClassType():
            returnValue = libtoontown._inPdt4yd_rg()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def assign(self, copy):
            returnValue = libtoontown._inPdt4y2iao(self.this, copy.this)
            returnObject = DNAData(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_read_ptrDNAData_ptrFilename_ptrOstream(self, filename, error):
            returnValue = libtoontown._inPdt4yREo0(self.this, filename.this, error.this)
            return returnValue

        
        def overloaded_read_ptrDNAData_ptrFilename(self, filename):
            returnValue = libtoontown._inPdt4yEs50(self.this, filename.this)
            return returnValue

        
        def overloaded_read_ptrDNAData_ptrIstream_ptrOstream(self, _in, error):
            returnValue = libtoontown._inPdt4yPMhI(self.this, _in.this, error.this)
            return returnValue

        
        def overloaded_read_ptrDNAData_ptrIstream(self, _in):
            returnValue = libtoontown._inPdt4yPCgQ(self.this, _in.this)
            return returnValue

        
        def overloaded_resolveExternals_ptrDNAData_atomicstring_ptrOstream(self, searchpath, error):
            returnValue = libtoontown._inPdt4yX1LE(self.this, searchpath, error.this)
            return returnValue

        
        def overloaded_resolveExternals_ptrDNAData_atomicstring(self, searchpath):
            returnValue = libtoontown._inPdt4yQvKM(self.this, searchpath)
            return returnValue

        
        def overloaded_writeDna_ptrDNAData_ptrFilename_ptrOstream_ptrDNAStorage(self, filename, error, store):
            returnValue = libtoontown._inPdt4ykdGG(self.this, filename.this, error.this, store.this)
            return returnValue

        
        def overloaded_writeDna_ptrDNAData_ptrOstream_ptrOstream_ptrDNAStorage(self, out, error, store):
            returnValue = libtoontown._inPdt4yFMLP(self.this, out.this, error.this, store.this)
            return returnValue

        
        def setCoordinateSystem(self, coordsys):
            returnValue = libtoontown._inPdt4ykjA5(self.this, coordsys)
            return returnValue

        
        def getCoordinateSystem(self):
            returnValue = libtoontown._inPdt4yvY3I(self.this)
            return returnValue

        
        def setDnaFilename(self, directory):
            returnValue = libtoontown._inPdt4yuKTB(self.this, directory.this)
            return returnValue

        
        def getDnaFilename(self):
            returnValue = libtoontown._inPdt4ycEXP(self.this)
            returnObject = Filename.Filename(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setDnaStorage(self, store):
            returnValue = libtoontown._inPdt4yYAd5(self.this, store.this)
            return returnValue

        
        def getDnaStorage(self):
            returnValue = libtoontown._inPdt4ykB0g(self.this)
            returnObject = DNAStorage.DNAStorage(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                elif isinstance(_args[0], DNAData):
                    return self.overloaded_constructor_ptrConstDNAData(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAData> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def resolveDnaFilename(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Filename.Filename):
                    return DNAData.overloaded_resolveDnaFilename_ptrFilename(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
            elif numArgs == 2:
                if isinstance(_args[0], Filename.Filename):
                    if isinstance(_args[1], DSearchPath.DSearchPath):
                        return DNAData.overloaded_resolveDnaFilename_ptrFilename_ptrConstDSearchPath(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <DSearchPath.DSearchPath> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        resolveDnaFilename = PandaStatic.PandaStatic(resolveDnaFilename)
        
        def read(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Istream.Istream):
                    return self.overloaded_read_ptrDNAData_ptrIstream(_args[0])
                elif isinstance(_args[0], Filename.Filename):
                    return self.overloaded_read_ptrDNAData_ptrFilename(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> <Filename.Filename> '
            elif numArgs == 2:
                if isinstance(_args[0], Istream.Istream):
                    if isinstance(_args[1], Ostream.Ostream):
                        return self.overloaded_read_ptrDNAData_ptrIstream_ptrOstream(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Ostream.Ostream> '
                elif isinstance(_args[0], Filename.Filename):
                    if isinstance(_args[1], Ostream.Ostream):
                        return self.overloaded_read_ptrDNAData_ptrFilename_ptrOstream(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Ostream.Ostream> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Istream.Istream> <Filename.Filename> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def writeDna(self, *_args):
            numArgs = len(_args)
            if numArgs == 3:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], Ostream.Ostream):
                        if isinstance(_args[2], DNAStorage.DNAStorage):
                            return self.overloaded_writeDna_ptrDNAData_ptrOstream_ptrOstream_ptrDNAStorage(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <DNAStorage.DNAStorage> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Ostream.Ostream> '
                elif isinstance(_args[0], Filename.Filename):
                    if isinstance(_args[1], Ostream.Ostream):
                        if isinstance(_args[2], DNAStorage.DNAStorage):
                            return self.overloaded_writeDna_ptrDNAData_ptrFilename_ptrOstream_ptrDNAStorage(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <DNAStorage.DNAStorage> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Ostream.Ostream> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> <Filename.Filename> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 '

        
        def resolveExternals(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_resolveExternals_ptrDNAData_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], Ostream.Ostream):
                        return self.overloaded_resolveExternals_ptrDNAData_atomicstring_ptrOstream(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Ostream.Ostream> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['DNAData'] = DNAData

