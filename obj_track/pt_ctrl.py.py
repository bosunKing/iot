from getchar import Getchar
import serial

sp  = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

pan = _pan = 75
tlt = _tlt = 75

def main(args=None):
    global pan; global _pan; global tlt; global _tlt;
    kb = Getchar()
    key = ''
    
    while key!='Q':
    
        key = kb.getch()
        
        if key == 'w':
            if tlt - 1 >= 25:
                tlt = tlt - 1
                print("tilt up,   pan = %s, tilt = %s."%(pan, tlt))
            else:
                tlt = 25
        elif key == 's':
            if tlt + 1 <= 125:
                tlt = tlt + 1
            print("tilt down, pan = %s, tilt = %s."%(pan, tlt))
            else:
                tlt = 125
            if pan + 1 <= 125:
                pan = pan + 1
            else:
                pan = 125
        elif key == 'a':
            if pan + 1 <= 125:
                pan = pan + 1
            else:
                pan = 125
            print("pan right, pan = %s, tilt = %s."%(pan, tlt))
        if key == 'd':
            if pan - 1 >= 25:
                pan = pan - 1
            else:
                pan = 25
            print("panleft, pan = %s, tilt = %s."%(pan, tlt))
        else:   pass
        

if __name__ == '__main__':
    main()

