"""
Do not remove this file. Ensure your main function is in this file.

I will execute your game like this:

python3 game.py

Yes, you may add additional files to this folder.
"""
import random
import math
import copy
import time
import itertools


def CLASS():
    return ({
        'Rogue': {1: {'NAME': 'Thief',
                      'SKILL': 'Knife Throw',
                      'MAX_EXP': 100,
                      'MAX_HP': 90,
                      'ATK': 60},
                  2: {'NAME': 'Bandit',
                      'SKILL': 'Deep Sting',
                      'MAX_EXP': 180,
                      'MAX_HP': 190,
                      'ATK': 85},
                  3: {'NAME': 'Assassin',
                      'SKILL': 'Assassinate',
                      'MAX_EXP': 9999999999,
                      'MAX_HP': 290,
                      'ATK': 110}
                  },

        'Archer': {1: {'NAME': 'Hunter',
                       'SKILL': 'Quick Shot',
                       'MAX_EXP': 100,
                       'MAX_HP': 85,
                       'ATK': 65},
                   2: {'NAME': 'Marksman',
                       'SKILL': 'Frost Arrow',
                       'MAX_EXP': 210,
                       'MAX_HP': 180,
                       'ATK': 85},
                   3: {'NAME': 'Sniper',
                       'SKILL': 'Headshot',
                       'MAX_EXP': 9999999999,
                       'MAX_HP': 280,
                       'ATK': 120}
                   },

        'Wizard': {1: {'NAME': 'Summoner',
                       'SKILL': 'Thunderbolt',
                       'MAX_EXP': 100,
                       'MAX_HP': 80,
                       'ATK': 55},
                   2: {'NAME': 'Alchemist',
                       'SKILL': 'Blizzard Storm',
                       'MAX_EXP': 230,
                       'MAX_HP': 180,
                       'ATK': 95},
                   3: {'NAME': 'Wizard',
                       'SKILL': 'Meteor',
                       'MAX_EXP': 9999999999,
                       'MAX_HP': 260,
                       'ATK': 130}
                   },

        'Paladin': {1: {'NAME': 'Barbarian',
                        'SKILL': 'Whirlwind',
                        'MAX_EXP': 100,
                        'MAX_HP': 100,
                        'ATK': 70},
                    2: {'NAME': 'Knight',
                        'SKILL': 'Reckless Rush',
                        'MAX_EXP': 220,
                        'MAX_HP': 200,
                        'ATK': 90},
                    3: {'NAME': 'Sword Master',
                        'SKILL': 'Trinity Strike',
                        'MAX_EXP': 9999999999,
                        'MAX_HP': 300,
                        'ATK': 100}
                    },
    })


def CLASS_DESCRIPTION():
    return ({1: "  Faster growth",
             2: " Balanced stat",
             3: " Low HP, powerful skill",
             4: "Tank. great HP"})


def FOES():
    return ({1: {'NAME': 'Skeleton',
                 'SKILL': 'Bone Missile',
                 'HP': 100,
                 'MAX_HP': 100,
                 'ATK': 10,
                 'EXP': 90},

             2: {'NAME': 'Titan',
                 'SKILL': 'Rock Hammer',
                 'HP': 200,
                 'MAX_HP': 200,
                 'ATK': 15,
                 'EXP': 150},

             3: {'NAME': 'Ruined Baron',
                 'SKILL': 'Death Sentence',
                 'HP': 300,
                 'MAX_HP': 300,
                 'ATK': 22,
                 'EXP': 200}
             })


def BOSS():
    return ({'NAME': 'Dark Dragon',
             'SKILL': 'Hellfire',
             'HP': 750,
             'MAX_HP': 750,
             'ATK': 25,
             'EXP': 1000})


def COMMAND():
    return "Attack", "Flee"


def FIELDS():
    return 'Swamp', 'Valley', 'Desert', 'Forest', 'Volcano', 'Ruins', 'Tomb'
    # tuple


