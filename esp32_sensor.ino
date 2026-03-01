#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";

// The IP address of your Raspberry Pi Gateway
const char* gateway_url = "http://192.168.1.XX:5000/route"; 
const char* zero_trust_token = "AMD-EDU-AUTH-99283A"; // Simulated secure token

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  Serial.print("Connecting to Campus WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to Campus Network!");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(gateway_url);
    http.addHeader("Content-Type", "application/json");
    http.addHeader("Authorization", zero_trust_token);

    // Simulate normal campus lab temperature (20C to 25C)
    // To trigger the AI alarm during demo, change this to a crazy number like 999
    float lab_temp = random(200, 250) / 10.0; 

    String payload = "{\"device_id\": \"Lab_Sensor_01\", \"Chemistry_Lab_Temp\": " + String(lab_temp) + "}";
    
    int httpResponseCode = http.POST(payload);
    
    Serial.print("Sent Data: ");
    Serial.println(payload);
    Serial.print("Gateway Response Code: ");
    Serial.println(httpResponseCode);
    
    http.end();
  }
  delay(5000); // Send data every 5 seconds
}
