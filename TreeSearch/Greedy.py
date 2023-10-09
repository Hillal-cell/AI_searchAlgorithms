import heapq

state_infos = {
    'S': {
        "path_costs": {"B": 1, "A": 3},
        "heuristic_value": 7
    },
    'A': {
        "path_costs": {"C": 2, "B": 2},   #TODO same applies here 
        "heuristic_value": 5
    },
    'B': {
        "path_costs": {"C": 3},
        "heuristic_value": 7
    },
    'C': {
        "path_costs": {"G": 4, "D": 4}, # TODO seems like the pathcosts should be specified in this order such that for the DFS to work correctly in the Alphabetical tie breaking 
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


def greedy_search(graph, start, goal):
    open_list = []  # Priority queue to store nodes to be evaluated
    heapq.heappush(open_list, (graph[start]["heuristic_value"], start, [start]))  # Also storing the path in the tuple
    
    came_from = {node: None for node in graph}
    expanded = []

    while open_list:
        _, current, path_so_far = heapq.heappop(open_list)

        if current in expanded:
            continue

        expanded.append(current)

        if current == goal:
            unexpanded = list(set(graph.keys()) - set(expanded))
            return path_so_far, expanded, unexpanded

        neighbors = sorted(graph[current]["path_costs"].keys())
        for neighbor in neighbors:
            if neighbor not in expanded:
                came_from[neighbor] = current
                new_path = list(path_so_far)
                new_path.append(neighbor)
                heapq.heappush(open_list, (graph[neighbor]["heuristic_value"], neighbor, new_path))

    unexpanded = list(set(graph.keys()) - set(expanded))
    return None, expanded, unexpanded

path, expanded_states, unexpanded_states = greedy_search(state_infos, 'S', 'G')

if path:
    print(f"Path using Greedy Search: {' -> '.join(path)}")
    print(f"Order of states expanded: {', '.join(expanded_states)}")
    print(f"States that were not expanded: {', '.join(unexpanded_states)}")
else:
    print("No path found using Greedy Search!")
