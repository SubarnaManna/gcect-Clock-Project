#include <SD.h>                      // need to include the SD library
#define SD_ChipSelectPin 10 //using digital pin 4 on arduino nano 328, can use other pins
#include <TMRpcm.h>           //  also need to include this library...
#include <SPI.h>
#include <DS3231.h>

//  Creating the Clock Object
DS3231 myRTC;

// Creating the Audio Object
TMRpcm Audio;   

// Boolean Variable for receiving the Hour Format Either 12 or 24 and Century for Receving Month 
bool h12 , hPM , Century ;

// Boolean Variables for Different Clock States 
bool isTempSpoken = false , ExamTimerMode = false ; 
//  Hour and minute veriable : 
byte  hr, mn, sec, mx = 100, my = 100 , mz = 100 ; 
int dp ; 
// ------------- Hour and minutes Array for Storing the Upcoimg Speaking Time Data ------------- 
// byte HrMinArr[2];
// Exam Veriable deceleration :
// byte E1h, E1m, E1d, E2h, E2m, E2d, E3h, E3m, E3d ; 

// ************************* Global Variables for Storing All Receiver Data ************************* 

// String Variable to catch the incoming Data 
String inData = "" ; 
// Variables to store incoming Exam data
// byte E1sH , E1sM , E1tD , E2sH , E2sM , E2tD , E3sH , E3sM , E3tD , EDay , EMonth , EYear , totalExams = 0 , currentExam = 0  ; 
byte EDay , EMonth , EYear , totalExams = 0 , currentExam = 0  ; 
byte AllExamTime[3][3];
// bool isExamStarted = false , isExmover = true , isCheckpointTime = false, SpeakTime = false , isUploaded = false , isSpeaked ;
bool  isCheckpointTime = false, SpeakTime = false , isUploaded = false , isSpeaked = false ;

// ------------- All possible Duration sets for Validation of the Receiving Time Data ------------- 
// const byte DurationSet [18] = { 10, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255 };
const byte checkPoints [11] = { 255, 240, 210, 180, 150, 120, 90, 60, 30, 15, 5 };
// const byte checkPoints [12] = { 255, 240, 210, 180, 150, 120, 90, 60, 30, 15, 5, 0 };

byte nextCheckpoint , checkpointer ;
// Checkpoints are the times where Speaking operations are done. After done , the pointer is moved to next checkpoint ;
// From the duration set the initial value of the checkpointer will be set. After that we just increment it.

// Variables for Exam 01
// byte E1et1h = 0, E1et1m = 0, E1et2h = 0, E1et2m = 0, E1et3h = 0, E1et3m = 0, E1et4h = 0, E1et4m = 0, E1et5h = 0, E1et5m = 0, E1et6h = 0, E1et6m = 0;
// byte E1et1h, E1et1m, E1et2h, E1et2m, E1et3h, E1et3m, E1et4h, E1et4m, E1et5h, E1et5m, E1et6h, E1et6m ;



// **************** Seven Segment Display ****************
//      _______
//     |   a   |
//   f |       | b
//     |_______|
//     |   g   |
//   e |       | c
//     |_______|
//         d

// ----------- Pin Wire Connections -----------
// a = violet pin 
// b = green pin
// c = yellow pin
// d = orange pin
// e = red pin
// f = blue pin
// g = brown pin

// **************** Arduino Digital Pin Connections **************** 

// ----------- Data Pins [Cathode] -----------
// const int a = 7;
// const int b = 5;
// const int c = 4;
// const int d = 3;
// const int e = 2;
// const int f = 6;
// const int g = 1;

const int a = 8;
const int b = 6;
const int c = 5;
const int d = 4;
const int e = 3;
const int f = 7;
const int g = 2;

// ----------- [New] Selection pins [Anode] -----------

// D1 = white pin  
// D2 = black pin
// D3 = yellow pin
// D4 = grey pin

// ----------- For Audio Pin 9 is reserved -----------
// ----------- For Chip Select Pin 10 is reserved -----------
/*
    So, for the above reasons, I choose the analog pins for the Digital Outputs 
    & the reason behind starting from A0 is that, I have also the pin A4 and A5 for Serial communications
    So, Available Digital pins are  = 11, 12, 13 
*/

