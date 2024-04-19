from getchar import Getchar
import serial


sp  = serial.Serial('COM3', 9600, timeout=1)

pan = _pan = 100
tlt = _tlt = 40

def send_pan(pan):
    tx_dat = "pan" + str(pan) + "\n"
    sp.write(tx_dat.encode())
    print(tx_dat)

def send_tilt(tlt):
    tx_dat = "tilt" + str(tlt) + "\n"
    sp.write(tx_dat.encode())
    print(tx_dat)

def main(args=None):
    global pan; global _pan; global tlt; global _tlt;
    send_pan(100)
    send_tilt(40)
    kb = Getchar()
    key = ''
    
    while key!='Q':
    
        key = kb.getch()
            ####################################################### tilt control ########################################
        if key == 'w': 
            if tlt - 1 >= 0:
                tlt = tlt - 1
            else:
                tlt = 0
            print("tilt up,   pan = %s, tilt = %s."%(pan, tlt))
            send_tilt(tlt)
        elif key == 's':
            if tlt + 1 <= 150:
                tlt = tlt + 1
            else:
                tlt = 150
                
            print("tilt down, pan = %s, tilt = %s."%(pan, tlt))
            send_tilt(tlt)
            ####################################################### pan control ########################################
        elif key == 'a': # pan left
            if pan + 1 <= 180:
                pan = pan + 1
            else:
                pan = 180
            print("pan left,  pan = %s, tilt = %s."%(pan, tlt))
            send_pan(pan)
        elif key == 'd': # pan right
            if pan - 1 >= 0:
                pan = pan - 1
            else:
                pan = 0
            print("panright,  pan = %s, tilt = %s."%(pan, tlt))
            send_pan(pan)
        else:   pass
        
        #send_pan(pan)
        #send_tilt(tlt)
        

if __name__ == '__main__':
    main()

