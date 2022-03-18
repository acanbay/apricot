import apricotbl.Beamline as bl
import apricotbl.Functions as fn
import apricotbl.Outputs as out

ParticleTpye = "electron"   # particle
NumberOfParticles = 10000   # number of particle
BeamEnergy = 250e3          # beam energy keV
x_rms = 0.003               # sigma_x    m  
y_rms = 0.003               # sigma_y    m  

# Createing a FODO Lattice with 2.5 m drift tube and 0.5 m quadrupole magnet (strength = 0.54102)
lattice1 = bl.FODO("FODO",2.5,0.5,0.54102)
# Creating beamline with FODO lattice
beamline = bl.Beamline( "beamline", [lattice1] )

# Proper beam generation with FODO lattice
Beam = lattice1.RandomBeam( ParticleTpye, NumberOfParticles, BeamEnergy, x_rms, y_rms )
# Creating beam graphs
out.getBeam( Beam, path="outputs", tag="Initial" )

# Running beam on beamline
fn.TransportBeam( Beam, beamline.Elements, 0.05 )
# Generating the outputs
out.getBeam( Beam, path="outputs", tag="Final" )
out.getBeamPositions( Beam, beamline.Elements, path="outputs/", tag="Final" )
