# Source Generated with Decompyle++
# File: Material.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VBase4
import Ostream
import TypeHandle
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
classDefined = 0

def generateClass_Material():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Material(TypedWritableReferenceCount.TypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPMAKP3YND()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstMaterial(self, copy):
            self.this = libpanda._inPMAKP_p_b(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPMAKPVVBP()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def assign(self, copy):
            returnValue = libpanda._inPMAKP2Cpi(self.this, copy.this)
            returnObject = Material(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def hasAmbient(self):
            returnValue = libpanda._inPMAKP055w(self.this)
            return returnValue

        
        def getAmbient(self):
            returnValue = libpanda._inPMAKPS2qI(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setAmbient(self, color):
            returnValue = libpanda._inPMAKPwSWB(self.this, color.this)
            return returnValue

        
        def clearAmbient(self):
            returnValue = libpanda._inPMAKPX5xD(self.this)
            return returnValue

        
        def hasDiffuse(self):
            returnValue = libpanda._inPMAKPNinK(self.this)
            return returnValue

        
        def getDiffuse(self):
            returnValue = libpanda._inPMAKP0iai(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setDiffuse(self, color):
            returnValue = libpanda._inPMAKPSOFb(self.this, color.this)
            return returnValue

        
        def clearDiffuse(self):
            returnValue = libpanda._inPMAKP5DrE(self.this)
            return returnValue

        
        def hasSpecular(self):
            returnValue = libpanda._inPMAKPPUA4(self.this)
            return returnValue

        
        def getSpecular(self):
            returnValue = libpanda._inPMAKP1_wP(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setSpecular(self, color):
            returnValue = libpanda._inPMAKPW5yI(self.this, color.this)
            return returnValue

        
        def clearSpecular(self):
            returnValue = libpanda._inPMAKPVnUr(self.this)
            return returnValue

        
        def hasEmission(self):
            returnValue = libpanda._inPMAKPtRsd(self.this)
            return returnValue

        
        def getEmission(self):
            returnValue = libpanda._inPMAKPUQd1(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setEmission(self, color):
            returnValue = libpanda._inPMAKPpieu(self.this, color.this)
            return returnValue

        
        def clearEmission(self):
            returnValue = libpanda._inPMAKPcksu(self.this)
            return returnValue

        
        def getShininess(self):
            returnValue = libpanda._inPMAKP12pp(self.this)
            return returnValue

        
        def setShininess(self, shininess):
            returnValue = libpanda._inPMAKP3d1v(self.this, shininess)
            return returnValue

        
        def getLocal(self):
            returnValue = libpanda._inPMAKP_GA2(self.this)
            return returnValue

        
        def setLocal(self, local):
            returnValue = libpanda._inPMAKP2dMm(self.this, local)
            return returnValue

        
        def getTwoside(self):
            returnValue = libpanda._inPMAKPCtRL(self.this)
            return returnValue

        
        def setTwoside(self, twoside):
            returnValue = libpanda._inPMAKPtUcF(self.this, twoside)
            return returnValue

        
        def eq(self, other):
            returnValue = libpanda._inPMAKPG3w5(self.this, other.this)
            return returnValue

        
        def ne(self, other):
            returnValue = libpanda._inPMAKPoBg5(self.this, other.this)
            return returnValue

        
        def lessThan(self, other):
            returnValue = libpanda._inPMAKPpwha(self.this, other.this)
            return returnValue

        
        def compareTo(self, other):
            returnValue = libpanda._inPMAKPefQk(self.this, other.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPMAKPahq5(self.this, out.this)
            return returnValue

        
        def write(self, out, indent):
            returnValue = libpanda._inPMAKPHRX7(self.this, out.this, indent)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], Material):
                    return self.overloaded_constructor_ptrConstMaterial(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Material> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['Material'] = Material