const int D1 = A0;
const int D2 = A1;
const int D3 = A2;
const int D4 = A3;


// **************** 7 Segment Display Datasets *************** 

// ----------- Display Control Dataset -----------
  int ledPins[11] = {a,b,c,d,e,f,g,D1,D2,D3,D4};
  int segment[7]={a,b,c,d,e,f,g};
  byte n0[7]={1,1,1,1,1,1,0};
  byte n1[7]={0,1,1,0,0,0,0};
  byte n2[7]={1,1,0,1,1,0,1};
  byte n3[7]={1,1,1,1,0,0,1};
  byte n4[7]={0,1,1,0,0,1,1};
  byte n5[7]={1,0,1,1,0,1,1};
  byte n6[7]={1,0,1,1,1,1,1};
  byte n7[7]={1,1,1,0,0,0,0};
  byte n8[7]={1,1,1,1,1,1,1};
  byte n9[7]={1,1,1,1,0,1,1};


// ----------- Function for Setting All CLOCK Pins as OUTPUT pin -----------
void setPin(byte x){
    pinMode(x, OUTPUT);
}

// **************** Arduino PREVIOUS SETUP AREA **************** 

// -------------- Selecting Display --------------- 
void display_Select(byte dx){
  digitalWrite(dx, HIGH); 
  digitalWrite(dp, LOW); // dp=> last pointing display
  dp = dx ; 
}

// -------------- Writing on Display --------------- 
void setSegment(byte *pin){
    for (byte i=0;i<7;i++){
        digitalWrite(segment[i], pin[i] );
    }
  delay(2);
}

void Segment_Write(byte number){

  switch (number) {
    case 0: setSegment(n0);
      break;
    case 1: setSegment(n1);
      break;
    case 2: setSegment(n2);
      break;
    case 3: setSegment(n3);
      break;
    case 4: setSegment(n4);
      break;
    case 5: setSegment(n5);
      break;
    case 6: setSegment(n6);
      break;
    case 7: setSegment(n7);
      break;
    case 8: setSegment(n8);
      break;
    case 9: setSegment(n9);
      break;
      }  
}

void setHour(byte hr){

  byte hx1 = hr/10;
  byte hx2 = hr%10;

  display_Select(D1);
  Segment_Write(hx1);

  display_Select(D2); 
  Segment_Write(hx2);

}

void setMinute(byte mn){

  byte MinuteSection01 = mn/10;
  byte MinuteSection02 = mn%10;

  display_Select(D3);
  Segment_Write(MinuteSection01);

  display_Select(D4);
  Segment_Write(MinuteSection02);

}

// **************** VOICE SEQUENCE AREA **************** 

/* -------------- For 3 Hours Exam -------------- 
  a => Alert ⚠ 
  a0 = At 3 hr [That Exam is just started ]
  a1 = At 2 hr 30 min 
  a2 = At 2 hr
  a3 = At 1 hr 30 min 
  a4 = At 1 hour
  a5 = At 30 min
  a6 = At 15 min
  a7 = At 5 min
  a8 = At 0 min [That Exam time is over.]
*/

/* -------------- For 45 minutes Exam -------------- 
  a => Alert ⚠ 
  a0 = At 45 min [That Exam is just started ]
  a1 = At 15 min
  a2 = At 5 min
  a3 = At 0 min [That Exam time is over.]
*/


