from . import BeamlineComponents as blc
from . import Functions as fn
import numpy as np
import math

class Beamline():
    Type="BeamLine"
    def __init__( self, Name, Elements ):
        self.Name = Name

        tmp_Elements = []
        for Element in Elements:
            if type( Element ) == list:
                tmp_Elements.extend( Element )
            elif hasattr(Element, 'Elements'):
                tmp_Elements.extend( Element.Elements )
            else:
                tmp_Elements.append( Element )

        self.Elements = tmp_Elements
    
    def DefineMatrix( self ):
        Matrix = np.eye(6)
        for i in range( len( self.Elements ) ):
            Matrix = self.Elements[i].Matrix @ Matrix

        if abs( Matrix[0,0] + Matrix[1,1] ) > 2 or abs( Matrix[2,2] + Matrix[3,3] ) > 2:
            print("Lattice is not stable!")
            exit()
        
        self.Matrix = Matrix
    
    def DefineTwissParameters( self ):
        if not( hasattr(self, 'Matrix') ):
            self.DefineMatrix()
            
        Cx = ( self.Matrix[0,0] + self.Matrix[1,1] ) / 2
        Sx = math.sqrt( 1 - Cx**2 )
        
        Beta_x = self.Matrix[0,1] / Sx
        Alpha_x = ( self.Matrix[0,0] - self.Matrix[1,1] ) / ( 2 * Sx )
        self.Beta_x = Beta_x
        self.Alpha_x = Alpha_x
        
        Cy = ( self.Matrix[2,2] + self.Matrix[3,3] ) / 2
        Sy = math.sqrt( 1 - Cy**2 )
        
        Beta_y = self.Matrix[2,3] / Sy
        Alpha_y = ( self.Matrix[2,2] - self.Matrix[3,3] ) / ( 2 * Sy )
        self.Beta_y = Beta_y
        self.Alpha_y = Alpha_y
    
    def RandomBeam( self, ParticleTpye, NumberOfParticles, BeamEnergy, x_rms, y_rms, z_rms=None, dE=None ):
        self.DefineTwissParameters()
        
        Emittance_x = x_rms**2 / self.Beta_x
        Emittance_y = y_rms**2 / self.Beta_y
        
        return fn.RandomBeam( ParticleTpye, NumberOfParticles, BeamEnergy, x_rms, y_rms, Emittance_x, Emittance_y, self.Alpha_x, self.Alpha_y, z_rms, dE )
     
class FODO( Beamline ):
    Type="FODO"
    def __init__( self, Name, DriftLength, QuadrupoleMagnetLength, QuadrupoleMagnetStrength ):        
        drift = blc.DriftTube( "{}_Drift".format( Name ), DriftLength )
        quad1 = blc.QuadrupoleMagnet( "{}_Quadrupole_xFocusing".format( Name ), QuadrupoleMagnetLength / 2 , QuadrupoleMagnetStrength )
        quad2 = blc.QuadrupoleMagnet( "{}_Quadrupole_xdeFocusing".format( Name ), QuadrupoleMagnetLength, -QuadrupoleMagnetStrength )
        
        Elements = [quad1,drift,quad2,drift,quad1]
        super().__init__( Name, Elements )
