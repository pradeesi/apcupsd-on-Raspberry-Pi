##------------------------------------------
##--- Author: Pradeep Singh
##--- Date: 1st May 2016
##--- Version: 1.0
##--- Raspberry Pi OS: Raspbian
##--- Python Ver: 2.7
##--- Description: This python code will read command line argument and publish that to MQTT
##------------------------------------------


# Import package
import argparse
import paho.mqtt.client as mqtt

# Define Variables
MQTT_BROKER = "iot.eclipse.org"
MQTT_TOPIC = "Replace this string with your MQTT Topic"


MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45

# Read command line argument and Publish on MQTT Topic
parser = argparse.ArgumentParser(description='APC UPS Event Messages')
parser.add_argument('event_data')
args = parser.parse_args()
MQTT_MSG = (args.event_data)

# Define on_connect event Handler
def on_connect(mosq, obj, rc):
	print "Connected to MQTT Broker"

# Define on_publish event Handler
def on_publish(client, userdata, mid):
	print "Message Published..."

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect

# Connect with MQTT Broker
mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 

# Publish message to MQTT Topic 
mqttc.publish(MQTT_TOPIC,MQTT_MSG)

# Disconnect from MQTT_Broker
mqttc.disconnect()
