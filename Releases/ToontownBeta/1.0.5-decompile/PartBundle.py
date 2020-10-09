# Source Generated with Decompyle++
# File: PartBundle.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PartBundleNode
import AnimControl
import Ostream
import AnimBundle
import AnimControlCollection
import TypeHandle
import PartGroup
import Namable
import Event
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import ReferenceCount
import TypeHandle
import TypedWritableReferenceCount
import ReferenceCount
import TypeHandle
import Writable
import TypedWritable
import Namable
import Ostream
import TypeHandle
import PartGroup
import Ostream
import Namable
import TypeHandle
import ReferenceCount
import TypedWritableReferenceCount
import AnimControlCollection
import AnimControl
import Event
classDefined = 0

def generateClass_PartBundle():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PartBundle(PartGroup.PartGroup, AnimControlCollection.AnimControlCollection, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPn9gM5WPu:
                libpanda._inPn9gM5WPu(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPn9gM0q2E()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getNode(self):
            returnValue = libpanda._inPn9gMpL3U(self.this)
            returnObject = PartBundleNode.PartBundleNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def clearControlEffects(self):
            returnValue = libpanda._inPn9gMQsiY(self.this)
            return returnValue

        
        def setControlEffect(self, control, effect):
            returnValue = libpanda._inPn9gMVXPe(self.this, control.this, effect)
            return returnValue

        
        def getControlEffect(self, control):
            returnValue = libpanda._inPn9gM9xhs(self.this, control.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPn9gM_qkL(self.this, out.this)
            return returnValue

        
        def write(self, out, indentLevel):
            returnValue = libpanda._inPn9gM6Z1u(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_bindAnim_ptrPartBundle_ptrAnimBundle_int(self, anim, hierarchyMatchFlags):
            returnValue = libpanda._inPn9gM2d6Q(self.this, anim.this, hierarchyMatchFlags)
            returnObject = AnimControl.AnimControl(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_bindAnim_ptrPartBundle_ptrAnimBundle(self, anim):
            returnValue = libpanda._inPn9gMXGTx(self.this, anim.this)
            returnObject = AnimControl.AnimControl(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_bindAnim_ptrPartBundle_ptrAnimBundle_atomicstring_int(self, anim, name, hierarchyMatchFlags):
            returnValue = libpanda._inPn9gMckUy(self.this, anim.this, name, hierarchyMatchFlags)
            return returnValue

        
        def overloaded_bindAnim_ptrPartBundle_ptrAnimBundle_atomicstring(self, anim, name):
            returnValue = libpanda._inPn9gMRnTE(self.this, anim.this, name)
            return returnValue

        
        def upcastToAnimControlCollection(self):
            returnValue = libpanda._inPn9gMbS6Z(self.this)
            returnObject = AnimControlCollection.AnimControlCollection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getNumChildren(self):
            upcastSelf = self
            returnValue = libpanda._inPn9gMp5p4(upcastSelf.this)
            return returnValue

        
        def getChild(self, n):
            upcastSelf = self
            returnValue = libpanda._inPn9gMF7IO(upcastSelf.this, n)
            returnObject = PartGroup.PartGroup(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def findChild(self, name):
            upcastSelf = self
            returnValue = libpanda._inPn9gMz0Sh(upcastSelf.this, name)
            returnObject = PartGroup.PartGroup(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def writeWithValue(self, out, indentLevel):
            upcastSelf = self
            returnValue = libpanda._inPn9gMzpSE(upcastSelf.this, out.this, indentLevel)
            return returnValue

        
        def upcastToNamable(self):
            upcastSelf = self
            returnValue = libpanda._inPn9gM9LUs(upcastSelf.this)
            returnObject = Namable.Namable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def upcastToReferenceCount(self):
            upcastSelf = self
            returnValue = libpanda._inPflbod2f_(upcastSelf.this)
            returnObject = ReferenceCount.ReferenceCount(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def upcastToWritable(self):
            upcastSelf = self
            returnValue = libpanda._inPflbo_8Kt(upcastSelf.this)
            returnObject = Writable.Writable(None)
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

        
        def storeAnim(self, control, name):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMCAu2(upcastSelf.this, control.this, name)
            return returnValue

        
        def findAnim(self, name):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gM87vI(upcastSelf.this, name)
            returnObject = AnimControl.AnimControl(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def unbindAnim(self, name):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMXXcu(upcastSelf.this, name)
            return returnValue

        
        def getNumAnims(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMhoNk(upcastSelf.this)
            return returnValue

        
        def clearAnims(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMG8LN(upcastSelf.this)
            return returnValue

        
        def setStopEvent(self, stopEvent):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMqSwI(upcastSelf.this, stopEvent.this)
            return returnValue

        
        def clearStopEvent(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMfsKm(upcastSelf.this)
            return returnValue

        
        def hasStopEvent(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMvUuA(upcastSelf.this)
            return returnValue

        
        def getStopEvent(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMKCaz(upcastSelf.this)
            returnObject = Event.Event(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_play_ptrAnimControlCollection_atomicstring(self, animName):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMNnjN(upcastSelf.this, animName)
            return returnValue

        
        def overloaded_play_ptrAnimControlCollection_atomicstring_int_int(self, animName, _from, to):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gM3gRl(upcastSelf.this, animName, _from, to)
            return returnValue

        
        def overloaded_loop_ptrAnimControlCollection_atomicstring_bool(self, animName, restart):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gM6iEH(upcastSelf.this, animName, restart)
            return returnValue

        
        def overloaded_loop_ptrAnimControlCollection_atomicstring_bool_int_int(self, animName, restart, _from, to):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMMoG2(upcastSelf.this, animName, restart, _from, to)
            return returnValue

        
        def stop(self, animName):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMnBiQ(upcastSelf.this, animName)
            return returnValue

        
        def pose(self, animName, frame):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMfa9Z(upcastSelf.this, animName, frame)
            return returnValue

        
        def overloaded_playAll_ptrAnimControlCollection(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMm8z5(upcastSelf.this)
            return returnValue

        
        def overloaded_playAll_ptrAnimControlCollection_int_int(self, _from, to):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMVTrb(upcastSelf.this, _from, to)
            return returnValue

        
        def overloaded_loopAll_ptrAnimControlCollection_bool(self, restart):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMF4O5(upcastSelf.this, restart)
            return returnValue

        
        def overloaded_loopAll_ptrAnimControlCollection_bool_int_int(self, restart, _from, to):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMK_09(upcastSelf.this, restart, _from, to)
            return returnValue

        
        def stopAll(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMQux8(upcastSelf.this)
            return returnValue

        
        def poseAll(self, frame):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMCHfr(upcastSelf.this, frame)
            return returnValue

        
        def overloaded_getFrame_ptrConstAnimControlCollection_atomicstring(self, animName):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMzcy2(upcastSelf.this, animName)
            return returnValue

        
        def overloaded_getFrame_ptrConstAnimControlCollection(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMaxpY(upcastSelf.this)
            return returnValue

        
        def getNumFrames(self, animName):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMo_KP(upcastSelf.this, animName)
            return returnValue

        
        def overloaded_isPlaying_ptrConstAnimControlCollection_atomicstring(self, animName):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMf45y(upcastSelf.this, animName)
            return returnValue

        
        def overloaded_isPlaying_ptrConstAnimControlCollection(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gMzfhs(upcastSelf.this)
            return returnValue

        
        def whichAnimPlaying(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToAnimControlCollection()
            returnValue = libpanda._inPn9gM6hcV(upcastSelf.this)
            return returnValue

        
        def bindAnim(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], AnimBundle.AnimBundle):
                    return self.overloaded_bindAnim_ptrPartBundle_ptrAnimBundle(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <AnimBundle.AnimBundle> '
            elif numArgs == 2:
                if isinstance(_args[0], AnimBundle.AnimBundle):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_bindAnim_ptrPartBundle_ptrAnimBundle_int(_args[0], _args[1])
                    elif isinstance(_args[1], types.StringType):
                        return self.overloaded_bindAnim_ptrPartBundle_ptrAnimBundle_atomicstring(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <AnimBundle.AnimBundle> '
            elif numArgs == 3:
                if isinstance(_args[0], AnimBundle.AnimBundle):
                    if isinstance(_args[1], types.StringType):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_bindAnim_ptrPartBundle_ptrAnimBundle_atomicstring_int(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <AnimBundle.AnimBundle> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '


    globals()['PartBundle'] = PartBundle

