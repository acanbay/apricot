from . import Functions as fn
from . import BeamlineComponents as blc
from . import Statistics as st
import numpy as np
import math
import time

class Gun():
    def __init__( self, Voltage = None, ParticleType = None  ):
        self.Energy = Voltage
        self.ParticleType = ParticleType
        self.Emittance_x = None
        self.Emittance_y = None
        self.x_rms = None
        self.y_rms = None
        self.Alpha_x=None
        self.Alpha_y=None
        self.z_rms=None
        self.dE=None

    def GenerateBeam( self, NumberofParticles):
        return fn.RandomBeam( self.ParticleType, NumberofParticles, self.Energy, self.x_rms, self.y_rms, self.Emittance_x, self.Emittance_y, Alpha_x=None, Alpha_y=None, z_rms=None, dE=None )

class ElectronGun():
    Type  = "ElectronGun"
    Alpha_x=None
    Alpha_y=None
    z_rms=0
    dE=0
    
    def __init__( self, r_Cathode, Temperature, Voltage ):
        self.Voltage = Voltage
        self.Energy = abs( Voltage )
        self.ParticleType = "Electron"
        self.Mass =  0.51099895e6
        self.r_Cathode = r_Cathode
        
        kB=8.617e-5 #eV*K^-1
        Emittance = self.r_Cathode * math.sqrt( kB * Temperature / self.Mass )
        self.Emittance = Emittance
        
    def GenerateBeam( self, NumberofParticles ):
        r = self.r_Cathode * np.random.random( NumberofParticles )
        theta = np.random.random( NumberofParticles ) * 2 * math.pi
        
        x = r * np.cos(theta)
        x_rms = st.myrms(x)
        xp_rms = self.Emittance**2 / x_rms
        
        y = r * np.sin(theta)
        y_rms = st.myrms(y)
        yp_rms = self.Emittance**2 / y_rms

        self.x_rms = x_rms
        self.xp_rms = xp_rms
        self.y_rms = y_rms
        self.yp_rms = yp_rms

        Beta_x = x_rms**2 / self.Emittance
        Beta_y = y_rms**2 / self.Emittance

        print("""\nCreating beam with parameters below:
            
        Particle Type           : {}
        Number of Particles     : {}
        Beam Energy (KeV)       : {:.3e}
        RMS x size (mm)         : {:.3e}
        RMS y size (mm)         : {:.3e}
        RMS z size (mm)         : {:.3e}
        Emittance x (mrad)      : {:.3e}
        Emittance y (mrad)      : {:.3e}
        Alpha x                 : {:.3e}
        Alpha y                 : {:.3e}
        %Energy Spread          : {}\n""".format("electron",NumberofParticles,self.Voltage*1e-3,x_rms*1e-3,y_rms*1e-3,self.z_rms*1e-3,self.Emittance*1e-3,self.Emittance*1e-3,self.Alpha_x, self.Alpha_y,self.dE))
        time.sleep(2)

        BeamMatrix = np.zeros( [ 6, NumberofParticles ] )
        BeamMatrix[0] = x_rms * np.random.randn( NumberofParticles )
        BeamMatrix[1] = xp_rms * np.random.randn( NumberofParticles )
        BeamMatrix[2] = y_rms * np.random.randn( NumberofParticles )
        BeamMatrix[3] = yp_rms * np.random.randn( NumberofParticles )
        BeamMatrix[4] = np.zeros( NumberofParticles )
        BeamMatrix[5] = np.ones( NumberofParticles ) * self.Voltage
    
        TwissParameters = np.array( [[ self.Emittance, Beta_x, self.Emittance, Beta_y ]] )
        BeamPositions = np.array( [[ BeamMatrix[0], BeamMatrix[2], BeamMatrix[4] ]] )
    
        return blc.Beam( "Electron", NumberofParticles, self.Mass, self.Voltage, BeamMatrix, TwissParameters, BeamPositions ) 
