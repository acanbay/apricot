from . import Statistics as st
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.transforms as transforms
import numpy as np

def BeamShape_xy( beam, path=None, tag=None ):
    if path==None:
        path="."

    x = np.copy( beam.BeamMatrix[0,:] ) * 1e3 # m to mm
    y = np.copy( beam.BeamMatrix[2,:] ) * 1e3 # m to mm

    plt.figure( figsize = ( 6, 6 ) )

    plt.subplot( 2, 2, 1 )
    plt.hist( x, 50, color = 'darkblue' )
    plt.xlim( x.min(), x.max() )
    plt.ylabel( r'$N_P$' )
    plt.xticks( [ ] )

    plt.subplot( 2, 2, 2 )
    plt.axis( 'off' )
    plt.text( 0.3, 0.55, r'$\sigma_{}$={:.3} mm'.format( '{rms,x}', st.myrms( x ) ), fontsize = 10 )
    plt.text( 0.3, 0.45, r'$\sigma_{}$={:.3} mm'.format( '{rms,y}', st.myrms( y ) ), fontsize = 10 )

    plt.subplot( 2, 2, 3 )
    plt.hist2d( x, y, bins = 100, norm = mpl.colors.LogNorm(), cmap = plt.cm.jet )
    #plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
    plt.xlim( x.min(), x.max() )
    plt.ylim( y.min(), y.max() )
    plt.xlabel( 'x (mm)' )
    plt.ylabel( 'y (mm)' )

    plt.text( x.min(), y.min()-y.min()*0.01, r'APRICOT',fontsize = 13, fontstyle="oblique", weight='bold', alpha=0.44 )

    plt.subplot( 2, 2, 4 )
    plt.ylim( y.min(), y.max() )
    plt.hist( y, 50, color = 'darkblue', orientation = u'horizontal' )
    plt.yticks( [ ] )
    plt.xlabel( r'$N_P$' )
    plt.subplot( 2, 2, 3 )

    plt.tight_layout()
    plt.subplots_adjust( wspace=0.005, hspace=0.005 )
    
    #plt.show()
    if tag == None:
        plt.savefig(path+'/BeamShape_xy.png',dpi=200)
    else: 
        plt.savefig(path+"/"+tag+"_BeamShape_xy.png",dpi=200)
    plt.close()

def BeamShape_yz( beam, path=None, tag=None ):
    if path==None:
        path="."

    y = np.copy( beam.BeamMatrix[2,:] ) * 1e3 # m to mm
    z = np.copy( beam.BeamMatrix[4,:] ) * 1e3 # m to mm
    z = z - st.mymean(z)

    plt.figure( figsize = ( 6, 6 ) )

    plt.subplot( 2, 2, 1 )
    plt.hist( y, 50, color = 'darkblue' )
    plt.xlim( y.min(), y.max() )
    plt.ylabel( r'$N_P$' )
    plt.xticks( [ ] )

    plt.subplot( 2, 2, 2 )
    plt.axis( 'off' )
    plt.text( 0.3, 0.55, r'$\sigma_{}$={:.3} mm'.format( '{rms,y}', st.myrms( y ) ), fontsize = 10 )
    plt.text( 0.3, 0.45, r'$\sigma_{}$={:.3} mm'.format( '{rms,z}', st.myrms( z ) ), fontsize = 10 )

    plt.subplot( 2, 2, 3 )
    plt.hist2d( y, z, bins = 100, norm = mpl.colors.LogNorm(), cmap = plt.cm.jet )
    #plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
    plt.xlim( y.min(), y.max() )
    plt.ylim( z.min(), z.max() )
    plt.xlabel( 'y (mm)' )
    plt.ylabel( 'z (mm)' )

    plt.text( y.min(), z.min()-z.min()*0.01, r'APRICOT',fontsize = 13, fontstyle="oblique", weight='bold', alpha=0.44 )

    plt.subplot( 2, 2, 4 )
    plt.ylim( z.min(), z.max() )
    plt.hist( z, 50, color = 'darkblue', orientation = u'horizontal' )
    plt.yticks( [ ] )
    plt.xlabel( r'$N_P$' )
    plt.subplot( 2, 2, 3 )

    plt.tight_layout()
    plt.subplots_adjust( wspace=0.005, hspace=0.005 )
    
    #plt.show()
    if tag == None:
        plt.savefig(path+'/BeamShape_yz.png',dpi=200)
    else: 
        plt.savefig(path+"/"+tag+"_BeamShape_yz.png",dpi=200)
    plt.close()

