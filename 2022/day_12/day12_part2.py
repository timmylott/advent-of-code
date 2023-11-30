import queue
from collections import defaultdict, deque


def BFS_SP(graph, start, goal):
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    #print("Shortest path = ", *new_path)
                    return new_path
            explored.append(node)

    # Condition when the nodes
    # are not connected
   # print("So sorry, but a connecting" \
    #      "path doesn't exist :(")
    return []

def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("


def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

file1 = open('day12_input.txt', 'r')
file_line = file1.readlines()

edges = []
heightmap = []
graph = {}

letter_value = {chr(l + 96): l for l in range(1, 27)}

for line in file_line:
    line = line.strip()
    new_line = []
    for l in line:
        if l not in ('S', 'E'):
            new_line.append(l + ':' + str(letter_value[l]))
        else:
            if l == 'S':
                new_line.append(l + ':' + '1')
            else:
                new_line.append(l + ':' + '26')
    heightmap.append(new_line)

for hml in range(len(heightmap)):
    for pos in range(len(heightmap[hml])):
        pos_value = int(heightmap[hml][pos].split(':')[-1])
        edge_item = []
        #if 'E:' in heightmap[hml][pos]:
        #    break
        if pos != len(heightmap[hml]) - 1:
            if int(heightmap[hml][pos + 1].split(':')[-1]) <= pos_value + 1:
                edge_item.append(str(hml) + ',' + str(pos + 1) + ':' + heightmap[hml][pos + 1])
                #edges.append(edge_item)
        if pos != 0:
            if int(heightmap[hml][pos - 1].split(':')[-1]) <= pos_value + 1:
                edge_item.append(str(hml) + ',' + str(pos - 1) + ':' + heightmap[hml][pos - 1])
                #edges.append(edge_item)
        if hml != len(heightmap) - 1:
            if int(heightmap[hml + 1][pos].split(':')[-1]) <= pos_value + 1:
                edge_item.append(str(hml + 1) + ',' + str(pos) + ':' + heightmap[hml + 1][pos])
                #edges.append(edge_item)
        if hml != 0:
            if int(heightmap[hml - 1][pos].split(':')[-1]) <= pos_value + 1:
                edge_item.append(str(hml - 1) + ',' + str(pos) + ':' + heightmap[hml - 1][pos])
                #edges.append(edge_item)
        graph[str(hml) + ',' + str(pos) + ':' + heightmap[hml][pos]] = edge_item


for kk in graph:
    #if 'S:' in k:
    #    start = k
    if 'E:' in kk:
        print(kk)
        end = kk

shortest = -1

for k in graph:
    if 'S:' in k or 'a:' in k:
        short_path = BFS_SP(graph, k, end)
        print(k)
        print(f'short_path: {len(short_path)-1}')
        if shortest == -1:
            shortest = len(short_path) - 1

        if len(short_path) - 1 < shortest and len(short_path) != 0:
            shortest = len(short_path) - 1
            print(f'current shortest: {shortest}')

print(f'the shortest path from 0 is: {shortest}')

#399 was right, I do not know why