"""
Module for the hop don't walk challenge located at
https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&category=343&page=show_problem&problem=2738
"""

__author__ = "Matt Rathbun"
__email__ = "mrathbun80@gmail.com"
__version__ = "1.0"

from collections import deque

def state_space_bfs(graph, start_node):
    """
    Use BFS to perform a state space search on the graph
    """
    queue = deque([])
    max_depth = 10
    current_depth = 0
    start_node = {
        "depth": current_depth,
        "parent": None
    }
    queue.append(start_node)

    while len(queue) > 0 and current_depth <= max_depth:
        node = queue.popleft()
        generated_state_spaces = generate_state_spaces(node)

        if len(generated_state_spaces) > 0:
            for state_space in generated_state_spaces:
                state_space.depth = node.depth + 1
                state_space.parent = node

                queue.append(state_space)

def generate_state_spaces(node):
    """
    Generate a list of state spaces that can occur from a specified node
    """

    # @TODO Jump left
    # @TODO Move left
    # @TODO Move right
    # @TODO Jump right
    state_spaces = []

    return state_spaces

if __name__ == "__main__":
    initial_state = raw_input()
    start_node = {
        "state": initial_state,
        "depth": None,
        "parent": None
    }
    graph = [start_node]
    state_space_bfs(graph, start_node)

    print graph
