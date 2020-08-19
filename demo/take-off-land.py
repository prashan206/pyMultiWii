#!/usr/bin/env python

"""take-off-land.py: Script to demonstrate takeoff, position hold and land"""

__author__ = "Guru Prashanth Sridhar"
__copyright__ = "Copyright 2020 trakster.de"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Guru Prashanth Sridhar"
__email__ = "prashanth.5491@gmail.com"
__status__ = "Development"

from pymultiwii import MultiWii
from sys import stdout

if __name__ == "__main__":

    board = MultiWii("/dev/ttyACM0")
    pitch=1500
    roll=1500
    rotate=1500
    throttle=1000
   
    try:
        board.arm()
        while True:
            board.getData(MultiWii.RAW_IMU)
            #print (board.attitude) #uncomment for regular printing

            # Fancy printing (might not work on windows...)
            message = "ax = {:+.0f} \t ay = {:+.0f} \t az = {:+.0f} gx = {:+.0f} \t gy = {:+.0f} \t gz = {:+.0f} mx = {:+.0f} \t my = {:+.0f} \t mz = {:+.0f} \t elapsed = {:+.4f} \t" .format(float(board.rawIMU['ax']),float(board.rawIMU['ay']),float(board.rawIMU['az']),float(board.rawIMU['gx']),float(board.rawIMU['gy']),float(board.rawIMU['gz']),float(board.rawIMU['mx']),float(board.rawIMU['my']),float(board.rawIMU['mz']),float(board.attitude['elapsed']))
            stdout.write("\r%s" % message )
            stdout.flush()
            data = [roll,pitch,rotate,throttle]
            board.sendCMD(8,MultiWii.SET_RAW_RC,data)

            # End of fancy printing
        board.disarm()
    except Exception,error:
        print ("Error on Main: "+str(error))
        board.disarm()       
