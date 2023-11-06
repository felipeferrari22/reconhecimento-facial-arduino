void setup() 
{
     Serial.begin(9600); 
     pinMode(5,OUTPUT);
     digitalWrite(5,HIGH);  
     Serial.print("Porta fechada");
}
void loop() 
{
  char cmd;
  if (Serial.available()>0)
    {
        cmd = Serial.read();
        if (cmd == 'a') 
        {
           digitalWrite(5,LOW);
           Serial.print("Porta aberta");
           delay(2000);
           digitalWrite(5,HIGH);
           Serial.print("Porta fechada");
         }    
  }
}