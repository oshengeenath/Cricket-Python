def previous_tournament():
    check = 0
    while check != 5:
        while True:
            try:
                check = int(input('What do you want to check?\n1.Match summaries\n2.Top 5 Batsmen\n3.Top 5 Bowler\n4.Tournament Standings\n5.Continue\n'))
                print('--------------------------------------------------------------------------------------')
                if check > 0 and check < 6:
                    break
                else:
                    raise Exception
            except Exception:
                print('Invalid Input')
        if check == 1:
            print('--------------------------------------------------------------------------------------')
            print('Which match summary do you want to check')
            print('--------------------------------------------------------------------------------------')
            summary_file = open('previous_summary.txt', 'r')
            summary_list = summary_file.readlines()
            summary_file.close()

            for match_number in range(7):
                corrected_match = match_number + 1
                team1vsteam2 = summary_list[(match_number * 7) + 1]
                print('Match 0' + str(corrected_match) + '\n' + team1vsteam2)

            while True:
                try:
                    print('--------------------------------------------------------------------------------------')
                    m_summary = int(input('>>>'))
                    if m_summary > 0 and m_summary < 8:
                        break
                    else:
                        raise Exception
                except ValueError:
                    print('Invalid Input')
                except Exception:
                    print('Invalid Input')
            print('--------------------------------------------------------------------------------------')

            corrected_m_summary = (m_summary - 1) * 7
            for user_match_summary in range(corrected_m_summary, corrected_m_summary + 7):
                print(summary_list[user_match_summary])

            print('--------------------------------------------------------------------------------------')

        elif check == 2:
            batsmen = open('previous_best_batsmen.txt', 'r')
            top5_batsmen = batsmen.readlines()
            batsmen.close()
            runs = open('previous_best_batsmen_runs.txt', 'r')
            batsmen_runs = runs.readlines()
            runs.close()
            for top5 in range(5):
                position = top5 + 1
                temporary = batsmen_runs[top5].split()
                print(str(position) + ')' + top5_batsmen[top5][1:].removesuffix('\n') + ' - ' + temporary[0][1:] + '(' +
                      temporary[2].removesuffix('\n') + ')')
            print('--------------------------------------------------------------------------------------')

        elif check == 3:
            baller = open('previous_best_balling.txt', 'r')
            top5_baller = baller.readlines()
            baller.close()
            wickets = open('previous_best_balling_wickets.txt', 'r')
            baller_wickets = wickets.readlines()
            wickets.close()
            for top5 in range(5):
                position = top5 + 1
                print(str(position) + ')' + top5_baller[top5][1:].removesuffix('\n') + ' - ' + baller_wickets[top5][1:].removesuffix('\n'))
            print('--------------------------------------------------------------------------------------')

        elif check == 4:
            leaderboard = open('previous_leaderboard.txt', 'r')
            team_standings = leaderboard.readlines()
            leaderboard.close()
            for teams in range(8):
                position = teams + 1
                print(str(position) + ' - ' + team_standings[teams][1:])
            print('--------------------------------------------------------------------------------------')

def edit_the_team(edit_team):
    if edit_team == '1':
        readteamfile = open('teams.txt', 'r')
        teams = readteamfile.readlines()
        readteamfile.close()
        print('--------------------------------------------------------------------------------------')
        print('What team name should you edit?')
        print('--------------------------------------------------------------------------------------')
        for i in range(8):
            print(i + 1, '-', teams[i][1:])
        print('--------------------------------------------------------------------------------------')
        while True:
            try:
                team_name = int(input('>>>'))
                if team_name > 0 and team_name <= 8:
                    break
                else:
                    raise Exception
            except ValueError:
                print('Invalid Input!')
            except Exception:
                print('Invalid Input!')
        print('---------------------------------------------------------------------------------------')
        new_team_name = str(input("What name should we change it to?"))
        teams[team_name - 1] = teams[team_name - 1][0] + new_team_name + '\n'
        append_team_name = open('teams.txt', 'w')
        append_team_name.writelines(teams)
        append_team_name.close()

