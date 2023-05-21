def rps_game_winner(array_player):
    try:
        if len(array_player) > 2:
            raise Exception("WrongNumberOfPlayersError")
        for i in array_player:
            if i[1] not in 'RSP':
                raise Exception("NoSuchStrategyError")
        win1 = array_player[0][0] + ' ' + str(array_player[0][1])
        win2 = array_player[1][0] + ' ' + str(array_player[1][1])
        if array_player[0][1] == 'R':
            if array_player[1][1] == 'S':
                return win1
            elif array_player[1][1] == 'P':
                return win2
            else:
                return win1
        elif array_player[0][1] == 'P':
            if array_player[1][1] == 'S':
                return win2
            elif array_player[1][1] == 'P':
                return win1
            else:
                return win1
        else:
            if array_player[1][1] == 'S':
                return win1
            elif array_player[1][1] == 'P':
                return win1
            else:
                return win2
    except Exception:
        raise


#m = rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])
#print(m)
#m = s.rps_game_winner([['player1', 'P'], ['player2', 'A']])
#print(m)
m = rps_game_winner([['player1', 'P'], ['player2', 'S']])
print(m)
m = rps_game_winner([['player1', 'P'], ['player2', 'P']])
print(m)