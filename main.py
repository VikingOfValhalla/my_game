import clear_console

game_name = "Forgotten Valhalla"
value = True
game_name_variable = {game_name: value}
print("hello, and welcome to ", [game_name_variable])

Race = {'elf','human','dragon','valykrie'}

# added game_master to identify perspective

class game_master:
    Race = 'dragon'
    name = 'Tom'    
        
# print(game_master.Race)

# added character variable to save 

class character:
    starting_Attributes = {'health': 0, 'strength': 0, 'wisdom': 0, 'dexterity': 0}
    selected_Name = str(input("please enter your name: "))
    print(selected_Name + ": " + str(starting_Attributes))
# loop for try and except to prevent incorrect entries
    while True:
        try: 
# this first print statement is to print the list of races
            print("""Please select a race:""")
            print(Race)
            selected_Race = str(input("please enter race: "))
            # this line is needs to be fixed
            if selected_Race in Race:
                print(selected_Race)
            else:
                break 
                print("please retry")
            break
        except value_Error:
            print("please retry")
