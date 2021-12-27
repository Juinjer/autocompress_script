#!/usr/bin/env python3
from config import *

import os
import time

if not os.path.isdir(input_dir+ "/in"):
    os.mkdir(input_dir+"/in")
if not os.path.isdir(output_dir):
    os.mkdir(input_dir+"/out")

files = []
processing = []
while 1:
    for file in os.listdir(input_dir + "/in"):
            if file.endswith(".mp4") and file not in files and file not in processing:
                    files.append(file)
    if len(files)>0 and len(processing)<1:
        first = files.pop()
        processing.append(first)
        st = f'HandBrakeCLI -i {input_dir}/in/{first} -o {output_dir}/{first} --preset-import-file {input_dir}/{handbrake_preset}.json -Z "{handbrake_preset}"'
        os.system(st)
        processing.pop()
        os.system(f'rm {input_dir}/in/{first}')
        try:
            os.system(f'scp "{output_dir}/{first}" "{scp_adress}:{remote_dir}"')
        except:
            print("Client not available")

    else :
        time.sleep(30)