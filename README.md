# IOT 스마트 자동 물류 분류 시스템
#### IoT 프로젝트 3조 '가산Hub'

> 물류량은 나날이 늘어가고, 물류 역량이 경쟁력이 되는 시대이다. \
> 물류 처리 자동화는 발전 속도를 빠르게 증가시킨다. \
> 물류 센터나 창고에서의 작업 부하를 경감하고, 전반적인 물류 처리 
과정의 신속성과 정확성을 향상시키는 것이 목표이다.
> 
<br>

### ⬥ 동작
1. 상자 QR 코드를 **인식**하면, DB 저장과 동시에 지정 hub로 물류가 **이동**한다.\
   ⬦ 이동 방식 : 컨베이어 벨트가 **동작**하고, 나무판을 붙인 서보모터가 작동하여 물류를 **분류**한다.
2. 분류 **완료**를 탐지하여 DB 업데이트, **GUI**에서 완료 표시로 변환한다.
   
<br>

## ⬥ Team member
***⬦ 최가은(팀장)*** : 통신 server, database 구축 <br>
***⬦ 김보선*** : 컨베이어벨트 제작 및 motor 동작 <br>
***⬦ 이정욱*** : QT GUI 구현 <br> 
***⬦ 유재상*** : 컨베이어벨트 제작, 바코드 모듈 및 mqtt 통신 보드 제어 <br>
***⬦ 정다연*** : 컨베이어벨트 동작 코드

---
## ⬥ 전체 구성
<img src="https://github.com/addinedu-ros-4th/iot-repo-3/assets/102429136/97f7e615-d8dd-4b56-9c4c-86e5b2b4455b" width="600" height="500"/>

## ⬥ 실제 가동 모습 & 모니터링
<img src="https://github.com/addinedu-ros-4th/iot-repo-3/assets/102429136/80628a38-0520-4cfd-a8ef-08bf227d9c0b" width="300" height="300"/> <img src="https://github.com/addinedu-ros-4th/iot-repo-3/assets/102429136/b095b69a-fcf5-4a3f-8808-9f0ce22169aa" width="300" height="300"/>

---
### ⬥ 기능 리스트
<img src="https://github.com/addinedu-ros-4th/iot-repo-3/assets/102429136/3c074be2-9ecf-42ad-8d42-753726ef7062" width="600" height="400"/>

## ⬥ System 구조
<img src="https://github.com/addinedu-ros-4th/iot-repo-3/assets/102429136/f3e8c1e4-a5f1-4508-a44f-e282b5fe32d9" width="600" height="500"/>

#### ⬦ QR코드 구성
<img src="https://github.com/addinedu-ros-4th/iot-repo-3/assets/102429136/d3614adc-9423-4e7a-a452-7fcea222df84" width="600" height="200"/>

#### ⬦ Database
<img src="https://github.com/addinedu-ros-4th/iot-repo-3/assets/102429136/03769c51-3943-4df9-b4ca-6f2fca1956db" width="500" height="200"/>

---
## ⬥ QT GUI 시현 영상
1. 물품 찾기, 물품 통계량 기능

[gui](https://github.com/addinedu-ros-4th/iot-repo-3/assets/102429136/e073fc87-4c36-439e-9a8d-c89939099736)