def make_board(rows: int, columns: int) -> dict:
    """
    Creates game board

    Generates and returns a dictionary that contains rows * columns keys, where each key is a tuple that contains
    a set of coordinates, and each value is a short string description.

    :param rows: integers
    :param columns: integers
    :precondition: rows, columns are positive integers
    :postcondition: must return a dictionary that contains rows * columns keys
    :postcondition: each key is a tuple that contains a set of coordinates
    :postcondition: each value is a short string description
    :return: a dictionary
    """
    game_map = {(x, y): field for x in range(rows) for y in range(columns) for field in random.choices(FIELDS())}
    return game_map


def get_user_name() -> str:
    """
    Ask the user for the name of character and return that name.

    :postcondition: it should return the name of character.
    :return: string
    """
    username = input("Name your character: ")
    return username


def display_user_class():
    """
    Prints the classes and description of each class

    >>> display_user_class()
    1, Rogue:      Faster growth
    2, Archer:     Balanced stat
    3, Wizard:     Low HP, powerful skill
    4, Paladin:    Tank. great HP
    """
    for index, item in enumerate(CLASS().keys(), 1):
        print(f"{index}, {item}:    {CLASS_DESCRIPTION()[index]}")


def get_user_class() -> int:
    """
    Prints a numbered list of character classes and get user's input

    Displays a numbered list of classes to user and ask the user to enter the class they wish to choose.

    :postcondition: it should return user's choice as an integer
    :return: an integer
    """
    display_user_class()
    user_choice = int(input("Select your Class in number: ")) - 1
    return user_choice


def make_character(name: str, user_class: int, level: int) -> dict:
    """
    Creates a game character

    Creates a game character that has dictionary which has multiple properties as keys.

    :param name: a string
    :param user_class: an integer
    :param level: an integer
    :precondition: name should be a string
    :precondition: user_class is a non-negative integer between [0, 3]
    :precondition: level is positive integer between [1, 3]
    :postcondition: it must return a dictionary that has information of your character
    :return: a character dictionary

    >>> player = make_character('Jesper', 0, 1)
    >>> player # doctest: +NORMALIZE_WHITESPACE
    {'Name': 'Jesper', 'Class': 'Rogue', 'Job': 'Thief', 'Lvl': 1, 'Current HP': 90, 'Max_HP': 90, 'Skill': 'Knife Throw', 'ATK': 60, 'Current_EXP': 0, 'Max_EXP': 100, 'X': 0, 'Y': 0}
    """

    class_type = list(CLASS().keys())[user_class]
    chosen_class = CLASS()[class_type]
    char = {"Name": name,
            "Class": class_type,
            "Job": chosen_class[level]['NAME'],
            "Lvl": level,
            "Current HP": chosen_class[level]['MAX_HP'],
            "Max_HP": chosen_class[level]['MAX_HP'],
            "Skill": chosen_class[level]['SKILL'],
            "ATK": chosen_class[level]['ATK'],
            "Current_EXP": 0,
            "Max_EXP": chosen_class[level]['MAX_EXP'],
            "X": 0,
            "Y": 0}
    return char


