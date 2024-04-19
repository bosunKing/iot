#include<stdlib.h>
#include <Servo.h>
#define max 180
#define min 0
#define step 10
Servo panServo,tiltServo;

String inputString = "";      // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete

void setup() { 
  //pinMode(A2,OUTPUT);
  //pinMode(A3,OUTPUT);
  Serial.begin(9600); 
  inputString.reserve(200);
  panServo.attach(12);
  tiltServo.attach(13);
  panServo.write(100);delay(40);
  tiltServo.write(20);delay(40);
  analogWrite(A2,0);
  analogWrite(A3,190);
}

void loop() {
  
  // print the string when a newline arrives:
  if (stringComplete) {
    if(inputString.substring(0,3)=="pan"){
      int pan=atoi(inputString.substring(3).c_str());
      Serial.print("pan = ");
      Serial.println(pan);
      panServo.write(pan);
    }
    else if(inputString.substring(0,4)=="tilt"){
      int tilt=atoi(inputString.substring(4).c_str());
      Serial.print("tilt = ");
      Serial.println(tilt);
      tiltServo.write(tilt);
    }
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
