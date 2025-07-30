# verificar_eigrp6.py
from restconf_client import RestconfClient

client = RestconfClient("192.168.190.2", "admin", "cisco123")

res1 = client.get("ietf-interfaces:interfaces")
res2 = client.get("Cisco-IOS-XE-eigrp-oper:eigrp-oper-data")
res3 = client.get("ietf-routing:routing-state/routing-instance")

with open("evidencias/log_interfaces.txt", "w") as f:
    f.write("Interfaces:\n" + res1.text + "\n")

with open("evidencias/log_vecinos_eigrp.txt", "w") as f:
    f.write("Vecinos EIGRP:\n" + res2.text + "\n")

with open("evidencias/log_routing_table.txt", "w") as f:
    f.write("Routing Table:\n" + res3.text + "\n")

print("✅ Verificación completada.")