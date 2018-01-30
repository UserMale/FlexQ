import sys
import math
import os.path
import argparse

from pylab import *
from numpy.core.numeric import * # imports empty
from matplotlib.pyplot import *  # imports figure
import matplotlib.pyplot as plt  # defines plt

def RadFromDeg( a ): return a * math.pi / 180.0
def DegFromRad( a ): return a * 180.0 / math.pi

#
# Sensor simulation dump format is:
#
#     yawAngle, pitchAngle, distanceFromBase, maximumIncidenceAngle,
#     num visible points, visible sensor extent in basestation x, y, z,
#     trials with a pose, trials with no pose, rotation err, translation err,
#     list of visible sensors
#

def ParseSensorSimLine( L ):
    p = L.split()
    d = {}
    d["yawAngle"] = 0.1 * round( 10.0 * DegFromRad( float( p[0] ) ) )
    d["pitchAngle"] = 0.1 * round( 10.0 * DegFromRad( float(p[1]) ) )
    d["distance"] = float(p[2])
    d["maxIncidence"] = float(p[3])
    d["numVisible"] = int(p[4])
    d["extentX"] = float(p[5])
    d["extentY"] = float(p[6])
    d["extentZ"] = float(p[7])
    d["gotPose"] = int(p[8])
    d["noPose"] = int(p[9])
    d["rotErr"] = DegFromRad( float( p[10] ) )
    d["transErr"] = float(p[11])
    d["visibleSensors"] = [ int(i) for i in p[12:] ]
    return d

def ReadSensorSimFile( filename ):
    simData = []
    for L in open( filename, "rb" ):
        simData.append( ParseSensorSimLine( L ) )
    return simData

def AnglesFromSimData( simData ):
    yawAngles = {}
    pitchAngles = {}
    for d in simData:
        yawAngles[ d[ "yawAngle" ] ] = 1
        pitchAngles[ d[ "pitchAngle" ] ] = 1
    return ( sorted( yawAngles.keys() ), sorted( pitchAngles.keys() ) )


def SetBounds( bTightBounds ):
    global maxValidVisibleSensors, maxValidFailurePercentage, maxValidRotErr, maxValidTransErr
    if bTightBounds:
        maxValidVisibleSensors = 6
        maxValidFailurePercentage = 5.0
        maxValidRotErr = 1.5
        maxValidTransErr = 0.010
    else:
        maxValidVisibleSensors = 6
        maxValidFailurePercentage = 100.0
        maxValidRotErr = 5.0
        maxValidTransErr = 0.030


def FindClosest( targetAngle, angleList ):
    aList = [ -9999.0 ] + angleList + [ 9999.0 ]
    for ( i, a ) in enumerate( aList ):
        if a > targetAngle:
            break
    diffLow = abs( aList[i-1] - targetAngle )
    diffHigh = abs( aList[i] - targetAngle )
    if diffLow < diffHigh:
        return i-2
    else:
        return i-1

def PrintPoseSummary( d ):

    if len( d[ "visibleSensors" ] ) != 0:
        print "    Saw %d sensors:" % ( d[ "numVisible" ], ),
        for s in d[ "visibleSensors" ]:
            print "  %d" % ( s, ),
        print
    else:
        print "    Saw %d sensors." % ( d[ "numVisible" ], )
    print "    Pose failure:  %.2f%%" % ( 100.0 * d["noPose"] / float ( d["gotPose"] + d["noPose"] ) )
    print "    RMS rotation error:  %.2f" % ( d["rotErr"] )
    print "    RMS translation error:  %.4f" % ( d["transErr"] )
    #print "X/Y/Z extent of visible sensors is ( %f %f %f ) millimeters" % ( d["extentX"]*1000, d["extentY"]*1000, d["extentZ"]*1000 )

class GraphClicker:
    def __init__( self, yawAngles, pitchAngles, simData ):
        self.yawAngles = yawAngles
        self.pitchAngles = pitchAngles
        self.simData = simData
    def __call__( self, event ):
        if event.xdata != None and event.ydata != None:
            yawIdx = FindClosest( event.xdata, self.yawAngles )
            pitchIdx = FindClosest( event.ydata, self.pitchAngles )
            print
            d = self.simData[ yawIdx * len(self.pitchAngles) + pitchIdx ]
            print "Clicked at %f, %f on yaw/pitch of ( %f , %f ):" % ( event.xdata, event.ydata, d["yawAngle"] - 180.0, d["pitchAngle"] )
            PrintPoseSummary( d )

def Axes( p, yawAngles, pitchAngles ):
    p.xlabel( "Yaw Angle" )
    p.xticks( arange( round(min(yawAngles)), round(max(yawAngles))+0.0001, 45.0 ) )
    p.ylabel( "Pitch Angle" )
    p.yticks( arange( round(min(pitchAngles)), round(max(pitchAngles))+0.0001, 30.0 ) )

