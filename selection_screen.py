import clear_console

game_name = "Coding Game"

Player_1 = int(0)

Player_2 = int(0)

Player_1_nom = "Player 1's score: "
    
Player_2_nom = "Player 2's: score: "

# figure out how to do this
class Game_main:

    Player_1: int  = 0
    
    Player_2: int  = 0    
        
def game_function():

    clear_console.clear()

    # provides a menu to select from during startup

    menu_options = {
        1: 'New Game',
        2: 'Campaign',
        3: 'Quit'
    }

    def print_menu():
        
        for key in menu_options.keys():
            
            print(key, '--', menu_options[key])
        
    print_menu()

    # input selection for initial selection
        
    selected_input = input("Please input your selection: ", )

    selected_input = int(selected_input)

    # current selected winning input
    
    if selected_input == int(1): 

        print(f"Welcome to {game_name}")

        Game_main.Player_1 += 1

        print(f"{Player_1_nom} ", Game_main.Player_1)

    elif selected_input == int(2):

        print("Player 2 Wins!")

        Game_main.Player_2 += 1

        print(f"{Player_2_nom} ", Game_main.Player_1)

    # catch all if player 1 doesn't win

    else:
        print("nothing happened")
        
game_function()
