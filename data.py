#wifi information
wifi_channel= "1"
wifi_bssid= "C8:3A:35:46:5F:30"
wifi_essid= " Tenda_465F30"
wifi_encrypt= " WPA2 WPA"
wifi_password= ""
wifi_version = "v"

#router information
router= "7200 Software (C7200-ADVENTERPRISEK9-M)"
router_ip= "192.168.1.1"
router_version = "12.4(24)TS"
router_vulnerability= "Default Credentials Attack"
router_username= "admin"
router_usrpw= "admin"


#Scan subnets
host_up= ["192.168.0.1", "192.168.1.1", "192.168.10.1", "192.168.10.103", "192.168.10.104", "192.168.2.1", "192.168.3.1", "192.168.3.5"]
subnets_input= ["192.168.0-15.0/24"]

#Scan service
ip_scan_service= ["192.168.1.1"]
nmap_result= ["21/tcp - state:filtered - service:ftp", "22/tcp - state:filtered - service:ssh", "23/tcp - state:open - service:telnet Cisco router telnetd", "25/tcp - state:filtered - service:smtp", "80/tcp - state:open - service:http Cisco IOS http config", "443/tcp - state:filtered - service:https"]
