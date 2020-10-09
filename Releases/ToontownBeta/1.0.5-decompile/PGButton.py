# Source Generated with Decompyle++
# File: PGButton.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ArcChain
import ButtonHandle
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
import PGItem
import VBase4
import Node
import ArcChain
import PGFrameStyle
import ButtonHandle
import AudioSound
import TextNode
import TypeHandle
classDefined = 0

def generateClass_PGButton():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PGButton(PGItem.PGItem, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        SReady = 0
        SDepressed = 1
        SInactive = 3
        SRollover = 2
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPVvimQMhN(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVvimd3ae()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClickPrefix():
            returnValue = libpanda._inPVvimaOEu()
            return returnValue

        getClickPrefix = PandaStatic.PandaStatic(getClickPrefix)
        
        def getClassType():
            returnValue = libpanda._inPVvimcYeU()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_setup_ptrPGButton_atomicstring(self, label):
            returnValue = libpanda._inPVvimRJF_(self.this, label)
            return returnValue

        
        def overloaded_setup_ptrPGButton_ptrConstArcChain(self, ready):
            returnValue = libpanda._inPVvimzvUL(self.this, ready.this)
            return returnValue

        
        def overloaded_setup_ptrPGButton_ptrConstArcChain_ptrConstArcChain(self, ready, depressed):
            returnValue = libpanda._inPVvimoM_k(self.this, ready.this, depressed.this)
            return returnValue

        
        def overloaded_setup_ptrPGButton_ptrConstArcChain_ptrConstArcChain_ptrConstArcChain(self, ready, depressed, rollover):
            returnValue = libpanda._inPVvimIVnL(self.this, ready.this, depressed.this, rollover.this)
            return returnValue

        
        def overloaded_setup_ptrPGButton_ptrConstArcChain_ptrConstArcChain_ptrConstArcChain_ptrConstArcChain(self, ready, depressed, rollover, inactive):
            returnValue = libpanda._inPVvim3_Tm(self.this, ready.this, depressed.this, rollover.this, inactive.this)
            return returnValue

        
        def addClickButton(self, button):
            returnValue = libpanda._inPVvim_aUK(self.this, button.this)
            return returnValue

        
        def removeClickButton(self, button):
            returnValue = libpanda._inPVvim0s68(self.this, button.this)
            return returnValue

        
        def hasClickButton(self, button):
            returnValue = libpanda._inPVvimR8LX(self.this, button.this)
            return returnValue

        
        def getClickEvent(self, button):
            returnValue = libpanda._inPVvimSOm2(self.this, button.this)
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

        
        def setup(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_setup_ptrPGButton_atomicstring(_args[0])
                elif isinstance(_args[0], ArcChain.ArcChain):
                    return self.overloaded_setup_ptrPGButton_ptrConstArcChain(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <ArcChain.ArcChain> '
            elif numArgs == 2:
                if isinstance(_args[0], ArcChain.ArcChain):
                    if isinstance(_args[1], ArcChain.ArcChain):
                        return self.overloaded_setup_ptrPGButton_ptrConstArcChain_ptrConstArcChain(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <ArcChain.ArcChain> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <ArcChain.ArcChain> '
            elif numArgs == 3:
                if isinstance(_args[0], ArcChain.ArcChain):
                    if isinstance(_args[1], ArcChain.ArcChain):
                        if isinstance(_args[2], ArcChain.ArcChain):
                            return self.overloaded_setup_ptrPGButton_ptrConstArcChain_ptrConstArcChain_ptrConstArcChain(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <ArcChain.ArcChain> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <ArcChain.ArcChain> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <ArcChain.ArcChain> '
            elif numArgs == 4:
                if isinstance(_args[0], ArcChain.ArcChain):
                    if isinstance(_args[1], ArcChain.ArcChain):
                        if isinstance(_args[2], ArcChain.ArcChain):
                            if isinstance(_args[3], ArcChain.ArcChain):
                                return self.overloaded_setup_ptrPGButton_ptrConstArcChain_ptrConstArcChain_ptrConstArcChain_ptrConstArcChain(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <ArcChain.ArcChain> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <ArcChain.ArcChain> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <ArcChain.ArcChain> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <ArcChain.ArcChain> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '


    globals()['PGButton'] = PGButton

