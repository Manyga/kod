import json

pah_json = r'C:\Users\manij\OneDrive\Рабочий стол\домэшка\Stats_version_1_seas_20_21.json'
with open(pah_json, 'r') as file:
    json_data = json.load(file)
#print(json_data.keys())
#print(json_data['matches'][0].values())
#print(json_data.values())
#print(json_data['matches'][0].values())
commands = {}
for command in json_data:
    command_id = command["id"]
    command_name = command["name"]
    commands[command_id] = command_name
print(commands)