def BeamShape_zx( beam, path=None, tag=None ):
    if path==None:
        path="."

    z = np.copy( beam.BeamMatrix[4,:] ) * 1e3 # m to mm
    z = z - st.mymean(z)
    x = np.copy( beam.BeamMatrix[0,:] ) * 1e3 # m to mm

    plt.figure( figsize = ( 6, 6 ) )

    plt.subplot( 2, 2, 1 )
    plt.hist( z, 50, color = 'darkblue' )
    plt.xlim( z.min(), z.max() )
    plt.ylabel( r'$N_P$' )
    plt.xticks( [ ] )

    plt.subplot( 2, 2, 2 )
    plt.axis( 'off' )
    plt.text( 0.3, 0.55, r'$\sigma_{}$={:.3} mm'.format( '{rms,z}', st.myrms( z ) ), fontsize = 10 )
    plt.text( 0.3, 0.45, r'$\sigma_{}$={:.3} mm'.format( '{rms,x}', st.myrms( x ) ), fontsize = 10 )

    plt.subplot( 2, 2, 3 )
    plt.hist2d( z, x, bins = 100, norm = mpl.colors.LogNorm(), cmap = plt.cm.jet )
    #plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
    plt.xlim( z.min(), z.max() )
    plt.ylim( x.min(), x.max() )
    plt.xlabel( 'z (mm)' )
    plt.ylabel( 'x (mm)' )

    plt.text( z.min(), x.min()-x.min()*0.01, r'APRICOT',fontsize = 13, fontstyle="oblique", weight='bold', alpha=0.44 )

    plt.subplot( 2, 2, 4 )
    plt.ylim( x.min(), x.max() )
    plt.hist( x, 50, color = 'darkblue', orientation = u'horizontal' )
    plt.yticks( [ ] )
    plt.xlabel( r'$N_P$' )
    plt.subplot( 2, 2, 3 )

    plt.tight_layout()
    plt.subplots_adjust( wspace=0.005, hspace=0.005 )
    
    #plt.show()
    if tag == None:
        plt.savefig(path+'/BeamShape_zx.png',dpi=200)
    else: 
        plt.savefig(path+"/"+tag+"_BeamShape_zx.png",dpi=200)
    plt.close()

def PhaseSpace(beam, path=None, tag=None):
    if path==None:
        path="."

    x = np.copy( beam.BeamMatrix[0,:] ) * 1e3
    xp = np.copy( beam.BeamMatrix[1,:] ) * 1e3
    y = np.copy( beam.BeamMatrix[2,:] ) * 1e3
    yp = np.copy( beam.BeamMatrix[3,:] ) * 1e3

    plt.figure( figsize = ( 6, 3 ) )

    ax1 = plt.subplot( 1, 2, 1 )

    ax1.hist2d( x, xp, bins = 100, norm = mpl.colors.LogNorm(), cmap = plt.cm.jet )

    ax1.axvline( c = 'grey', lw = 1 )
    ax1.axhline( c = 'grey', lw = 1 )

    confidence_ellipse( x, xp, ax1, edgecolor='red' )
    ax1.scatter( 0, 0, c='red', s=1 )
    ax1.set_xlabel( "x (mm)" )
    ax1.set_ylabel( "x' (mrad)" )
    plt.text( x.min(), xp.min()-xp.min()*0.01, r'APRICOT',fontsize = 10, fontstyle="oblique", weight='bold', alpha=0.44 )

    ax2 = plt.subplot( 1, 2, 2)

    ax2.hist2d( y, yp, bins = 100, norm = mpl.colors.LogNorm(), cmap = plt.cm.jet )

    ax2.axvline( c = 'grey', lw = 1 )
    ax2.axhline( c = 'grey', lw = 1 )

    confidence_ellipse( y, yp, ax2, edgecolor = 'red' )
    ax2.scatter( 0, 0, c = 'red', s = 1 )
    ax2.set_xlabel( "y (mm)" )
    ax2.set_ylabel( "y' (mrad)" )
    plt.text( y.min(), yp.min()-yp.min()*0.01, r'APRICOT',fontsize = 10, fontstyle="oblique", weight='bold', alpha=0.44 )

    plt.tight_layout()
    
    #plt.show()
    if tag == None:
        plt.savefig(path+'/PhaseSpace.png',dpi=200)
    else: 
        plt.savefig(path+"/"+tag+"_PhaseSpace.png",dpi=200)
    plt.close()