def show_intro(character: dict):
    """
    Prints the game intro script.

    :param character: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: character must be on the valid location of the board
    :postcondition: it should print the intro script.


    """
    print(f""".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\nA LONG TIME AGO IN THIS WORLD...
    
    There was a Dark Dragon that almost destroyed the whole world with his mighty ability: HELLFIRE.
    The mighty heroes fought with the Dark dragon for 10 nights and days.
    At last, a wizard managed to make the Dark Dragon sleep forever under the LENOVO mountain. world became peaceful.
    """)
    time.sleep(4.0)

    print(f"""    
    However, on the day that <<{character['Name']}>> was born, the Dark Dragon has awakened.
    <{character['Name']}> had a soul of one of the mighty heroes that had fought with the Dark Dragon.
    Sleeping Dragon sensed that soul and it made him rage.
    Dragon destroyed <{character['Name']}>'s town and claimed the LENOVO mountain near the town.""")

    time.sleep(4.0)
    print(f"""
    <{character['Name']}> has survived. 
    Unfortunately {character['Name']}'s family was died while protecting {character['Name']}.
    
    """)

    time.sleep(3.0)

    print(f"""
    20 years from then,  
    Dragon is still hunting {character['Name']}'s town's people for fun.
    {character['Name']} swore to eliminated the Dark dragon.\n\n\n""")

    print(f"""    A new legend is about to be born.....""")
    time.sleep(3.0)
    print("""
    ______                             _____ _                       
    |  _  \                           /  ___| |                      
    | | | |_ __ __ _  __ _  ___  _ __ \ `--.| | __ _ _   _  ___ _ __ 
    | | | | '__/ _` |/ _` |/ _ \| '_ \ `--. \ |/ _` | | | |/ _ \ '__|
    | |/ /| | | (_| | (_| | (_) | | | /\__/ / | (_| | |_| |  __/ |   
    |___/ |_|  \__,_|\__, |\___/|_| |_\____/|_|\__,_|\__, |\___|_|   
                      __/ |                           __/ |          
                     |___/                           |___/        """)
    print(f"""     
    {character["Name"]} is coming...
    Dark Dragon waits for you {character["Name"]} at somewhere(* in the map).\n\n
    """)
    time.sleep(3.0)


def display_map(board: dict, character: dict):
    """
    Prints a map that shows current location of the player and boss(marked as *)

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board is a dictionary created by calling make_board(rows, columns)
    :precondition: board is a dictionary with keys(tuple of coordinates) and values(short string description)
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: character must be on the valid location of the board
    postcondition: it should print a map that shows current location of the player and boss.


    >>> my_board = make_board(10,10)
    >>> my_char = make_character("jesper", 1, 1)
    >>> my_char['X'] = 2
    >>> my_char['Y'] = 3
    >>> display_map(my_board, my_char)
    .
    .
    .
    [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
    [ ][ ][X][ ][ ][ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ][ ][ ][ ][ ][*]
    """
    print(f".\n.\n.")
    rows = int(math.sqrt(len(board)))
    columns = int(math.sqrt(len(board)))

    empty_map = []
    for row in range(rows):
        column_elems = []
        for col in range(columns):
            column_elems.append('[ ]')
        empty_map.append(column_elems)
    empty_map[rows - 1][columns - 1] = '[*]'
    empty_map[character['Y']][character['X']] = "[X]"

    for index in range(rows):
        each_row = "".join(empty_map[index])
        print(f"{each_row}")


def describe_current_location(board: dict, character: dict):
    """
    Prints a brief description of character's current location.

    Prints a description of character's current location in the given board.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board is a dictionary created by calling make_board(rows, columns)
    :precondition: board is a dictionary with keys(tuple of coordinates) and values(short string description)
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: character must be on the valid location of the board
    :postcondition: it must print string that describes current location of character in the board.
    """

    print(f"Great! You are in the {board[(character['X'], character['Y'])]}")


def get_user_choice() -> str:
    """
    Gets the user's input for direction

    Display a numbered list of directions to user and ask the user to enter the direction they wish to go.

    :postcondition: it should return user input as a string
    :return: a string
    """
    user_choice = ""
    direction_list = ["1", "2", "3", "4", "q"]
    direction_detail = "\n1. to north \n2. to east\n3. to south\n4. to west \nq. (quit game)"
    while user_choice not in direction_list:
        print(f"\nWhere do you want to go? choose one of them! {direction_detail}")
        user_choice = input("Select direction: ")
        if user_choice == "":
            return "0"
        else:
            return user_choice