def PlotSensorSim( simData, outputFilename = None ):
    ( yawAngles, pitchAngles ) = AnglesFromSimData( simData )

    simDataDict = {}
    for d in simData:
        simDataDict[ ( d["yawAngle"], d["pitchAngle"] ) ] = d

    yawAngles = [ a - 180.0 for a in yawAngles ]
    pitchAngles = [ a for a in pitchAngles ]

    nYaw = len( yawAngles )
    nPitch = len( pitchAngles )

    deltaAngle = yawAngles[1] - yawAngles[0]

    print "Read in data for %d x %d headset poses." % ( nYaw, nPitch )
    print "Yaw range %.1f to %.1f, Pitch range %.1f to %.1f." % ( min(yawAngles), max(yawAngles), min(pitchAngles), max(pitchAngles) )
    print "Sample angle resolution %.1f degrees." % ( deltaAngle, )

    graphExtent = [ min(yawAngles) - deltaAngle / 2.0, max(yawAngles) + deltaAngle / 2.0, min(pitchAngles) - deltaAngle / 2.0, max(pitchAngles) + deltaAngle / 2.0 ]

    poseChars = []
    errs = []
    for d in simData:
        poseSuccessFrac = 0.0
        poseAttempts = d["gotPose"] + d["noPose"]
        if poseAttempts != 0:
            poseSuccessFrac = float( d["gotPose"] ) / float( poseAttempts )
        minExtent = min( d["extentX"], min( d["extentY"], d["extentZ"] ) )
        poseFailurePercent = 100.0 * ( 1.0 - poseSuccessFrac )
        poseChars.append( ( d["numVisible"], minExtent, poseFailurePercent ) )
        if poseFailurePercent < 90.0:
            rotErr = min( d["rotErr"], maxValidRotErr )
            transErr = min( d["transErr"], maxValidTransErr )
            errs.append( ( rotErr, transErr ) )
        else:
            errs.append( ( 9999.0, 9999.0 ) )

    numVisibleArray = empty( [ nPitch, nYaw ] )
    minExtentArray = empty( [ nPitch, nYaw ] )
    poseFailureArray = empty( [ nPitch, nYaw ] )
    rotErrorArray = empty( [ nPitch, nYaw ] )
    transErrorArray = empty( [ nPitch, nYaw ] )
    for i in range( nYaw ):
        for j in range( nPitch ):
            numVisibleArray[j,i] = poseChars[ i * nPitch + j ][0]
            minExtentArray[j,i] = poseChars[ i * nPitch + j ][1]
            poseFailureArray[j,i] = poseChars[ i * nPitch + j ][2]
            rotErrorArray[j,i] = errs[ i * nPitch + j ][0]
            transErrorArray[j,i] = errs[ i * nPitch + j ][1]

    fig = figure( figsize = ( 20, 10 ) )
    plt.subplots_adjust( left = 0.05, right = 0.95, bottom = 0.05, top = 0.95 )

    fwd_cmap = matplotlib.cm.get_cmap('jet')
    rev_cmap = matplotlib.cm.get_cmap('jet_r')

    subplot( 2, 2, 2 )
    title( "Pose Rotation Error" )
    plt.imshow( rotErrorArray, vmin = 0.0, vmax = maxValidRotErr, extent = graphExtent, interpolation = "nearest", origin = "lower", cmap = fwd_cmap )
    Axes( plt, yawAngles, pitchAngles )
    plt.colorbar()

    subplot( 2, 2, 4 )
    title( "Pose Translation Error" )
    plt.imshow( transErrorArray, vmin = 0.0, vmax = maxValidTransErr, extent = graphExtent, interpolation = "nearest", origin = "lower", cmap = fwd_cmap )
    Axes( plt, yawAngles, pitchAngles )
    plt.colorbar()

    subplot( 2, 2, 1 )
    title( "Number of Visible Sensors" )
    plt.imshow( numVisibleArray, vmin = 0.0, vmax = maxValidVisibleSensors, extent = graphExtent, interpolation = "nearest", origin = "lower", cmap = rev_cmap )
    Axes( plt, yawAngles, pitchAngles )
    plt.colorbar()

    subplot( 2, 2, 3 )
    title( "Initial Pose Possible?" )
    plt.imshow( poseFailureArray, vmin = 0.0, vmax = maxValidFailurePercentage, extent = graphExtent, interpolation = "nearest", origin = "lower", cmap = fwd_cmap )
    Axes( plt, yawAngles, pitchAngles )
    plt.colorbar()

    if outputFilename:
        savefig( outputFilename, transparent = False, facecolor = (0.7,0.7,0.7) )

    gclicker = GraphClicker( yawAngles, pitchAngles, simData )
    cid = fig.canvas.mpl_connect( 'button_press_event', gclicker )

    show()

def main():
    parser = argparse.ArgumentParser( prefix_chars = '-/' )
    parser.add_argument( "filename", help = "sensor placement simulation data filename" )
    parser.add_argument( "/tightbounds", action = "store_true", help = "plot with tighter error bounds for more detail" )
    args = parser.parse_args()
    SetBounds( args.tightbounds )
    simData = ReadSensorSimFile( args.filename )
    basename, extension = os.path.splitext( args.filename )
    outputFilename =  basename + '.png'
    print 'Output will be saved to %s' % ( outputFilename, )
    PlotSensorSim( simData, outputFilename )

if __name__ == "__main__":
    main()
