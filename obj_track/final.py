import cv2
import numpy as np
import serial
import time
import datetime

_pan = pan = 75
_tilt = tilt = 75

sp  = serial.Serial('COM5', 115200, timeout=1)

cap = cv2.VideoCapture(0)       # 카메라 모듈 사용.

tx_dat = "pan75\n"
sp.write(tx_dat.encode())
tx_dat2 = "tilt75\n"
sp.write(tx_dat2.encode())

codec = "DIVX"
capture = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*codec)
record = False


while(1):
    now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    ret, frame = cap.read()     #   카메라 모듈 연속프레임 읽기
    
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("/Image/Star.mp4")

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    # BGR을 HSV로 변환해줌

    # define range of blue color in HSV
    lower_blue = np.array([100,100,120])          # 파랑색 범위
    upper_blue = np.array([150,255,255])

    lower_green = np.array([50, 150, 50])        # 초록색 범위
    upper_green = np.array([80, 255, 255])

    lower_red = np.array([150, 50, 50])        # 빨강색 범위
    upper_red = np.array([180, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)     # 110<->150 Hue(색상) 영역을 지정.
    mask1 = cv2.inRange(hsv, lower_green, upper_green)  # 영역 이하는 모두 날림 검정. 그 이상은 모두 흰색 두개로 Mask를 씌움.
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res1 = cv2.bitwise_and(frame, frame, mask=mask)      # 흰색 영역에 파랑색 마스크를 씌워줌.
    res = cv2.bitwise_and(frame, frame, mask=mask1)    # 흰색 영역에 초록색 마스크를 씌워줌.
    res2 = cv2.bitwise_and(frame, frame, mask=mask2)    # 흰색 영역에 빨강색 마스크를 씌워줌.
    
    gray = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)    
    _, bin = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
        
    contours, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    largest_contour = None
    largest_area = 0    
    
    COLOR = (0, 255, 0)
    for cnt in contours:                # 가장 큰 파란 물체만 인식.
        area = cv2.contourArea(cnt)
        if area > largest_area:
            largest_area = area
            largest_contour = cnt
            
     # 초록색 사각형 그리기
    if largest_contour is not None:
        #area = cv2.contourArea(cnt)
        if largest_area > 120:  # 일정 크기 이상인 경우에만 사각형을 그림
            x, y, width, height = cv2.boundingRect(largest_contour)
    #for cnt in contours:
        #area = cv2.contourArea(cnt)
        #if area > 300:  # 일정 크기 이상인 경우에만 사각형을 그림
            #x, y, width, height = cv2.boundingRect(cnt)
            center_x = x + width//2
            center_y = y + height//2
            print("center: ( %s, %s )"%(center_x, center_y))
            if center_x <= 320-20:
                pan = pan + 1
                if pan > 125:
                    pan = 125
                else:
                    pan = pan + 1
                print("less than 280")
            elif 300<center_x<=340:
                pan = _pan
                print("===")
            elif center_x > 320+20:
                pan = pan - 1
                print("more than 380")
                if pan < 25:
                    pan = 25
                else:
                    pan = pan - 1 
            else:
                pass
            if center_y <= 240-20:
                tilt = tilt - 1
                if tilt < 25:
                    tilt = 25 
                else:
                    tilt = tilt - 1
                print("less than 100")
            elif 220<center_y<=260:
                tilt = _tilt
                print("===")
            elif center_y > 240+20:
                tilt = tilt + 1
                print("more than 380")
                if tilt > 125:
                    tilt = 125
                else:
                    tilt = tilt + 1
           
            else:
                pass
            
            tx_dat = 'pan' + str(pan) + '\n'
            sp.write(tx_dat.encode())
            
            print(tx_dat)
            time.sleep(0.05)
            tx_dat2 = 'tilt' + str(tilt) + '\n'
            print(tx_dat2)
            
            sp.write(tx_dat2.encode())
            
            _pan = pan
            _tilt = tilt           
            cv2.rectangle(frame, (x, y), (x + width, y + height), COLOR, 2)
            time.sleep(0.05)   
    cv2.imshow("VideoFrame",frame)       # 원본 영상을 보여줌
    cv2.imshow('Blue', res1)           # 마스크 위에 파랑색을 씌운 것을 보여줌.
    #cv2.imshow('Green', res1)          # 마스크 위에 초록색을 씌운 것을 보여줌.
    #cv2.imshow('red', res2)          # 마스크 위에 빨강색을 씌운 것을 보여줌.

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break    
    key = cv2.waitKey(33)

        
    if key == 24:
        print("녹화 시작")
        record = True
        video = cv2.VideoWriter("D:/" + str(now) + ".avi", fourcc, 10.0, (frame.shape[1], frame.shape[0]))
            
    elif key == 26:
        print("녹화 중지")
        record = False
        video.release()
        
    if record == True:
        print("녹화 중..")
        video.write(frame)    
        
capture.release()
cv2.destroyAllWindows()
