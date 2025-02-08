#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const int buttonPin = 0;
bool IS_ON = 0;
bool buttonPressed = false;
long Temp;
//String postAddr = "http://127.0.0.1:8000/post"; // web ip address
const char* serverIP = "192.168.0.204"; // local ip addrss
const int serverPort = 8000; // port for local communication
String postAddr = String("http://") + serverIP + ":" + serverPort + "/post"; // complete url address

const char* ssid = "GreenNet1";
const char* password = "niunia1234";

int TempGenerator(){
  long randTemp;
  randTemp = random(-10,10);
  delay(5000);
  return randTemp;
}

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
//Serial.println(buttonState);
delay(300);


//when button is pressed 1 is free 0 is pushed
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
  Temp = TempGenerator();
  JsonDocument doc;
  doc["place"] = "Ozarow Mazowiecki";
  doc["temp"] = Temp;
  String payload;
  serializeJson(doc, payload);
  Serial.println("Wyslana wiadomosc:");
  Serial.println(payload);

  if(WiFi.status() == WL_CONNECTED){
    HTTPClient http;
    http.begin(postAddr.c_str());

    int httpResponseCode = http.POST(payload);
    
    if(httpResponseCode > 0){
      Serial.println("HTTP Response code: ");
      Serial.println(httpResponseCode);
    }
    else{
      Serial.println("HTTP Response code: ");
      Serial.println(httpResponseCode);
    }
    http.end();


  }
}

}