def confidence_ellipse( x, y, ax, n_std = 2.7, facecolor = 'none', **kwargs ):
    if x.size != y.size:
        raise ValueError( "x and y must be the same size" )

    cov = np.cov( x, y )
    pearson = cov[0, 1] / np.sqrt( cov[0, 0] * cov[1, 1] )
    ell_radius_x = np.sqrt( 1 + pearson )
    ell_radius_y = np.sqrt( 1 - pearson )
    ellipse = mpatches.Ellipse( ( 0, 0 ), width = ell_radius_x * 2, height = ell_radius_y * 2, facecolor = facecolor, linewidth = 3, **kwargs )

    scale_x = np.sqrt( cov[0, 0] ) * n_std
    mean_x = st.mymean( x )

    scale_y = np.sqrt( cov[1, 1] ) * n_std
    mean_y = st.mymean( y )

    transf = transforms.Affine2D() \
        .rotate_deg( 45 ) \
        .scale( scale_x, scale_y ) \
        .translate( mean_x, mean_y )

    ellipse.set_transform( transf + ax.transData )
    return ax.add_patch( ellipse )

def PositionGraph( Beam, beamline, path=None, tag=None ):
    if path==None:
        path="."

    x =  Beam.BeamPositions[:,0]* 1e3
    y =  Beam.BeamPositions[:,1]* 1e3
    z =  Beam.BeamPositions[:,2]
    
    x_max = np.max( x, 1 )
    x_min = np.min( x, 1 )
    
    y_max = np.max( y, 1 )
    y_min = np.min( y, 1 )
    
    mean_z = np.mean( z, 1 )
    
    z_max=0
    for component in beamline:
        z_max+=component.Length

    DriftTube_color=(0, 0, 1, 0.1)
    QuadrupoleMagnet_color=(1, 0, 0, 0.1)
    DipoleMagnet_color=(0, 1, 0, 0.1)
    Solenoid_color=(1, 0.5, 0, 0.1)
    
    plt.subplot(2,1,1)
    Position=0
    for component in beamline:
        min_ = Position
        max_ = Position + component.Length
        Position = max_
        if component.Type=="DriftTube":
            plt.axvspan(min_, max_, color=DriftTube_color)
        elif component.Type=="QuadrupoleMagnet":
            plt.axvspan(min_, max_, color=QuadrupoleMagnet_color)
        elif component.Type=="DipoleMagnet":
            plt.axvspan(min_, max_, color=DipoleMagnet_color)
        elif component.Type=="Solenoid":
            plt.axvspan(min_, max_, color=Solenoid_color)

    plt.plot( mean_z, x_max, "b", label="x" )
    plt.plot( mean_z, x_min, "b" )
    plt.plot( mean_z, y_max, "r", label="y" )
    plt.plot( mean_z, y_min, "r" )
    plt.xlabel( 'z (m)' )
    plt.ylabel( 'x, y (mm)' )
    plt.xlim(0,mean_z[-1])
    plt.legend( loc="best", fontsize=8, facecolor="None", edgecolor="None" )

    min_ = min([x_min.min(),y_min.min()])
    min_=min_+min_*0.09
    plt.text( 0, min_, r'APRICOT',fontsize = 10, fontstyle="oblique", weight='bold', alpha=0.44 )

    plt.subplot(2,1,2)
    plt.axis( 'off' )

    N_Components=[0,0,0,0]
    Component_Name=[]
    Component_Color=[]
    for component in beamline:
        if component.Type=="DriftTube":
            N_Components[0]+=1
        elif component.Type=="QuadrupoleMagnet":
            N_Components[1]+=1   
        elif component.Type=="DipoleMagnet":
            N_Components[2]+=1
        elif component.Type=="Solenoid":
            N_Components[3]+=1

    Component_Name=["Drift Tube","Quadrupole Magnet","Dipole Magnet","Solenoid"]
    Component_Color=[DriftTube_color,QuadrupoleMagnet_color,DipoleMagnet_color,Solenoid_color]
    
    x_position=0.33
    y_position=0.79
    y_diff=0.11
    for i in range(len(N_Components)):
        if N_Components[i]>0:
            rectangle = plt.Rectangle((x_position,y_position), 0.1, 0.1, fc=(Component_Color[i]),ec="black")
            plt.gca().add_patch(rectangle)
            plt.text( x_position+0.04, y_position+0.02, r'{}'.format(N_Components[i]), fontsize = 9 )
            plt.text( x_position+0.11, y_position+0.02, Component_Name[i], fontsize = 9 )
            plt.gca()
            y_position-=y_diff
        
    plt.tight_layout()
    #plt.show()
    if tag == None:
        plt.savefig(path+'/BeamPosition.png',dpi=200)
    else: 
        plt.savefig(path+"/"+tag+"_BeamPosition",dpi=200)
    plt.close()
    
