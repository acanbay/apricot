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
APRICOT currently has **Drift Tube**, **Quadrupole Magnet**, **Dipole Magnet** and **Solenoid** beamline components. In addition to these, it also allows the production of **lattice**.

### 2.1. Drift Tube
The following parameters are used to create Drift Tube:

```py
Name    # Name of the element
Length  # Length of the element
```

Drift Tube object is created from the DriftTube class in the BeamLineComponent library as follows:
```py
DriftTube(Name, Length)
```

### 2.2. Quadrupole Magnet
The following parameters are used to create Quadrupole Magnet:

```py
Name      # Name of the element
Length    # Length of the element
Strength  # Strength of the element
```

Quadrupole Magnet object is created from the QuadrupoleMagnet class in the BeamLineComponent library as follows:
```py
QuadrupoleMagnet(Name, Length, Strength)
```

### 2.3. Dipole Magnet
The following parameters are used to create Quadrupole Magnet:

```py
Name      # Name of the element
Length    # Length of the element
Angle     # Angle expected to bend
ybend     # Enter 1 to bend in the y-axis (not mandatory)
```

Quadrupole Magnet object is created from the DipoleMagnet class in the BeamLineComponent library as follows:
```py
DipoleMagnet(Name, Length, Angle, ybend)
```

### 2.4. Solenoid
The following parameters are used to create Solenoid:

```py
Name      # Name of the element
Length    # Length of the element
Strength  # Strength of the element
```

Solenoid object is created from the Solenoid class in the BeamLineComponent library as follows:
```py
Solenoid(Name, Length, Strength)
```

## 3. Beamline
After the beamline components are defined, the beamline must be aligned. The following parameters are used to create beamline:

```py
Name      # Name of the element
Elements  # Elements in beamline (in list form, in brackets)
```

The beamline object is generated from the BeamLine class of the BeamLine library as follows:
```py
Beamline(Name, Elements)
```

To pass the beam in the beamline, the TransportBeam function from the Functions library is used.
```py
TransportBeam( Beam, beamline.Elements )
```
This proceeds by specifying the parameters of the beam at the end of each element. If the behavior inside the elements is also to be calculated, the step size (m) for the z-axis must be determined in the code.

```py
TransportBeam( Beam, beamline.Elements, dz )
```
**!** The step length must be the exact divisor of the element lengths **!**
### 3.1. FODO Lattice
The following parameters are needed to create a FODO lattice:

```py
Name                      # Name of the element
DriftLength               # Length of the drift tubes
QuadrupoleMagnetLength    # Length of the quadrupole magnets
QuadrupoleMagnetStrength  # Strength of the quadrupole magnets
```

The FODO object is generated from the FODO class of the BeamLine library as follows:
```py
Beamline(Name, DriftLength, QuadrupoleMagnetLength, QuadrupoleMagnetStrength)
```
**If step size is used for FODO:** step size should be the exact divisor of half of the quadrupole magnet length and the drift tube length.

## 4. Outputs
Outputs library is used for outputs.

### 4.1. Beam Graphs
The beam graphs can be stored with the getBeam function. getBeam needs the following parameters:

```py
Beam   # Beam object
path   # File path to save graphics (not mandatory)
tag    # name tag (not mandatory)
```
The default value for **path** is the file path of the script.

By using the getBeam function as below, beam shape and phase space graphs are created.
```py
getBeam(Beam, path, tag)
```
**Examples:**

![alt text](https://github.com/lcnby/apricot/blob/main/output_samples/Initial_BeamShape_xy.png) ![alt text](https://github.com/lcnby/apricot/blob/main/output_samples/Initial_PhaseSpace.png)


### 4.1. Position Graphs
