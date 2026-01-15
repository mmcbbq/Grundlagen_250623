import json

names = [
    "Thorsten",
    "Sherwin",
    "Felix",
    "Wlad",
    "Michael",
    "Alexander",
    "Hassan",
    "Achmed",
    "Reza",
    "Jiwan",
    "Yanwolf",
    "Jason",
    "Edwin"
]

# Erstellen sie eine Liste mit Dictionaries fuer jeden Namen


# name : Jason, subnet: 192.168.0.0, agent_ip :172.16.99.100, raum:r_1
# name : Edwin, subnet: 192.168.10.0, agent_ip :172.16.99.101, raum:r_2
# data = []
# subnet_ip = 0
# agent_ip = 100
# r_nr = 1
# for x in names:
#     line = {'name': x, 'subnet': f'192.168.{subnet_ip}.0', 'agent_ip': f'172.16.99.{agent_ip}', 'raum': f'r_{r_nr}'}
#     data.append(line)
#     subnet_ip += 10
#     agent_ip += 1
#     r_nr += 1
# # Speichere die Liste in einem jason file 'name'-network-data
# # for y in data:
# #     print(y)
#
# with open('manuel-network-data.json','w') as f:
#     f.write(json.dumps(data))


# erstelle eine netplan conf fuer jeden router
with open('manuel-network-data.json') as f:
    data = json.loads(f.read())
# print(type(data))

for x in data:
    name = x['name'].lower()
    bbq_net = x['agent_ip']
    subnet = x['subnet']
    sp = '  '
    with open(f'netplan-conf/99_{name}.yaml', 'w') as f:
        f.write('network:\n')
        f.write(f'{sp *1}version: 2\n')
        f.write(f'{sp *1}ethernets:\n')
        f.write(f'{sp *2}eth0:\n')
        f.write(f'{sp *3}addresses: [{bbq_net}/24]\n')
        f.write(f'{sp *3}routes:\n')
        f.write(f'{sp *4}- to: default\n')
        f.write(f'{sp *5}via: 172.16.98.254\n')
        for route in data:
            r_name = route['name'].lower()
            r_bbq_net = route['agent_ip']
            r_subnet = route['subnet']
            if x == route:
                continue
            f.write(f'# {r_name}\n')
            f.write(f'{sp *4}- to: {r_subnet}/24\n')
            f.write(f'{sp *5}via: {r_bbq_net}\n')


        f.write(f'{sp *2}eth1:\n')
        f.write(f'{sp *3}addresses: [{subnet}/24]\n')