def edit_the_player(edit_player):
    if edit_player == '1':
        team_file = open('teams.txt', 'r')
        teams = team_file.readlines()
        team_file.close()
        player_file = open('players.txt', 'r')
        players = player_file.readlines()
        player_file.close()
        print('--------------------------------------------------------------------------------------')
        print('What is the team number of the player that you want to replace')
        print('--------------------------------------------------------------------------------------')
        for i in range(8):
            print(i + 1, '-', teams[i][1:])
            for j in range(i * 12, ((i + 1) * 12) - 1):
                print(players[j][1:])
            print('--------------------------------------------------------------------------------------')
        while True:
            try:
                team_name = int(input('>>>'))
                if team_name > 0 and team_name <= 8:
                    break
                else:
                    raise Exception
            except ValueError:
                print('Invalid Input!')
            except Exception:
                print('Invalid Input!')
        print('--------------------------------------------------------------------------------------')
        corrected_team_num = team_name - 1
        print('What player do you want to replace')
        print('--------------------------------------------------------------------------------------')
        for k in range(corrected_team_num * 12, (corrected_team_num + 1) * 12 - 1):
            print(k + 1, '-', players[k][1:])
        while True:
            try:
                player_num = int(input('\n>>>'))
                if player_num > corrected_team_num * 12 and player_num <= (corrected_team_num + 1) * 12 - 1:
                    break
                else:
                    raise Exception
            except ValueError:
                print('Invalid Input')
            except Exception:
                print('Invalid Input')
        print('--------------------------------------------------------------------------------------')
        new_player = str(input('What player are you going to add'))
        print('--------------------------------------------------------------------------------------')
        players[player_num - 1] = new_player + '\n'
        edit_player_file = open('players.txt', 'w')
        edit_player_file.writelines(players)
        edit_player_file.close()

def shuffle_teams():
    team_file = open('teams.txt', 'r')
    team_list = team_file.readlines()
    team_file.close()

    import random
    random.shuffle(team_list)

    new_team_file = open('teams.txt', 'w')
    new_team_file.writelines(team_list)
    new_team_file.close()
    team_standings_file = open('team_standing_names.txt', 'w')
    team_standings_file.writelines(team_list)
    team_standings_file.close()

def toss(team):
    import random as coin
    toss = coin.randint(0, 1)
    if toss == 0:
        toss_won = team
        import random as bat_or_ball
        decision = bat_or_ball.randint(0, 1)
        if decision == 0:
            bat_first = team
            ball_first = team + 1
        else:
            bat_first = team + 1
            ball_first = team
    else:
        toss_won = team + 1
        import random as bat_or_ball
        decision = bat_or_ball.randint(0, 1)
        if decision == 0:
            bat_first = team + 1
            ball_first = team
        else:
            bat_first = team
            ball_first = team + 1
    return(bat_first, ball_first, toss_won, decision)

