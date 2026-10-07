def update_teams(teams, updates):
    new_teams = []

    # clone each inner list
    for team in teams:
        new_teams.append(team[:])

    # apply updates to the cloned structure
    for update in updates:
        team_index = update[0]
        player_id = update[1]

        new_teams[team_index].append(player_id)

    return new_teams