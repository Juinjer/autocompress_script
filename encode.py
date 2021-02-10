#!/usr/bin/env python3
import getpass
import os
import time
from keyboard import press
inp = "/home/{}/Downloads".format(getpass.getuser())
output ="/home/{}/Downloads/out".format(getpass.getuser())
if not os.path.isdir(inp+ "/in"):
    os.mkdir(inp+"/in")
if not os.path.isdir(output):
    os.mkdir(inp+"/out")

files = []
processing = []
while 1:
    for file in os.listdir(inp + "/in"):
            if file.endswith(".mp4") and file not in files and file not in processing:
                    files.append(file)
    if len(files)>0 and len(processing)<1:
        first = files.pop()
        processing.append(first)
        st = "HandBrakeCLI -i {0}/in/{1} -o {2}/{1} --preset-import-file {0}/Stef_test_nvid.json -Z 'Stef_test_nvid'".format(inp,first,output)
        os.system(st)
        print(st)
        #time.sleep(round(duration/2))
        press('enter')
        processing.pop()
        os.system("rm {0}/in/{1}".format(inp,first))
    else :
        time.sleep(30)
