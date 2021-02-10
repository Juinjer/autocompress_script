#!/usr/bin/env python3

import os
import time
from keyboard import press
input = "/home/ajuin/Downloads"
output ="/home/ajuin/Downloads/out"

files = []
processing = []
while 1:
    for file in os.listdir(input + "/in"):
            if file.endswith(".mp4") and file not in files and file not in processing:
                    files.append(file)
    if len(files)>0 and len(processing)<1:
        first = files.pop()
        processing.append(first)
        st = "HandBrakeCLI -i {0}/in/{1} -o {2}/{1} --preset-import-file {0}/Stef_test_nvid.json -Z 'Stef_test_nvid'".format(input,first,output)
        os.system(st)
        print(st)
        #time.sleep(round(duration/2))
        press('enter')
        processing.pop()
        os.system("rm {0}/in/{1}".format(input,first))
    else :
        time.sleep(30)