def matches(match, bat_first, ball_first, innings):
    players = 0
    player_score = 0
    no_of_balls_player = 0
    player_wicket = 0
    baller = 5
    overall_batting_file = open('overall_batting.txt', 'r')
    overall_batting_list = overall_batting_file.readlines()
    overall_batting_file.close()
    overall_balling_file = open('overall_balling.txt', 'r')
    overall_balling_list = overall_balling_file.readlines()
    overall_balling_file.close()
    overall_score_file = open('overall_teamscore.txt', 'r')
    overall_score_list = overall_score_file.readlines()
    overall_score_file.close()
    batting_file_name = 'batting_match-' + str(match) + '.txt'
    batting_file = open(batting_file_name, 'r')
    batting_list = batting_file.readlines()
    batting_file.close()
    temporary_batting_file = open(batting_file_name, 'r')
    batsmen_change = temporary_batting_file.readlines()
    temporary_batting_file.close()
    balling_file_name = 'balling_match-' + str(match) + '.txt'
    balling_file = open(balling_file_name, 'r')
    balling_list = balling_file.readlines()
    balling_file.close()
    batsmen_number = players + (bat_first * 12)
    batsmen_change[batsmen_number] = 'True\n'
    batsmen_change[batsmen_number + 1] = 'False\n'
    overall_score = 0
    total_wicket = 0
    all_players_notout = False
    import random
    for overs in range(20):
        for balls in range(6):
            score = random.randint(0, 6)
            if not score == 5:
                overall_score = overall_score + score
                for player1 in range(batsmen_number, 95):
                    if batsmen_change[player1] == 'True\n':
                        temporary_list = batting_list[player1].split(' ')
                        player_score = int(temporary_list[0]) + score
                        no_of_balls_player = int(temporary_list[2]) + 1
                        batting_list[player1] = str(player_score) + ' - ' + str(no_of_balls_player) + ' - notout' + '\n'
                        break
                if score == 1 or score == 3:
                    for player2 in range(batsmen_number, 95):
                        if batsmen_change[player2] == 'True\n':
                            batsmen_change[player2] = 'False\n'
                        elif batsmen_change[player2] == 'False\n':
                            batsmen_change[player2] = 'True\n'
            else:
                for player3 in range(batsmen_number, 95):
                    if batsmen_change[player3] == 'True\n':
                        total_wicket = total_wicket + 1
                        temporary_list = batting_list[player3].split()
                        overall_temporary_list = overall_batting_list[player3].split()
                        overall_player_runs = int(overall_temporary_list[0][1:]) + int(temporary_list[0])
                        no_of_balls_player = int(temporary_list[2]) + 1
                        overall_player_balls = int(overall_temporary_list[2]) + no_of_balls_player
                        method_of_dismissal = random.randint(1, 4)
                        if method_of_dismissal == 1:
                            dismissal = 'caught'
                        elif method_of_dismissal == 2:
                            dismissal = 'bowled'
                        elif method_of_dismissal == 3:
                            dismissal = 'LBW'
                        else:
                            dismissal = 'stumped'
                        batting_list[player3] = str(temporary_list[0]) + ' - ' + str(no_of_balls_player) + ' - ' + dismissal + '\n'
                        overall_batting_list[player3] = overall_batting_list[player3][:1] + str(overall_player_runs) \
                                                        + ' - ' + str(overall_player_balls) + '\n'
                        batsmen_change[player3] = '-1\n'
                    if batsmen_change[player3] == '0 - 0 - notout\n':
                        batsmen_change[player3] = 'True\n'
                        break
                baller_number = baller + (ball_first * 12)
                player_wicket =int(balling_list[baller_number]) + 1
                balling_list[baller_number] = str(player_wicket) + '\n'
                overall_player_wicket = int(overall_balling_list[baller_number][1:].removesuffix('\n')) + 1
                overall_balling_list[baller_number] = overall_balling_list[baller_number][:1] + str(overall_player_wicket) + '\n'
                players = players + 1
            if innings > 0:
                if overall_score > int(overall_score_list[ball_first]):
                    all_players_notout = True
                    break
            if players >= 10:
                break
        if innings > 0:
            if overall_score > int(overall_score_list[ball_first]):
                all_players_notout = True
                break
        if players >= 10:
            break
        baller = baller + 1
        if baller > 10:
            baller = 5
        for player4 in range(batsmen_number, 95):
            if batsmen_change[player4] == 'True\n':
                batsmen_change[player4] = 'False\n'
            elif batsmen_change[player4] == 'False\n':
                batsmen_change[player4] = 'True\n'
    new_batting_file = open(batting_file_name, 'w')
    new_batting_file.writelines(batting_list)
    new_batting_file.close()
    new_balling_file = open(balling_file_name, 'w')
    new_balling_file.writelines(balling_list)
    new_balling_file.close()
    new_overall_batting = open('overall_batting.txt', 'w')
    new_overall_batting.writelines(overall_batting_list)
    new_overall_batting.close()
    new_overall_balling = open('overall_balling.txt', 'w')
    new_overall_balling.writelines(overall_balling_list)
    new_overall_balling.close()
    overall_score_list[bat_first] = str(overall_score) + '\n'
    new_overall_score = open('overall_teamscore.txt', 'w')
    new_overall_score.writelines(overall_score_list)
    new_overall_score.close()
    return all_players_notout, total_wicket

