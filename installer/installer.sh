#! /bib/bash

HOSTNAME = "robot1"
SSID = $HOSTNAME
SSID_PSK = "robot1"

USER     = "robot"
PASSWORD = "Swordfish" 



# 
# sets up pi as access point

echo "installing access point" 
echo
echo

sudo apt-get install hostapd udhcpd -y

echo "
start 10.0.0.2 #This is the range of IPs that the hostspot will give to client devices.
end 10.0.0.12
interface wlan0 # The device uDHCP listens on.
remaining yes
opt dns 1.1.1.1 1.0.0.1 # The DNS servers client devices will use.
opt subnet 255.255.255.0
opt router 10.0.0.1 # The Pi's IP address on wlan0 which we will set up shortly.
opt lease 300 # 5 min DHCP lease time in seconds
" | sudo tee /etc/default/udhcpd


##########################
# configure the network with fixed ip 10.0.0.1
##########################

sudo ifconfig wlan0 10.0.0.1 netmask 255.255.255.0

echo "
# interfaces(5) file used by ifup(8) and ifdown(8)
# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d

auto lo
iface lo inet loopback

iface eth0 inet manual

iface wlan0 inet static
  address 10.0.0.1
  netmask 255.255.255.0

#allow-hotplug wlan0
#iface wlan0 inet manual
#    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

allow-hotplug wlan1
iface wlan1 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

" | sudo tee /etc/network/interfaces
 
##########################
# configure hostapd
##########################
 
echo "
interface=wlan0
driver=nl80211
ssid= \${SSID}
hw_mode=g
channel=6
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=\&{SSID_PSK}
wpa_key_mgmt=WPA-PSK
#wpa_pairwise=TKIP	# You better do not use this weak encryption (only used by old client devices)
rsn_pairwise=CCMP
ieee80211n=1          # 802.11n support
wmm_enabled=1         # QoS support
ht_capab=[HT40][SHORT-GI-20][DSSS_CCK-40]
" | tee /etc/hostapd/hostapd.conf


sudo sed -i 's|#DAEMON_CONF=""|DAEMON_CONF="/etc/hostapd/hostapd.conf"|g' /etc/default/hostapd

sudo systemctl start hostapd
sudo systemctl start udhcpd 
