from . import Statistics as st
from . import BeamlineComponents as blc
import numpy as np
import math
import time

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 40, fill = '⬮', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = round( length * iteration / total)
    bar = '-' * (filledLength) + fill + '-' * (length - filledLength)
    
    print(f'\rProgress: {prefix} >{bar}> {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def RandomBeam( ParticleTpye, NumberOfParticles, BeamEnergy, x_rms, y_rms, Emittance_x, Emittance_y, Alpha_x=None, Alpha_y=None, z_rms=None, dE=None ):
    if z_rms == None:
        z_rms = 0
    if dE == None:
        dE = 0
    if Alpha_x == None:
        Alpha_x = 0
    if Alpha_y == None:
        Alpha_y = 0
    
    print("""\nCreating beam with parameters below:
        
    Particle Type           : {}
    Number of Particles     : {}
    Beam Energy (KeV)       : {:.3e}
    RMS x size (mm)         : {:.3e}
    RMS y size (mm)         : {:.3e}
    RMS z size (mm)         : {:.3e}
    Emittance x (mm-mrad)   : {:.3e}
    Emittance y (mm-mrad)   : {:.3e}
    Alpha x                 : {:.3e}
    Alpha y                 : {:.3e}
    %Energy Spread          : {:.3e}\n""".format(ParticleTpye,NumberOfParticles,BeamEnergy*1e-3,x_rms*1e-3,y_rms*1e-3,z_rms*1e-3,Emittance_x*1e-3,Emittance_y*1e-3,Alpha_x, Alpha_y,dE))
    time.sleep(2)

    ex=10e-6;      # emittance x m.rad
    ey=10e-6;      # emittance y m.rad
    sz=0.005;       # sigma z m
    ax=-0.50;       # alpha x unitless
    ay=-0.50;       # alpha y unitless
    
    if ParticleTpye.lower() == "electron":
        ParticleMass = 0.510e6
    elif ParticleTpye.lower() == "proton":
        ParticleMass = 938.272e6
    elif ParticleTpye.lower() == "muon":
        ParticleMass = 105.658e6
    
    Beta_x = x_rms**2 / Emittance_x
    Beta_y = y_rms**2 / Emittance_y
    Gamma_x = (1-Alpha_x**2)/Beta_x
    Gamma_y = (1-Alpha_y**2)/Beta_y
    
    xp_rms = np.sqrt( Emittance_x * Gamma_x )
    yp_rms = np.sqrt( Emittance_y * Gamma_y )
    
    BeamMatrix = np.zeros( [ 6, NumberOfParticles ] )
    BeamMatrix[0] = x_rms * np.random.randn( NumberOfParticles )
    BeamMatrix[1] = xp_rms * np.random.randn( NumberOfParticles )
    BeamMatrix[2] = y_rms * np.random.randn( NumberOfParticles )
    BeamMatrix[3] = yp_rms * np.random.randn( NumberOfParticles )
    BeamMatrix[5] = np.ones( NumberOfParticles ) * BeamEnergy
    
    TwissParameters = np.array( [[ Emittance_x, Beta_x, Emittance_y, Beta_y ]] )
    BeamPositions = np.array( [[ BeamMatrix[0], BeamMatrix[2], BeamMatrix[4] ]] )

    if z_rms == 0:
        BeamMatrix[4] = np.zeros( NumberOfParticles )
        return blc.Beam( ParticleTpye, NumberOfParticles, ParticleMass, BeamEnergy, BeamMatrix, TwissParameters, BeamPositions )
    else:
        dz = z_rms * np.random.randn( NumberOfParticles )
        dz = dz + abs(dz.min())
        BeamMatrix[4] = dz
        return blc.Beam( ParticleTpye, NumberOfParticles, ParticleMass, BeamEnergy, BeamMatrix, TwissParameters, BeamPositions, True )

def calcTwissParameters( Beam ):
    x = np.copy( Beam.BeamMatrix[0,:] )
    xp = np.copy( Beam.BeamMatrix[1,:] )
    y = np.copy( Beam.BeamMatrix[2,:] )
    yp = np.copy( Beam.BeamMatrix[3,:] )
    
    var_x = np.var( x )
    var_xp = np.var( xp )
    mean_x = np.mean( x )
    mean_xp = np.mean( xp ) 
    #std_xxp = np.mean( ( x - mean_x ) * ( xp - mean_xp ) )**2
    std_xxp = st.mymean2( x, xp )**2

    var_y = np.var( y )
    var_yp = np.var( yp )
    mean_y = np.mean( y )
    mean_yp = np.mean( yp ) 
    #std_yyp = np.mean( ( y - mean_y ) * ( yp - mean_yp ) )**2
    std_yyp = st.mymean2( y, yp )**2
        
    Emittance_x = math.sqrt( var_x * var_xp - std_xxp )
    Emittance_y = math.sqrt( var_y * var_yp - std_yyp )
        
    Beta_x = np.std( x )**2 / Emittance_x
    Beta_y = np.std( y )**2 / Emittance_y
        
    newTwissParameters = np.array( [[ Emittance_x, Beta_x, Emittance_y, Beta_y ]] )
    Beam.TwissParameters=np.append(Beam.TwissParameters, newTwissParameters, axis=0)
    
def TransportBeam( Beam, BeamLine, Delta_s = None, Track_Mode = None ):
    if Track_Mode != None:
        if Delta_s == None:
            print( "ds cannot be undefined when Trancink Mode is", Track_Mode )
            exit()
        ParticleTracking( Beam, BeamLine, Track_Mode, Delta_s  )
    else:
        if Delta_s == None:
            BeamTracking( Beam, BeamLine )
        else:
            ParticleTracking( Beam, BeamLine, 0, Delta_s  )

def ParticleTracking( Beam, BeamLine, Track_Mode, Delta_s ):
    if Track_Mode == 0:
        NumberOfElements = len( BeamLine )
        ElementsPositions = [0.]
        for i in range( NumberOfElements ):
            if not( BeamLine[i] in BeamLine[0:i] ):
                BeamLine[i].reDefineMatrix( Delta_s )
            ElementsPositions.append( round( ElementsPositions[-1] + BeamLine[i].Length, 5) )

            if BeamLine[i].Length / Delta_s != int( BeamLine[i].Length / Delta_s ):
                print("!! Step size (dz) is greater than or equal to one or more beam line elements!!\n")
                exit()
                
        if NumberOfElements == 0:
            print( "!! Beamline doesn't have any element !!\n" )
            exit()
        else:
            NumberOfParticles = Beam.NumberOfParticles
            LengthOfBeamline = ElementsPositions[-1]
        
            newPositions = np.array( [ [ [0]*NumberOfParticles, [0]*NumberOfParticles, [0]*NumberOfParticles ] ] * round( LengthOfBeamline / Delta_s ) )   
            Beam.BeamPositions=np.append(Beam.BeamPositions,newPositions, axis=0)
                        
            iteration = 1
            printProgressBar( 0, LengthOfBeamline )
            for Length in np.arange( Delta_s, round( LengthOfBeamline + Delta_s, 5 ), Delta_s ):
                
                printProgressBar( Length, LengthOfBeamline )
            
                mean_z = np.mean( Beam.BeamMatrix[4,:] )
                RelativisticGammas = np.around( Beam.BeamMatrix[5,:] / Beam.ParticleMass + 1, 5 )
            
                dz = np.around( Beam.BeamMatrix[4,:] - mean_z )
                dE = np.around( Beam.BeamMatrix[5,:] - Beam.BeamEnergy ) / Beam.BeamEnergy
                tmp_Beam = np.copy( Beam.BeamMatrix )
                tmp_Beam[4,:] = dz
                tmp_Beam[5,:] = dE
            
                for i in range( NumberOfParticles ):
                    for j in range( NumberOfElements ):
                        if Beam.BeamMatrix[4,i] < ElementsPositions[j+1]:
                            BeamLine[j].Matrix[4,5] = Length / RelativisticGammas[i]**2                        
                            TransportedParticle = BeamLine[j].Matrix @ tmp_Beam[:,i]
                            TransportedParticle[4] = round( Beam.BeamMatrix[4,i] + Delta_s, 5 )
                            TransportedParticle[5] = Beam.BeamMatrix[5,i]

                            Beam.BeamMatrix[:,i] = TransportedParticle
                            Beam.BeamPositions[iteration,:,i]=np.array([ TransportedParticle[0], TransportedParticle[2], TransportedParticle[4] ])
                        
                            break
                iteration += 1
                calcTwissParameters( Beam )
                
    if Track_Mode == 1:
        pass

def BeamTracking( Beam, BeamLine ):
    NumberOfParticles = Beam.NumberOfParticles
    NumberOfElements = len( BeamLine )
    newPositions = np.array( [ [ [0]*NumberOfParticles, [0]*NumberOfParticles, [0]*NumberOfParticles ] ] * NumberOfElements )
    Beam.BeamPositions=np.append(Beam.BeamPositions,newPositions, axis=0)
        
    printProgressBar( 0, NumberOfElements )
    for j in range( NumberOfElements ):

        printProgressBar( j+1, NumberOfElements )
        
        mean_z = np.mean( Beam.BeamMatrix[4,:] )
        RelativisticGammas = np.around( Beam.BeamMatrix[5,:] / Beam.ParticleMass + 1, 5 )
            
        dz = np.around( Beam.BeamMatrix[4,:] - mean_z )
        dE = np.around( Beam.BeamMatrix[5,:] - Beam.BeamEnergy ) / Beam.BeamEnergy
        tmp_Beam = np.copy( Beam.BeamMatrix )
        tmp_Beam[4,:] = dz
        tmp_Beam[5,:] = dE
            
        for i in range( NumberOfParticles ):
            BeamLine[j].Matrix[4,5] = BeamLine[j].Length / RelativisticGammas[i]**2                        
            TransportedParticle = BeamLine[j].Matrix @ tmp_Beam[:,i]
            TransportedParticle[4] = round( Beam.BeamMatrix[4,i] + BeamLine[j].Length, 5 )
            TransportedParticle[5] = Beam.BeamMatrix[5,i]

            Beam.BeamMatrix[:,i] = TransportedParticle
            Beam.BeamPositions[j+1,:,i]=np.array([ TransportedParticle[0], TransportedParticle[2], TransportedParticle[4] ])
            
        calcTwissParameters( Beam )