def match_summary(match, match_number, all_players_notout, wickets, toss_won, decision, bat_first, ball_first, match_type):
    team_file = open('team_standing_names.txt', 'r')
    team_list = team_file.readlines()
    team_file.close()
    team1 = team_list[bat_first][1:-1]
    team2 = team_list[ball_first][1:-1]
    team_standing_file = open('team_standings.txt', 'r')
    team_standing_list = team_standing_file.readlines()
    team_standing_file.close()
    overall_teamscore_file = open('overall_teamscore.txt', 'r')
    overall_teamscore_list = overall_teamscore_file.readlines()
    overall_teamscore_file.close()
    summary_file = open('match_summary.txt', 'r')
    summary_list = summary_file.readlines()
    summary_file.close()
    batting_file_name = 'batting_match-' + str(match) + '.txt'
    batting_file = open(batting_file_name, 'r')
    batting_list = batting_file.readlines()
    batting_file.close()
    balling_file_name = 'balling_match-' + str(match) + '.txt'
    balling_file = open(balling_file_name, 'r')
    balling_list = balling_file.readlines()
    balling_file.close()
    players_file = open('players.txt', 'r')
    batting_players_list = players_file.readlines()
    players_file.close()
    players_file1 = open('players.txt', 'r')
    balling_players_list = players_file1.readlines()
    players_file1.close()
    toss = team_list[toss_won][1:-1]
    team_standing_list[bat_first] = str(int(team_standing_list[bat_first][:1])+ 1) + team_standing_list[bat_first][1:]
    team_standing_list[ball_first] = str(int(team_standing_list[ball_first][:1]) + 1) + team_standing_list[ball_first][1:]
    no_more_changes = False
    while no_more_changes == False:
        no_more_changes = True
        rounds = 0
        for i in range(94 - rounds):
            temporary1 = batting_list[i + 1].split()
            temporary2 = batting_list[i].split()
            if int(temporary1[0]) > int(temporary2[0]):
                batting_list[i], batting_list[i+1] = batting_list[i+1], batting_list[i]
                batting_players_list[i], batting_players_list[i+1] = batting_players_list[i+1], batting_players_list[i]
                no_more_changes = False
            if int(balling_list[i+1].removesuffix('\n')) > int(balling_list[i].removesuffix('\n')):
                balling_list[i], balling_list[i + 1] = balling_list[i + 1], balling_list[i]
                balling_players_list[i], balling_players_list[i + 1] = balling_players_list[i + 1], balling_players_list[i]
                no_more_changes = False
            rounds = rounds - 1
    if int(overall_teamscore_list[bat_first]) > int(overall_teamscore_list[ball_first]):
        won = team1
        team_standing_list[bat_first] = team_standing_list[bat_first][0:2] + str(int(team_standing_list[bat_first][2:3]) + 1) \
                                        + team_standing_list[bat_first][3:]
        team_standing_list[ball_first] = team_standing_list[ball_first][0:4] + str(int(team_standing_list[ball_first][4:5]) + 1) \
                                         + team_standing_list[ball_first][5:]
        won_by = int(overall_teamscore_list[bat_first]) - int(overall_teamscore_list[ball_first])
    else:
        won = team2
        team_standing_list[ball_first] = team_standing_list[ball_first][0:2] + str(int(team_standing_list[ball_first][2:3]) + 1) \
                                        + team_standing_list[ball_first][3:]
        team_standing_list[bat_first] = team_standing_list[bat_first][0:4] + str(int(team_standing_list[bat_first][4:5]) + 1) \
                                        + team_standing_list[bat_first][5:]
        won_by = 10 - wickets
    if decision == 0:
        choose = 'bat first\n'
    else:
        choose = 'ball first\n'
    temporary3 = batting_list[0].split()
    if all_players_notout == True:
        message = (match_type + ' - Match 0' + str(match) + '\n' + team1 + ' vs. ' + team2 + '\n' + toss +
                   ' won the toss and choosed to ' + choose + won + ' won the match by ' +
                   str(won_by) + ' wickets\n' + 'Best batsmen of the match was ' + batting_players_list[0][1:].removesuffix('\n')
                   + ' - ' + temporary3[0] + '(runs), ' + temporary3[2] + '(balls), ' + 'Method of dismissal - ' + temporary3[4] +
                   '\nBest bowler of the match was ' + balling_players_list[0][1:].removesuffix('\n') + ' - ' + 'wickets - ' + balling_list[0])
    else:
        message = (match_type + ' - Match 0' + str(match) + '\n' + team1 + ' vs. ' + team2 + '\n' + toss +
                   ' won the toss and choosed to ' + choose + won + ' won the match by ' +
                   str(won_by) + ' runs\n' + 'Best batsmen of the match was ' + batting_players_list[0][1:].removesuffix('\n')
                   + ' - ' + temporary3[0] + '(runs) ' + temporary3[2] + '(balls) ' + 'Method of dismissal - ' + temporary3[4] +
                   '\nBest bowler of the match was ' + balling_players_list[0][1:].removesuffix('\n') + ' - ' + 'wickets - ' +balling_list[0])
    summary_list[(match_number - 1) * 7] = message
    match_summary_file = open('match_summary.txt', 'w')
    match_summary_file.writelines(summary_list)
    match_summary_file.close()
    new_team_standing = open('team_standings.txt', 'w')
    new_team_standing.writelines(team_standing_list)
    new_team_standing.close()
    summary = open('previous_summary.txt', 'w')
    summary.writelines(summary_list)
    summary.close()

