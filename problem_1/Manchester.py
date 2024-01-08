players_data = {
    'Bruno Fernandes': {
        'goal': 5,
        'point_in_speed': 6,
        'point_in_assist': 9,
        'points_in_passing_accuracy': 10,
        'defensive_involvements': 3,
        'number': 8
    },
    'Rasmus Hojlund': {
        'goal': 12,
        'point_in_speed': 8,
        'point_in_assist': 2,
        'points_in_passing_accuracy': 6,
        'defensive_involvements': 2,
        'number': 11
    },
    'Harry Maguire': {
        'goal': 1,
        'point_in_speed': 5,
        'point_in_assist': 1,
        'points_in_passing_accuracy': 7,
        'defensive_involvements': 9,
        'number': 5
    },
    'Alejandro Garnacho': {
        'goal': 8,
        'point_in_speed': 7,
        'point_in_assist': 8,
        'points_in_passing_accuracy': 6,
        'defensive_involvements': 0,
        'number': 17
    },
    'Mason Mount': {
        'goal': 2,
        'point_in_speed': 6,
        'point_in_assist': 4,
        'points_in_passing_accuracy': 8,
        'defensive_involvements': 1,
        'number': 7
    },
}

def main_menu():        
    print('''
        **** Option 1 Player Review ****
        **** Option 2 Compare two players ****
        **** Option 3 Identify the fastest player ****
        **** Option 4 Identify the top goal scorer ****
        **** Option 5 Identify the player with the most assists ****
        **** Option 6 Identify the player with the highest passing accuracy ****
        **** Option 7 Identify the player with the most defensive involvements ****
        **** Option 0 Exit ****
        ''')
    
def print_user_info(key):
    print(f'''
        **** La informacion del jugador {key} ****
        **** goal: {players_data[key]['goal']} ****
        **** point in speed: {players_data[key]['point_in_speed']} ****
        **** point in assist: {players_data[key]['point_in_assist']} ****
        **** points in passing accuracy: {players_data[key]['points_in_passing_accuracy']} ****
        **** defensive involvements: {players_data[key]['defensive_involvements']} ****
        **** number: {players_data[key]['number']} ****
        ''')

def most_something(name):
    keys = players_data.keys()
    data_number = 0
    player_key = ''

    for key in keys:
        if players_data[key][name] > data_number:
            data_number = players_data[key][name]
            player_key = key
    
    return player_key

def main():
    exit = False

    while exit is False:
        error = True
        main_menu()
        option = input()

        if (option == '1'):
            while error:
                print('**** Escriba el numero del jugador O presione 0 para volver al menu inicial ****')
                try:
                    player_number = input()
                    player_number = int(player_number)
                except ValueError:
                    error = True
                    print('**** Debe introducir un nunmero ****')
                    continue
                if player_number == 0:
                    break
                keys = players_data.keys()
                found = False

                for key in keys:
                    if players_data[key]['number'] == player_number:
                        found = True
                        print_user_info(key)
                
                if found is False:
                    print(f'**** No se ha encontrado el jugador {player_number} ****')
                    continue
                error = False
        
        if (option == '2'):
            while error:
                print('**** Escriba el numero del jugador 1 O presione 0 para volver al menu inicial ****')
                try:
                    player_1_number = input()
                    player_1_number = int(player_1_number)
                except ValueError:
                    error = True
                    print('**** Debe introducir un nunmero ****')
                    continue

                if player_1_number == 0:
                    break

                print('**** Escriba el numero del jugador 2 ****')
                try:
                    player_2_number = input()
                    player_2_number = int(player_2_number)
                except ValueError:
                    error = True
                    print('**** Debe introducir un nunmero ****')
                    continue

                keys = players_data.keys()
                found = 0

                for key in keys:
                    if players_data[key]['number'] == player_1_number:
                        player_1 = players_data[key]
                        player_1['name'] = key
                        found += 1
                    if players_data[key]['number'] == player_2_number:
                        player_2 = players_data[key]
                        player_2['name'] = key
                        found += 1

                if found == 2:
                        print(f'''
                              **** Comparacion de los jugadores {player_1['name']} y {player_2['name']} ****
                              **** goal player 1: {player_1['goal']} ==== goal player 2: {player_2['goal']} ****
                              **** point in speed player 1: {player_1['point_in_speed']} ==== point in speed player 2: {player_2['point_in_speed']} ****
                              **** point in assist player 1: {player_1['point_in_assist']} ==== point in assist player 2: {player_2['point_in_assist']} ****
                              **** points in passing accuracy player 1: {player_1['points_in_passing_accuracy']} ==== points in passing accuracy player 2: {player_2['points_in_passing_accuracy']} ****
                              **** defensive involvements player 1: {player_1['defensive_involvements']} ==== defensive involvements player 2: {player_2['defensive_involvements']} ****
                              **** number player 1: {player_1['number']} ==== number player 2: {player_2['number']} ****
                              ''')
                else:
                    print('jugadores no encontrados')
                    continue
                
                error = False

        if (option == '3'):
            key = most_something('point_in_speed')
            print_user_info(key)
        
        if (option == '4'):
            key = most_something('goal')
            print_user_info(key)

        if (option == '5'):
            key = most_something('point_in_assist')
            print_user_info(key)

        if (option == '6'):
            key = most_something('points_in_passing_accuracy')
            print_user_info(key)

        if (option == '7'):
            key = most_something('defensive_involvements')
            print_user_info(key)

        if (option == '0'):
            exit = True

main()