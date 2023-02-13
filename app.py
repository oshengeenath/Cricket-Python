import time
import functions
while True:
    try:
        previous_team = str(input('Do you want to check the previous tournament details?\n1.Yes\n2.No\n'))
        print('--------------------------------------------------------------------------------------')
        if previous_team == '1' or previous_team == '2':
            break
        else:
            raise Exception
    except Exception:
        print('Invalid Input!')
if previous_team == '1':
    functions.previous_tournament()

while True:
    try:
        edit_team = str(input('Do you want to edit team name?\n''1.Yes\n''2.No\n'))
        if edit_team == '1':
            break
        elif edit_team == '2':
            break
        else:
            raise Exception
    except Exception:
        print('Invalid Input!')
functions.edit_the_team(edit_team)

while True:
    try:
        print('--------------------------------------------------------------------------------------')
        edit_player = str(input('Do you want to replace a player\n''1.Yes\n''2.No\n'))
        if edit_player == '1':
            break
        elif edit_player == '2':
            break
        else:
            raise Exception
    except Exception:
        print('Invalid Input!')
functions.edit_the_player(edit_player)

functions.shuffle_teams()

functions.rearrange_players()

functions.rearrange_batting()

functions.rearrange_balling()

functions.rename()

time.sleep(1)
print('--------------------------------------------------------------------------------------')
print('The T20 Cricket Tournament is Officially Starting now')
print('--------------------------------------------------------------------------------------')
time.sleep(1)

team_file = open('teams.txt', 'r')
team_list = team_file.readlines()
team_file.close()
print('Teams in Group A are:\n')
for teams in range(4):
    print(team_list[teams][1:])
print('--------------------------------------------------------------------------------------')
print('Teams in Group B are:\n')
for teams in range(4, 8):
    print(team_list[teams][1:])
print('--------------------------------------------------------------------------------------')

