#include "rgb_lcd.h"
#include <string.h>

/* Initialize Grove LCD RGB Backlight */
rgb_lcd lcd;

/* Input pin for Button control */
const int buttonPin = 7;

/* Global variable for button state */
int buttonState = 0;

/* Global variables for background color */
const int colorR = 255;
const int colorG = 150;
const int colorB = 206;

/* Sets up Arduino */
void setup() {

  /* Initializes LCD with 16 columns and 2 rows */
  lcd.begin(16, 2);

  /* Sets LCD background color to RGB(255, 150, 206) */
  lcd.setRGB(colorR, colorG, colorB);

  /* Creates a connection with local ports with 9600 baudrate */
  Serial.begin(9600);

  /* Sets the button pin to Input mode */
  pinMode(buttonPin, INPUT);
}

/* Defines Arduino loop process */
void loop() {

  /* Initialize variables */
  char c;
  int length = 0;
  int flag = 1;

  /* Reads for button input and prints value on terminal */
  buttonState = digitalRead(buttonPin);
  Serial.print(buttonState);
  Serial.write(buttonState);

  /* Scan for any input from Python source code */
  if (Serial.available()) {

    /* Clears LCD display */
    lcd.clear();

    /* Scans for any further input from Python */
    while(Serial.available()) {

      /* Read String value per character */
      c = Serial.read();

      /* Monitor characters read */
      length++;

      /* If 16 characters has been read, move cursor to second line */
      if (length >= 16 && flag) {
        
        /* Sets cursor to column 0 and row 1 */
        lcd.setCursor(0, 1);
        flag = 0;
      }

      /* Prints out character to LCD */
      lcd.write(c);
      
    }
  }

  delay(300);

}
