import apricotbl.BeamlineComponents as blc
import apricotbl.Beamline as bl
import apricotbl.Functions as fn
import apricotbl.Outputs as out

ParticleTpye = "electron"   # particle type
NumberOfParticles = 10000   # number of particle
BeamEnergy = 250e3          # beam energy keV
x_rms = 0.003               # sigma_x    m  
y_rms = 0.003               # sigma_y    m  
Emittance_x = 1e-6          # emittance x m.rad
Emittance_y = 1e-6          # emittance y m.rad
Alpha_x = -0.50             # alpha x unitless
Alpha_y = -0.50             # alpha y unitless

# Random beam generation
Beam = fn.RandomBeam( ParticleTpye, NumberOfParticles, BeamEnergy, x_rms, y_rms, Emittance_x, Emittance_y, Alpha_x, Alpha_y  )
# Creating beam graphs
out.getBeam( Beam, path="outputs", tag="Initial" )

# Createing a Drift Tube with a length of 0.2 m
drift = blc.DriftTube("drift",0.2)
# Creating a Solenoid with a length of 0.2 m and a power of 400
sole = blc.Solenoid("solenoid",0.2,400)
# Creating beamline
beamline = bl.Beamline( "beamline", [drift,sole] )

# Running beam on beamline
fn.TransportBeam( Beam, beamline.Elements,0.05 )
# Generating the outputs
out.getBeam( Beam, path="outputs", tag="Final" )
out.getBeamPositions( Beam, beamline.Elements, path="outputs/", tag="Final" )
