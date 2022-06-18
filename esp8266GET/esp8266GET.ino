#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <Arduino_JSON.h>
#include "FastLED.h"            // 此示例程序需要使用FastLED库
#define NUM_LEDS 5             // LED灯珠数量
#define LED_DT D8                // Arduino输出控制信号引脚
#define LED_TYPE WS2812         // LED灯带型号
#define COLOR_ORDER GRB         // RGB灯珠中红色、绿色、蓝色LED的排列顺序
uint8_t max_bright = 64;       // LED亮度控制变量，可使用数值为 0 ～ 255， 数值越大则光带亮度越高
CRGB leds[NUM_LEDS];

const char* ssid = "";
const char* password = "";

// THE DEFAULT TIMER IS SET TO 10 SECONDS FOR TESTING PURPOSES
// For a final application, check the API call limits per hour/minute to avoid getting blocked/banned
unsigned long lastTime = 0;
// Timer set to 10 minutes (600000)
//unsigned long timerDelay = 600000;
// Set timer to 10 seconds (10000)
unsigned long timerDelay = 1000;

String jsonBuffer;

String LEDstatus;
String LEDindexSTR;
int LEDindexINT;
void setup() {
  Serial.begin(115200);
  
  LEDS.addLeds<LED_TYPE, LED_DT, COLOR_ORDER>(leds, NUM_LEDS);
  FastLED.setBrightness(max_bright); // 设置光带亮度
  
  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
 
  Serial.println("Timer set to 1 seconds (timerDelay variable), it will take 10 seconds before publishing the first reading.");
  FastLED.clear(true);
  delay (100);
}

void loop() {
  // Send an HTTP GET request
  if ((millis() - lastTime) > timerDelay) {
    // Check WiFi connection status
    if(WiFi.status()== WL_CONNECTED){
      String serverPath = "http://192.168.208.12:8000/ledstatus/1";
      
      jsonBuffer = httpGETRequest(serverPath.c_str());
      Serial.println(jsonBuffer);
      JSONVar myObject = JSON.parse(jsonBuffer);
  
      // JSON.typeof(jsonVar) can be used to get the type of the var
      if (JSON.typeof(myObject) == "undefined") {
        Serial.println("Parsing input failed!");
        return;
      }
    
      Serial.print("JSON object = ");
      Serial.println(myObject);
      Serial.print("Led: ");
      Serial.println(myObject["Led_status"]);
      LEDstatus = (const char*)myObject["Led_status"]; 
      LEDindexSTR = (const char*)myObject["Led_index"];
      LEDindexINT = LEDindexSTR.toInt();
      Serial.print("Led_index: ");
      Serial.println(LEDindexINT);
    }
    else {
      Serial.println("WiFi Disconnected");
    }
    lastTime = millis();
  }
  if(LEDstatus == "on"){
    for(int i=0;i<LEDindexINT;i++){
      leds[i] = CRGB::White;          // 设置光带中第一个灯珠颜色为红色，leds[0]为第一个灯珠，leds[1]为第二个灯珠
      FastLED.show();                // 更新LED色彩
    }
    FastLED.clear(true);
  }
  else{
    FastLED.clear(true);
    delay (10);
  }
}

String httpGETRequest(const char* serverName) {
  WiFiClient client;
  HTTPClient http;
    
  // Your IP address with path or Domain name with URL path 
  http.begin(client, serverName);
  
  // Send HTTP POST request
  int httpResponseCode = http.GET();
  String payload = "{}"; 
  if (httpResponseCode>0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    payload = http.getString();
  }
  else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }
  // Free resources
  http.end();
  return payload;
}
