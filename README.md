# APRICOT [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/lcnby/apricot/HEAD)

>**Particle Tracking Module** for python - Ali Can Canbay

APRICOT is a python3 module that simulates the behavior of particle beams in electromagnetic fields as they pass through various beamline elements and calculates beamline parameters at the end of the beamline.

The module needs **numpy** (vector analysis), **matplotlib** (visualization) and **scipy** (small interval calculation) modules to work. Compatible versions of required modules can be installed on your system with the following command:

```
pip install -r requirements.txt
```

<br />

*By clicking the **"launch binder"** button above, you can use APRICOT without any installation on your computer (Tutorials created with jupyter in the examples directory can also be run with binder).*

_____

## 1. Beam Generation
APRICOT has two different beam generation methods: random beam generator and electron gun beam generator.

In both methods, before the beam generation, the information text of the parameters is printed on the terminal screen as follows.
```
Creating beam with parameters below:
        
    Particle Type           : electron
    Number of Particles     : 100000
    Beam Energy (KeV)       : 2.500e+02
    RMS x size (mm)         : 3.000e-06
    RMS y size (mm)         : 3.000e-06
    RMS z size (mm)         : 1.000e-06
    Emittance x (mrad)      : 7.200e-10
    Emittance y (mrad)      : 1.171e-09
    Alpha x                 : 1.169e-16
    Alpha y                 : -1.169e-16
    %Energy Spread          : 0.000e+00
```

### 1.1. Random Beam
Random beam generation is provided by the **RandomBeam** method in the **Functions** module. Here is the usage of the parameters required by the RandomBeam (in **Outputs** module):

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

Then the egun is created with the **ElectronGun** class in the **Gun** module:
```py
egun = ElectronGun(r_Cathode, Temperature, Voltage)
```

Finally, the egun's GenerateBeam method is called.
```py
egun.GenerateBeam(NumberOfParticles)
```

The method will return the generated beam object as return value.

## 2. Beamline Elements
APRICOT currently has **Drift Tube**, **Quadrupole Magnet**, **Dipole Magnet** and **Solenoid** beamline components. In addition to these, it also allows the production of **lattice**.

### 2.1. Drift Tube
The following parameters are used to create Drift Tube:

```py
Name    # Name of the element
Length  # Length of the element
```

Drift Tube object is created from the **DriftTube** class in the **BeamLineComponent** module as follows:
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

Quadrupole Magnet object is created from the **QuadrupoleMagnet** class in the **BeamLineComponent** module as follows:
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

Quadrupole Magnet object is created from the **DipoleMagnet** class in the **BeamLineComponent** module as follows:
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

Solenoid object is created from the **Solenoid** class in the **BeamLineComponent** module as follows:
```py
Solenoid(Name, Length, Strength)
```

## 3. Beamline
After the beamline components are defined, the beamline must be aligned. The following parameters are used to create beamline:

```py
Name      # Name of the element
Elements  # Elements in beamline (in list form, in brackets)
```

The beamline object is generated from the **BeamLine** class of the **BeamLine** module as follows:
```py
Beamline(Name, Elements)
```

To pass the beam in the beamline, the **TransportBeam** method from the **Functios** module is used (assume that BeamLine object is named as beamline).
```py
TransportBeam( Beam, beamline.Elements )
```
This proceeds by specifying the parameters of the beam at the end of each element. If the behavior inside the elements is also to be calculated, the step size (m) for the z-axis must be determined in the code.

```py
TransportBeam( Beam, beamline.Elements, dz )
```
**! The step length must be the exact divisor of the element lengths.** It is recommended that the minimum value of step length should be in millimeters (it can be taken down to 10 microns).

### 3.1. FODO Lattice
The following parameters are needed to create a FODO lattice:

```py
Name                      # Name of the element
DriftLength               # Length of the drift tubes
QuadrupoleMagnetLength    # Length of the quadrupole magnets
QuadrupoleMagnetStrength  # Strength of the quadrupole magnets
```

The FODO object is generated from the **FODO** class of the **BeamLine** module as follows:
```py
Beamline(Name, DriftLength, QuadrupoleMagnetLength, QuadrupoleMagnetStrength)
```
**If step size is used for FODO:** step size should be the exact divisor of half of the quadrupole magnet length and the drift tube length.

## 4. Outputs
Outputs module is used for outputs. 

### 4.1. Beam Graphs
The beam graphs can be stored with the **getBeam** method (in **Outputs** module). getBeam needs the following parameters:

```py
Beam   # Beam object
path   # File path to save graphics (not mandatory)
tag    # Name tag (not mandatory)
```
The default value for **path** is the file path of the script.

By using the getBeam method as below, beam shape and phase space graphs are created. The Beam Position graph gives the beam's length in the x and y axes relative to the z axis (not rms).
```py
getBeam(Beam, path, tag)
```
**Examples:** 7th example

<img src="https://github.com/lcnby/apricot/blob/main/output_samples/Final_BeamShape_xy.png" width="300">  <img src="https://github.com/lcnby/apricot/blob/main/output_samples/Final_PhaseSpace.png" width="300">

### 4.1. Position Graphs
The position graphs can be stored with the **getBeamPositions** method (in **Outputs** module). getBeamPositions needs the following parameters:

```py
Beam                # Beam object
beamline.Elements   # Elements of beamline object
path                # File path to save graphics (not mandatory)
tag                 # Name tag (not mandatory)
```
The default value for **path** is the file path of the script.

By using the getBeamPositions method as below, beam position and beta function graphs are created.
```py
getBeamPositions(Beam, beamline.Elements, path, tag)
```
**Examples:**  7th example

<img src="https://github.com/lcnby/apricot/blob/main/output_samples/Final_BeamPosition.png" width="300"> <img src="https://github.com/lcnby/apricot/blob/main/output_samples/Final_BeamPositionRMSsize.png" width="300">  <img src="https://github.com/lcnby/apricot/blob/main/output_samples/Final_BetaFunction.png" width="300">

getBeamPositions function prints an output with the final state beam parameters as follows:
```
Beam parameters in the final state:
        
    RMS x size (mm)         : 2.870e-06
    RMS y size (mm)         : 3.008e-06
    Emittance x (mrad)      : 7.208e-10
    Emittance y (mrad)      : 1.170e-09
    Beta x (mm)             : 1.143e+01
    Beta y (mm)             : 7.730e+00
```

## 5. Plots
The Graph module can be used if the graphs are to be viewed without saving them. Plots are displayed as follows:

**Beam Graphs:** To look at Beam shape in the xy, yz and zx-axes.
```py 
plotBeamShape_xy(Beam)
```

**Phase Space:** 
```py 
plotPhaseSpace(Beam)
```

**Position Graph:** To look at the behavior of the beam size in the beamline
```py 
plotPositionGraph( Beam, beamline.Elements ):
```

**Position Graph (RMS size):** To look at the behavior of the RMS beam size in the beamline
```py 
plotPositionGraph_RMSsize( Beam, beamline.Elements ):
```
**Beta Function:**
```py 
plotBetaFunctions( Beam, beamline.Elements ):
```
____
