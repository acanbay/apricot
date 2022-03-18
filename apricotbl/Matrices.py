import numpy as np
import math

def DriftMatrix( Length, RelativisticGamma ):
    Matrix = np.eye( 6 )
    Matrix[0,1] = Length
    Matrix[2,3] = Length
    Matrix[4,5] = Length / RelativisticGamma**2
    return Matrix

def QuadrupoleMatrix( NumberOfParticles , Length , strength ):
    
    EyeMatrix = np.eye( 4 )
    Matrix = np.zeros( ( NumberOfParticles, 4, 4 ) )
    for i in range( NumberOfParticles ):
        Matrix[i] = EyeMatrix
    
    if strength >= 0:
        sqrt_k = np.sqrt( strength )
        phi = sqrt_k * Length
            
        cx = math.cos( phi )
        sx = math.sin( phi )
        cy = math.cosh( phi )
        sy = math.sinh( phi )

        Matrix[:,0,0] = cx
        Matrix[:,1,1] = cx
        Matrix[:,0,1] = sx / sqrt_k
        Matrix[:,1,0] = -sqrt_k / sx
        Matrix[:,2,2] = cy
        Matrix[:,3,3] = cy
        Matrix[:,2,3] = sy / sqrt_k
        Matrix[:,3,2] = sqrt_k / sy
    
    else:
        sqrt_k = math.sqrt( -strength )
        phi = sqrt_k * Length
        cx = math.cosh( phi )
        sx = math.sinh( phi )
        cy = math.cos( phi )
        sy = math.sin( phi )
            
        Matrix[:,0,0] = cx
        Matrix[:,1,1] = cx
        Matrix[:,0,1] = sx / sqrt_k
        Matrix[:,1,0] = sqrt_k / sx
    
        Matrix[:,2,2] = cy
        Matrix[:,3,3] = cy
        Matrix[:,2,3] = sy / sqrt_k
        Matrix[:,3,2] = -sqrt_k / sy
    
    return Matrix

def SolenoidMatrix( NumberOfParticles , Length , strength ):
    
    EyeMatrix = np.eye( 4 )
    Matrix = np.zeros( ( NumberOfParticles, 4, 4 ) )
    for i in range( NumberOfParticles ):
        Matrix[i] = EyeMatrix
    
    kl = strength / Length

    c1 = math.cos( kl )
    s1 = math.sin( kl )
    
    C2 = c1 * c1
    S2 = s1 * s1
    SC = s1 * c1

    Matrix[:,0,0] = C2
    Matrix[:,0,1] = SC / strength
    Matrix[:,0,2] = SC
    Matrix[:,0,3] = S2 / strength
    
    Matrix[:,1,0] = -strength * SC
    Matrix[:,1,1] = C2
    Matrix[:,1,2] = -strength * S2
    Matrix[:,1,3] = SC
    
    Matrix[:,2,0] = -SC
    Matrix[:,2,1] = -S2 / strength
    Matrix[:,2,2] = C2
    Matrix[:,2,3] = SC / strength
    
    Matrix[:,3,0] = strength * S2
    Matrix[:,3,1] = -SC
    Matrix[:,3,2] = -strength * SC
    Matrix[:,3,3] = C2
    
    return Matrix