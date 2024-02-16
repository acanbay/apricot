import apricotbl.Outputs as out
import apricotbl.Functions as fn

ParticleTpye = "electron"   # particle type
NumberOfParticles = 10000   # Number of particles
BeamEnergy = 250e3          # beam energy (keV)
x_rms = 0.003               # RMS beam size of x (m)  
y_rms = 0.003               # RMS beam size of y (m) 
Emittance_x = 1e-6          # emittance x (m.rad)
Emittance_y = 1e-6          # emittance y (m.rad)
Alpha_x = -0.50             # alpha x
Alpha_y = -0.50             # alpha y

# Random beam generation
Beam = fn.RandomBeam( ParticleTpye, NumberOfParticles, BeamEnergy, x_rms, y_rms, Emittance_x, Emittance_y, Alpha_x, Alpha_y  )
# Creating beam graphs
out.getBeam( Beam, path="outputs", tag="Initial" )
