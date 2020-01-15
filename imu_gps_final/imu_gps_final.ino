#include <Wire.h>



#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <math.h>
int angle;
float lati;
float lon;
#include <TinyGPS++.h>
#include <SoftwareSerial.h>
static const int RXPin = 7, TXPin = 8;
static const uint32_t GPSBaud = 9600;

// The TinyGPS++ object
TinyGPSPlus gps;

// The serial connection to the GPS device
SoftwareSerial ss(RXPin, TXPin);

uint16_t BNO055_SAMPLERATE_DELAY_MS = 1000;

// Check I2C device address and correct line below (by default address is 0x29 or 0x28)
//                                   id, address
Adafruit_BNO055 bno = Adafruit_BNO055(-1, 0x28);

void setup(void)
{
  Serial.begin(9600);
  ss.begin(GPSBaud);
  if (!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.println("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while (1);
  }

  delay(1000);
}
void printEvent(sensors_event_t* event,float lati,float lon) {
 // Serial.println();
 /// Serial.print(event->type);
  double x = -1000000, y = -1000000 , z = -1000000; //dumb values, easy to spot problem
  if (event->type == SENSOR_TYPE_ACCELEROMETER) {
    x = event->acceleration.x;
    y = event->acceleration.y;
    z = event->acceleration.z;
 //   Serial.print("acce");
  }
  else if (event->type == SENSOR_TYPE_ORIENTATION) {
    x = event->orientation.x;
    y = event->orientation.y;
    z = event->orientation.z;
   // Serial.print("orien");
  }
  else if (event->type == SENSOR_TYPE_MAGNETIC_FIELD) {
    x = event->magnetic.x;
    y = event->magnetic.y;
    z = event->magnetic.z;
    //Serial.print("mag");
  }
  else if ((event->type == SENSOR_TYPE_GYROSCOPE) || (event->type == SENSOR_TYPE_ROTATION_VECTOR)) {
    x = event->gyro.x;
    y = event->gyro.y;
    z = event->gyro.z;
    //Serial.print("gyro");
  }

  //Serial.print(": x= ");
  //Serial.print(x);
  //Serial.print(" | y= ");
  //Serial.print(y);
  //Serial.print(" | z= ");
  //Serial.println(z);
  delay(300);

   if (atan2(y, x) >= 0) {
        angle = atan2(y, x) * (180 / 3.14);
      }
      else {
        angle = (atan2(y, x) + 2 * 3.14) * (180 / 3.14);
      }  
 
  //Serial.print(F("Location: "));

   
    Serial.print(" lat ");
    Serial.print(lati,16);
    Serial.print(" lon ");
    Serial.print(lon,16);
    Serial.print(" ang ");
 Serial.println(angle);
 


}

void loop(void)
{  
  //could add VECTOR_ACCELEROMETER, VECTOR_MAGNETOMETER,VECTOR_GRAVITY...
  sensors_event_t orientationData , angVelocityData , linearAccelData,accelerometerData,magnetometerData;
  bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  bno.getEvent(&angVelocityData, Adafruit_BNO055::VECTOR_GYROSCOPE);
  bno.getEvent(&linearAccelData, Adafruit_BNO055::VECTOR_LINEARACCEL);
  bno.getEvent(&accelerometerData, Adafruit_BNO055::VECTOR_ACCELEROMETER);
  bno.getEvent(&magnetometerData, Adafruit_BNO055::VECTOR_MAGNETOMETER);
   while (ss.available() > 0){
    if (gps.encode(ss.read())){
if (gps.location.isValid())
  {
    lati=gps.location.lat();
    lon=gps.location.lng();
   }  
   else{Serial.print("INVALID");
    }
  //printEvent(&orientationData);
  //printEvent(&angVelocityData);
  //printEvent(&linearAccelData);
  //printEvent(&accelerometerData);
   //printEvent(&magnetometerData,lati,lon);
   
    int8_t boardTemp = bno.getTemp();
   // Serial.print(F("temperature: "));
   // Serial.println(boardTemp);
    delay(BNO055_SAMPLERATE_DELAY_MS);
    }   }
   printEvent(&magnetometerData,lati,lon);

    
    }
