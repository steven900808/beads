#include <Servo.h>   //載入函式庫，這是內建的，不用安裝

Servo myservo8,myservo9,myservo10,myservo11,myservo12;  // 馬達

void setup() {
  Serial.begin(9600);
  myservo8.attach(8);  // 設定要將伺服馬達接到哪一個PIN腳
  myservo9.attach(9);
  myservo10.attach(10);
  myservo11.attach(11);
  myservo12.attach(12);
 
  myservo8.write(52);             //上電後先在馬達入口抖動
  myservo9.write(68);            //in1     
  myservo10.write(65);            //in1
  myservo11.write(22);             //in1
  myservo12.write(30);             //in1            
    delay(100);
  myservo8.write(47);    
  myservo9.write(63);
  myservo10.write(62);
  myservo11.write(30);
  myservo12.write(25);
    delay(100);
  myservo8.write(57);    
  myservo9.write(73);
  myservo10.write(72);
  myservo11.write(20);
  myservo12.write(30);
    delay(100);
  myservo8.write(47);            
  myservo9.write(63);
  myservo10.write(62);
  myservo11.write(30);
  myservo12.write(25);
    delay(100);
  myservo8.write(52);             //上電後先在馬達入口抖動
  myservo9.write(68);            //in1     
  myservo10.write(65);            //in1
  myservo11.write(22);             //in1
  myservo12.write(30);             //in1

  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(13,OUTPUT);
}
void loop() {  
  char mode = 0;
  mode = Serial.read();      //接收python指令
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
  digitalWrite(4,HIGH);
  digitalWrite(5,HIGH);
  digitalWrite(6,HIGH);
if(mode=='O'){                    //python傳送O指令，馬達轉到出口
                                                  myservo10.write(121);
                                                  delay(50);
                                                  myservo10.write(115);
                                                  delay(50);
                                                  myservo10.write(118);            //out
                                                  delay(150);
                              myservo9.write(123);  
                              delay(50);
                              myservo9.write(117);  
                              delay(50);
                              myservo9.write(120);             //out 
                              delay(150);     
                                                                       myservo11.write(79);   
                                                                       delay(50);    
                                                                       myservo11.write(73);   
                                                                       delay(50);                          
                                                                       myservo11.write(76);            //out
                                                                       delay(300);   
          myservo8.write(107);
          delay(50); 
          myservo8.write(100);
          delay(50); 
          myservo8.write(103);              //out
          delay(300);  
                                                                                             myservo12.write(84);  
                                                                                             delay(50);   
                                                                                             myservo12.write(78);  
                                                                                             delay(50);                                 
                                                                                             myservo12.write(81);            //out
}
if(mode=='I'){                //python傳送I指令，轉到第一個入口           
  myservo8.write(52);             //in1   
  myservo9.write(68);            //in1     
  myservo10.write(65);            //in1
  myservo11.write(26);             //in1
  myservo12.write(30);             //in1            
    delay(100);
  myservo8.write(47);    
  myservo9.write(63);
  myservo10.write(62);
  myservo11.write(30);
  myservo12.write(25);
    delay(100);
  myservo8.write(57);    
  myservo9.write(73);
  myservo10.write(72);
  myservo11.write(20);
  myservo12.write(30);
    delay(100);
  myservo8.write(47);            
  myservo9.write(63);
  myservo10.write(62);
  myservo11.write(30);
  myservo12.write(25);
    delay(100);
  myservo8.write(52);             //in1   
  myservo9.write(68);            //in1     
  myservo10.write(65);            //in1
  myservo11.write(26);             //in1
  myservo12.write(30);             //in1
  delay(600);
  }
if(mode=='i'){                //python傳送i指令，轉到第二入口
  myservo8.write(148);        //in2  
  myservo9.write(169);            //in2    
  myservo10.write(165);       //in2
  myservo11.write(128);        //in2
  myservo12.write(30);             //in1
    delay(100);
  myservo8.write(143);  
  myservo9.write(164);  
  myservo10.write(162);
  myservo11.write(120); 
  myservo12.write(35); 
    delay(100);
  myservo8.write(153);  
  myservo9.write(174);
  myservo10.write(172);
  myservo11.write(130);
  myservo12.write(30);
    delay(100);
  myservo8.write(143);  
  myservo9.write(164);
  myservo10.write(162);
  myservo11.write(120);
  myservo12.write(25);
    delay(100);
  myservo8.write(148);        //in2  
  myservo9.write(169);            //in2    
  myservo10.write(165);       //in2
  myservo11.write(128);        //in2
  myservo12.write(30);             //in1
    delay(600);
}
 if(mode=='5'){          //python傳送5指令，以下皆為依據欲掉落拚豆分別列出之馬達轉動出口訊號//**sg90s轉動角度很常跑掉所以執行前都要人工對正**//
                                                  myservo10.write(121);
                                                  delay(50);
                                                  myservo10.write(115);
                                                  delay(50);
                                                  myservo10.write(118);            //out
                                                  delay(150);
                              myservo9.write(123);  
                              delay(50);
                              myservo9.write(117);  
                              delay(50);
                              myservo9.write(120);             //out 
                              delay(150);     
                                                                       myservo11.write(79);   
                                                                       delay(50);    
                                                                       myservo11.write(73);   
                                                                       delay(50);                          
                                                                       myservo11.write(76);            //out
                                                                       delay(300);        
          myservo8.write(106);
          delay(50); 
          myservo8.write(100);
          delay(50); 
          myservo8.write(103);              //out
          delay(300);  
                                                                                             myservo12.write(84);  
                                                                                             delay(50);   
                                                                                             myservo12.write(78);  
                                                                                             delay(50);                                 
                                                                                             myservo12.write(81);            //out
 }
 if(mode=='4'){
                                                  myservo10.write(121);
                                                  delay(50);
                                                  myservo10.write(115);
                                                  delay(50);
                                                  myservo10.write(118);            //out
                                                  delay(150);
                              myservo9.write(123);  
                              delay(50);
                              myservo9.write(117);  
                              delay(50);
                              myservo9.write(120);             //out 
                              delay(150);     
                                                                       myservo11.write(79);   
                                                                       delay(50);    
                                                                       myservo11.write(73);   
                                                                       delay(50);                          
                                                                       myservo11.write(76);            //out
                                                                       delay(300);        
          myservo8.write(106);
          delay(50); 
          myservo8.write(100);
          delay(50); 
          myservo8.write(103);              //out
 }
if(mode=='3'){
                                                  myservo10.write(121);
                                                  delay(50);
                                                  myservo10.write(115);
                                                  delay(50);
                                                  myservo10.write(118);            //out
                                                  delay(150);
                              myservo9.write(123);  
                              delay(50);
                              myservo9.write(117);  
                              delay(50);
                              myservo9.write(120);             //out 
                              delay(300);      
          myservo8.write(106);
          delay(50); 
          myservo8.write(100);
          delay(50); 
          myservo8.write(103);              //out
}
if(mode=='2'){ 
                              myservo9.write(123);  
                              delay(50);
                              myservo9.write(117);  
                              delay(50);
                              myservo9.write(120);             //out 
                              delay(300);      
          myservo8.write(106);
          delay(50); 
          myservo8.write(100);
          delay(50); 
          myservo8.write(103);              //out
}
 if(mode=='1'){      
          myservo8.write(106);
          delay(50); 
          myservo8.write(100);
          delay(50); 
          myservo8.write(103);              //out                        
 }
 if(mode=='6'){    //8,9,12   
                              myservo9.write(123);  
                              delay(50);
                              myservo9.write(117);  
                              delay(50);
                              myservo9.write(120);             //out 
                              delay(300);       
          myservo8.write(106);
          delay(50); 
          myservo8.write(100);
          delay(50); 
          myservo8.write(103);              //out
          delay(300);  
                                                                                             myservo12.write(84);  
                                                                                             delay(50);   
                                                                                             myservo12.write(78);  
                                                                                             delay(50);                                 
                                                                                             myservo12.write(81);            //out
 }
 if(mode=='7'){  //8,9,10,12

                                                  myservo10.write(121);
                                                  delay(50);
                                                  myservo10.write(115);
                                                  delay(50);
                                                  myservo10.write(118);            //out
                                                  delay(150);
                              myservo9.write(123);  
                              delay(50);
                              myservo9.write(117);  
                              delay(50);
                              myservo9.write(120);             //out 
                              delay(300);      
          myservo8.write(106);
          delay(50); 
          myservo8.write(100);
          delay(50); 
          myservo8.write(103);              //out
          delay(300);  
                                                                                             myservo12.write(84);  
                                                                                             delay(50);   
                                                                                             myservo12.write(78);  
                                                                                             delay(50);                                 
                                                                                             myservo12.write(81);            //out
 }
}
