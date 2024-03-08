
![Help](/doc/img/help_update.png)

### RougeBTS Fork For DragonOS

This project was forked from DrLafa to work specifically on the DragonOS distro. This was created for easy deployment of Osmocom GSM stack and convenient interaction with users

  - E(GPRS) support
  - Asterisk support
  - Monitoring online subscribers
  - Automatic interaction with new users, like sms, ussd or call
  - Manual interaction with individual users
  - USSD-broadcast
  - SMS-broadcast
  - SMS-spam >:D


![RougeBTS](/doc/img/RougeBTS_update.png)

Software was tested on [LimeSDR-Mini + Orange Pi Zero](https://codeby.net/threads/miniatjurnaja-sotovaja-stancija-na-baze-limesdr-mini-i-orange-pi-zero.66747/) with Armbian Bionic and Debian 10. Forked version tested with USRP B210 on DragonOS. 

### Installation (Not Required For DragonOS)
Installing LimeSuite
```
apt install git g++ cmake libsqlite3-dev libi2c-dev libusb-1.0-0-dev
git clone https://github.com/myriadrf/LimeSuite.git
cd LimeSuite
mkdir builddir && cd builddir
cmake ../
make -j4
sudo make install
sudo ldconfig
cd ../udev-rules/
sudo sh LimeSuite/udev-rules/install.sh
cd ~/
```
Installing UHD
```
sudo add-apt-repository ppa:ettusresearch/uhd
sudo apt-get update
apt install libuhd-dev libuhd003 uhd-host
```
Adding the Osmocom repository
```
sudo su
wget http://download.opensuse.org/repositories/network:/osmocom:/latest/Debian_10//Release.key
apt-key add Release.key
rm Release.key
echo "deb  http://download.opensuse.org/repositories/network:/osmocom:/latest/Debian_10/ ./" > /etc/apt/sources.list.d/osmocom-latest.list
apt update
exit
```
Installing
```
sudo apt install osmocom-nitb osmo-trx-lms osmo-bts-trx osmo-ggsn osmo-sgsn osmo-pcu osmo-sip-connector libsofia-sip-ua-glib-dev asterisk sqlite3 libsmpp1 telnet python3-pip
sudo pip3 install smpplib
```
It is necessary to install Osmocom stack from apt, because it configure Systemd services. If you compile osmocom from sources, you need to install Systemd services by yourself with script `install_services.sh`
```
sudo ./install_services.sh
```
Stopping launched services after installation
```
sudo su
systemctl stop osmocom-nitb
systemctl stop osmo-nitb
systemctl stop osmo-trx-lms
systemctl stop osmo-bts-trx
systemctl stop osmo-ggsn
systemctl stop osmo-sgsn
systemctl stop osmo-pcu
systemctl stop osmo-sip-connector
systemctl stop asterisk
exit
```
Disabling service autostart
```
sudo su
systemctl disable osmocom-nitb
systemctl disable osmo-nitb
systemctl disable osmo-trx-lms
systemctl disable osmo-bts-trx
systemctl disable osmo-ggsn
systemctl disable osmo-sgsn
systemctl disable osmo-pcu
systemctl disable osmo-sip-connector
systemctl disable asterisk
```
Cloning
```
git clone https://github.com/DrLafa/osmo-nitb-scripts
```

### Configure
All osmocom config files stored in `config/` folder and updating everytime when you start `main.py`. You can change it by youself.

### config.json
For easy setup of user-interactivity you can use config.json
- config.json example
```
{
   "scripts":{
      "sms":{
         "enabled": true,
         "sender_extension": "DragonOS",
         "message":[
            "If you are reading this, you are on the DragonOS BTS Network"
         ]
      },
      "ussd":{
         "enabled": false,
         "ussd_type": 1,
         "message":[
            "Welcome to DragonOS!",
            "If you are reading this, you are on the DragonOS BTS Network"
         ]
      },
      "call":{
         "enabled": false,
         "caller_extension": 666,
         "voice-file": "tt-monkeys"
      }
   }
}
```
#### sms
Send sms to new users. When user connect to network, script choose 1 random message from ```message``` section and sending it from extension ```sender_extension```

#### ussd
Send ussd to new users. Script choose 1 random message from ```message``` section adn sending it to user

#### call
Make a call to new user. This function works only with Asterisk support. voice-file is 16-bit 8 kHz wav file. If ```caller_extension``` is ```false```, then the user sees that the phone is not defined.
