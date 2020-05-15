from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()
player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# 1 Get current room id
# 2 Get the exits in that room
# 3 Have a visited dictionary that holds all the rooms the player has been to
# 4 Have a prev_room that holds data about the previous room
# 5 Have a traversal_path that is a list of directions the player has traveled
# 6 While the number of visited rooms is less than the world.rooms move to another room
# 7 Get the exits in the room
# 8 Iterate through the exits in the room if there is an exit not yet explored go into that exit
# 8   change the current_room to become the previous room before going into an exit
# 9       Get the data from the room  AND save the direction you took to get there
# 10      Mark the room as visited
# 11 Get the exits in the room IF there are no exits
# 12      Go to the reverse direction until you get to a room with an exit to a room that is not visited.

stack = Stack()
current_path = player.current_room.id
visited = {}
traversal_path = []
exits = []
previous = None
previous = set(None)
print(previous)


def reverse(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'w':
        return 'e'
    if direction == 'e':
        return 'w'


def mark_exits(current_path, path_exits):
    for exit in path_exits:
        # Mark room exits with ?s
        visited[current_path][exit] = '?'


def traverse(current_path):
    # Build my stack
    stack.push(current_path)
    previous = set()
    # Get all exits for current room
    exits = player.current_room.get_exits()
    if current_path not in visited:
        mark_exits(current_path)
    ran_dir = random.choice(list(visited[current_path].keys()))
    visited[current_path][ran_dir] = player.current_room.get_room_in_direction(
        ran_dir)
    # set previous to current before traveling
    previous = current_path
    # travel to dir
    player.travel(ran_dir)
    # add the move to my path
    traversal_path.append(ran_dir)
    visited[current_path][reverse(ran_dir)] = previous
    print(visited)
    print('trav:', traversal_path)


print(traverse())

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
