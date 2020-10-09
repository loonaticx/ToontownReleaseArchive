# Source Generated with Decompyle++
# File: PGItem.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VBase4
import Node
import ArcChain
import PGFrameStyle
import ButtonHandle
import AudioSound
import TextNode
import TypeHandle
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import BoundedObject
import BoundingVolume
import TypeHandle
import ReferenceCount
import TypeHandle
import Node
import TypeHandle
import NodeRelation
import Ostream
import BoundedObject
import ReferenceCount
import Writable
import TypedWritable
import BoundingVolume
import Namable
import Ostream
import TypeHandle
import NamedNode
import Namable
import TypeHandle
import Node
import NodeRelation
import Ostream
import BoundedObject
import ReferenceCount
classDefined = 0

def generateClass_PGItem():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PGItem(NamedNode.NamedNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPVvimnwRQ(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVvimgL9d()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getEnterPrefix():
            returnValue = libpanda._inPVvimcbNc()
            return returnValue

        getEnterPrefix = PandaStatic.PandaStatic(getEnterPrefix)
        
        def getExitPrefix():
            returnValue = libpanda._inPVvimDwYV()
            return returnValue

        getExitPrefix = PandaStatic.PandaStatic(getExitPrefix)
        
        def getFocusInPrefix():
            returnValue = libpanda._inPVvimh2SU()
            return returnValue

        getFocusInPrefix = PandaStatic.PandaStatic(getFocusInPrefix)
        
        def getFocusOutPrefix():
            returnValue = libpanda._inPVvim5BtI()
            return returnValue

        getFocusOutPrefix = PandaStatic.PandaStatic(getFocusOutPrefix)
        
        def getPressPrefix():
            returnValue = libpanda._inPVvimDhW8()
            return returnValue

        getPressPrefix = PandaStatic.PandaStatic(getPressPrefix)
        
        def getReleasePrefix():
            returnValue = libpanda._inPVvimegfV()
            return returnValue

        getReleasePrefix = PandaStatic.PandaStatic(getReleasePrefix)
        
        def getTextNode():
            returnValue = libpanda._inPVvimEJ3y()
            returnObject = TextNode.TextNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        getTextNode = PandaStatic.PandaStatic(getTextNode)
        
        def setTextNode(node):
            returnValue = libpanda._inPVviml1Ih(node.this)
            return returnValue

        setTextNode = PandaStatic.PandaStatic(setTextNode)
        
        def getFocusItem():
            returnValue = libpanda._inPVvimRKKY()
            returnObject = PGItem(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        getFocusItem = PandaStatic.PandaStatic(getFocusItem)
        
        def getClassType():
            returnValue = libpanda._inPVvimAsTl()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_setFrame_ptrPGItem_float_float_float_float(self, left, right, bottom, top):
            returnValue = libpanda._inPVvimU_kh(self.this, left, right, bottom, top)
            return returnValue

        
        def overloaded_setFrame_ptrPGItem_ptrConstLVecBase4f(self, frame):
            returnValue = libpanda._inPVvimYdEN(self.this, frame.this)
            return returnValue

        
        def getFrame(self):
            returnValue = libpanda._inPVvimYDC8(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def hasFrame(self):
            returnValue = libpanda._inPVvimRzs9(self.this)
            return returnValue

        
        def clearFrame(self):
            returnValue = libpanda._inPVvimMdLq(self.this)
            return returnValue

        
        def setState(self, state):
            returnValue = libpanda._inPVvimzJoe(self.this, state)
            return returnValue

        
        def getState(self):
            returnValue = libpanda._inPVvimuXh7(self.this)
            return returnValue

        
        def setActive(self, active):
            returnValue = libpanda._inPVvimka9v(self.this, active)
            return returnValue

        
        def getActive(self):
            returnValue = libpanda._inPVvim_lel(self.this)
            return returnValue

        
        def setFocus(self, focus):
            returnValue = libpanda._inPVvimQ5x_(self.this, focus)
            return returnValue

        
        def getFocus(self):
            returnValue = libpanda._inPVvimI3FX(self.this)
            return returnValue

        
        def setBackgroundFocus(self, focus):
            returnValue = libpanda._inPVvimsYA6(self.this, focus)
            return returnValue

        
        def getBackgroundFocus(self):
            returnValue = libpanda._inPVvimzaEP(self.this)
            return returnValue

        
        def getNumStateDefs(self):
            returnValue = libpanda._inPVvim3z0S(self.this)
            return returnValue

        
        def clearStateDef(self, state):
            returnValue = libpanda._inPVvim8MjL(self.this, state)
            return returnValue

        
        def hasStateDef(self, state):
            returnValue = libpanda._inPVvimyQ7N(self.this, state)
            return returnValue

        
        def getStateDef(self, state):
            returnValue = libpanda._inPVvim3MwN(self.this, state)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def instanceToStateDef(self, state, chain):
            returnValue = libpanda._inPVvimwBxb(self.this, state, chain.this)
            return returnValue

        
        def getFrameStyle(self, state):
            returnValue = libpanda._inPVvimwkSW(self.this, state)
            returnObject = PGFrameStyle.PGFrameStyle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setFrameStyle(self, state, style):
            returnValue = libpanda._inPVvimHNNg(self.this, state, style.this)
            return returnValue

        
        def getId(self):
            returnValue = libpanda._inPVvimO91_(self.this)
            return returnValue

        
        def setId(self, id):
            returnValue = libpanda._inPVvim8_im(self.this, id)
            return returnValue

        
        def getEnterEvent(self):
            returnValue = libpanda._inPVvimP4D9(self.this)
            return returnValue

        
        def getExitEvent(self):
            returnValue = libpanda._inPVvimmTZg(self.this)
            return returnValue

        
        def getFocusInEvent(self):
            returnValue = libpanda._inPVvim2r_I(self.this)
            return returnValue

        
        def getFocusOutEvent(self):
            returnValue = libpanda._inPVvimWKxe(self.this)
            return returnValue

        
        def getPressEvent(self, button):
            returnValue = libpanda._inPVvimDp2p(self.this, button.this)
            return returnValue

        
        def getReleaseEvent(self, button):
            returnValue = libpanda._inPVvimlTAe(self.this, button.this)
            return returnValue

        
        def setSound(self, event, sound):
            returnValue = libpanda._inPVvimgehS(self.this, event, sound.this)
            return returnValue

        
        def clearSound(self, event):
            returnValue = libpanda._inPVvimGjW1(self.this, event)
            return returnValue

        
        def getSound(self, event):
            returnValue = libpanda._inPVvimacA4(self.this, event)
            returnObject = AudioSound.AudioSound(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def hasSound(self, event):
            returnValue = libpanda._inPVviml3q5(self.this, event)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setFrame(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setFrame_ptrPGItem_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setFrame_ptrPGItem_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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


    globals()['PGItem'] = PGItem

