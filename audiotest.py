import sounddevice as sd
import numpy as np
import time as t
duration = 20  # seconds

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata
    print(outdata)

print(sd.query_devices())
inDevice = input("input: ")
outDevice = input("output: ")

with sd.Stream(device=(int(inDevice), int(outDevice)), channels=2, callback=callback):
    sd.sleep(int(duration * 1000))