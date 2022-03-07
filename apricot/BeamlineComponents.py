import numpy as np
import math
from scipy.linalg import expm, logm

class Beam():
    Type="Beam"
    def __init__( self, ParticleTpye=None, NumberOfParticles=None, ParticleMass=None, BeamEnergy=None, BeamMatrix=None, TwissParameters=None, BeamPositions=None, dz=None ):
         self.ParticleTpye = ParticleTpye
         self.NumberOfParticles = NumberOfParticles
         self.ParticleMass = ParticleMass
         self.BeamEnergy = BeamEnergy
         self.BeamMatrix = BeamMatrix
         self.TwissParameters = TwissParameters
         self.BeamPositions = BeamPositions
         self.dz = dz
    
    #def __str__( self ):
    def print_help( self ):
        return """
Beam Class
----------
Contains Beam objects.
    
    Beam( ParticleType, NumberOfParticles, ParticleMass, BeamEnergy, BeamMatrix, BeamPositions  )
    
    ParticleType    :   electron, proton, muon
    BeamMatrix      :   6x6 matrix with initial parameters x ,x', y, y', z, E
    BeamPositions   :   Array of initial condisions x, y, z
    
Use the RandomBeam function to create an object from the Beam class.
    """

class BeamLineComponents():
    def __init__(self, Name = None, Length = None, Matrix = None ):
        self.Name = Name
        self.Length = Length
        self.Matrix = Matrix
        
    def reDefineMatrix( self, Delta_s = None ):
        if Delta_s != None and Delta_s != self.Length:
            if self.Type == "DriftTube":
                self.Matrix[0,1] = Delta_s
                self.Matrix[2,3] = Delta_s
            else:
                self.Matrix = expm( Delta_s * logm( self.Matrix ) /self.Length  )
            
                #n = 1/int( self.Length / Delta_s )
                #evalues, evectors = np.linalg.eig( self.Matrix )
                #assert (evalues >= 0).all()
                #self.Matrix = np.real( evectors @ np.diag( np.power( evalues ,n ) ) @ np.linalg.inv( evectors ) )
            
class DriftTube( BeamLineComponents ):
    Type = "DriftTube"
    def __init__( self, Name = None, Length = None ):
        
        Matrix = np.eye( 6 )
        Matrix[0,1] = Length
        Matrix[2,3] = Length
        
        super().__init__( Name, Length, Matrix )
    
class QuadrupoleMagnet( BeamLineComponents ):
    Type="QuadrupoleMagnet"
    def __init__( self, Name=None, Length=None, Strength=None ):
        self.Strength = Strength
        
        Matrix = np.eye( 6 )
        if self.Strength >= 0:
            sqrt_k = math.sqrt( self.Strength )
            phi = sqrt_k * Length
            cx = math.cos( phi )
            sx = math.sin( phi )
            cy = math.cosh( phi )
            sy = math.sinh( phi )

            Matrix[0,0] = cx
            Matrix[1,1] = cx
            Matrix[0,1] = sx / sqrt_k
            Matrix[1,0] = -sqrt_k * sx
            Matrix[2,2] = cy
            Matrix[3,3] = cy
            Matrix[2,3] = sy / sqrt_k
            Matrix[3,2] = sqrt_k * sy
    
        else:
            sqrt_k = math.sqrt( -self.Strength )
            phi = sqrt_k * Length
            cx = math.cosh( phi )
            sx = math.sinh( phi )
            cy = math.cos( phi )
            sy = math.sin( phi )
            
            Matrix[0,0] = cx
            Matrix[1,1] = cx
            Matrix[0,1] = sx / sqrt_k
            Matrix[1,0] = sqrt_k * sx
            Matrix[2,2] = cy
            Matrix[3,3] = cy
            Matrix[2,3] = sy / sqrt_k
            Matrix[3,2] = -sqrt_k * sy

        super().__init__( Name, Length, Matrix )

class DipoleMagnet( BeamLineComponents ):
    Type="DipoleMagnet"
    def __init__( self, Name=None, Length=None, Angle=None, ybend=0 ):
        self.Angle = Angle
        rho = Length/Angle
        
        Matrix = np.eye( 6 )
        if ybend == 0:
            Matrix[0,0] = math.cos(Angle)
            Matrix[1,1] = math.cos(Angle)
            Matrix[0,1] = rho * math.sin(Angle)
            Matrix[1,0] = -1/rho * math.sin(Angle)
            Matrix[2,3] = Length
        else:
            Matrix[0,1] = Length
            Matrix[2,2] = math.cos(Angle)
            Matrix[3,3] = math.cos(Angle)
            Matrix[2,3] = rho * math.sin(Angle)
            Matrix[3,2] = -1/rho * math.sin(Angle)

        Matrix[0,5] = rho * (1 - math.cos(Angle) )
        Matrix[1,4] = rho * (1 - math.cos(Angle) )
        Matrix[1,5] = math.sin(Angle)
        Matrix[0,4] = math.sin(Angle)
        Matrix[5,4] = rho * (Angle - math.sin(Angle) )
            
        super().__init__( Name, Length, Matrix )

class Solenoid( BeamLineComponents ):
    Type="Solenoid"
    def __init__( self, Name=None, Length=None, Strength=None ):
        self.Strength = Strength
                
        Matrix = np.eye( 6 )

        kl = self.Strength * Length

        c1 = math.cos( kl )
        s1 = math.sin( kl )
        
        C2 = c1 * c1
        S2 = s1 * s1
        SC = s1 * c1

        Matrix[0,0] = C2
        Matrix[0,1] = SC / self.Strength
        Matrix[0,2] = SC
        Matrix[0,3] = S2 / self.Strength
        Matrix[1,0] = -self.Strength * SC
        Matrix[1,1] = C2
        Matrix[1,2] = -self.Strength * S2
        Matrix[1,3] = SC
        Matrix[2,0] = -SC
        Matrix[2,1] = -S2 / self.Strength
        Matrix[2,2] = C2
        Matrix[2,3] = SC / self.Strength
        Matrix[3,0] = self.Strength * S2
        Matrix[3,1] = -SC
        Matrix[3,2] = -self.Strength * SC
        Matrix[3,3] = C2
        
        super().__init__( Name, Length, Matrix )