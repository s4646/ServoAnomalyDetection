#include <Arduino.h>
#include <ESP32Servo.h>

static const int servoPin = 5; // this is the data pin that sends the data to the servo (make sure to cahnge acordingly)

Servo servo1;

void setup() {

  Serial.begin(115200);
  servo1.attach(servoPin);
  servo1.write(0);
  servo1.write(10);
}

void loop() {

  for(int posDegrees = 0; posDegrees <= 180; posDegrees++) {
    servo1.write(posDegrees);
    Serial.println(posDegrees);
    delay(10);
  }

  for(int posDegrees = 180; posDegrees >= 0; posDegrees--) {
    servo1.write(posDegrees);
    Serial.println(posDegrees);
    delay(10);
  }

}