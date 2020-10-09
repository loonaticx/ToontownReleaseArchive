# Source Generated with Decompyle++
# File: PosHpr.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import FFIExternalObject
import Point3
classDefined = 0

def generateClass_PosHpr():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PosHpr(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(self, pos, hpr):
            self.this = libtoontown._inPdt4yCYnZ(pos.this, hpr.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLPoint3f(self, pos):
            self.this = libtoontown._inPdt4y8OC1(pos.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libtoontown._inPdt4ysX08()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4ydd4a:
                libtoontown._inPdt4ydd4a(self.this)
            

        
        def getPos(self):
            returnValue = libtoontown._inPdt4yD3TP(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getHpr(self):
            returnValue = libtoontown._inPdt4y9_7x(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], Point3.Point3):
                    return self.overloaded_constructor_ptrConstLPoint3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            elif numArgs == 2:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], Point3.Point3):
                        return self.overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


    globals()['PosHpr'] = PosHpr

