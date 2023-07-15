import json
from team_play import team_play
pah_json = (r'C:\Users\manij\OneDrive\Рабочий стол\домэшка\premier_league_statistic.json')
with open(pah_json, 'r') as file:
    json_data = json.load(file)
#print(json_data.keys())
#print(json_data['matches'][0].values())
#print(json_data.values())
#print(json_data['matches'][0].values())
# for match in json_data['matches']:
    # match_day_str = match['utcDate']
    # match_day_str = match_day_str[:10]
    # print(type(match_day_str))
    # print(type(data_2))

# def extract_teams_from_json(json_data):
#     teams = {}
#     matches = json_data["matches"]
#     for match in matches:
#         home_team = match["homeTeam"]
#         away_team = match["awayTeam"]
#         teams[home_team["id"]] = home_team["name"]
#         teams[away_team["id"]] = away_team["name"]
#     return teams
# result = extract_teams_from_json(json_data)
# print(result)

date = '2020-11-06'
team_play(json_data, date)

