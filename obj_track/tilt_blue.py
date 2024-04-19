import cv2
import numpy as np
import serial
import time
'''
    0         pan left(pan++)           300   320         pan right(pan--)               640
  0 +------------------------------------+-----+-----+------------------------------------+
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    | 
    |                                    |     |     |          tilt up(tilt--)           | 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    | 
220 +------------------------------------+-----+-----+------------------------------------+ 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    |  
240 +------------------------------------+-----+-----+------------------------------------+ 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    |  
260 +------------------------------------+-----+-----+------------------------------------+ 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    | 
    |                                    |     |     |          tilt down(tilt++)         | 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    | 
    |                                    |     |     |                                    |  
480 +------------------------------------+-----+-----+------------------------------------+ 

'''

margin_x = 90
margin_y = 80

_pan = pan = 75
_tilt = tilt = 75



sp  = serial.Serial('COM3', 9600, timeout=1)

def send_ptval(pan, tilt):
    tx_dat = str(pan) + " " + str(tilt) + "\n"
    sp.write(tx_dat.encode())
    print(tx_dat)

send_ptval(75, 75)

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

cap = cv2.VideoCapture(1)       # /dev/video4


while(1):
    time.sleep(0.05)
    ret, frame = cap.read()     #  read camera frame

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    # Convert from BGR to HSV

    # define range of blue color in HSV
    lower_blue = np.array([100,100,120])          # range of blue
    upper_blue = np.array([150,255,255])

    lower_green = np.array([50, 150, 50])        # range of green
    upper_green = np.array([80, 255, 255])

    lower_red = np.array([150, 50, 50])        # range of red
    upper_red = np.array([180, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)     # color range of blue
    mask1 = cv2.inRange(hsv, lower_green, upper_green)  # color range of green
    mask2 = cv2.inRange(hsv, lower_red, upper_red)      # color range of red

    # Bitwise-AND mask and original image
    res1 = cv2.bitwise_and(frame, frame, mask=mask)      # apply blue mask
    res = cv2.bitwise_and(frame, frame, mask=mask1)    # apply green mask
    res2 = cv2.bitwise_and(frame, frame, mask=mask2)    # apply red mask
    
    gray = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)    
    _, bin = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
        
    contours, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    largest_contour = None
    largest_area = 0    
    
    COLOR = (0, 255, 0)
    for cnt in contours:                # find largest blue object
        area = cv2.contourArea(cnt)
        if area > largest_area:
            largest_area = area
            largest_contour = cnt
            
     # draw bounding box with green line
    if largest_contour is not None:
        #area = cv2.contourArea(cnt)
        if largest_area > 500:  # draw only larger than 500
            x, y, width, height = cv2.boundingRect(largest_contour)
            center_x = x + width//2
            center_y = y + height//2
            print("center: ( %s, %s )"%(center_x, center_y))
            if center_x < 320-margin_x: ########################################### need pan left
                if pan + 1 <= 180:
                    pan = pan + 1
                else:
                    pan = 180
                    send_ptval(pan, tilt)
            elif center_x < 320 + margin_x: ########################################### do not change pan value
                pan = _pan
                send_ptval(pan, tilt)
            else: ########################################### need pan right
                if pan - 1 >= 0:
                    pan = pan -1
                else:
                    pan = 0
                    send_ptval(pan, tilt)
            if center_y <= 240-margin_y:########################################### need tilt up
                if tilt - 1 >= 0:
                    tilt = tilt - 1
                else:
                    tilt = 0
                    send_ptval(pan, tilt)
            elif center_y < 240+margin_y: ########################################### do not change tilt value
                tilt = _tilt
                send_ptval(pan, tilt)
            else: ########################################### need tilt down
                    if tilt + 1 <= 180:
                        tilt = tilt + 1
                        send_ptval(pan, tilt)
                    else:
                        tilt = 180
                        send_ptval(pan, tilt)
            
           # _pan = pan; _tilt = tilt;
            cv2.rectangle(frame, (x, y), (x + width, y + height), COLOR, 2)
            time.sleep(0.05)   
    cv2.imshow("VideoFrame",frame)       # show original frame
    #cv2.imshow('Blue', res)           # show applied blue mask
    #cv2.imshow('Green', res1)          # show appliedgreen mask
    #cv2.imshow('red', res2)          # show applied red mask

    k = cv2.waitKey(5) & 0xFF
        
    if k == 27:
        break
   
        
cap.release()
cv2.destroyAllWindows()
