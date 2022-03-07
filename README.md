# APRICOT 
>**Particle Tracking Module** for python


APRICOT is a python module that simulates the behavior of particle beams in electromagnetic fields as they pass through various beamline elements and calculates beamline parameters at the end of the beamline.

The module needs **numpy** (vector analysis), **matplotlib** (visualization) and **scipy** (small interval calculation) modules to work.

## 1. Beam Generation
APRICOT has two different beam generation methods: random beam generator and electron gun beam generator.

### 1.1. Random Beam
Random beam generation is provided by the **RandomBeam** function in the Functions library. Here is the usage of the parameters required by the RandomBeam function:

```py
ParticleTpye        # 'electron', 'proton' or 'muon'
NumberOfParticles   # Number of particles
BeamEnergy          # Beam energy (keV)
x_rms               # RMS beam size of x (m)  
y_rms               # RMS beam size of y (m) 
z_rms               # RMS beam size of y (m) (not mandatory)
Emittance_x         # Emittance x (mrad)
Emittance_y         # Emittance y (mrad)
Alpha_x             # Alpha x
Alpha_y             # Alpha y
dE                  # Energy Spread (not mandatory)
```
After these parameters are determined, random beam generation is provided as follows. 
```py 
RandomBeam(ParticleTpye, NumberOfParticles, BeamEnergy, x_rms, y_rms, Emittance_x, Emittance_y, Alpha_x, Alpha_y, z_rms, dE)
```

The function will return the generated beam object as return value.

### 1.2. Electron Gun
For beam generation with the electron gun, the necessary parameters should be defined as follows:
```py
NumberOfParticles   # Number of particles
r_Cathode           # Cathode radius (m)
Temperature         # Cathode temperature (C)
Voltage             # Gun voltage (V)
```

Then the egun is created with the ElectronGun class in the Gun library:
```py
egun = ElectronGun(r_Cathode, Temperature, Voltage)
```

Finally, the egun's GenerateBeam function is called.
```py
egun.GenerateBeam(NumberOfParticles)
```

The function will return the generated beam object as return value.

## 2. Beamline Elements
### 2.1. Drift Tube
