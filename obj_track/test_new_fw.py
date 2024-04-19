from getchar import Getchar
import serial

sp  = serial.Serial('COM5', 115200, timeout=1)

pan = _pan = 75
tlt = _tlt = 75

def send_ptval(pan, tilt):
    tx_dat = str(pan) + " " + str(tilt) + "\n"
    sp.write(tx_dat.encode())
    print(tx_dat)

def main(args=None):
    global pan; global _pan; global tlt; global _tlt;
    
    while True:
       if sp.readable():
        rx_dat = sp.readline()
        print(rx_dat.decode()[:len(rx_dat)-1])
       pan  = int(input("input pan  value: "))
       tilt = int(input("input tilt value: "))
       send_ptval(pan, tilt)

if __name__ == '__main__':
    main()

