# Source Generated with Decompyle++
# File: ForceGroup.pyo (Python 2.0)

from PandaObject import *
from DirectObject import *
from PhysicsManagerGlobal import *
import ForceNode
import DirectNotifyGlobal

class ForceGroup(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('ForceGroup')
    id = 1
    
    def __init__(self, name = None):
        if name == None:
            self.name = 'ForceGroup-%d' % ForceGroup.id
            ForceGroup.id += 1
        else:
            self.name = name
        self.node = ForceNode.ForceNode(self.name)
        self.nodePath = hidden.attachNewNode(self.node)
        self.fEnabled = 0
        self.particleEffect = None

    
    def cleanup(self):
        for f in self.asList():
            self.removeForce(f)
        
        self.nodePath.removeNode()
        self.node = None
        self.particleEffect = None

    
    def enable(self):
        for i in range(self.node.getNumForces()):
            f = self.node.getForce(i)
            f.setActive(1)
        
        self.fEnabled = 1

    
    def disable(self):
        for i in range(self.node.getNumForces()):
            f = self.node.getForce(i)
            f.setActive(0)
        
        self.fEnabled = 0

    
    def isEnabled(self):
        return self.fEnabled

    
    def addForce(self, force):
        self.node.addForce(force)
        if self.particleEffect:
            self.particleEffect.addForce(force)
        

    
    def removeForce(self, force):
        self.node.removeForce(force)
        if self.particleEffect != None:
            self.particleEffect.removeForce(force)
        

    
    def getName(self):
        return self.name

    
    def getNode(self):
        return self.node

    
    def getNodePath(self):
        return self.nodePath

    
    def __getitem__(self, index):
        numForces = self.node.getNumForces()
        if numForces == 0:
            raise IndexError
        
        if (index < 0) | (index >= self.node.getNumForces()):
            raise IndexError
        
        return self.node.getForce(index)

    
    def __len__(self):
        return self.node.getNumForces()

    
    def asList(self):
        l = []
        for i in range(self.node.getNumForces()):
            l.append(self.node.getForce(i))
        
        return l

    
    def printParams(self, file = sys.stdout, targ = 'self'):
        file.write('# Force parameters\n')
        for i in range(self.node.getNumForces()):
            f = self.node.getForce(i)
            fname = 'force%d' % i
            if isinstance(f, LinearForce):
                amplitude = f.getAmplitude()
                massDependent = f.getMassDependent()
                if isinstance(f, LinearCylinderVortexForce):
                    file.write(fname + ' = LinearCylinderVortexForce(%.4f, %.4f, %.4f, %.4f, %d)\n' % (f.getRadius(), f.getLength(), f.getCoef(), amplitude, massDependent))
                elif isinstance(f, LinearDistanceForce):
                    radius = f.getRadius()
                    falloffType = f.getFalloffType()
                    ftype = 'FTONEOVERR'
                    if falloffType == LinearDistanceForce.FTONEOVERR:
                        ftype = 'FTONEOVERR'
                    elif falloffType == LinearDistanceForce.FTONEOVERRSQUARED:
                        ftype = 'FTONEOVERRSQUARED'
                    elif falloffType == LinearDistanceForce.FTONEOVERRCUBED:
                        ftype = 'FTONEOVERRCUBED'
                    
                    forceCenter = f.getForceCenter()
                    if isinstance(f, LinearSinkForce):
                        file.write(fname + ' = LinearSinkForce(Point3(%.4f, %.4f, %.4f), LinearDistanceForce.%s, %.4f, %.4f, %d)\n' % (forceCenter[0], forceCenter[1], forceCenter[2], ftype, radius, amplitude, massDependent))
                    elif isinstance(f, LinearSourceForce):
                        file.write(fname + ' = LinearSourceForce(Point3(%.4f, %.4f, %.4f), LinearDistanceForce.%s, %.4f, %.4f, %d)\n' % (forceCenter[0], forceCenter[1], forceCenter[2], ftype, radius, amplitude, massDependent))
                    
                elif isinstance(f, LinearFrictionForce):
                    file.write(fname + ' = LinearFrictionForce(%.4f, %.4f, %d)\n' % (f.getCoef(), amplitude, massDependent))
                elif isinstance(f, LinearJitterForce):
                    file.write(fname + ' = LinearJitterForce(%.4f, %d)\n' % (amplitude, massDependent))
                elif isinstance(f, LinearNoiseForce):
                    file.write(fname + ' = LinearNoiseForce(%.4f, %d)\n' % (amplitude, massDependent))
                elif isinstance(f, LinearVectorForce):
                    vec = f.getLocalVector()
                    file.write(fname + ' = LinearVectorForce(Vec3(%.4f, %.4f, %.4f), %.4f, %d)\n' % (vec[0], vec[1], vec[2], amplitude, massDependent))
                
            elif isinstance(f, AngularForce):
                if isinstance(f, AngularVectorForce):
                    vec = f.getLocalVector()
                    file.write(fname + ' = AngularVectorForce(Vec3(%.4f, %.4f, %.4f))\n' % (vec[0], vec[1], vec[2]))
                
            
            file.write(fname + '.setActive(%d)\n' % f.getActive())
            file.write(targ + '.addForce(%s)\n' % fname)
        


