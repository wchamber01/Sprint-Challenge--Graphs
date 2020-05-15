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
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()
player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
''' UPER
1.  Get current room id
2.  Check if room has been visited
3.  If not visited then push current room to my stack
4.  Get all exits in that room
5.  Mark all room exits with ?s
6.  Pop current room from the stack and start exploring
7.  Choose a direction to travel
8.  Mark room as visited and replace ? on selected travel direction with direction
9.  Set previous room to current room before traveling
10. After traveling set current room to previous
11. Set reverse direction to previous room id
12. Loop over rooms and repeat steps 4 - 11 while visited < number of rooms
'''
visited = {}
traversal_path = []


def reverse(dot):  # Reverse direction of travel
    if dot == 'n':
        return 's'
    if dot == 's':
        return 'n'
    if dot == 'w':
        return 'e'
    if dot == 'e':
        return 'w'


def mark_exits(current_room, path_exits):  # Mark exits with ?s
    # Create an exits dict within the visited dict
    visited[current_room] = {}
    for x in path_exits:
        # Mark room exits with ?s
        visited[current_room][x] = '?'


def traverse(current_room):  # Traverse the graph
    stack = Stack()
    current_room = player.current_room.id
    exits = player.current_room.get_exits()
    # Initialize previous room
    previous = None
    # Build my stack beginning with the starting room
    stack.push([None, current_room, previous, exits])

    # traverse (loop) through all rooms until the end
    while len(visited) < len(room_graph):
        # Pop top element from stack and destructure for easier user
        path = stack.pop()
        dot = path[0]
        current_room = path[1]
        previous = path[2]
        exits = path[3]

        # Process my element
        # Check if current room not in visited
        if current_room not in visited:
            # Mark current room exits
            mark_exits(current_room, exits)

        # Am I still here? Have I moved yet? Set current room to previous
        if dot is not None:
            visited[current_room][reverse(dot)] = previous

        # Do I have a previous room? Set previous room to current
        if previous is not None:
            visited[previous][dot] = current_room

        # Explore all paths in the current room
        for exits in visited[current_room]:
            print(visited[current_room].keys())
            # If there are unexplored paths in the current room
            if visited[current_room][exits] == '?':
                # Push my current path to the stack
                stack.push(path)
                # Set previous room to current room
                previous = player.current_room.id
                # Traverse exits
                player.travel(exits)
                # Record path taken
                traversal_path.append(exits)
                # Push new current room to stack
                stack.push(
                    [exits, player.current_room.id, previous, player.current_room.get_exits()])
                # break the loop
                break
        # reverse traversal
        if current_room == player.current_room.id:
            player.travel(reverse(dot))
            traversal_path.append(reverse(dot))


traverse(player.current_room.id)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

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
