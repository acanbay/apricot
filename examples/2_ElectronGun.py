import apricot.Gun as gun
import apricot.outputs as out

NumberOfParticles = 10000   # Number of particles
r_Cathode = 0.05            # Cathode radius (m)
Temperature = 4000          # Cathode temperature (C)
Voltage = 10                # Gun voltage (V)

# Creating an electron gun
egun = gun.ElectronGun(r_Cathode, Temperature, Voltage)
# Beam generation from electron gun
Beam = egun.GenerateBeam(NumberOfParticles)
# Creating beam graphs
out.getBeam( Beam, path="outputs", tag="Initial" )