def check_for_quit(direction: str) -> bool:
    """
    Determines whether user wants to quit the game

    :param direction: a string
    :precondition: direction is one of these strings("1", "2", "3", "4", "q")
    :postcondition: return True if user wants to quit, else False.
    :return: True or False

    >>> check_for_quit("q")
    True
    """
    decision = direction == "q"
    return decision


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Determines whether the character can travel in their desired direction.

    Determine where the character is on the board and whether they can travel in their desired direction.

    :param board: a dictionary
    :param character: a dictionary
    :param direction: a string
    :precondition: board is a dictionary created by calling make_board(rows, columns)
    :precondition: board is a dictionary with keys(tuple of coordinates) and values(short string description)
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: character must be on the valid location of the board
    :precondition: direction is one of these strings("1", "2", "3", "4")
    :postcondition: return True if the character is on the board, and it can travel in its desired direction.
    :return: True or False

    >>> test_board = make_board(2,2)
    >>> test_character = make_character('Jesper', 0, 1)
    >>> test_direction = "2"
    >>> validate_move(test_board, test_character, test_direction)
    True
    >>> test_character['X'] = 1
    >>> test_character['Y'] = 0
    >>> test_direction = "2"
    >>> validate_move(test_board, test_character, test_direction)
    False
    """
    north_end = 0
    east_end = math.sqrt(len(board)) - 1
    south_end = math.sqrt(len(board)) - 1
    west_end = 0

    if direction == "1":
        return character['Y'] - 1 >= north_end
    elif direction == "2":
        return character['X'] + 1 <= east_end
    elif direction == "3":
        return character['Y'] + 1 <= south_end
    elif direction == "4":
        return character['X'] - 1 >= west_end
    else:
        return False


def move_character(direction: str, character: dict):
    """
    Updates the character’s X- or Y-coordinates appropriately.

    Update character's X- or Y-coordinates by changing a value inside the character dictionary.

    :param character: a dictionary
    :param direction: a string
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: character must be on the valid location of the board
    :precondition: direction is one of these strings("1", "2", "3", "4")
    :postcondition: must increase or decrease character’s ['X'] or ['Y'] field by 1.
    :return: character dictionary with updated ['X'] or ['Y'] coordinate values.

    >>> test_direction = "2"
    >>> test_character = make_character('Jesper', 0, 1)
    >>> test_character['X']
    0
    >>> move_character(test_direction, test_character)
    >>> test_character['X']
    1
    """
    if direction == "1":
        character['Y'] -= 1
    elif direction == "2":
        character['X'] += 1
    elif direction == "3":
        character['Y'] += 1
    else:
        character['X'] -= 1


def display_command(character: dict):
    """Prints a numbered list of command to user

    :param character: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: character must be on the valid location of the board
    :postcondition: it should print a numbered list of command to user
    >>> test_character = make_character('Jesper', 0, 1)
    >>> display_command(test_character)
    Jesper, enter your next action:
     [1], Attack
     [2], Flee
    """
    print(f"{character['Name']}, enter your next action: ")
    for index, command in enumerate(COMMAND(), 1):
        print(f" [{index}], {command}")


def make_foe(character: dict) -> dict:
    """
    Creates a foe

    Creates a foe that has dictionary which has multiple properties as keys

    :param character: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: character must be on the valid location of the board
    :postcondition: it must return a dictionary that has information of foe
    :return: a foe dictionary

    >>> player = make_character('Jesper', 1, 1)
    >>> first_foe = make_foe(player)
    >>> first_foe
    {'NAME': 'Skeleton', 'SKILL': 'Bone Missile', 'HP': 100, 'MAX_HP': 100, 'ATK': 10, 'EXP': 90}
    """
    x = character['X']
    y = character['Y']
    zone1 = 8
    zone2 = 13
    zone3 = 17
    if x + y <= zone1:
        foe = copy.deepcopy(FOES()[1])
    elif x + y <= zone2:
        foe = copy.deepcopy(FOES()[2])
    elif x + y <= zone3:
        foe = copy.deepcopy(FOES()[3])
    else:
        foe = copy.deepcopy(BOSS())
    return foe


def foe_fight_back(character: dict, foe: dict):
    """Prints the description of the case that foe fights back to the player

    Prints the description of the case that foe fights back to the player

    :param character: a dictionary
    :param foe: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: foe is a dictionary that has been created by calling make_foe(character)
    :postcondition: it should print the description when the foe fights back to the player.

    >>> player = make_character('Jesper', 0, 1)
    >>> test_foe = make_foe(player)
    >>> foe_fight_back(player, test_foe)
        Skeleton's HP is 100/100
    <BLANKLINE>
        Skeleton casts Bone Missile to you.
        [SYSTEM] Your HP is 80..
    <BLANKLINE>
    """
    print(f"    {foe['NAME']}'s HP is {foe['HP']}/{foe['MAX_HP']}\n\n    {foe['NAME']} casts {foe['SKILL']} to you.")
    character["Current HP"] -= foe["ATK"]
    if character["Current HP"] > 0:
        print(f"    [SYSTEM] Your HP is " + str(character["Current HP"]) + "..\n")
        time.sleep(1)
    else:
        print(f"[SYSTEM] {character['Name']} has 0 HP...")


def reduce_foe_hp(foe: dict, character: dict):
    """
    Reduce foe's HP

    :param character: a dictionary
    :param foe: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: foe is a dictionary that has been created by calling make_foe(character)
    :postcondition: it should decrease foe's HP by character's ATK value.

    >>> player = make_character('Jesper', 0, 1)
    >>> test_foe = make_foe(player)
    >>> reduce_foe_hp(test_foe, player)
    >>> test_foe["HP"]
    40

    """
    foe["HP"] -= character["ATK"]


def foe_is_alive(foe: dict) -> bool:
    """
    Determines whether foe is still alive

    :param foe: a dictionary
    :precondition: foe is a dictionary that has been created by calling make_foe(character)
    :postcondition: it should True if foe's HP is greater than 0, else False.
    :return: boolean

    >>> test_character = make_character('Jesper', 0, 1)
    >>> test_foe = make_foe(test_character)
    >>> test_foe["HP"] = 0
    >>> foe_is_alive(test_foe)
    False
    """
    foe_survived = foe["HP"] > 0
    return foe_survived


def get_exp(character: dict, foe: dict):
    """
    Increases Current_EXP of character

    :param character: a dictionary
    :param foe: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: foe is a dictionary that has been created by calling make_foe(character)
    :postcondition: it should increase character["Current_EXP"] with the value of foe["EXP"]

    >>> test_character = make_character('Jesper', 0, 1)
    >>> test_foe = make_foe(test_character)
    >>> get_exp(test_character, test_foe)
    >>> test_character["Current_EXP"]
    90
    """
    character["Current_EXP"] += foe["EXP"]


def not_enough_current_exp_for_lvl_up(character: dict) -> bool:
    """
    Determines whether character doesn't have enough exp to leve up.

    :param character: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :postcondition:  it should true if character's Current_EXP is not enough to level up. else False
    :return: boolean

    >>> test_character = make_character('Jesper', 0, 1)
    >>> test_character["Current_EXP"] = 99
    >>> not_enough_current_exp_for_lvl_up(test_character)
    True
    """
    exp_is_not_enough = character["Current_EXP"] < character['Max_EXP']
    return exp_is_not_enough


def combat_round(character: dict, foe: dict):
    """
    Prints the description of combat

    :param character: a dictionary
    :param foe: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: foe is a dictionary that has been created by calling make_foe(character)
    :postcondition: It should print the description of battle.

    >>> player = make_character('jesper', 1, 1)
    >>> enemy = make_foe(player)
    >>> combat_round(player, enemy)
    <BLANKLINE>
        jesper casts Quick Shot!
        Skeleton's HP is 35/100
    <BLANKLINE>
        Skeleton casts Bone Missile to you.
        [SYSTEM] Your HP is 75..
    <BLANKLINE>

    """
    print(f"\n    {character['Name']} casts {character['Skill']}!")
    reduce_foe_hp(foe, character)
    if foe_is_alive(foe):
        foe_fight_back(character, foe)
    else:
        get_exp(character, foe)
        if not_enough_current_exp_for_lvl_up(character):
            print(f"""\n    [SYSTEM]You killed {foe['NAME']}\n    [SYSTEM]You earned {foe['EXP']}EXP\n""")
        else:
            print(f"    [SYSTEM]You killed {foe['NAME']}")


def character_and_foe_are_alive(character: dict, foe: dict) -> bool:
    """
    Determines whether character and foe are both alive.

    :param character: a dictionary
    :param foe: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: foe is a dictionary that has been created by calling make_foe(character)
    :postcondition: it should return True if both character and foe are alive, else False.
    :return: bool

    >>> test_character = make_character('Jesper', 0, 1)
    >>> test_foe = make_foe(test_character)
    >>> character_and_foe_are_alive(test_character, test_foe)
    True
    """
    are_both_alive = character['Current HP'] > 0 and foe['HP'] > 0
    return are_both_alive


def get_battle_command() -> int:
    """
    Gets battle command from user.

    :postcondition: it should return user input
    :return: string
    """
    battle_command = int(input("Enter your command(1 or 2): "))
    return battle_command


def combat(character: dict):
    """
    Describes a combat

    Describes a battle using while loop until the character kills the foe or the character flees.

    :param character: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :postcondition: if the user enters 1(attack) for command, fight(call combat_round) and check whether foe flees.
    :postcondition: if the user enters 2(flee) for command, try to run away(call 'flee' function).
    :postcondition: if foe_flee() is True, break the loop and finish executing this function
    :postcondition: if foe_flee() is False, continue the while loop(keep fighting).
    :postcondition if flee() is True, break the loop and finish executing this function
    :postcondition if flee() is False, keep looping(fighting).
    """
    foe = make_foe(character)
    print(f"\nWild {foe['NAME']} has appeared!")
    while character_and_foe_are_alive(character, foe):
        display_command(character)
        command = get_battle_command()
        if command == 1:
            combat_round(character, foe)
            if foe_flee(foe):
                break
        if command == 2:
            flee_possible = check_flee_chance()
            if flee(character, foe, flee_possible):
                break


def foe_flee(foe: dict) -> bool:
    """
    Determines whether foe ran away.

    :param foe: a dictionary
    :precondition: foe is a dictionary that has been created by calling make_foe(character)
    :postcondition: it should return True, if foe ran away, else return False.
    :return: a True or False
    """
    if foe['HP'] > 0 and not foe["NAME"] == 'Dark Dragon':
        flee_possibility = random.randint(1, 5)
        if flee_possibility == 1:
            print(f"<ALERT>: {foe['NAME']} has escaped\n")
            return True
        else:
            return False
    else:
        return False


def foe_hits_character() -> bool:
    """Determines whether foe will attack the character while the character flees.

    :postcondition: it should return True with 20% of chance, else return False
    :return: a True or False

    """
    wound_possibility = random.randint(1, 5)
    return wound_possibility == 1


def check_flee_chance() -> bool:
    """Determines whether the character can escape from combat or not

    :postcondition: it returns True with 20% of chance.
    :return: a True or False
    """
    flee_possibility = random.randint(1, 5)
    return flee_possibility == 1


def flee(character: dict, foe: dict, flee_possible: bool) -> bool:
    """Determines whether the user can escape from combat.

    :param character: a dictionary
    :param foe: a dictionary
    :param flee_possible: a boolean
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: foe is a dictionary that has been created by calling make_foe(character)
    :precondition: flee_possible is True or False
    :postcondition: it should return True if character can flee with or without getting damage from foe.
    :postcondition: it should return false if character is engaging with final boss.
    :postcondition: it should print description no matter it returns True or False.
    :return: a True or False

    >>> player = make_character('Jesper', 1, 1)
    >>> test_foe = make_foe(player)
    >>> test_flee_possible = True
    >>> flee(player, test_foe, test_flee_possible)
    <BLANKLINE>
    <ALERT> Jesper escaped successfully!
    <BLANKLINE>
    True
    """
    foe_is_boss = foe["NAME"] == 'Dark Dragon'
    foe_hits_back = foe_hits_character()
    if flee_possible and not foe_is_boss:
        if foe_hits_back:
            character["Current HP"] -= foe["ATK"]
            print(f"\n\n    {foe['NAME']} casted {foe['SKILL']} to you while you are running away")
            print(f"    You got " + str(foe["ATK"]) + f" DMG from {foe['NAME']}..\n")
            print(f"<ALERT> {character['Name']} escaped from battle with some wound!\n")
        else:
            print(f"\n<ALERT> {character['Name']} escaped successfully!\n")
        return True

    else:
        print(f"\n<ALERT> {character['Name']} failed to escape. Keep fighting!\n")
        return False


def level_up(character: dict, user_class: int) -> dict:
    """Promotes a character to upper level.

    :param character: a dictionary
    :param user_class: an integer
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: user_class is a non-negative integer between [0, 3]
    :postcondition: it should promote character if its "Current_EXP" value reaches to its "Max_EXP" value.
    :return: a character dictionary

    >>> player = make_character("Jes", 3, 1)
    >>> player['X'] = 5
    >>> player['Y'] = 5
    >>> player["Current_EXP"] =  100
    >>> level_up(player, 3) # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    [SYSTEM]★★★★★ Good job! Jes is promoted to Knight and recovered HP!★★★★★
    <BLANKLINE>
    <ALERT>Your class is updated as below
    {'NAME': 'Knight', 'SKILL': 'Reckless Rush', 'MAX_EXP': 220, 'MAX_HP': 200, 'ATK': 90}
    <BLANKLINE>
    {'Name': 'Jes', 'Class': 'Paladin', 'Job': 'Knight', 'Lvl': 2, 'Current HP': 200, 'Max_HP': 200, 'Skill': 'Reckless Rush', 'ATK': 90, 'Current_EXP': 0, 'Max_EXP': 220, 'X': 5, 'Y': 5}
    """
    class_type = list(CLASS().keys())[user_class]
    if character["Current_EXP"] >= character["Max_EXP"]:
        x_coord = character['X']
        y_coord = character['Y']
        character = make_character(character["Name"], user_class, character['Lvl'] + 1)
        character['X'] = x_coord
        character['Y'] = y_coord

        print(f"\n[SYSTEM]★★★★★ Good job! {character['Name']} is promoted to "
              f"{CLASS()[class_type][character['Lvl']]['NAME']} and recovered HP!★★★★★\n\n"
              f"<ALERT>Your class is updated as below \n{CLASS()[class_type][character['Lvl']]}\n")
    return character


def bless_for_final_battle(character: dict):
    """Recovers character's wounds

    Make character fully healed.

    :param character: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :postcondition: it should make character's fully healed.
    :postcondition: it should print some description
    >>> player = make_character("Jes", 1, 1)
    >>> bless_for_final_battle(player)
    <BLANKLINE>
    <BLANKLINE>
    SOULS OF FORGOTTEN MIGHTY HEROES bless Jes for the FINAL BATTLE
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    [SYSTEM] ★★★★Jes is fully healed★★★★
    <BLANKLINE>
    <BLANKLINE>
    >>> player['Current HP'] == player["Max_HP"]
    True
    """
    character["Current HP"] = character["Max_HP"]
    time.sleep(1)
    print(f"\n\nSOULS OF FORGOTTEN MIGHTY HEROES bless {character['Name']} for the FINAL BATTLE\n\n\n")
    time.sleep(2)
    print(f"[SYSTEM] ★★★★{character['Name']} is fully healed★★★★\n\n")
    time.sleep(2)


def check_for_foes(character: dict) -> bool:
    """
    Determines whether there is a foe.

    Determines whether the player will encounter a foe or not. Returns True if the player is about to encounter a foe.

    :param character: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :postcondition: return true 20% of the time.
    :return: True or False
    """
    if character['X'] == 9 and character['Y'] == 9:
        bless_for_final_battle(character)
        return True
    else:
        possibility = random.randint(1, 5)
        return possibility == 1


def is_alive(character: dict) -> bool:
    """
    Determines whether character is alive.

    Return True if character's HP is not 0.

    :param character: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :postcondition: returns True if character's HP is not 0, else False.
    :return: True or False

    >>> player = make_character('Jesper', 1, 1)
    >>> is_alive(player)
    True
    """
    return character["Current HP"] > 0


def check_if_goal_attained(board: dict, character: dict) -> bool:
    """
    Determine whether the character has made it to its destination(* on the map).

    Compare coordinates of the goal and character to determine whether the character has made it to the goal.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board is a dictionary created by calling make_board(rows, cols)
    :precondition: board is a dictionary with keys(tuple of coordinates) and values(short string description)
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    :precondition: character must be on the valid location of the board
    :postcondition: return True if the character has made it to the destination, else False.
    :return: True or False

    >>> test_rows = 10
    >>> test_columns = 10
    >>> test_board = make_board(test_rows, test_columns)
    >>> test_character = make_character('Jesper', 0, 1)
    >>> test_character['X'] = 9
    >>> test_character['Y'] = 9
    >>> check_if_goal_attained(test_board, test_character)
    True
    """
    rows = int(math.sqrt(len(board)))
    columns = int(math.sqrt(len(board)))
    return (character['X'], character['Y']) == (rows - 1, columns - 1)


def paint(number: str) -> str:
    """Change given string to a star emoji

    :param number: a string
    :precondition: the parameter 'number' should be a string "1" or "2"
    :postcondition: it should change 'number' to "☆" or "★"
    :return: string
    >>> paint("1")
    '☆'
    """
    if number == "1":
        return "☆"
    if number == "2":
        return "★"


def mission_clear_message(character):
    """Returns string decorated with beautiful stars

    :postcondition: it should return beautiful star patterns.
    :return: string
    """
    decoration = ""
    decoration_generator = itertools.cycle(["1", "2"])
    for _ in range(40):
        decoration += (next(decoration_generator))

    deco_in_list = list(map(paint, decoration))
    new_deco = str.join("", deco_in_list)
    new_decos = ""

    for _ in range(10):
        new_decos = new_decos + "\n" + new_deco

    print(f"{new_decos}"
          f"\n\n\n\nThank you {character['Name']}!\n"
          f"The era of Dark Dragon has gone...!\n\n"
          f"The world will remember our new saviour, <<{character['Name']} the DRAGON SLAYER>>...!!\n"
          f"\n\n\n\n\nThe End"
          f"\n\n\n              -Created by GM JESPER")


def alert_wrong_move(character):
    """
    Prints alert message for wrong direction

    :param character: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    """
    print(f"\n{character['Name']}, you can't go in that direction")


def notify_death(character):
    """
    Prints death notification.

    :param character: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    """
    print(f"\n\n\n {character['Name']} is bleeding... \n\n"
          f"[SYSTEM]{character['Name']} dead...")


def display_quit_message(character):
    """
    Prints message when user quit game

    :param character: a dictionary
    :precondition: character is a dictionary that has been created by calling make_character(name, user_class, level)
    """
    print(f"\n.\n.\nFarewell, {character['Name']}..\nYou chose to quit the game\n\n\n"
          f"[SYSTEM] You terminated the game")


def game():  # called from main
    """
    Runs the game
    """
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    name = get_user_name()
    user_class = get_user_class()
    character = make_character(name, user_class, 1)
    achieved_goal = False
    user_wants_to_quit = False
    show_intro(character)
    display_map(board, character)
    describe_current_location(board, character)
    while not achieved_goal and is_alive(character) and not user_wants_to_quit:
        direction = get_user_choice()
        user_wants_to_quit = check_for_quit(direction)
        if user_wants_to_quit:
            break
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(direction, character)
            display_map(board, character)
            describe_current_location(board, character)
            there_is_a_challenger = check_for_foes(character)
            if there_is_a_challenger:
                combat(character)
                character = level_up(character, user_class)
                time.sleep(1)
                display_map(board, character)
            achieved_goal = check_if_goal_attained(board, character)
        else:
            alert_wrong_move(character)
    if not is_alive(character):
        notify_death(character)
    elif user_wants_to_quit:
        display_quit_message(character)
    else:
        mission_clear_message(character)


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