matches_in_a_round = 7
loops = 0
for rounds_in_tournament in range(3):
    if matches_in_a_round == 0:
        matches_in_a_round = 1
    if rounds_in_tournament == 0:
        match_type = 'Qualifiers'
        add_to_match = 0
    elif rounds_in_tournament == 1:
        match_type = 'Semi-Finals'
        add_to_match = 4
    else:
        match_type = 'Finals'
        add_to_match = 6
    temporary = 1
    print(match_type + ' will start now')
    print('--------------------------------------------------------------------------------------')
    team = 0
    for team in range(0, matches_in_a_round, 2):
        match_no = int((team / 2) + 1)
        if team == 0 and rounds_in_tournament != 2:
            print('Starting with Group A matches')
            print('--------------------------------------------------------------------------------------')
            time.sleep(1)
        if team == 4 or team == 1:
            print('Group A matches are over')
            print('--------------------------------------------------------------------------------------')
            time.sleep(1)
            print('Group B Matches will start now')
            print('--------------------------------------------------------------------------------------')
            time.sleep(1)
        print(match_type + '\n' + 'Match - ' + str(int(match_no)) + ' will start now')
        print('--------------------------------------------------------------------------------------')
        match = team + temporary
        match_number = match + add_to_match
        temporary = temporary - 1

        bat_first, ball_first, toss_won, decision = functions.toss(team)

        for innings in range(2):
            all_players_notout, wickets = functions.matches(match, bat_first, ball_first, innings)
            temporary_for_innings = bat_first
            bat_first = ball_first
            ball_first = temporary_for_innings

        functions.match_summary(match, match_number,  all_players_notout, wickets, toss_won, decision, bat_first, ball_first, match_type)

        functions.sort_batsman()

        functions.sort_baller()

        functions.team_standings()

        time.sleep(1)
        summary_file = open('match_summary.txt', 'r')
        summary_list = summary_file.readlines()
        summary_file.close()
        summary_number = loops*7
        print(match_type + '\n' + 'Match - ' + str(int(match_no)) + ' just finished\n')
        print('--------------------------------------------------------------------------------------')
        time.sleep(1)
        while True:
            try:
                match_summary1 = str(input('Do you want to check the Match summary of the match that just finished?\n1.Yes\n2.No\n'))
                if match_summary1 == '1' or match_summary1 == '2':
                    break
                else:
                    raise Exception
            except Exception:
                print('Invalid Input')
        print('--------------------------------------------------------------------------------------')
        if match_summary1 == '1':
            for user_match_summary in range(int(summary_number), int(summary_number) + 7):
                print(summary_list[user_match_summary])
        time.sleep(1)

        while True:
            try:
                print('--------------------------------------------------------------------------------------')
                top_batsmen = str(input('Do you want to check the 5 best batsmen right now?\n1.Yes\n2.No\n'))
                if top_batsmen == '1' or top_batsmen == '2':
                    break
                else:
                    raise Exception
            except Exception:
                print('Invalid Input')
        print('--------------------------------------------------------------------------------------')
        if top_batsmen == '1':
            batting_file = open('temporary_overall_batting.txt', 'r')
            batting_list = batting_file.readlines()
            batting_file.close()
            player_file = open('temporary_overall_batting_players.txt', 'r')
            player_list = player_file.readlines()
            player_file.close()
            for top_5 in range(5):
                position = top_5 + 1
                temporary_list = batting_list[top_5].split()
                print(str(position) + ')' + player_list[top_5][1:].removesuffix('\n') + ' - ' + temporary_list[0][1:] +
                      '(' + temporary_list[2].removesuffix('\n') + ')')
        time.sleep(1)

        while True:
            try:
                print('--------------------------------------------------------------------------------------')
                top_baller = str(input('Do you want to check the 5 best bowlers right now?\n1.Yes\n2.No\n'))
                if top_baller == '1' or top_baller == '2':
                    break
                else:
                    raise Exception
            except Exception:
                print('Invalid Input')
        print('--------------------------------------------------------------------------------------')
        if top_baller == '1':
            balling_file = open('temporary_overall_balling.txt', 'r')
            balling_list = balling_file.readlines()
            balling_file.close()
            player_file = open('temporary_overall_balling_players.txt', 'r')
            player_list = player_file.readlines()
            player_file.close()
            top_5 = 0
            for top_5 in range(5):
                position = top_5 + 1
                print(str(position) + ')' + player_list[top_5][1:].removesuffix('\n') + ' - ' + balling_list[top_5][1:])
            print('--------------------------------------------------------------------------------------')
        time.sleep(1)

        while True:
            try:
                team_standing = str(input('Do you want to check the team standings for now?\n1.Yes\n2.No\n'))
                if team_standing == '1' or team_standing == '2':
                    break
                else:
                    raise Exception
            except Exception:
                print('Invalid Input')
        print('--------------------------------------------------------------------------------------')
        if team_standing == '1':
            standing_file = open('team_standings.txt', 'r')
            standing_list = standing_file.readlines()
            standing_file.close()
            standing_team = open('team_standing_names.txt', 'r')
            standing_team_name = standing_team.readlines()
            standing_team.close()
            for standing in range(8):
                temporary1 = standing_list[standing].split(' ')
                position = standing + 1
                print(str(position) + ')' + standing_team_name[standing][1:] + ' Matches - ' + temporary1[0] + '\n'
                      + ' Won - ' + temporary1[1] + '\n' + ' Lose - ' + temporary1[2])
            print('--------------------------------------------------------------------------------------')

        loops = loops + 1

    time.sleep(1)
    print('--------------------------------------------------------------------------------------')
    print('Group B Matches are over')
    print('--------------------------------------------------------------------------------------')
    time.sleep(1)
    print(match_type + ' Round of the T20 Tournament is over')
    print('--------------------------------------------------------------------------------------')

    time.sleep(1)
    while True:
        try:
            print('--------------------------------------------------------------------------------------')
            match_summary = str(input('Do you want to check the match summaries\n1.Yes\n2.No\n'))
            if match_summary == '1' or match_summary == '2':
                break
            else:
                raise Exception
        except Exception:
            print('Invalid Input')
    if match_summary == '1':
        functions.check_match_summary(rounds_in_tournament)
    time.sleep(1)

    while True:
        try:
            print('--------------------------------------------------------------------------------------')
            team_standing = str(input('Do you want to check the team standings for now?\n1.Yes\n2.No\n'))
            print('--------------------------------------------------------------------------------------')
            if team_standing == '1' or team_standing == '2':
                break
            else:
                raise Exception
        except Exception:
            print('Invalid Input')
    print('--------------------------------------------------------------------------------------')
    if team_standing == '1':
        standing_file = open('team_standings.txt', 'r')
        standing_list = standing_file.readlines()
        standing_file.close()
        standing_team = open('team_standing_names.txt', 'r')
        standing_team_name = standing_team.readlines()
        standing_team.close()
        standing = 0
        for standing in range(8):
            temporary1 = standing_list[standing].split(' ')
            position = standing + 1
            print(str(position) + ')' + standing_team_name[standing][1:] + ' Matches - ' + temporary1[0] + '\n' +
                  ' Won - ' + temporary1[1] + '\n' + ' Lose - ' + temporary1[2])

    functions.rearrange_teams()

    functions.rearrange_players()

    functions.rearrange_balling()

    functions.rearrange_batting()

    functions.rename()

    functions.reset_files()

    matches_in_a_round = matches_in_a_round - 3

winner_file = open('team_standing_names.txt', 'r')
winner = winner_file.readlines()
winner_file.close()
print('The winner of the T20 Tournament is ' + str(winner[0][1:]))
