# configurar_eigrp6.py
from restconf_client import RestconfClient
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Instanciar el cliente
client = RestconfClient("192.168.190.2", "admin", "cisco123")

# --- Hostname
with open("payloads/hostname.json") as f:
    hostname = json.load(f)
res1 = client.patch("Cisco-IOS-XE-native:native/hostname", hostname)

# --- Interfaces
with open("payloads/interfaces.json") as f:
    interfaces = json.load(f)
res2 = client.patch("ietf-interfaces:interfaces", interfaces)

# --- Unicast
with open("payloads/unicast_routing.json") as f:
    unicast = json.load(f)
res3 = client.patch("Cisco-IOS-XE-native:native", unicast)

# --- Router config
with open("payloads/router.json") as f:
    router = json.load(f)
res4 = client.patch("Cisco-IOS-XE-native:native", router)

# Guardar logs
with open("evidencias/log_configuracion.txt", "w") as f:
    f.write("Hostname:\n" + res1.text + "\n")
    f.write("Interfaces:\n" + res2.text + "\n")
    f.write("Unicast:\n" + res3.text + "\n")
    f.write("EIGRPv6:\n" + res4.text + "\n")

print("✅ Configuración completada.")