def update_cpu_usage(servers, usages, server_id, new_usage):
    for i in range (len(servers)):
        if servers[i] == server_id:
            usages[i] = new_usage
            return True
    return False

def decommission_idle_servers(servers, usages, idle_threshold):
    for i in range(len(servers) - 1, -1, -1):
        if usages[i] < idle_threshold:
            del servers[i]
            del usages[i]

def flag_server_load(servers, usages, high_load_threshold):
    high_load_servers = []
    normal_load_servers = []
    for i in range(len(servers)):
        if usages[i] >= high_load_threshold:
            high_load_servers.append(servers[i])
        else:
            normal_load_servers.append(servers[i])
    return high_load_servers, normal_load_servers

def analyze_server_health(initial_servers, initial_usages, server_to_update, decommission_threshold, high_load_threshold):
    servers_copy = initial_servers[:]
    usages_copy = initial_usages[:]

    update_cpu_usage(servers_copy, usages_copy, server_to_update[0], server_to_update[1])
    decommission_idle_servers(servers_copy, usages_copy, decommission_threshold)
    high_load, normal_load = flag_server_load(servers_copy, usages_copy, high_load_threshold)

    return high_load, normal_load
    
servers = ["db-01", "app-01", "web-01", "cache-01"]
usages = [12.5, 88.0, 75.5, 15.0]
update_info = ["db-01", 14.0]
idle_max_usage = 18.0
high_load_min_usage = 80.0

high_load, normal_load = analyze_server_health(servers, usages, update_info, idle_max_usage, high_load_min_usage)
print("High load:", high_load)
print("Normal load:", normal_load)

