#! /usr/bin/python3

import os, subprocess, time
while(True):
    proc = subprocess.Popen(['date','+%a_%d_%b_%y_%H_%M_%S'], stdout=subprocess.PIPE)
    daystring = str(proc.stdout.readline().decode()[0:-1])
    picname = r'/media/ldhagen/Transcend/timelapse/' + daystring + r'.jpg'
    os.system(r'/usr/bin/raspistill -w 680 -h 420 -o ' + picname)
    time.sleep(2)
