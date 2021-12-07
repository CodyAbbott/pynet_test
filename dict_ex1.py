network_device = { 
    "ip_address":"10.1.1.4",
    "username":"admin",
    "password":"cisco123",
    "vendor":"cisco",
    "model":"Nexus"
}

network_device["password"] = "Cisco1234!"
network_device["secret"] = "s4gjhv34klnon65fg3sd"
for i in network_device:
    print(i + "  " + network_device[i])

print(network_device.get("device_type", "cisco_ios"))