def depth_first_search(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes.
    expanded = []
    stack = [(start, [start])]  # Stack for DFS. Each element is a tuple (current_node, path_so_far)

    while stack:
        state, path = stack.pop()  # Pop a state and its path from the stack

        if state == goal:
            unexpanded = [item[0] for item in stack]
            return path, expanded, unexpanded

        if state not in visited:
            visited.add(state)
            expanded.append(state)

            # Add neighbors to the stack if they are not visited
            for neighbor in reversed(sorted(graph[state]['path_costs'].keys())):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append((neighbor, new_path))

    return None, expanded, []

state_infos = {
    'S': {
        "path_costs": {"A": 3, "B": 1},
        "heuristic_value": 7
    },
    'A': {
        "path_costs": {"B": 2, "C": 2},
        "heuristic_value": 5
    },
    'B': {
        "path_costs": {"C": 3},
        "heuristic_value": 7
    },
    'C': {
        "path_costs": {"D": 4, "G": 4},
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
path, expanded_states, unexpanded_states = depth_first_search(state_infos, start_state, goal_state)

if path:
    print(f"Path using DFS: {' -> '.join(path)}")
    print(f"Order of states expanded: {', '.join(expanded_states)}")
    print(f"States that were not expanded: {', '.join(unexpanded_states)}")
else:
    print(f"No path found from {start_state} to {goal_state} using DFS!")
