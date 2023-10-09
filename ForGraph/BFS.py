from collections import deque

def bfs_graph_search(graph, start, goal):
    visited = set()
    expanded = []
    queue = deque([(start, [start])])

    while queue:
        state, path = queue.popleft()

        if state == goal:
            unexpanded = [item[0] for item in queue]
            return path, expanded, unexpanded

        if state not in visited:
            visited.add(state)
            expanded.append(state)

            for neighbor in sorted(graph[state]['path_costs'].keys()):
                if neighbor not in visited and neighbor not in [i[0] for i in queue]:
                    queue.append((neighbor, path + [neighbor]))

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

path, expanded_states, unexpanded_states = bfs_graph_search(state_infos, start_state, goal_state)

if path:
    print(f"Path using BFS Graph Search: {' -> '.join(path)}")
    print(f"Order of states expanded: {', '.join(expanded_states)}")
    print(f"States that were not expanded: {', '.join(unexpanded_states)}")
else:
    print("No path found using BFS Graph Search!")
