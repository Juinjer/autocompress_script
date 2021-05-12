#!/usr/bin/env python3
from dotenv import load_dotenv
load_dotenv()

import os
import time
import keyboard

inp = os.environ.get('inp')
output = os.environ.get('output')
remote = os.environ.get('remote')
adress = os.environ.get('adress')
preset = os.environ.get('preset')
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
        st = "HandBrakeCLI -i {0}/in/{1} -o {2}/{1} --preset-import-file {0}/{4}.json -Z '{4}'".format(inp,first,output, preset)
        os.system(st)
        print(st)
        keyboard.press('enter')
        processing.pop()
        os.system("rm {0}/in/{1}".format(inp,first))
        try:
            os.system('scp "{0}/{2}" "{3}:{1}"'.format(output,remote,first, adress))
        except:
            print("Client not available")

    else :
        time.sleep(30)