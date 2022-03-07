import numpy as np

def mymean( array ):
    return sum( array ) / len( array )

def myrms( array ):
    return np.sqrt( sum( array**2 ) / len( array ) )

def myvar( array, option=0 ):
    mu = mymean( array )
    if option==0:
        return sum( ( array-mu )**2 ) / ( len( array ) - 1 )
    elif option==1:
        return sum( ( array-mu )**2 ) / ( len(array) )

def mystd( array, option=0 ):
    return np.sqrt( myvar( array, option ))

def mymean2( array1, array2 ):
    mu1=mymean( array1 )
    mu2=mymean( array2 )
    return sum( ( array1-mu1 ) * ( array2-mu2 ) ) / len( array1 )

def myols( array1, array2 ):
    mu1 = mymean( array1 )
    mu2 = mymean( array2 )
    return sum( ( array1-mu1 ) * ( array2-mu2 ) ) / len( array1 ) / sum( ( array1-mu1 )**2 )

