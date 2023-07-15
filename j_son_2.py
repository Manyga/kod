import datetime
import os
import json
import time 
import dateutil 


# date = input('Введите дату в формае дд.мм.гггг: ')
#date = '20230505'
#data_2 =datetime.datetime.strptime(date,'%Y%m%d')
#print(data_2.strftime('%y-%m-%d'))                       ТУТ ОБЪЯСНЯЕТСЯ КАК  ЗАЛАТЬ ФОРМАТ

path_json = (r'C:\Users\manij\OneDrive\Рабочий стол\домэшка\Stats_version_1_seas_20_21.json')
with open(path_json, 'r') as file_read:

    data_dict = json.load(file_read)
    
#for match in data_dict['matches']:
    #match_day_str = match['utcDate']
    #match_day_str = match_day_str[:10]
    #print(type(match_day_str))
    #print(type(data_2))
    #match_day_datatime = datetime.datetime.strptime(match_day_str.replace('-',''),'%Y%m%d') 
    
    #exit()
    # match_day_datatime = datetime.datetime.strptime(match_day_str,'%y-%m-%dT%H:%M:%SZ')
    # match_day_datatime = dateutil.parser.parse(match_day_str)
    # print(match_day_str)

# for index in range(len(match_day_str)):
#     # print(match_day_str)
#     print(match_day_str[index:10])
    
