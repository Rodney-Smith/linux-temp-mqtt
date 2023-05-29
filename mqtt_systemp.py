#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f"Sorry! This program requires Python >= 3.6 😅"

import json
import os
import time
import paho.mqtt.publish as paho
from subprocess import check_output
from re import findall


def getConfig():
    # Pull the configuratin from env vars or the config file
    if os.path.isfile('./config.json'):
        with open('./config.json') as json_file:
            c = json.load(json_file)
    else:
        print("Could not find configuration file.")
        exit(1)

    # must have an mqtt topic
    if c['mqtt_']['topic'] is None:
        print("Please supply an MQTT TOPIC value.")
        exit(1)

    # must have an mqtt broker
    if c['mqtt_']['broker'] is None:
        print("Please supply an MQTT BROKER value.")
        exit(1)

    # set the mqtt port
    if c['mqtt_']['port'] is None:
        print("Please supply an MQTT PORT set to default value.")
        c['mqtt_']['port']=1883

    # must have the mqtt user
    if c['mqtt_']['user'] is None:
        print("Please supply an MQTT USER value.")
        exit(1)

    # must have the mqtt password
    if c['mqtt_']['password'] is None:
        print("Please supply an MQTT PASSWORD value.")
        exit(1)

    return c


def get_temp():
    temp_celsius = float(check_output(["vcgencmd","measure_temp"]).decode("UTF-8"))
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return str(temp_fahrenheit)


def mqtt(payload):
    print("Publishing to MQTT topic: " + mqtt_topic)
    print("Temperature: " + payload)
    try:
        mqtt_auth = None
        if len(mqtt_user) > 0:
            mqtt_auth = { 'username': mqtt_user, 'password': mqtt_password }

        paho.single(mqtt_topic, payload, qos=0, retain=False, hostname=mqtt_broker,
        port=mqtt_port, client_id=mqtt_clientid, keepalive=60, will=None, auth=mqtt_auth,
        tls=None)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        pass 


config = getConfig()
# get the config
mqtt_clientid = config['mqtt_']['clientid']
mqtt_topic = config['mqtt_']['topic']
mqtt_broker = config['mqtt_']['broker']
mqtt_port = config['mqtt_']['port']
mqtt_user = config['mqtt_']['user']
mqtt_password = config['mqtt_']['password']

while(True):
    #
    # Connect to the local MQTT broker
    #
    try:
        temp = get_temp()
        mqtt(temp)

        # Blocking loop to the local Mosquitto broker
        paho.loop_forever()
    except:
        print("Failed connection to local MQTT broker");

    time.sleep(900)


__author__ = "Rodney Smith"
__copyright__ = "Copyright 2021, Temperature Reporting Project"
__license__ = "MIT"
__version__ = "1.0.2"
__contact__ = "rodney.delauer@gmail.com"
__status__ = "Development"
