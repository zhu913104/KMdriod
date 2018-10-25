#include <Stepper.h>
#define STEPS 128

//Ultrasonic ultrasonic2(8);
Stepper stepper1(STEPS, 12, 11, 10, 9);

Stepper stepper2(STEPS, 6, 5, 4,3);
char cmd ='K';
char cmdd ='J';
int  ddd=0;
int maxspeed = 400;
void setup()
{
Serial.begin(9600);

stepper1.setSpeed(100000);   
stepper2.setSpeed(100000); 


}
void loop()
{ 
  int t;
    t = millis();
  long RangeInCentimeters1;
  long RangeInCentimeters2;
//  RangeInCentimeters1 = ultrasonic1.MeasureInCentimeters(); // two measurements should keep an interval
  //RangeInCentimeters2 = ultrasonic2.MeasureInCentimeters(); // two measurements should keep an interval
//  Serial.print(RangeInCentimeters1);//0~400cm
//  Serial.println(" cm");
//  //Serial.print(RangeInCentimeters2);//0~400cm
//  Serial.println(" cm");
  //delay(250);
  
//  if(RangeInCentimeters1|RangeInCentimeters2<80)
//  right();
//  if((RangeInCentimeters1<80)||(RangeInCentimeters2<85))
//  left();
  
char incomingByte = "";   // for incoming serial data
  if (Serial.available() > 0){
    incomingByte = Serial.read();
    if (incomingByte){
    switch(char(incomingByte)){
      case 'w':
        cmd='w';
        break;  
      case 's':
        cmd='s';
        break;  
      case 'd':
        cmd='d';
        break;  
      case 'a':
        cmd='a';
        break;
      case 'q':
        cmd='q';
        break;
      default:
        break;
      }

    }
  }
    switch(cmd)
    {
      case 'w':
        if (cmd==cmdd){
          cmdd=cmd;
          if (ddd> maxspeed){
             ddd = maxspeed;
          }
          else{
            ddd=ddd+5;
          }
        }
        else{
          cmdd=cmd;
          ddd=0;
          ddd=0;
        }
        forward();
        break;  
      case'a':
        if (cmd==cmdd){
          cmdd=cmd;
          if (ddd> maxspeed){
             ddd = maxspeed;
          }
          else{
            ddd=ddd+5;
          }
        }
        else{
          cmdd=cmd;
          ddd=0;
          ddd=0;
        }
        left();
        break;  
      case'd':
        if (cmd==cmdd){
          cmdd=cmd;
          if (ddd> maxspeed){
             ddd = maxspeed;
          }
          else{
            ddd=ddd+5;
          }
        }
        else{
          cmdd=cmd;
          ddd=0;
          ddd=0;
        }
        right();
        break;  
      case's':
        if (cmd==cmdd){
          cmdd=cmd;
          if (ddd> maxspeed){
             ddd = maxspeed;
          }
          else{
            ddd=ddd+5;
          }
        }
        else{
          cmdd=cmd;
          ddd=0;
          ddd=0;
        }
        back();
        break;
      case'q':
        stop_();
        break;
      default:
        break;
      }
      //%超音波寫這邊
}
void forward()
{
  stepper1.step(ddd*-1);
  stepper2.step(ddd);
  Serial.println("forward"); 
}
void back()
{
  stepper1.step(ddd);
  stepper2.step(ddd*-1);
  Serial.println("back"); 
}
void right()
{ 
  stepper1.step(ddd/-2);
  stepper2.step(ddd/-2);
  Serial.println("left"); 
}
void left()
{ 
  stepper1.step(ddd/2);
  stepper2.step(ddd/2);
  Serial.println("right"); 
}

void stop_()
{ 
  stepper1.step(0);
  stepper2.step(0);
  Serial.println("stop"); 
}
