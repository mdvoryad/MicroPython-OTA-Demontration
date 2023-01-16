import time
from umqttsimple import MQTTClient
import umqtt.simple
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
import ssl
import ubinascii
import machine
try:
  import usocket as socket
except:
    import requests
try:
  import urequests as requests
except:
  import requests
import os 
import sys
import esp
esp.osdebug(None)
import gc
gc.collect()
from utime import sleep
from utime import sleep_ms
import network




ssid = 'FRITZ!Box 7490'
password = '57345154416262824818'
mqtt_server = '192.168.178.101'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'testTopic'
topic_pub = b'notification'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())



def sub_cb(topic, msg):
  print((topic, msg))
  if msg != None:
        #print(msg)
        print('Downloading update')
    #download the update and overwrite program.py
        string = msg.decode('utf-8')
        parts = string.split("\n")
        parts.pop()
        print(len(parts))
        for element in parts:
            print(element)
            response = requests.get(upd_url+element)
            x = response.text.find("FAIL")
        
            f = open(element,"w")
            f.write(response.text)
            f.flush()
            f.close
            
      
        print('reboot now')
        machine.deepsleep(5000) 
  
# Set up the MQTT broker connection details
BROKER_ADDRESS = "192.168.178.148"
BROKER_PORT = 8883  # default MQTT over TLS port
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b'ESP32/update'
USER = 'ESP32'
PASSWORD = 'mike'
KEEPALIVE = 5
upd_url="http://192.168.178.148/esp32/index.php?file=/repo/"
# Set up the TLS configuration
with open("ca.key", "r") as f: 
    key = f.read()
print("Got Key")

with open("ca.crt", "r") as f: 
    cert = f.read()
print("Got Cert")

print(key)
print(cert)
# Connect to the MQTT broker
mqtt = umqtt.simple.MQTTClient(CLIENT_ID, BROKER_ADDRESS, BROKER_PORT,USER,PASSWORD,KEEPALIVE, ssl=True,  ssl_params={"cert":cert, "server_side":False})
print(mqtt.user)
print(mqtt.pswd)
print(mqtt.client_id)

mqtt.set_callback(sub_cb)
mqtt.connect()
mqtt.subscribe(TOPIC)
x = 0

while True:
    mqtt.ping()
    msg = mqtt.check_msg()
    print("I do stuff for demonstration")
    

    

# Publish the message to the MQTT broker

# Disconnect from the MQTT broker
mqtt.disconnect()
# This file is executed on every boot (including wake-boot from deepsleep)
print("lolo")
#import esp

#esp.osdebug(None)

#import webrepl

#webrepl.start()


