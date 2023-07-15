def team_play(json_data, date):
    teams = []
    matches = json_data["matches"]
    for match in matches:
        match_date = match["utcDate"]
        match_date = match_date[:-10]
        if match_date == date:
            home_team = match["homeTeam"]["name"]
            away_team = match["awayTeam"]["name"]
            print(home_team, away_team)
        #print(match_date)