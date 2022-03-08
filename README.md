# [Raspberry Pi Temperature Project](https://github.com/Rodney-Smith/linux-temp-mqtt)

Raspberry Pi Temperature Reporting

### Hardware supplies needed for this project:

- [Raspberry Pi Zero WH](https://www.adafruit.com/product/3708)
- [Raspberry Pi 3 - Model B](https://www.adafruit.com/product/3055)
- [Raspberry Pi 4 Model B (2GB, 4GB or 8GB)](https://www.adafruit.com/product/4296)

- HomeAssistant Installation with Mosquitto broker


### RPi OS used:

- Installed Bullseye - Lite - Headless - Pi Zero WH

### Download the project on the Raspberry Pi
```
sudo mkdir /opt/scripts
sudo chown pi:root /opt/scripts
cd /opt/scripts
git clone https://github.com/Rodney-Smith/linux-temp-mqtt.git
```

### Install dependencies
```
sudo apt-get update && sudo apt-get install -y build-essential git python3 python3-pip python3-dev python3-libgpiod python3-pil python3-setuptools
sudo pip3 install -r requirements.txt
```

### Modify the config.json file
```
cd /opt/scripts/linux-temp-mqtt
mv config.example.json config.json
nano config.json
{
    "mqtt": {
        "clientid":"unique-id",
        "topic":"linux/hostname/temperature",
        "broker":"mqttbroker.local",
        "port":1883,
        "user":"mqttusername",
        "password":"mqttpassword"
    }
}
```

### Enable and start the service

Create or copy the startup service for the python script:
```
sudo cp /opt/scripts/linux-temp-mqtt/SystemTemperature.service /etc/systemd/system/SystemTemperature.service
```

Next you will need to reload, enable and start the new service:
```
sudo systemctl daemon-reload
sudo systemctl enable SystemTemperature.service
sudo systemctl start SystemTemperature.service
```
Ensure there are no errors.
`systemctl status SystemTemperature.service`
or
`sudo journalctl -u ReportTemp.service -f`
