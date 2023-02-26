#include <dht.h>        // Include library
#define outPin 8
const int led_1 = 13; 
const int ledPin = 5; // digital pin 5 
const int ldrPin = A0;
int led1 = 0;
int x;// Defines pin number to which the sensor is connected

dht DHT;                // Creates a DHT object

void setup() {
Serial.begin(115200);
pinMode(ledPin, OUTPUT); // Here LED is determined as an output or an indicator.
pinMode(ldrPin, INPUT);


}

void loop() {    
  
    
     
    int readData = DHT.read11(outPin);
    int ldrStatus = analogRead(ldrPin);
        
  
    
    if(ldrStatus>1000){
       digitalWrite(led_1, HIGH);
    }else{
      digitalWrite(led_1, LOW);
    }
  
    float t = DHT.temperature;        // Read temperature
    float h = DHT.humidity;           // Read humidity
    Serial.print(t);
    Serial.print(",");
    Serial.print((t*9.0)/5.0+32.0);        // Convert celsius to fahrenheit
    Serial.print(",");
    Serial.print(h);
    Serial.print(",");
    Serial.print(ldrStatus);
   delay(300);}
