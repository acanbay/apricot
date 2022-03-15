import apricot.Beamline as bl
import apricot.BeamlineComponents as blc
import apricot.Functions as fn
import apricot.Outputs as out

ParticleTpye = "electron"   # particle type
NumberOfParticles = 10000   # number of particle
BeamEnergy = 250e3          # beam energy keV
x_rms = 0.003               # sigma_x    m  
y_rms = 0.003               # sigma_y    m  
z_rms = 0.001               # sigma_z    m  

# Createing a FODO Lattice with 2 m drift tube and 0.4 m quadrupole magnet (strength = 0.54102)
lattice1 = bl.FODO("FODO",2,0.4,0.54102)
# Proper beam generation with FODO lattice
Beam = lattice1.RandomBeam( ParticleTpye, NumberOfParticles, BeamEnergy, x_rms, y_rms, z_rms )
# Creating beam graphs
out.getBeam( Beam, path="outputs", tag="Initial" )

# Createing a Drift Tube with a length of 0.2 m
drift = blc.DriftTube("drift",0.2)
# Creating a Dipole Magnet with a length of 0.2 m and 0.1 rad bending angle
dipole = blc.DipoleMagnet("dipole",0.2,0.1)

# Creating beamline
beamline = bl.Beamline( "beamline", [lattice1,drift,dipole,drift] )

# Running beam on beamline
fn.TransportBeam( Beam, beamline.Elements, 0.01)
# Generating the outputs
out.getBeam( Beam, path="outputs", tag="Final" )
out.getBeamPositions( Beam, beamline.Elements, path="outputs/", tag="Final" )