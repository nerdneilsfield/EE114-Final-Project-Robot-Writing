#include <Braccio.h>
#include <Servo.h>
Servo base;
Servo shoulder;
Servo elbow;
Servo wrist_rot;
Servo wrist_ver;
Servo gripper;
String inString = "";
int angles[6] = {40,40,40,40,90,10};
void setup(){
    Serial.begin(9600);
    while(!Serial){
        ;
    }
    Braccio.begin();
    Serial.println("Connected successful!");
}

void loop(){
    //int angles[6];
    if(Serial.available()){
        int inChar = 0;
        int count  = 0;
        int j = 0;
        inChar  = Serial.read();   
        if (inChar == 'p') Serial.print("Pong");
        for(int i=0;i<6;i++)
        {
            while(count <4)
            {
                inChar  = Serial.read();         
                if(isDigit(inChar))
                {
                    if(count == 0)
                    {
                      j = inChar;
                     }else{   
                    inString+=(char)inChar;
                     }
                    count++;
                }
            }
            if(inString!="")
            {
            Serial.println(j-48);
            Serial.println(inString);
            angles[j-49]=inString.toInt();
            }
            else{
             }
            //angles[inString[0].toInt()-1] = inString.toInt();
            count = 0;
            inString = "";
        }
        Braccio.ServoMovement(20, angles[0], angles[1], angles[2], angles[3], angles[4], angles[5]);
        

    }

}
