#include "rgb_lcd.h"
#include <string.h>

/* Initialize Grove  */
rgb_lcd lcd;

const int buttonPin = 7;

int buttonState = 0;

const int colorR = 255;
const int colorG = 150;
const int colorB = 206;

void setup() {
  
  lcd.begin(16, 2);

  lcd.setRGB(colorR, colorG, colorB);
  
  Serial.begin(9600);

  pinMode(buttonPin, INPUT);
}


void loop() {

  char c;
  int length = 0;
  int flag = 1;
  
  buttonState = digitalRead(buttonPin);
  Serial.print(buttonState);
  Serial.write(buttonState);

  if (Serial.available()) {
    lcd.clear();

    while(Serial.available()) {

      c = Serial.read();
      length++;

      if (length >= 16 && flag) {
        
        lcd.setCursor(0, 1);
        flag = 0;
      }
      
      lcd.write(c);
      
    }
  }

  delay(300);

}
