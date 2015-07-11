"""
Module for the hop don't walk challenge located at
https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&category=343&page=show_problem&problem=2738

This uses a BFS approach to walking the graph except this does not construct a graph or store parent information in the
nodes because the state-space can become too large.
"""

__author__ = "Matt Rathbun"
__email__ = "mrathbun80@gmail.com"
__version__ = "1.0"

from collections import deque

def state_space_bfs(start_node):
    """
    Use BFS to perform a state space search on the graph
    """
    queue = deque([])
    max_depth = 10
    current_depth = 0
    queue.append(start_node)

    while len(queue) > 0 and current_depth <= max_depth:
        node = queue.popleft()

        # Check the current node for a goal state
        if is_goal_state(node["state"]):
            return node["depth"]

        successors = generate_successor_nodes(node)

        if len(successors) > 0:
            for successor in successors:
                successor["depth"] = node["depth"] + 1

                # Check the successor for a goal state
                if is_goal_state(successor["state"]):
                    return successor["depth"]

                if successor["depth"] > current_depth:
                    current_depth = successor["depth"]

            queue.append(successor)

    return -1

def generate_successor_nodes(node):
    """
    Generate a list of new nodes that are successors of a specified node
    """
    successors = []
    frog_position = node["frog_position"]
    state_size = len(node["state"])

    # Walk left
    if frog_position > 0:
        walk_left_state = list(node["state"])
        walk_left_state = swap_positions(walk_left_state, frog_position, frog_position - 1)
        successors.append({
            "state": walk_left_state,
            "depth": 0,
            "frog_position": frog_position - 1
        })

    # Jump left
    if frog_position > 1:
        jump_left_state = list(node["state"])

        if jump_left_state[frog_position - 2] == "B":
            jump_left_state[frog_position - 2] = "W"
        else:
            jump_left_state[frog_position - 2] = "B"

        jump_left_state = swap_positions(jump_left_state, frog_position, frog_position - 2)
        successors.append({
            "state": jump_left_state,
            "depth": 0,
            "frog_position": frog_position - 2
        })

    # Walk right
    if frog_position < state_size - 1:
        walk_right_state = list(node["state"])
        walk_right_state = swap_positions(walk_right_state, frog_position, frog_position + 1)
        successors.append({
            "state": walk_right_state,
            "depth": 0,
            "frog_position": frog_position + 1
        })

    # Jump right
    if frog_position < state_size - 2:
        jump_right_state = list(node["state"])

        if jump_right_state[frog_position + 2] == "B":
            jump_right_state[frog_position + 2] = "W"
        else:
            jump_right_state[frog_position + 2] = "B"

        jump_right_state = swap_positions(jump_right_state, frog_position, frog_position + 2)
        successors.append({
            "state": jump_right_state,
            "depth": 0,
            "frog_position": frog_position + 2
        })

    return successors

def swap_positions(state_space, position1, position2):
    """
    Swap two positions in the state space
    """
    state_space[position1], state_space[position2] = state_space[position2], state_space[position1]

    return state_space

def find_frog_position(state_space):
    """
    Find the frogs position (0 based) in the state space
    """
    for index, value in enumerate(state_space):
        if value == "F":
            return index

    return None

def is_goal_state(state_space):
    """
    Check to see if the state space is a goal state
    """
    last_black_tile_index = None
    possible_conflicting_white_tile_found = False

    for index, value in enumerate(state_space):
        if value == "B" and last_black_tile_index is not None and possible_conflicting_white_tile_found is True:
            return False
        elif value == "B":
            last_black_tile_index = index
        elif value == "W" and last_black_tile_index is not None:
            possible_conflicting_white_tile_found = True

    return True

if __name__ == "__main__":
    input = raw_input()
    state_space = []

    for i in range(len(input)):
        state_space.append(input[i])

    start_node = {
        "state": state_space,
        "depth": 0,
        "frog_position": find_frog_position(state_space)
    }
    number_of_moves_needed = state_space_bfs(start_node)

    print number_of_moves_needed