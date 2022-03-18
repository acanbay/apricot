from . import Statistics as st
from . import Graphs as gp
import numpy as np
import time
import math
import os


def getBeam( beam, path=None, tag=None ):
    if path!=None:
        if not os.path.exists(path):
            os.makedirs(path)

    print("\n'{}' Beam Graphs are being saved...\n".format(tag))
    
    gp.BeamShape_xy( beam, path, tag )
    if beam.dz == True:
        gp.BeamShape_yz( beam, path, tag )
        gp.BeamShape_zx( beam, path, tag )
    gp.PhaseSpace( beam, path, tag )

def getBeamPositions( beam, beamline=None, path=None, tag=None ):
    if path!=None:
        if not os.path.exists(path):
            os.makedirs(path)

    print("'{}' Position Graphs are being saved...\n".format(tag))

    gp.PositionGraph( beam, beamline, path, tag )
    gp.PositionGraph_RMSsize( beam, beamline, path, tag )
    gp.BetaFunctions( beam, beamline, path, tag )

    x = np.copy( beam.BeamMatrix[0,:] )
    xp = np.copy( beam.BeamMatrix[1,:] )
    y = np.copy( beam.BeamMatrix[2,:] )
    yp = np.copy( beam.BeamMatrix[3,:] )

    var_x = np.var( x )
    var_xp = np.var( xp )
    std_xxp = st.mymean2( x, xp )**2

    var_y = np.var( y )
    var_yp = np.var( yp )
    std_yyp = st.mymean2( y, yp )**2
        
    Emittance_x = math.sqrt( var_x * var_xp - std_xxp )
    Emittance_y = math.sqrt( var_y * var_yp - std_yyp )
        
    Beta_x = np.std( x )**2 / Emittance_x
    Beta_y = np.std( y )**2 / Emittance_y

    x_rms = st.myrms(x)
    y_rms = st.myrms(y)

    print("""\nBeam parameters in the final state:
        
    RMS x size (mm)         : {:.3e}
    RMS y size (mm)         : {:.3e}
    Emittance x (mrad)      : {:.3e}
    Emittance y (mrad)      : {:.3e}
    Beta x (mm)             : {:.3e}
    Beta y (mm)             : {:.3e}\n\n""".format(x_rms*1e-3,y_rms*1e-3,Emittance_x*1e-3,Emittance_y*1e-3,Beta_x, Beta_y))
    time.sleep(2)
