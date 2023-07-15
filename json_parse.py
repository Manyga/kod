import os
import json

path = 'Stats_version_1_seas_20_21.json'
with open(path, 'r') as f:
    data_dict = json.load(f)
    
for match in data_dict['matches']:
    print(match['id'])
# print(data_dict['matches'])