void ClockDisplayOFF(){
  digitalWrite(D1, LOW);
  digitalWrite(D2, LOW); 
  digitalWrite(D3, LOW); 
  digitalWrite(D4, LOW); 
}
void ClockStart(){
  dp = D1;
}
void displayTest(){
  digitalWrite(D1,HIGH);
  digitalWrite(D2,HIGH);
  digitalWrite(D3,HIGH);
  digitalWrite(D4,HIGH);
  Segment_Write(8);
  delay(3000);
  ClockDisplayOFF();
  ClockStart();
}
void speakStartExam( byte StrtTime ){
    Audio.play("s46.wav"); // Every Student in this room,
    delay(2500);
    Audio.play("s1.wav"); // kindly please listen,
    delay(2000);
    Audio.play("s47.wav"); // Your exam time is of : 
    delay(2000);
    int fNo = int(StrtTime);
    char File_Name[10];
    snprintf(File_Name, sizeof(File_Name), "s%i.wav", fNo);
    Audio.play(File_Name); // xa hours and y minutes
    delay(2500);
    Audio.play("s23.wav"); // wish you all, a very, good luck for todays exam.
    delay(5000);  // perfect
    // Audio.play("s24a.wav"); //and, 
    // delay(1500);
    Audio.play("s24b.wav"); // Your Exam time starts from,
    delay(3300);
    Audio.play("s25.wav"); // now. 
    delay(1000);
    // Serial.println("\n speakStartExam"+String(StrtTime)+"\n");      
}
void speakLeftTime(byte checkpnt){
    Audio.play("s26.wav"); // You have 
    delay(1000);
    int fNo = int(checkpnt);
    char File_Name[10];
    snprintf(File_Name, sizeof(File_Name), "s%i.wav", fNo);
    Audio.play(File_Name); // x hours and y minutes 
    // Serial.println(checkpnt+"\n");
    delay(2000);
    Audio.play("s27.wav"); // left. to finish your exam.
    delay(2100);
}
void FiftnMinRem(){
    Audio.play("s29.wav"); // now, you have, only, 15 minutes left. to finish your exam. 
    delay(5500);
    // Serial.println("15 min Remaining ...\n");
}
void fiveMinRem(){
    Audio.play("s28.wav"); // you have, just only, 5 minutes left. to finish your exam.
    delay(5000);
    // Serial.println("5 min Remaining ...\n");
}
void speakExamOver(){
    Audio.play("s33a.wav"); // Your Exam Time is over.
    delay(2000);
    Audio.play("s33b.wav"); // so, please submit your paper to the respected invigilator,
    delay(4400);
    Audio.play("s33c.wav"); // I repeat,  Your Exam is over. 
    delay(2500);
    Audio.play("s33b.wav"); // so, please submit your paper to the respected invigilator,
    delay(4400);
    Audio.play("s33e.wav"); // Thank u.
    delay(990);
    // Serial.println("speakExamOver\n");
}
void speakTemperature(){
    Audio.play("s42.wav"); //According to my sensors,  Current Temperature of this room, is, about // Runtime 4.77 Seconds
    delay(4850);
    int temp = int(myRTC.getTemperature());
    char File_Name[10];
    snprintf(File_Name, sizeof(File_Name), "n%i.wav", temp);
    Audio.play(File_Name); // x
    // Serial.println(File_Name);
    // Serial.println(int(myRTC.getTemperature()),2); // Prints the binary form of data.
    // Serial.println("\n");
    delay(1200);
    Audio.play("s38.wav"); // degree celcious
    delay(1500);
}
void SpeakSelection(byte incomingTime){

  switch (incomingTime) { 
    case 15: FiftnMinRem();
      break;
    case 5:fiveMinRem();
      break;
    case 0: speakExamOver();
      break;
    default: speakLeftTime(incomingTime);
      break;
      } 
}
void SpekClkMode(bool Nmode){
  Audio.play("s34.wav");
  delay(1000);
  if(Nmode == true){
    Audio.play("s36.wav");
  }else{
    Audio.play("s35.wav");
  }
  delay(1500);
}
void AlarmStatus (byte AlarmNo){
}
void SpekDtPrt(int data){
    char File_Name[10];
    snprintf(File_Name, sizeof(File_Name), "n%i.wav", data);
    Audio.play(File_Name);
    delay(1500);      
    }
void speakDate(){
    SpekDtPrt(myRTC.getDate());
    SpekDtPrt(myRTC.getMonth(Century)+75);
    SpekDtPrt(myRTC.getYear());    
}
void isUpJustNow(){
  if (isUploaded == true && time < 10 ){
  Audio.play("s95.wav"); // Yes! I received a set of information regarding Exams, within last 10 minutes.
  delay(6050);
  }else{
    Audio.play("s94b.wav"); // No, Within last 10 minutes no data has been uploaded in my system.
    delay(4800);
  }
}
void verifyUpInfo(){

  for (byte i=1; i <= totalExams; i++){
    //
  }

}

