# Source Generated with Decompyle++
# File: TexturePool.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Texture
import Ostream
classDefined = 0

def generateClass_TexturePool():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class TexturePool(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
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
            if libpanda and libpanda._inPMAKP1dhA:
                libpanda._inPMAKP1dhA(self.this)
            

        
        def hasTexture(filename):
            returnValue = libpanda._inPMAKP40Bv(filename)
            return returnValue

        hasTexture = PandaStatic.PandaStatic(hasTexture)
        
        def verifyTexture(filename):
            returnValue = libpanda._inPMAKP5yev(filename)
            return returnValue

        verifyTexture = PandaStatic.PandaStatic(verifyTexture)
        
        def overloaded_loadTexture_atomicstring(filename):
            returnValue = libpanda._inPMAKPY98J(filename)
            returnObject = Texture.Texture(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        overloaded_loadTexture_atomicstring = PandaStatic.PandaStatic(overloaded_loadTexture_atomicstring)
        
        def overloaded_loadTexture_atomicstring_atomicstring(filename, grayfilename):
            returnValue = libpanda._inPMAKPKdVS(filename, grayfilename)
            returnObject = Texture.Texture(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        overloaded_loadTexture_atomicstring_atomicstring = PandaStatic.PandaStatic(overloaded_loadTexture_atomicstring_atomicstring)
        
        def addTexture(texture):
            returnValue = libpanda._inPMAKPgMyl(texture.this)
            return returnValue

        addTexture = PandaStatic.PandaStatic(addTexture)
        
        def releaseTexture(texture):
            returnValue = libpanda._inPMAKPiYMr(texture.this)
            return returnValue

        releaseTexture = PandaStatic.PandaStatic(releaseTexture)
        
        def releaseAllTextures():
            returnValue = libpanda._inPMAKP5P_0()
            return returnValue

        releaseAllTextures = PandaStatic.PandaStatic(releaseAllTextures)
        
        def garbageCollect():
            returnValue = libpanda._inPMAKPYL_C()
            return returnValue

        garbageCollect = PandaStatic.PandaStatic(garbageCollect)
        
        def listContents(out):
            returnValue = libpanda._inPMAKPUy3s(out.this)
            return returnValue

        listContents = PandaStatic.PandaStatic(listContents)
        
        def loadTexture(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return TexturePool.overloaded_loadTexture_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.StringType):
                        return TexturePool.overloaded_loadTexture_atomicstring_atomicstring(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        loadTexture = PandaStatic.PandaStatic(loadTexture)

    globals()['TexturePool'] = TexturePool