def team_standings():
    team_standing_file = open('team_standings.txt', 'r')
    team_standing_list = team_standing_file.readlines()
    team_standing_file.close()
    team_name_file = open('team_standing_names.txt', 'r')
    team_name_list = team_name_file.readlines()
    team_name_file.close()
    no_more_change = False
    while no_more_change == False:
        no_more_change = True
        rounds = 0
        for matches in range(7 - rounds):
            if int(team_standing_list[matches+1][:1]) > int(team_standing_list[matches][:1]):
                team_standing_list[matches], team_standing_list[matches+1] = team_standing_list[matches+1], team_standing_list[matches]
                team_name_list[matches], team_name_list[matches+1] = team_name_list[matches+1], team_name_list[matches]
                no_more_change = False
            rounds = rounds + 1
    no_more_change = False
    while no_more_change == False:
        no_more_change = True
        rounds1 = 0
        for wins in range(7 - rounds1):
            if int(team_standing_list[wins+1][2:3]) > int(team_standing_list[wins][2:3]):
                team_standing_list[wins], team_standing_list[wins+1] = team_standing_list[wins+1], team_standing_list[wins]
                team_name_list[wins], team_name_list[wins + 1] = team_name_list[wins + 1], team_name_list[wins]
                no_more_change = False
            rounds1 = rounds1 + 1
    new_team_standing = open('team_standings.txt', 'w')
    new_team_standing.writelines(team_standing_list)
    new_team_standing.close()
    new_team_name = open('team_standing_names.txt', 'w')
    new_team_name.writelines(team_name_list)
    new_team_name.close()
    leaderboard = open('previous_leaderboard.txt', 'w')
    leaderboard.writelines(team_name_list)
    leaderboard.close()