// *********** All Control Software Calls and Instructions *********** 
  // -----| Left Side |-----
  
  // ----- Page-01 -----
  // ** UPLOAD DATA ** [Main Function]

  // ----- Page-02 ----- [All Testing Functions]
  // Alarm01Status
  // Alarm02Status
  // current Temperature
  // TodaysDate
  // isUpJustNow
  // verifyUpInfo

  // -----| Right Side |-----
  // Upload Network Data
  
// ------ End ------

void SetExamData(byte *dataSet){
// All Examination Data has been set Successfully.
}

void SetNetworkTime(){
}

byte data(byte s, byte e){
  return byte(inData.substring(s,e).toInt());
}

// **************** Arduino SETUP AREA **************** 
// ----------- Function for Setup of Board -----------
void setup() {

    // ----------- Newer Version for [ Clock + Sound ] -----------
    for (byte i=2; i<=8; i++){
      setPin(i);
    }
    pinMode(D1, OUTPUT);
    pinMode(D2, OUTPUT);
    pinMode(D3, OUTPUT);
    pinMode(D4, OUTPUT);
  // ----------- Opening Serial Port -----------
    Serial.begin(9600);

  // ----------- Audio pins SETUP AREA ----------- 
    Audio.speakerPin = 9; 
    Audio.setVolume(5); // 5 maximum , never do => 9  DANGEROUS LINE, ALMOST ALWAYS AVOID IT, FOR EXECUTE 

  // ----------- Checking the Curent status of the SD Card -----------
    if (!SD.begin(SD_ChipSelectPin)) {  // see if the card is present and can be initialized:
      Serial.println("SD fail");  
      // return ;   // dont do anything more if not
    }else{
    ClockDisplayOFF();
    // speakStartExam(255);
    // delay(2000);
    // speakLeftTime(180);
    // delay(2000);
    // FiftnMinRem();
    // delay(2000);
    // fiveMinRem();
    // delay(2000);
    // speakExamOver();
    // delay(2000);
    speakTemperature(); 
    delay(2000);
    // Serial.println("Music Systems are Working Properly ..... ");    
  }
  // Seting 13 global variables
  totalExams = 3 ; // range 1-3 
  EDay = 22 ; // Date of Exam
  EMonth = 4 ; // Month of Exam
  EYear = 23 ; // Year of Exam
  
  // AllExamTime[3][3] = {{E1sH,E1sM,E1tD},{E2sH,E2sM,E2tD},{E3sH,E3sM,E3tD}} ;
  AllExamTime[0][0] = 14 ; // hr in 24 hr format
  AllExamTime[0][1] = 35 ; 
  AllExamTime[0][2] = 15 ;
  
  AllExamTime[1][0] = 15 ; // hr in 24hr format
  AllExamTime[1][1] = 0  ;
  AllExamTime[1][2] = 90 ;
  
  AllExamTime[2][0] = 17 ; // hr in 24hr format
  AllExamTime[2][1] = 0 ;
  AllExamTime[2][2] = 120 ;
  ClockDisplayOFF();
  ClockStart();
}


