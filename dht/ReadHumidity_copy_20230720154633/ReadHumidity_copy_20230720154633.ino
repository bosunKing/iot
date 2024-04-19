#include <DHT11.h>
const unsigned int pinCDS=A1;
const unsigned int potPin = A0;
// Create an instance of the DHT11 class and set the digital I/O pin.
DHT11 dht11(2);

void setup()
{
    // Initialize serial communication at 115200 baud.
    Serial.begin(115200);
}

void loop()
{
    // Read the humidity from the sensor.
    int humidity = dht11.readHumidity();

    // If the humidity reading was successful, print it to the serial monitor.
    if (humidity != -1)
    {
        Serial.print("H");
        Serial.println(humidity);
        
    }
    else;
    long int cds =  analogRead(pinCDS);
    Serial.print("C");
    Serial.println(cds);

    unsigned int adcVal = analogRead(potPin);
    Serial.print("adc");  Serial.println(adcVal);

    // Wait for 2 seconds before the next reading.
    delay(2000);
}