def check_match_summary(rounds_in_tournament):
    if rounds_in_tournament == 0:
        summary_number = 4
    elif rounds_in_tournament == 1:
        summary_number = 6
    else:
        summary_number = 7
    summary = '1'
    while summary == '1':
        print('--------------------------------------------------------------------------------------')
        print('Which match summary do you want to check')
        print('--------------------------------------------------------------------------------------')
        summary_file = open('match_summary.txt', 'r')
        summary_list = summary_file.readlines()
        summary_file.close()

        for match_number in range(summary_number):
            corrected_match = match_number + 1
            team1vsteam2 = summary_list[(match_number * 7) + 1]
            print('Match 0' + str(corrected_match) + '\n' + team1vsteam2)

        while True:
            try:
                print('--------------------------------------------------------------------------------------')
                m_summary = int(input('>>>'))
                if m_summary > 0 and m_summary < summary_number+1:
                    break
                else:
                    raise Exception
            except ValueError:
                print('Invalid Input')
            except Exception:
                print('Invalid Input')
        print('--------------------------------------------------------------------------------------')

        corrected_m_summary = (m_summary - 1) * 7
        for user_match_summary in range(corrected_m_summary, corrected_m_summary + 7):
            print(summary_list[user_match_summary])

        print('--------------------------------------------------------------------------------------')
        while True:
            try:
                summary = str(input('Do you want to check the match summary\n1.Yes\n2.No\n'))
                if summary == '1' or summary == '2':
                    break
                else:
                    raise Exception
            except Exception:
                print('Invalid Input')

def sort_batsman():
    no_more_changes = False
    overall_batting_file = open('overall_batting.txt', 'r')
    overall_batting_list = overall_batting_file.readlines()
    overall_batting_file.close()
    batting_players_file = open('overall_batting_players.txt', 'r')
    batting_players_list = batting_players_file.readlines()
    batting_players_file.close()
    while no_more_changes == False:
        no_more_changes = True
        rounds = 0
        for i in range(94 - rounds):
            temporary1 = overall_batting_list[i + 1].split()
            temporary2 = overall_batting_list[i].split()
            if int(temporary1[0][1:]) > int(temporary2[0][1:]):
                overall_batting_list[i], overall_batting_list[i+1] = overall_batting_list[i+1], overall_batting_list[i]
                batting_players_list[i], batting_players_list[i+1] = batting_players_list[i+1], batting_players_list[i]
                no_more_changes = False
            rounds = rounds - 1
    new_overall_batting_file = open('temporary_overall_batting.txt', 'w')
    new_overall_batting_file.writelines(overall_batting_list)
    new_overall_batting_file.close()
    new_batting_players_file = open('temporary_overall_batting_players.txt', 'w')
    new_batting_players_file.writelines(batting_players_list)
    new_batting_players_file.close()
    batting = open('previous_best_batsmen.txt', 'w')
    batting.writelines(batting_players_list)
    batting.close()
    batting_runs = open('previous_best_batsmen_runs.txt', 'w')
    batting_runs.writelines(overall_batting_list)
    batting_runs.close()

def sort_baller():
    no_more_changes = False
    overall_balling_file = open('overall_balling.txt', 'r')
    overall_balling_list = overall_balling_file.readlines()
    overall_balling_file.close()
    balling_players_file = open('overall_balling_players.txt', 'r')
    balling_players_list = balling_players_file.readlines()
    balling_players_file.close()
    while no_more_changes == False:
        no_more_changes = True
        rounds = 0
        for i in range(94 - rounds):
            temporary1 = overall_balling_list[i + 1][1:].removesuffix('\n')
            temporary2 = overall_balling_list[i][1:].removesuffix('\n')
            if int(temporary1) > int(temporary2):
                overall_balling_list[i], overall_balling_list[i+1] = overall_balling_list[i+1], overall_balling_list[i]
                balling_players_list[i], balling_players_list[i+1] = balling_players_list[i+1], balling_players_list[i]
                no_more_changes = False
            rounds = rounds - 1
    new_overall_balling_file = open('temporary_overall_balling.txt', 'w')
    new_overall_balling_file.writelines(overall_balling_list)
    new_overall_balling_file.close()
    new_balling_players_file = open('temporary_overall_balling_players.txt', 'w')
    new_balling_players_file.writelines(balling_players_list)
    new_balling_players_file.close()
    balling = open('previous_best_balling.txt', 'w')
    balling.writelines(balling_players_list)
    balling.close()
    balling_wickets = open('previous_best_balling_wickets.txt', 'w')
    balling_wickets.writelines(overall_balling_list)
    balling_wickets.close()

