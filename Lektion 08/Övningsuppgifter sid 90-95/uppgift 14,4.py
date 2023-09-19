import dict

def add_game(home_team, home_score, away_team, away_score):
    """Fyller dictionaryt med matchinformation för en match."""
    # Uppdatera vinststatistik

    if home_score > away_score:
        home_team["wins"] += 1
        away_team["losses"] += 1
    elif home_score < away_score:
        away_team["wins"] += 1
        home_team["losses"] += 1
    else:
        home_team["draws"] += 1
        away_team["draws"] += 1

    # Uppdatera målstatistik

    home_team["goals_for"] += home_score
    home_team["goals_against"] += away_score
    away_team["goals_for"] += away_score
    away_team["goals_against"] += home_score


def print_table(teams):
    """Skriver ut en tabell med statistik för alla lag i gruppen."""
    print("-------------------------------------")
    print("| Nation | W | D | L | GF | GA |")
    print("-------------------------------------")
    for nation, data in teams.items():
        print(f"| {nation} | {data['wins']} | {data['draws']} | {data['losses']} | {data['goals_for']} | {data['goals_against']} |")
    print("-------------------------------------")

# 17 June 2018 #
add_game("Costa Rica", 0, "Serbia", 1)
add_game("Brazil", 1, "Switzerland", 1)
# 22 June 2018 #
add_game("Brazil", 2, "Costa Rica", 0)
add_game("Serbia", 1, "Switzerland", 2)
# 27 June 2018 #
add_game("Serbia", 0, "Brazil", 2)
add_game("Switzerland", 2, "Costa Rica", 2)

print_table(teams)
