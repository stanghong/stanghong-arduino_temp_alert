#include "max6675.h"

int thermoDO = 12;
int thermoCS = 10;
int thermoCLK = 13;

int ledPin = 7;
float threshold = 30.0; // Celsius

MAX6675 thermocouple(thermoCLK, thermoCS, thermoDO);

void setup() {
  Serial.begin(9600);
  Serial.println("Setup started.");  // Confirm code runs
  pinMode(ledPin, OUTPUT);
  delay(500); // allow MAX chip to settle
  Serial.println("Temperature Monitor Started...");
}

void loop() {
  float tempC = thermocouple.readCelsius();

  Serial.print("Current Temp: ");
  Serial.print(tempC);
  Serial.print(" °C - ");

  if (tempC > threshold) {
    digitalWrite(ledPin, HIGH);
    Serial.println("Above threshold! LED ON");
    Serial.println("ALERT_HIGH_TEMP"); // <-- This triggers your Python script
  } else {
    digitalWrite(ledPin, LOW);
    Serial.println("Below threshold. LED OFF");
  }

  delay(1000); // check every second
}