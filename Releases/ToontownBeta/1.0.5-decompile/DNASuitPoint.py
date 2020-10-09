# Source Generated with Decompyle++
# File: DNASuitPoint.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Point3
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

def generateClass_DNASuitPoint():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNASuitPoint(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        FRONTDOORPOINT = 1
        STREETPOINT = 0
        SIDEDOORPOINT = 2
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_int___enum__DNASuitPointType_ptrLPoint3f_int(self, index, type, pos, lbIndex):
            self.this = libtoontown._inPdt4yj0al(index, type, pos.this, lbIndex)
            self.userManagesMemory = 1

        
        def overloaded_constructor_int___enum__DNASuitPointType_ptrLPoint3f(self, index, type, pos):
            self.this = libtoontown._inPdt4yTChd(index, type, pos.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4yjKYD:
                libtoontown._inPdt4yjKYD(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPdt4y1WJf()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setIndex(self, index):
            returnValue = libtoontown._inPdt4yukrK(self.this, index)
            return returnValue

        
        def getIndex(self):
            returnValue = libtoontown._inPdt4yMhKF(self.this)
            return returnValue

        
        def setPointType(self, type):
            returnValue = libtoontown._inPdt4yINET(self.this, type)
            return returnValue

        
        def getPointType(self):
            returnValue = libtoontown._inPdt4y2wF8(self.this)
            return returnValue

        
        def setPos(self, pos):
            returnValue = libtoontown._inPdt4ypH_s(self.this, pos.this)
            return returnValue

        
        def getPos(self):
            returnValue = libtoontown._inPdt4yhsRO(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setLandmarkBuildingIndex(self, lbIndex):
            returnValue = libtoontown._inPdt4yZCG_(self.this, lbIndex)
            return returnValue

        
        def getLandmarkBuildingIndex(self):
            returnValue = libtoontown._inPdt4yMc6v(self.this)
            return returnValue

        
        def output(self, out):
            returnValue = libtoontown._inPdt4yKFyR(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstDNASuitPoint_ptrOstream_int(self, out, indentLevel):
            returnValue = libtoontown._inPdt4ylY4h(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstDNASuitPoint_ptrOstream(self, out):
            returnValue = libtoontown._inPdt4ygxK6(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 3:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], Point3.Point3):
                            return self.overloaded_constructor_int___enum__DNASuitPointType_ptrLPoint3f(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Point3.Point3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], Point3.Point3):
                            if isinstance(_args[3], types.IntType):
                                return self.overloaded_constructor_int___enum__DNASuitPointType_ptrLPoint3f_int(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Point3.Point3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstDNASuitPoint_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstDNASuitPoint_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['DNASuitPoint'] = DNASuitPoint

