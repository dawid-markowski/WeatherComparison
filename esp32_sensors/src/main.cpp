#include <WiFi.h>

const int buttonPin = 0;
bool IS_ON = 0;
bool buttonPressed = false;
long randTemp;

const char* ssid = "GreenNet1";
const char* password = "niunia1234";

void setup(){
  Serial.begin(115200);
  Serial.print("\n\nŁączenie z ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("Połączono z Wi-Fi");
  Serial.print("Adres IP: ");
  Serial.println(WiFi.localIP());

  randomSeed(analogRead(0));
  pinMode(buttonPin,INPUT_PULLUP);
}

void loop(){
int buttonState = digitalRead(buttonPin);
Serial.println(buttonState);
delay(300);


//Jesli przycisk wcisniety
if(buttonState == 0 && !buttonPressed){
  IS_ON = !IS_ON;
  Serial.println("Zmiana stanu Pomiaru");
  buttonPressed = true;
  delay(50);
}

if(buttonState == 1){
  buttonPressed = false;
}


if(IS_ON){
  TempGenerator();
}

}

void TempGenerator(){
  delay(5000);
  randTemp = random(-10,10);
  Serial.println(randTemp);
}