def BetaFunctions( Beam, beamline, path=None, tag=None ):
    if path==None:
        path="."
        
    Beta_x = np.sqrt( Beam.TwissParameters[:,1] )
    Beta_y = np.sqrt( Beam.TwissParameters[:,3] )
    mean_z =  np.mean(Beam.BeamPositions[:,2],1)
    
    z_max=0
    for component in beamline:
        z_max+=component.Length

    DriftTube_color=(0, 0, 1, 0.1)
    QuadrupoleMagnet_color=(1, 0, 0, 0.1)
    DipoleMagnet_color=(0, 1, 0, 0.1)
    Solenoid_color=(1, 0.5, 0, 0.1)
    
    plt.subplot(2,1,1)
    Position=0
    for component in beamline:
        min_ = Position
        max_ = Position + component.Length
        Position = max_
        if component.Type=="DriftTube":
            plt.axvspan(min_, max_, color=DriftTube_color)
        elif component.Type=="QuadrupoleMagnet":
            plt.axvspan(min_, max_, color=QuadrupoleMagnet_color)
        elif component.Type=="DipoleMagnet":
            plt.axvspan(min_, max_, color=DipoleMagnet_color)
        elif component.Type=="Solenoid":
            plt.axvspan(min_, max_, color=Solenoid_color)
    
    plt.plot(mean_z,Beta_x,"b",label=r"$\beta_x$" )
    plt.plot(mean_z,Beta_y,"r",label=r"$\beta_y$" )
    plt.xlabel( 'z (m)' )
    plt.ylabel( r'$\beta$ (mm)' )
    plt.xlim(0,mean_z[-1])
    plt.legend( loc="best", fontsize=8, facecolor="None", edgecolor="None" )

    min_ = min([Beta_x.min(),Beta_y.min()])
    min_=min_-min_*0.02
    plt.text( 0, min_, r'APRICOT',fontsize = 10, fontstyle="oblique", weight='bold', alpha=0.44 )

    plt.subplot(2,1,2)
    plt.axis( 'off' )

    N_Components=[0,0,0,0]
    Component_Name=[]
    Component_Color=[]
    for component in beamline:
        if component.Type=="DriftTube":
            N_Components[0]+=1  
        elif component.Type=="QuadrupoleMagnet":
            N_Components[1]+=1
        elif component.Type=="DipoleMagnet":
            N_Components[2]+=1
        elif component.Type=="Solenoid":
            N_Components[3]+=1

    Component_Name=["Drift Tube","Quadrupole Magnet","Dipole Magnet","Solenoid"]
    Component_Color=[DriftTube_color,QuadrupoleMagnet_color,DipoleMagnet_color,Solenoid_color]
    
    x_position=0.33
    y_position=0.79
    y_diff=0.11
    for i in range(len(N_Components)):
        if N_Components[i]>0:
            rectangle = plt.Rectangle((x_position,y_position), 0.1, 0.1, fc=(Component_Color[i]),ec="black")
            plt.gca().add_patch(rectangle)
            plt.text( x_position+0.04, y_position+0.02, r'{}'.format(N_Components[i]), fontsize = 9 )
            plt.text( x_position+0.11, y_position+0.02, Component_Name[i], fontsize = 9 )
            plt.gca()
            y_position-=y_diff
        
    plt.tight_layout()
    #plt.show()
    if tag == None:
        plt.savefig(path+'/BetaFunction.png',dpi=200)
    else: 
        plt.savefig(path+"/"+tag+"_BetaFunction",dpi=200)
    plt.close()