import heapq

def a_star_search(graph, start, goal):
    visited = set()
    expanded = []
    # The priority queue will contain tuples of (f(n), state, g(n), path_so_far)
    start_heuristic = graph[start]['heuristic_value']
    priority_queue = [(start_heuristic, start, 0, [start])]

    while priority_queue:
        f, state, g, path = heapq.heappop(priority_queue)

        if state == goal:
            unexpanded = [item[1] for item in priority_queue]
            return path, expanded, unexpanded

        if state not in visited:
            visited.add(state)
            expanded.append(state)

            for neighbor, cost in graph[state]['path_costs'].items():
                if neighbor not in visited:
                    new_g = g + cost
                    h = graph[neighbor]['heuristic_value']
                    new_f = new_g + h
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_f, neighbor, new_g, new_path))

    return None, expanded, []

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


start_state = 'S'
goal_state = 'G'

path, expanded_states, unexpanded_states = a_star_search(state_infos, start_state, goal_state)

if path:
    print(f"Path using A* Search: {' -> '.join(path)}")
    print(f"Order of states expanded: {', '.join(expanded_states)}")
    print(f"States that were not expanded: {', '.join(unexpanded_states)}")
else:
    print("No path found using A* Search!")
