import heapq

state_infos = {
    'S': {
        "path_costs": {"A": 3, "B": 1},
        "heuristic_value": 7
    },
    'A': {
        "path_costs": {"B": 2, "C": 2},   #TODO same applies here 
        "heuristic_value": 5
    },
    'B': {
        "path_costs": {"C": 3},
        "heuristic_value": 7
    },
    'C': {
        "path_costs": {"D": 4, "G": 4}, # TODO seems like the pathcosts should be specified in this order such that for the DFS to work correctly in the Alphabetical tie breaking 
        "heuristic_value": 4
    },
    'D': {
        "path_costs": {"G": 1},
        "heuristic_value": 1
    },
    'G': {
        'path_costs ': {},
        "heuristic_value": 0
    }
}




def a_star_search(graph, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    g_values = {node: float('inf') for node in graph}
    g_values[start] = 0
    
    f_values = {node: float('inf') for node in graph}
    f_values[start] = graph[start]["heuristic_value"]
    
    came_from = {node: None for node in graph}
    expanded = []
    in_open_list = {start}

    while open_list:
        _, current = heapq.heappop(open_list)
        in_open_list.remove(current)

        if current in expanded:
            continue

        if current == goal:
            unexpanded = list(set(graph.keys()) - set(expanded))
            return reconstruct_path(came_from, current), expanded, unexpanded

        expanded.append(current)
        neighbors = sorted(graph[current]["path_costs"].keys())

        for neighbor in neighbors:
            tentative_g_value = g_values[current] + graph[current]["path_costs"][neighbor]
            if tentative_g_value < g_values[neighbor]:
                came_from[neighbor] = current
                g_values[neighbor] = tentative_g_value
                f_values[neighbor] = g_values[neighbor] + graph[neighbor]["heuristic_value"]
                heapq.heappush(open_list, (f_values[neighbor], neighbor))
                in_open_list.add(neighbor)

    unexpanded = list(set(graph.keys()) - set(expanded))
    return None, expanded, unexpanded

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from.keys() and came_from[current] is not None:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

path, expanded_states, unexpanded_states = a_star_search(state_infos, 'S', 'G')

if path:
    print(f"Path using A* Tree Search: {' -> '.join(path)}")
    print(f"Order of states expanded: {', '.join(expanded_states)}")
    print(f"States that were not expanded: {', '.join(unexpanded_states)}")
else:
    print("No path found using A* Tree Search!")
