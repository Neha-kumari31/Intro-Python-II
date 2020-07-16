from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to th
e north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# # Make a new player object that is currently in the 'outside' room.
player = Player()

player.current_room = room['outside']
# Write a loop that:
user_input = ''

while user_input != 'q':
    # * Prints the current room name

    print(player.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
    # * Waits for user input and decides what to do.
    user_input = input("Press key (n, s, e, w )to move the player:")

    try:

        # If the user enters a cardinal direction, attempt to move to the room there.
        if user_input in  ['n', 's', 'e', 'w']:
            if getattr(player.current_room, f'{user_input}_to') !=None:
                player.current_room = getattr(player.current_room, f'{user_input}_to')
            else:
                print("Movement is not allowed there qplease enter different direction")
            # Print an error message if the movement isn't allowed.

    except:
        print('press q  to quit')
        
# # If the user enters "q", quit the game.
# player = Player()

# player.current_room = room['outside']

# # Write a loop that:

#     # * Prints the current room name
# print(player.current_room.name)
#     # * Prints the current description (the textwrap module might be useful here).
# print(player.current_room.description)
#     # * Waits for user input and decides what to do.
# user_input = input("Press key (n, s, e, w )to move the player:")

# if user_input in  ['n', 's', 'e', 'w']:
#    if  getattr(player.current_room, f'{user_input}_to') !=None:
#        player.current_room = getattr(player.current_room, f'{user_input}_to')

#    else:
#     print('No movement')
# # # Print an error message if the movement isn't allowed.

# print(player.current_room.name)
# print(player.current_room.description)
               
