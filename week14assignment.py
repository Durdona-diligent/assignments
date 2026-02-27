def load_server_config(config_list):
    config_dict = {item['ip_address']: item['hostname'] for item in config_list}
    return config_dict


def check_network_status(config_dict, active_ips):
    offline_set = set(config_dict.keys())
    active_set = set(active_ips)
    offline_servers = offline_set - active_set
    rogue_devices = active_set - offline_set
    return offline_servers, rogue_devices

def create_outage_alert(config_dict, offline_set):
#"CRITICAL: [Hostname] is DOWN ([IP])"
    alert = [(config_dict[ip], ip) for ip in offline_set]
    alert.sort(key=lambda item: item[0])
    alerts = [f"CRITICAL: {hostname} is DOWN ({ip})" for hostname, ip in alert]
    return alerts

config = [
    {'ip_address': "192.168.1.5", 'hostname': "Database-01"},
    {'ip_address': "192.168.1.6", 'hostname': "Web-01"},
    {'ip_address': "192.168.1.7", 'hostname': "Cache-01"}
]

pings = ["192.168.1.6", "192.168.1.7", "10.0.0.1"]

config_dict = load_server_config(config)
offline, rogue_devices = check_network_status(config_dict, pings)
alerts = create_outage_alert(config_dict, offline)
print(f'Offline Servers: {offline}')
print(f'Rogue Devices: {rogue_devices}')
print(f'Report: {alerts}')