// **************** Arduino LOOP AREA **************** 
void loop() {

 // ------------ Exam Timer Mode vs Normal Clock Mode Control  ------------ 
  if (ExamTimerMode == true){
    // ***** Run Timer *****
      // Collecting data from DS3231 Real Time Clock Module  
      hr = myRTC.getHour(h12, hPM);
      mn = myRTC.getMinute();
      sec = myRTC.getSecond();
      if (hPM == true && hr != 12) { hr = hr + 12 ;} 
      // Collecting Stored Exam Data
      byte Hr =  AllExamTime[currentExam][0] ;
      byte Mn =  AllExamTime[currentExam][1] ;
      byte Dn =  AllExamTime[currentExam][2] ;
    // 2. Calculating the remaining Time  
      byte remtime = Dn - ((hr - Hr)*60 + mn - Mn);
      byte nhr = remtime / 60 , nmn = remtime % 60 ;
      setHour(nhr);
      setMinute(nmn);
    // Setting the Countdown Timer in the form of Hours and Minutes 
      // ---------- Checking Special Time ---------- 
      if(sec == 0){
        for(byte i = 0 ; i < 11 ; i++){
          if( checkPoints[i] == remtime){
            isCheckpointTime = true;
            break;
          }else{
            isCheckpointTime = false;
            }
        }
      }
    if(( remtime == Dn || isCheckpointTime == true )&& sec == 1){
        ClockDisplayOFF();
        if(remtime == Dn){
          speakStartExam(Dn); 
          SpekClkMode(false);
        }else{
          SpeakSelection(remtime);
        }
    }
    if(remtime == 0 && sec == 1){
      ExamTimerMode = false ;
      ClockDisplayOFF();
      speakExamOver();
      SpekClkMode(true);
      if ( (currentExam + 1) == totalExams){
        //----- Reset All Variables ----- 
        currentExam = 0 , totalExams = 0 ;
        EDay = 0 , EMonth  = 0 , EYear = 0  ;
        for (byte i=0; i <3 ; i++){
          for (byte j=0; j <3 ; j++){
            AllExamTime[i][j] = 0 ; 
          }
        }
      }
    }//Remtime = 0 closing Brackets  
  }   
  else{ 
    // Run Normal Clock 
      // Collecting data from DS3231 Real Time Clock Module  
      hr = myRTC.getHour(h12, hPM);
      mn = myRTC.getMinute();
      sec = myRTC.getSecond();
      // Setting Hours and Minutes 
      setHour(hr);
      setMinute(mn);
      // inside clock
      // if(sec == 30 ){Serial.println("inside Clock");}
      // Speaks Temperature once in a hour.
      if( mn == 5 && sec == 2 ){
          ClockDisplayOFF();
          speakTemperature();
          delay(1000);
      }
  }

// -------------- Exam Mode and Normal Clock Mode Control Area --------------
  if( totalExams > 0 && ExamTimerMode == false){
    // Check Today is Exam Date or not 
    if ( EDay == myRTC.getDate() && EMonth == myRTC.getMonth(Century) && EYear == myRTC.getYear() ){
      hr = myRTC.getHour(h12, hPM);
      mn = myRTC.getMinute();
      if (hPM == true && hr != 12) { hr = hr + 12 ; }
      for (byte i=0; i < 3; i++){
        if(AllExamTime[i][0] == hr && AllExamTime[i][1] == mn){
          // Activating Exam Timer Mode 
          ExamTimerMode = true ; 
          currentExam = i ;
          break ; 
        }            
      }
    }
  }

  if (Serial.available() > 0){
    // read the incoming String in the serial buffer:
    inData = Serial.readString() ;
    // inData = "<g23Z7X6dbhA2S387D2jaHss723jhKw92|2|20|04|23|04|30|045|05|45|060|00|00|000|>";
    bool Validation = false ; 
    // validate serial data
    // 1. Match String 
    // 2. Validate Upcoming Numeric Values 
    // Here we will check the serial input by regular expresssion 
    String EntryKey = inData.substring(0,33); // if with "<" 33 lastIndex & without "<" 32 lastIndex 
    // if(  ){
    //   if(  ){
    //     Validation = true ;
    //   }
    // }

    if( Validation == true ){

      // Seting 12 global variables
      totalExams = data(34,35);
     
      EDay = data(36,38);
      EMonth = data(39,41);
      EYear = data(42,44);

      // AllExamTime[3][3] = {{E1sH,E1sM,E1tD},{E2sH,E2sM,E2tD},{E3sH,E3sM,E3tD}} ;
      AllExamTime[0][0] = data(45,47);
      AllExamTime[0][1] = data(48,50); 
      AllExamTime[0][2] = data(51,54); 
      
      AllExamTime[1][0] = data(55,57); 
      AllExamTime[1][1] = data(58,60); 
      AllExamTime[1][2] = data(61,64); 
      
      AllExamTime[2][0] = data(65,67);  
      AllExamTime[2][1] = data(68,70); 
      AllExamTime[2][2] = data(71,74); 

    }

  }

}
