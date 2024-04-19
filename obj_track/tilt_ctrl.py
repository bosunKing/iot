import cv2
import numpy as np
import serial
import time

margin_x = 90
margin_y = 20

_pan = pan = 75
_tilt = tilt = 75

sp  = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

pan = _pan = 75
tilt = _tilt = 75

def send_pan(pan):
    tx_dat = "pan" + str(pan) + "\n"
    sp.write(tx_dat.encode())
    print(tx_dat)

def send_tilt(tilt):
    tx_dat = "tilt" + str(tilt) + "\n"
    sp.write(tx_dat.encode())
    print(tx_dat)

def main(args=None):
    global pan; global _pan; global tilt; global _tilt;
    send_pan(75)
    send_tilt(75)


while(1):
    tilt = input("input tilt value: ")
    send_tilt(tilt)
    time.sleep(0.05)
