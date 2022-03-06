# APRICOT 
>**Particle Beam Tracking Module** for python


APRICOT is a python module that simulates the behavior of particle beams in electromagnetic fields as they pass through various beamline elements and calculates beamline parameters at the end of the beamline.

The module needs **numpy** (vector analysis), **matplotlib** (visualization) and **scipy** (small interval calculation) modules to work.

## 1. Beam Generation
APRICOT has two different beam generation methods: random beam generator and electron gun beam generator.

### 1.1. Random Beam
Random beam generation is provided by the **RandomBeam** function in the Functions library. Here is the usage of the parameters required by the RandomBeam function:

```py
ParticleTpye = "electron"   # particle type
NumberOfParticles = 10000   # Number of particles
BeamEnergy = 250e3          # beam energy (keV)
x_rms = 0.003               # RMS beam size of x (m)  
y_rms = 0.003               # RMS beam size of y (m) 
Emittance_x = 1e-6          # emittance x (mrad)
Emittance_y = 1e-6          # emittance y (mrad)
Alpha_x = -0.50             # alpha x
Alpha_y = -0.50             # alpha y
```
After these parameters are determined, random beam generation is provided as follows. 
```py 
RandomBeam( ParticleTpye, NumberOfParticles, BeamEnergy, x_rms, y_rms, Emittance_x, Emittance_y, Alpha_x, Alpha_y  )
```

The function will return the generated beam object as return value.

### 1.2. Electron Gun
For beam generation with the electron gun, the necessary parameters should be defined as follows:
```py
NumberOfParticles = 10000   # Number of particles
r_Cathode = 0.05            # Cathode radius (m)
Temperature = 4000          # Cathode temperature (C)
Voltage = 10                # Gun voltage (V)
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
