#include <Wire.h>
#include <NeoPixelConnect.h>
NeoPixelConnect p(16, 1);

byte com = 2;


void setup()
{
  Wire.setSDA(4);
  Wire.setSCL(5);
  Wire.begin(0x14);
  

 // bool setSDA(1);
  //bool setSCL(2);


  Wire.onReceive(DataReceive);

  Serial.begin(115200);
  
  delay(2000);

  
  
  p.neoPixelSetValue(0,64,0,0, true);
  delay(500);
  
  p.neoPixelSetValue(0,0,64,0, true);
  delay(500);
  
  p.neoPixelSetValue(0,0,0,64, true);
  delay(500);
  
  p.neoPixelSetValue(0,0,0,0, true);
 
}

void loop()
{

Serial.print(com);

delay(1000);


if(com == 0){
 p.neoPixelSetValue(0,0,0,0, true);
}
else if (com == 1){
  p.neoPixelSetValue(0,64,0,0, true);
}
else if (com == 2){
  p.neoPixelSetValue(0,0,64,0, true);
}
else if (com == 3){
  p.neoPixelSetValue(0,0,0,64, true);
}




}

void DataReceive(int numBytes)
{
  while(Wire.available()) 
  { 
    com = Wire.read();
  
  }
}

