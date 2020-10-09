# Source Generated with Decompyle++
# File: BitMask32.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Ostream
import TypeHandle
classDefined = 0

def generateClass_BitMask32():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class BitMask32(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPflbogvQd()
            self.userManagesMemory = 1

        
        def overloaded_constructor_unsignedint(self, initValue):
            self.this = libpanda._inPflbot4oo(initValue)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstBitMask32(self, copy):
            self.this = libpanda._inPflbo06MO(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPflbo45wA:
                libpanda._inPflbo45wA(self.this)
            

        
        def allOn():
            returnValue = libpanda._inPflboKobZ()
            returnObject = BitMask32(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        allOn = PandaStatic.PandaStatic(allOn)
        
        def allOff():
            returnValue = libpanda._inPflbocezX()
            returnObject = BitMask32(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        allOff = PandaStatic.PandaStatic(allOff)
        
        def lowerOn(onBits):
            returnValue = libpanda._inPflboBqak(onBits)
            returnObject = BitMask32(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        lowerOn = PandaStatic.PandaStatic(lowerOn)
        
        def bit(index):
            returnValue = libpanda._inPflbolgZS(index)
            returnObject = BitMask32(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        bit = PandaStatic.PandaStatic(bit)
        
        def getClassType():
            returnValue = libpanda._inPflbojP8v()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def assign(self, copy):
            returnValue = libpanda._inPflbo7zYM(self.this, copy.this)
            returnObject = BitMask32(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getNumBits(self):
            returnValue = libpanda._inPflbotBsT(self.this)
            return returnValue

        
        def getBit(self, index):
            returnValue = libpanda._inPflboXOTD(self.this, index)
            return returnValue

        
        def setBit(self, index):
            returnValue = libpanda._inPflboWWTx(self.this, index)
            return returnValue

        
        def clearBit(self, index):
            returnValue = libpanda._inPflboXfOW(self.this, index)
            return returnValue

        
        def setBitTo(self, index, value):
            returnValue = libpanda._inPflboWCS6(self.this, index, value)
            return returnValue

        
        def extract(self, lowBit, size):
            returnValue = libpanda._inPflboocn_(self.this, lowBit, size)
            return returnValue

        
        def store(self, value, lowBit, size):
            returnValue = libpanda._inPflboOD88(self.this, value, lowBit, size)
            return returnValue

        
        def getWord(self):
            returnValue = libpanda._inPflbobd5O(self.this)
            return returnValue

        
        def setWord(self, value):
            returnValue = libpanda._inPflbo9qWc(self.this, value)
            return returnValue

        
        def invertInPlace(self):
            returnValue = libpanda._inPflboE_d4(self.this)
            return returnValue

        
        def clear(self):
            returnValue = libpanda._inPflboRepe(self.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPflbow4Sz(self.this, out.this)
            return returnValue

        
        def overloaded_outputBinary_ptrConstBitMask32_ptrOstream_int(self, out, spacesEvery):
            returnValue = libpanda._inPflbo6nXy(self.this, out.this, spacesEvery)
            return returnValue

        
        def overloaded_outputBinary_ptrConstBitMask32_ptrOstream(self, out):
            returnValue = libpanda._inPflbo1T_6(self.this, out.this)
            return returnValue

        
        def overloaded_outputHex_ptrConstBitMask32_ptrOstream_int(self, out, spacesEvery):
            returnValue = libpanda._inPflboAjUc(self.this, out.this, spacesEvery)
            return returnValue

        
        def overloaded_outputHex_ptrConstBitMask32_ptrOstream(self, out):
            returnValue = libpanda._inPflbozteI(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstBitMask32_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPflbo6Y8k(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstBitMask32_ptrOstream(self, out):
            returnValue = libpanda._inPflboAJB7(self.this, out.this)
            return returnValue

        
        def eq(self, other):
            returnValue = libpanda._inPflbofowJ(self.this, other.this)
            return returnValue

        
        def ne(self, other):
            returnValue = libpanda._inPflbodYEB(self.this, other.this)
            return returnValue

        
        def lessThan(self, other):
            returnValue = libpanda._inPflbocT9v(self.this, other.this)
            return returnValue

        
        def compareTo(self, other):
            returnValue = libpanda._inPflboiY5v(self.this, other.this)
            return returnValue

        
        def __and__(self, other):
            returnValue = libpanda._inPflboZbiE(self.this, other.this)
            returnObject = BitMask32(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __or__(self, other):
            returnValue = libpanda._inPflbofTZo(self.this, other.this)
            returnObject = BitMask32(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __xor__(self, other):
            returnValue = libpanda._inPflbod77V(self.this, other.this)
            returnObject = BitMask32(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def bitwiseNot(self):
            returnValue = libpanda._inPflbotDYy(self.this)
            returnObject = BitMask32(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __lshift__(self, shift):
            returnValue = libpanda._inPflbo1IX_(self.this, shift)
            returnObject = BitMask32(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __rshift__(self, shift):
            returnValue = libpanda._inPflbozQkA(self.this, shift)
            returnObject = BitMask32(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def __iand__(self, other):
            returnValue = libpanda._inPflboKrDL(self.this, other.this)
            return self

        
        def __ior__(self, other):
            returnValue = libpanda._inPflboYj5u(self.this, other.this)
            return self

        
        def __ixor__(self, other):
            returnValue = libpanda._inPflboWLdc(self.this, other.this)
            return self

        
        def __ilshift__(self, shift):
            returnValue = libpanda._inPflboISEt(self.this, shift)
            return self

        
        def __irshift__(self, shift):
            returnValue = libpanda._inPflboBKRv(self.this, shift)
            return self

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_unsignedint(_args[0])
                elif isinstance(_args[0], BitMask32):
                    return self.overloaded_constructor_ptrConstBitMask32(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BitMask32> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def outputHex(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_outputHex_ptrConstBitMask32_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_outputHex_ptrConstBitMask32_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def outputBinary(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_outputBinary_ptrConstBitMask32_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_outputBinary_ptrConstBitMask32_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstBitMask32_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstBitMask32_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['BitMask32'] = BitMask32