def rearrange_teams():
    team_standings_file = open('team_standing_names.txt', 'r')
    team_standings_list = team_standings_file.readlines()
    team_standings_file.close()
    teams_file = open('teams.txt', 'w')
    teams_file.writelines(team_standings_list)
    teams_file.close()

def rearrange_players():
    teams_file = open('teams.txt', 'r')
    teams_list = teams_file.readlines()
    teams_file.close()
    player_file = open('players.txt', 'r')
    player_list = player_file.readlines()
    player_file.close()
    for teams in range(8):
        player_number = teams * 12
        for player in range(0, 94, 12):
            if player_list[player][0] == teams_list[teams][0]:
                if player == player_number:
                    break
                else:
                    player_list[player], player_list[player_number] = player_list[player_number], player_list[player]
                    player_list[player+1], player_list[player_number+1] = player_list[player_number+1], player_list[player+1]
                    player_list[player+2], player_list[player_number+2] = player_list[player_number+2], player_list[player+2]
                    player_list[player+3], player_list[player_number+3] = player_list[player_number+3], player_list[player+3]
                    player_list[player+4], player_list[player_number+4] = player_list[player_number+4], player_list[player+4]
                    player_list[player+5], player_list[player_number+5] = player_list[player_number+5], player_list[player+5]
                    player_list[player+6], player_list[player_number+6] = player_list[player_number+6], player_list[player+6]
                    player_list[player+7], player_list[player_number+7] = player_list[player_number+7], player_list[player+7]
                    player_list[player+8], player_list[player_number+8] = player_list[player_number+8], player_list[player+8]
                    player_list[player+9], player_list[player_number+9] = player_list[player_number+9], player_list[player+9]
                    player_list[player+10], player_list[player_number+10] = player_list[player_number+10], player_list[player+10]
    new_player_file = open('players.txt', 'w')
    new_player_file.writelines(player_list)
    new_player_file.close()

def rearrange_batting():
    teams_file = open('teams.txt', 'r')
    teams_list = teams_file.readlines()
    teams_file.close()
    batting_file = open('overall_batting.txt', 'r')
    batting_list = batting_file.readlines()
    batting_file.close()
    for teams in range(8):
        player_number = teams * 12
        for player in range(0, 94, 12):
            if batting_list[player][0] == teams_list[teams][0]:
                if player == player_number:
                    break
                else:
                    batting_list[player], batting_list[player_number] = batting_list[player_number], batting_list[player]
                    batting_list[player+1], batting_list[player_number+1] = batting_list[player_number+1], batting_list[player+1]
                    batting_list[player+2], batting_list[player_number+2] = batting_list[player_number+2], batting_list[player+2]
                    batting_list[player+3], batting_list[player_number+3] = batting_list[player_number+3], batting_list[player+3]
                    batting_list[player+4], batting_list[player_number+4] = batting_list[player_number+4], batting_list[player+4]
                    batting_list[player+5], batting_list[player_number+5] = batting_list[player_number+5], batting_list[player+5]
                    batting_list[player+6], batting_list[player_number+6] = batting_list[player_number+6], batting_list[player+6]
                    batting_list[player+7], batting_list[player_number+7] = batting_list[player_number+7], batting_list[player+7]
                    batting_list[player+8], batting_list[player_number+8] = batting_list[player_number+8], batting_list[player+8]
                    batting_list[player+9], batting_list[player_number+9] = batting_list[player_number+9], batting_list[player+9]
                    batting_list[player+10], batting_list[player_number+10] = batting_list[player_number+10], batting_list[player+10]
    new_batting_file = open('overall_batting.txt', 'w')
    new_batting_file.writelines(batting_list)
    new_batting_file.close()

