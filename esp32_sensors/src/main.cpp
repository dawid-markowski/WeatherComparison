#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <OneWire.h>
#include <DallasTemperature.h>

const int buttonPin = 0;
bool IS_ON = 0;
bool buttonPressed = false;
float Temp;
const int oneWireBus = 4;
OneWire oneWire(oneWireBus);
DallasTemperature sensors(&oneWire);
const char* serverIP = "192.168.0.207"; // local ip addrss
const int serverPort = 8000; // port for local communication
String postAddr = String("http://") + serverIP + ":" + serverPort + "/measurement"; // complete url address

const char* ssid = "GreenNet1";
const char* password = "niunia1234";

void setup(){
  Serial.begin(115200);
  sensors.begin();
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
  sensors.requestTemperatures();
  Temp = sensors.getTempCByIndex(0);
  JsonDocument doc;
  doc["place"] = "Ozarow Mazowiecki";
  doc["temp_sensor"] = Temp;
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
  delay(5000);
}

}