import json

with open('data.json', 'r') as file:
    data = json.load(file)
clients_actions = 0
data_list = data['events_data']
print(data_list)
for item in data_list:
    client_id = item['client_id']
    if client_id == 18923 or client_id == 52492:
        clients_actions += 1
print(clients_actions)
