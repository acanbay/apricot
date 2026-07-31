

# APRICOT 

>**Módulo de Seguimiento de Partículas** para Python - Ali Can Canbay

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12569328.svg)](https://zenodo.org/doi/10.5281/zenodo.12569328) 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/acanbay/apricot/HEAD)

<br>

APRICOT es un módulo de python3 que simula el comportamiento de haces de partículas en campos electromagnéticos a medida que pasan a través de diversos elementos de la línea de haz (beamline) y calcula los parámetros de la beamline al final de esta.

**Instalación mediante pip:**

APRICOT se puede instalar ejecutando el siguiente comando en la consola (todos los módulos necesarios se instalarán automáticamente).
```console
pip install apricotbl
```


**Instalación Manual:**

APRICOT requiere los módulos **numpy**, **scipy** y **matplotlib**. Si estos módulos no están instalados, puede instalarlos con el siguiente comando: 
```console
pip install -r requirements.txt
```
*requirements.txt* está disponible en [la página de github de APRICOT](https://github.com/lcnby/apricot/).

Luego, descargue la [última versión](https://github.com/acanbay/apricot/releases/tag/apricotbl-0.1.0) y extráigala. Ingrese a la carpeta extraída y ejecute el siguiente comando mediante la consola:
```console
python setup.py install
```


<br />

*Al hacer clic en el botón **"launch binder"** arriba, puede usar APRICOT sin necesidad de instalarlo en su computadora (Los tutoriales creados con jupyter en el directorio examples también se pueden ejecutar con binder).*

_____

## 1. Generación de Haces
APRICOT cuenta con dos métodos diferentes de generación de haces: generador de haces aleatorios y generador de haces con pistola de electrones.

En ambos métodos, antes de la generación del haz, se imprime en la consola el texto informativo de los parámetros de la siguiente manera.
```
Creando haz con los siguientes parámetros:
        
    Tipo de Partícula           : electron
    Número de Partículas        : 100000
    Energía del Haz (KeV)       : 2.500e+02
    Tamaño RMS x (mm)           : 3.000e-06
    Tamaño RMS y (mm)           : 3.000e-06
    Tamaño RMS z (mm)           : 1.000e-06
    Emittancia x (m.rad)        : 7.200e-10
    Emittancia y (m.rad)        : 1.171e-09
    Alpha x                     : 1.169e-16
    Alpha y                     : -1.169e-16
    % Dispersión de Energía     : 0.000e+00
```

### 1.1. Haz Aleatorio
La generación de haces aleatorios se proporciona mediante el método **RandomBeam** en el módulo **Functions**. A continuación se muestra el uso de los parámetros requeridos por RandomBeam (en el módulo **Outputs**):

```py
ParticleType        # 'electron', 'proton' o 'muon'
NumberOfParticles   # Número de partículas
BeamEnergy          # Energía del haz (keV)
x_rms               # Tamaño RMS del haz en x (m)  
y_rms               # Tamaño RMS del haz en y (m) 
z_rms               # Tamaño RMS del haz en y (m) (no obligatorio)
Emittance_x         # Emittancia x (m.rad)
Emittance_y         # Emittancia y (m.rad)
Alpha_x             # Alpha x
Alpha_y             # Alpha y
dE                  # Dispersión de energía (no obligatorio)
```
Una vez determinados estos parámetros, la generación del haz aleatorio se realiza de la siguiente manera. 
```py 
RandomBeam(ParticleType, NumberOfParticles, BeamEnergy, x_rms, y_rms, Emittance_x, Emittance_y, Alpha_x, Alpha_y, z_rms, dE)
```

La función devolverá el objeto de haz generado como valor de retorno.

### 1.2. Pistola de Electrones
Para la generación de haces con la pistola de electrones, los parámetros necesarios deben definirse de la siguiente manera:
```py
NumberOfParticles   # Número de partículas
r_Cathode           # Radio del cátodo (m)
Temperature         # Temperatura del cátodo (C)
Voltage             # Voltaje de la pistola (V)
```

Luego, el egun se crea con la clase **ElectronGun** en el módulo **Gun**:
```py
egun = ElectronGun(r_Cathode, Temperature, Voltage)
```

Finalmente, se llama al método GenerateBeam del egun.
```py
egun.GenerateBeam(NumberOfParticles)
```

El método devolverá el objeto de haz generado como valor de retorno.

## 2. Elementos de la Beamline
Actualmente, APRICOT cuenta con los componentes de beamline **Drift Tube**, **Quadrupole Magnet**, **Dipole Magnet** y **Solenoid**. Además de estos, también permite la creación de **lattice**.

### 2.1. Drift Tube
Los siguientes parámetros se utilizan para crear un Drift Tube:

```py
Name    # Nombre del elemento
Length  # Longitud del elemento
```

El objeto Drift Tube se crea desde la clase **DriftTube** en el módulo **BeamLineComponent** de la siguiente manera:
```py
DriftTube(Name, Length)
```

### 2.2. Quadrupole Magnet
Los siguientes parámetros se utilizan para crear un Quadrupole Magnet:

```py
Name      # Nombre del elemento
Length    # Longitud del elemento
Strength  # Intensidad del elemento
```

El objeto Quadrupole Magnet se crea desde la clase **QuadrupoleMagnet** en el módulo **BeamLineComponent** de la siguiente manera:
```py
QuadrupoleMagnet(Name, Length, Strength)
```

### 2.3. Dipole Magnet
Los siguientes parámetros se utilizan para crear un Dipole Magnet:

```py
Name      # Nombre del elemento
Length    # Longitud del elemento
Angle     # Ángulo esperado de curvatura
ybend     # Ingrese 1 para curvar en el eje y (no obligatorio)
```

El objeto Dipole Magnet se crea desde la clase **DipoleMagnet** en el módulo **BeamLineComponent** de la siguiente manera:
```py
DipoleMagnet(Name, Length, Angle, ybend)
```

### 2.4. Solenoid
Los siguientes parámetros se utilizan para crear un Solenoid:

```py
Name      # Nombre del elemento
Length    # Longitud del elemento
Strength  # Intensidad del elemento
```

El objeto Solenoid se crea desde la clase **Solenoid** en el módulo **BeamLineComponent** de la siguiente manera:
```py
Solenoid(Name, Length, Strength)
```

## 3. Beamline
Una vez definidos los componentes de la beamline, esta debe alinearse. Los siguientes parámetros se utilizan para crear la beamline:

```py
Name      # Nombre del elemento
Elements  # Elementos en la beamline (en forma de lista, entre corchetes)
```

El objeto beamline se genera desde la clase **BeamLine** del módulo **BeamLine** de la siguiente manera:
```py
Beamline(Name, Elements)
```

Para hacer pasar el haz por la beamline, se utiliza el método **TransportBeam** del módulo **Functios** (asumiendo que el objeto BeamLine se nombró como beamline).
```py
TransportBeam( Beam, beamline.Elements )
```
Esto se realiza especificando los parámetros del haz al final de cada elemento. Si también se desea calcular el comportamiento dentro de los elementos, se debe determinar el tamaño del paso (m) para el eje z en el código.

```py
TransportBeam( Beam, beamline.Elements, dz )
```
**! La longitud del paso debe ser un divisor exacto de las longitudes de los elementos.** Se recomienda que el valor mínimo de la longitud del paso sea en milímetros (se puede reducir hasta 10 micras).

### 3.1. FODO Lattice
Los siguientes parámetros son necesarios para crear un lattice FODO:

```py
Name                      # Nombre del elemento
DriftLength               # Longitud de los tubos de deriva
QuadrupoleMagnetLength    # Longitud de los imanes cuadrupolo
QuadrupoleMagnetStrength  # Intensidad de los imanes cuadrupolo
```

El objeto FODO se genera desde la clase **FODO** del módulo **BeamLine** de la siguiente manera:
```py
FODO(Name, DriftLength, QuadrupoleMagnetLength, QuadrupoleMagnetStrength)
```
**Si se utiliza tamaño de paso para FODO:** el tamaño del paso debe ser un divisor exacto de la mitad de la longitud del imán cuadrupolo y de la longitud del tubo de deriva.

## 4. Outputs
El módulo Outputs se utiliza para las salidas. 

### 4.1. Beam Graphs
Las gráficas del haz se pueden guardar con el método **getBeam** (en el módulo **Outputs**). getBeam necesita los siguientes parámetros:

```py
Beam   # Objeto de haz
path   # Ruta del archivo para guardar las gráficas (no obligatorio)
tag    # Etiqueta de nombre (no obligatorio)
```
El valor predeterminado para **path** es la ruta del archivo del script.

Al utilizar el método getBeam como se muestra a continuación, se crean gráficas de la forma del haz y del espacio de fases. La gráfica de posición del haz muestra la longitud del haz en los ejes x e y en relación con el eje z (no rms).
```py
getBeam(Beam, path, tag)
```
**Ejemplos:** 7º ejemplo

<img src="https://github.com/lcnby/apricot/blob/main/output_samples/Final_BeamShape_xy.png" width="300">  <img src="https://github.com/lcnby/apricot/blob/main/output_samples/Final_PhaseSpace.png" width="300">

### 4.1. Position Graphs
Las gráficas de posición se pueden guardar con el método **getBeamPositions** (en el módulo **Outputs**). getBeamPositions necesita los siguientes parámetros:

```py
Beam                # Objeto de haz
beamline.Elements   # Elementos del objeto beamline
path                # Ruta del archivo para guardar las gráficas (no obligatorio)
tag                 # Etiqueta de nombre (no obligatorio)
```
El valor predeterminado para **path** es la ruta del archivo del script.

Al utilizar el método getBeamPositions como se muestra a continuación, se crean gráficas de posición del haz y de la función beta.
```py
getBeamPositions(Beam, beamline.Elements, path, tag)
```
**Ejemplos:**  7º ejemplo

<img src="https://github.com/lcnby/apricot/blob/main/output_samples/Final_BeamPosition.png" width="300"> <img src="https://github.com/lcnby/apricot/blob/main/output_samples/Final_BeamPositionRMSsize.png" width="300">  <img src="https://github.com/lcnby/apricot/blob/main/output_samples/Final_BetaFunction.png" width="300">

La función getBeamPositions imprime una salida con los parámetros finales del haz de la siguiente manera:
```
Parámetros del haz en el estado final:
        
    Tamaño RMS x (mm)         : 2.870e-06
    Tamaño RMS y (mm)         : 3.008e-06
    Emittancia x (m.rad)      : 7.208e-10
    Emittancia y (m.rad)      : 1.170e-09
    Beta x (mm)               : 1.143e+01
    Beta y (mm)               : 7.730e+00
```

## 5. Plots
El módulo Graph se puede utilizar si se desea visualizar las gráficas sin guardarlas. Las gráficas se muestran de la siguiente manera:

**Beam Graphs:** Para observar la forma del haz en los ejes xy, yz y zx.
```py 
plotBeamShape_xy(Beam)
```

**Phase Space:** 
```py 
plotPhaseSpace(Beam)
```

**Position Graph:** Para observar el comportamiento del tamaño del haz en la beamline
```py 
plotPositionGraph( Beam, beamline.Elements )
```

**Position Graph (RMS size):** Para observar el comportamiento del tamaño RMS del haz en la beamline
```py 
plotPositionGraph_RMSsize( Beam, beamline.Elements )
```
**Beta Function:**
```py 
plotBetaFunctions( Beam, beamline.Elements )
```
____
