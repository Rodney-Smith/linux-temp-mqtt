# Raspberry Pi Temperature Project

Raspberry Pi Temperature Reporting

### Hardware supplies needed for this project:

- [Raspberry Pi Zero WH](https://www.adafruit.com/product/3708)
- [Raspberry Pi 3 - Model B](https://www.adafruit.com/product/3055)
- [Raspberry Pi 4 Model B (2GB, 4GB or 8GB)](https://www.adafruit.com/product/4296)

- HomeAssistant Installation with Mosquitto broker


### RPi OS used:

- Installed Buster - Lite - Headless

### Installed on the Raspberry Pi

- `sudo apt-get install -y git python3 build-essential python3-pip python3-dev python3-libgpiod python3-pil python3-setuptools`
- `sudo python3 -m pip install --upgrade pip setuptools wheel`
- `sudo pip3 install  -r requirements.txt`

ssh into the RPi

Modify the config.json to incorporate the MQTT broker configuration and the unique hostname in the topic path.

Create or copy the startup service for the Python script:

`sudo cp /opt/scripts/ReportTemp.service /etc/systemd/system/ReportTemp.service`

Next you will need to reload, enable and start the new service:

`sudo systemctl daemon-reload && systemctl enable ReportTemp.service && systemctl start ReportTemp;`

Ensure there are no errors.

`sudo journalctl -u ReportTemp.service -f`
