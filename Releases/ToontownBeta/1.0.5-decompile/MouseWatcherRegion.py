# Source Generated with Decompyle++
# File: MouseWatcherRegion.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VBase4
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

def generateClass_MouseWatcherRegion():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class MouseWatcherRegion(TypedReferenceCount.TypedReferenceCount, Namable.Namable, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring_float_float_float_float(self, name, left, right, bottom, top):
            self.this = libpanda._inPyiw5OkEG(name, left, right, bottom, top)
            self.userManagesMemory = 1

        
        def overloaded_constructor_atomicstring_ptrConstLVecBase4f(self, name, frame):
            self.this = libpanda._inPyiw5Qn0b(name, frame.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPyiw5Z2_U:
                libpanda._inPyiw5Z2_U(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPyiw5XH2g()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_setFrame_ptrMouseWatcherRegion_float_float_float_float(self, left, right, bottom, top):
            returnValue = libpanda._inPyiw5Mi04(self.this, left, right, bottom, top)
            return returnValue

        
        def overloaded_setFrame_ptrMouseWatcherRegion_ptrConstLVecBase4f(self, frame):
            returnValue = libpanda._inPyiw5orlo(self.this, frame.this)
            return returnValue

        
        def getFrame(self):
            returnValue = libpanda._inPyiw57Pud(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getArea(self):
            returnValue = libpanda._inPyiw5qKBe(self.this)
            return returnValue

        
        def setSort(self, sort):
            returnValue = libpanda._inPyiw5nujJ(self.this, sort)
            return returnValue

        
        def getSort(self):
            returnValue = libpanda._inPyiw5pq_6(self.this)
            return returnValue

        
        def setActive(self, active):
            returnValue = libpanda._inPyiw5AX7x(self.this, active)
            return returnValue

        
        def getActive(self):
            returnValue = libpanda._inPyiw56BHH(self.this)
            return returnValue

        
        def setKeyboard(self, keyboard):
            returnValue = libpanda._inPyiw53KPd(self.this, keyboard)
            return returnValue

        
        def getKeyboard(self):
            returnValue = libpanda._inPyiw5vjK8(self.this)
            return returnValue

        
        def setSuppressBelow(self, suppressBelow):
            returnValue = libpanda._inPyiw5p0D0(self.this, suppressBelow)
            return returnValue

        
        def getSuppressBelow(self):
            returnValue = libpanda._inPyiw5SDwY(self.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPyiw5dJWL(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstMouseWatcherRegion_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPyiw5b9OS(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstMouseWatcherRegion_ptrOstream(self, out):
            returnValue = libpanda._inPyiw5uEbj(self.this, out.this)
            return returnValue

        
        def upcastToNamable(self):
            returnValue = libpanda._inPyiw5neXk(self.this)
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

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], VBase4.VBase4):
                        return self.overloaded_constructor_atomicstring_ptrConstLVecBase4f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 5:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                    return self.overloaded_constructor_atomicstring_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4])
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 5 '

        
        def setFrame(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setFrame_ptrMouseWatcherRegion_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setFrame_ptrMouseWatcherRegion_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstMouseWatcherRegion_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstMouseWatcherRegion_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def setRelative(self, np, left, right, bottom, top):
            from PandaModules import *
            mat = np.getMat(render2d)
            ll = mat.xformPoint(Point3(left, 0, bottom))
            ur = mat.xformPoint(Point3(right, 0, top))
            self.setFrame(ll[0], ur[0], ll[2], ur[2])


    globals()['MouseWatcherRegion'] = MouseWatcherRegion

