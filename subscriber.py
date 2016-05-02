##------------------------------------------
##--- Author: Pradeep Singh
##--- Date: 1st May 2016
##--- Version: 1.0
##--- Python Ver: 2.7
##--- Description: This python code will listen to MQTT Topic and print the messages on console
##------------------------------------------

import paho.mqtt.client as mqtt

# Define Variables
MQTT_BROKER = "iot.eclipse.org"
MQTT_TOPIC = "Replace this string with your MQTT Topic"


MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45

# Define on_connect event Handler
def on_connect(mosq, obj, rc):
	#Subscribe to a the Topic
	mqttc.subscribe(MQTT_TOPIC, 0)

# Define on_subscribe event Handler
def on_subscribe(mosq, obj, mid, granted_qos):
    print "Subscribed to MQTT Topic"

# Define on_message event Handler
def on_message(mosq, obj, msg):
	print msg.payload

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect with MQTT Broker
mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL )

# Continue the network loop
mqttc.loop_forever()
