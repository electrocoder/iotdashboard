
// Iotdashboard project
// Date: 17 Aug 2017
// Author: Sahin MERSIN
// Demo: http://iotdashboard.pythonanywhere.com
// Source: https://github.com/electrocoder/iotdashboard
// https://iothook.com/
// http://mesebilisim.com
// Licensed under the Apache License, Version 2.0 (the "License").
// You may not use this file except in compliance with the License.
// A copy of the License is located at
// http://www.apache.org/licenses/

#include <EtherCard.h>

#define ethCSpin 10 // put your CS/SS pin here.

// ethernet interface mac address, must be unique on the LAN
static byte mymac[] = { 0x74, 0x69, 0x69, 0x2D, 0x30, 0x31 };
const char website[] PROGMEM = "iotdashboard.pythonanywhere.com";

byte Ethernet::buffer[700];
uint32_t timer;
Stash stash;
byte session;

//timing variable
int res = 100; // was 0


void setup () {
  Serial.begin(9600);
  Serial.println("\n[IoTdashboard example]");

  //Initialize Ethernet
  initialize_ethernet();
}


void loop () {
  //if correct answer is not received then re-initialize ethernet module
  if (res > 220) {
    initialize_ethernet();
  }

  res = res + 1;

  ether.packetLoop(ether.packetReceive());

  //200 res = 10 seconds (50ms each res)
  if (res == 200) {


    //Generate random info
    float demo = random(0, 500);
    word one = random(0, 500);
    String msje;

    if (demo < 250) {
      msje = "low";
    }
    else {
      msje = "high";
    }

    
    byte sd = stash.create();

    String data = "{\"api_key\":\"APIKEY\",\"value_1\":"+String(random(0,10))+",\"value_2\":"+String(random(0,10))+",\"value_3\":"+String(random(0,10))+"}";

    stash.print(data);
    stash.save();

    Serial.println(demo);

    // generate the header with payload - note that the stash size is used,
    // and that a "stash descriptor" is passed in as argument using "$H"
    Stash::prepare(PSTR("POST /api/v1.1/datas/ HTTP/1.1" "\r\n"
                        "Host: $F" "\r\n"
                        "Connection: close" "\r\n"
                        "Content-Type: application/json\r\n"
                        "Content-Length: $D" "\r\n"
                        "\r\n"
                        "$H"),
                   website, stash.size(), sd);

    // send the packet - this also releases all stash buffers once done
    session = ether.tcpSend();

    int freeCount = stash.freeCount();
    if (freeCount <= 3) {
      Stash::initMap(56);
    }
  }

  const char* reply = ether.tcpReply(session);

  if (reply != 0) {
    res = 0;
    Serial.println(F(" >>>REPLY recieved...."));
    Serial.println(reply);
  }
  delay(300);
}


void initialize_ethernet(void) {
  for (;;) { // keep trying until you succeed
    //Reinitialize ethernet module
    //pinMode(5, OUTPUT);  // do notknow what this is for, i ve got something elso on pin5
    //Serial.println("Reseting Ethernet...");
    //digitalWrite(5, LOW);
    //delay(1000);
    //digitalWrite(5, HIGH);
    //delay(500);

    if (ether.begin(sizeof Ethernet::buffer, mymac, ethCSpin) == 0) {
      Serial.println( "Failed to access Ethernet controller");
      continue;
    }

    if (!ether.dhcpSetup()) {
      Serial.println("DHCP failed");
      continue;
    }

    ether.printIp("IP:  ", ether.myip);
    ether.printIp("GW:  ", ether.gwip);
    ether.printIp("DNS: ", ether.dnsip);

    if (!ether.dnsLookup(website))
      Serial.println("DNS failed");

    ether.printIp("SRV: ", ether.hisip);

    //reset init value
    res = 180;
    break;
  }
}
