import queue
from collections import defaultdict


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


file1 = open('day12_input.txt', 'r')
file_line = file1.readlines()

edges = []
heightmap = []
graph = {}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

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
    if heightmap[hml][pos] == 'E':
        break

print(graph)
for k in graph:
    if 'S:' in k:
        start = k
    if 'E:' in k:
        end = k

short_path = bfs_shortest_path(graph, start, end)
print(short_path)
print(len(short_path)-1)
#408