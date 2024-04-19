import cv2
import numpy as np
import serial
import time

# import datetime
#
# def millis():  # I/D 게인 미사용, 주석 처리
#     return round(datetime.datetime.utcnow().timestamp() * 1000)

_pan = pan = _til = til = 75
move_value = 0.1  # error 값 수동 입력
move_P_gain = 2.2  # P 게인
prev_area = 0
x, y, width, height = [0] * 4

sp  = serial.Serial('COM3', 115200, timeout=1)
tx_dat = 'pan75' + ' til75' + '\n'
sp.write(tx_dat.encode())
cap = cv2.VideoCapture(0)       # 카메라 모듈 사용.

while(1):
    ret, frame = cap.read()     #   카메라 모듈 연속프레임 읽기

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
    res = cv2.bitwise_and(frame, frame, mask=mask)      # 흰색 영역에 파랑색 마스크를 씌워줌.
    
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)    
    _, bin = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
        
    contours, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

     # 초록색 사각형 그리기
    COLOR = (0, 255, 0)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100 and area > prev_area:  # 일정 크기 이상인 경우에만 사각형을 그림
            x, y, width, height = cv2.boundingRect(cnt)  # 바운딩만 처리
            prev_area = area  # 이전 면적 넘기기


    if prev_area > 0:
        cv2.rectangle(frame, (x, y), (x + width, y + height), COLOR, 2)  # 최종 객체만 그림

        center_x = x + width // 2
        center_y = y + height // 2
        print("center: ( %s, %s )" % (center_x, center_y))

        if center_x < 320 - 20:
            pan = pan + (move_value * move_P_gain)
            print("less than 320-30")
        elif center_x < 320 + 20:
            pan = _pan
            print("===")
        else:
            pan = pan - (move_value * move_P_gain)
            print("more than 320+30")

        if center_y < 320 - 20:  # tilt는 방향이 반대
            til = til - (move_value * move_P_gain)
            print("less than 320-30")
        elif center_y < 320 + 20:
            til = _til
            print("===")
        else:
            til = til + (move_value * move_P_gain)
            print("more than 320+30")

        tx_dat = 'pan' + str(int(pan)) + 'til' + str(int(til)) + '\n'
        print(tx_dat)
        sp.write(tx_dat.encode())
        _pan = pan
        _til = til
        # time.sleep(0.001)
    prev_area = 0  # 다 돌면 이전 면적은 삭제

    res1 = cv2.bitwise_and(frame, frame, mask=mask1)    # 흰색 영역에 초록색 마스크를 씌워줌.
    res2 = cv2.bitwise_and(frame, frame, mask=mask2)    # 흰색 영역에 빨강색 마스크를 씌워줌.

    cv2.imshow('frame',frame)       # 원본 영상을 보여줌
    #cv2.imshow('Blue', res)           # 마스크 위에 파랑색을 씌운 것을 보여줌.
    #cv2.imshow('Green', res1)          # 마스크 위에 초록색을 씌운 것을 보여줌.
    #cv2.imshow('red', res2)          # 마스크 위에 빨강색을 씌운 것을 보여줌.

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
