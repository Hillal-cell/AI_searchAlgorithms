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
        'path_costs': {},
        "heuristic_value": 0
    }
}




def depth_first_search_tree(graph, start_state, goal_state):
    stack = [(start_state, [])]  # Stack to store the current state and its path
    expanded = []

    while stack:
        current_state, path = stack.pop()
        
        # Avoid revisiting already expanded states
        if current_state in expanded:
            continue

        # Add the current state to the list of expanded states
        expanded.append(current_state)

        if current_state == goal_state:
            unexpanded = list(set(graph.keys()) - set(expanded))
            return path + [current_state], expanded, unexpanded
        
        # Get the neighbors of the current state
        neighbors = graph[current_state]["path_costs"].keys()

        # Reversed is used to pop the alphabetically first state from the stack first 
        for neighbor in reversed(sorted(neighbors)):
            if neighbor not in expanded:
                stack.append((neighbor, path + [current_state]))  # Add neighbors to the stack with updated path
    
    unexpanded = list(set(graph.keys()) - set(expanded))
    return None, expanded, unexpanded

# Example usage:
start_state = 'S'
goal_state = 'G'
result_path, result_expanded, result_unexpanded = depth_first_search_tree(state_infos, start_state, goal_state)

if result_path:
    print(f"Path using DFS Tree Search: {' -> '.join(result_path)}")
    print(f"Order of states expanded: {', '.join(result_expanded)}")
    print(f"States that were not expanded: {', '.join(result_unexpanded)}")
else:
    print("No path found using DFS Tree Search!")