def rearrange_balling():
    teams_file = open('teams.txt', 'r')
    teams_list = teams_file.readlines()
    teams_file.close()
    balling_file = open('overall_balling.txt', 'r')
    balling_list = balling_file.readlines()
    balling_file.close()
    for teams in range(8):
        player_number = teams * 12
        player = 0
        for player in range(0, 94, 12):
            if balling_list[player][0] == teams_list[teams][0]:
                if player == player_number:
                    break
                else:
                    balling_list[player], balling_list[player_number] = balling_list[player_number], balling_list[player]
                    balling_list[player+1], balling_list[player_number+1] = balling_list[player_number+1], balling_list[player+1]
                    balling_list[player+2], balling_list[player_number+2] = balling_list[player_number+2], balling_list[player+2]
                    balling_list[player+3], balling_list[player_number+3] = balling_list[player_number+3], balling_list[player+3]
                    balling_list[player+4], balling_list[player_number+4] = balling_list[player_number+4], balling_list[player+4]
                    balling_list[player+5], balling_list[player_number+5] = balling_list[player_number+5], balling_list[player+5]
                    balling_list[player+6], balling_list[player_number+6] = balling_list[player_number+6], balling_list[player+6]
                    balling_list[player+7], balling_list[player_number+7] = balling_list[player_number+7], balling_list[player+7]
                    balling_list[player+8], balling_list[player_number+8] = balling_list[player_number+8], balling_list[player+8]
                    balling_list[player+9], balling_list[player_number+9] = balling_list[player_number+9], balling_list[player+9]
                    balling_list[player+10], balling_list[player_number+10] = balling_list[player_number+10], balling_list[player+10]
    new_balling_file = open('overall_balling.txt', 'w')
    new_balling_file.writelines(balling_list)
    new_balling_file.close()

def rename():
    team_file = open('team_standing_names.txt', 'r')
    team_list = team_file.readlines()
    team_file.close()
    player_file = open('players.txt', 'r')
    player_list = player_file.readlines()
    player_file.close()
    team_standings_file = open('teams.txt', 'w')
    team_standings_file.writelines(team_list)
    team_standings_file.close()
    batting_players = open('overall_batting_players.txt', 'w')
    batting_players.writelines(player_list)
    batting_players.close()
    balling_players = open('overall_balling_players.txt', 'w')
    balling_players.writelines(player_list)
    balling_players.close()
    overall_players = open('team_standing_player_names.txt', 'w')
    overall_players.writelines(player_list)
    overall_players.close()


def reset_files():
    balling_file_1 = open('balling_match-1.txt', 'r')
    balling_list_1 = balling_file_1.readlines()
    balling_file_1.close()
    batting_file_1 = open('batting_match-1.txt', 'r')
    batting_list_1 = batting_file_1.readlines()
    batting_file_1.close()
    for rows in range(95):
        balling_list_1[rows] = '0\n'
        batting_list_1[rows] = '0 - 0 - notout\n'
    new_balling_file_1 = open('balling_match-1.txt', 'w')
    new_balling_file_1.writelines(balling_list_1)
    new_balling_file_1.close()
    new_balling_file_2 = open('balling_match-2.txt', 'w')
    new_balling_file_2.writelines(balling_list_1)
    new_balling_file_2.close()
    new_batting_file_1 = open('batting_match-1.txt', 'w')
    new_batting_file_1.writelines(batting_list_1)
    new_batting_file_1.close()
    new_batting_file_2 = open('batting_match-2.txt', 'w')
    new_batting_file_2.writelines(batting_list_1)
    new_batting_file_2.close()
    team_score = open('overall_teamscore.txt', 'r')
    team_score_list = team_score.readlines()
    team_score.close()
    for lines in range(8):
        team_score_list[lines] = '0\n'
    new_team_score = open('overall_teamscore.txt', 'w')
    new_team_score.writelines(team_score_list)
    new_team_score.close()