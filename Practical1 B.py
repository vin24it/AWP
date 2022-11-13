#For Making A Graph
graph = {'A': set(['B', 'C']),
         'B': set (['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set (['B', 'F']),
         'F': set (['C', 'E'])
         }
#Implement Logic of BFS
def bfs (start):
    queue = [start]
    levels={} #This Dict Keeps track of levels
    levels [start]=0 #Depth of start node is 0
    visited = set(start)
    while queue:
        node = queue.pop(0)
        neighbours=graph [node]
        for neighbor in neighbours:
            if neighbor not in visited:
                queue.append (neighbor)
                visited.add (neighbor)
                levels [neighbor]= levels[node]+1
    print(levels) #print graph Levels
    return visited
print(str(bfs ('A'))) #print graph node

#For Finding Breadth First Search Path
def bfs_paths (graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph [vertex] - set (path):
            if next == goal:
               yield path + [next]
            else:
                queue.append((next, path + [next]))
result=list (bfs_paths (graph, 'A', 'F'))
print (result)# [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
#For finding shortest path
def shortest_path (graph, start, goal):
    try:
        return next (bfs_paths(graph, start, goal))
    except StopIteration:
        return None
result=shortest_path(graph, 'A', 'F')
print(result) # ['A', 'C', 'F']
