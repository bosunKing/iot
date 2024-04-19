# finalproject_iot_smart_factory의 설명

교육용 팩토리 장비 2대 사용, 웹캠 2개사용

결과영상 : <https://www.youtube.com/watch?v=4ZsCijXwrUQ>

---
### 서버 (백앤드)
파이어베이스 서버 개설

* 스토리지와 리얼타임데이터베이스 사용

### 컨베이어 벨트 
1convayor_info_send.py와 2convayor_info_send.py가 기기를 동작시키고 이미지와 센서 데이터를 서버에 전송

### 안면인식
face폴더

 * 학습할 이미지와 코드 그리고 스트리밍 서버 오픈 (port=3000)
 검출된 객체 이름을 서버에 전송

 ### cctv 스트리밍
* cctv_streaming.py 스트리밍 서버 오픈 (port=5000)

### 온도습도조도
arduino_environment 폴더의 아두이노코드

* environment_send.py 아두이노에서 받은 데이터를 서버로 전송

### 웹페이지 (프론트앤드)
* streamlit_server폴더

IOT_pactory.py가 메인페이지,
* pages폴더 안에 있는 코드는 서브 페이지

streamlit 설치:

    pip install streamlit

실행 방법:

    streamlit run IOT_pactory.py



