#include <ros.h>
#include <geometry_msgs/Pose2D.h>
#include <Q2HX711.h>

ros::NodeHandle  nh;
geometry_msgs::Pose2D cont_msg ;
ros::Publisher pub_cont("contacto_paw", &cont_msg);



float lat;
float lon;
float pres;
int X,Y; 
const byte MPS_OUT_pin = 4; // OUT data pin
const byte MPS_SCK_pin = 5; // clock data pin

Q2HX711 MPS20N0040D(MPS_OUT_pin, MPS_SCK_pin); 

#define X1 A0
#define X2 A1
#define Y1 A2
#define Y2 A3


#define Xresolution 1024 
#define Yresolution 1024

void setup() {
  
  nh.initNode();
  nh.advertise(pub_cont);



  
}

void loop()
{
  pinMode(Y1,INPUT);
  pinMode(Y2,INPUT);  
  digitalWrite(Y2,LOW);
  pinMode(X1,OUTPUT);
  digitalWrite(X1,HIGH);
  pinMode(X2,OUTPUT);
  digitalWrite(X2,LOW);
  X = (analogRead(Y1))/(1024/Xresolution); //Reads Y (Latitude) axis touch position 
  
  pinMode(X1,INPUT);
  pinMode(X2,INPUT);
  digitalWrite(X2,LOW);
  pinMode(Y1,OUTPUT);
  digitalWrite(Y1,HIGH);
  pinMode(Y2,OUTPUT);
  digitalWrite(Y2,LOW);
  
  Y = (analogRead(X1))/(1024/Yresolution); //Reads Y (Longitude) axis touch position
  lat= X;
  lon= Y;
  pres = MPS20N0040D.read(); 

  cont_msg.x = lat;
  cont_msg.y = lon;
  cont_msg.theta = pres;
  pub_cont.publish(&cont_msg);


  nh.spinOnce();
  delay(5);
}
