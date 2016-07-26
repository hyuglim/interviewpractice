# is there a route between two nodes?
# undirected graph

class Node:
    def __init__(self, value, neighbors):
        self.value = value
        self.neighbors = neighbors


def is_there_route_between_two_nodes(source, destination):
    halfway_nodes = set()
    source_frontier = set(source)
    destination_frontier = set(destination)
    while !halfway_nodes and (source_frontier or destination_frontier):
        source_frontier = get_next_frontier(source_frontier)
        destination_frontier = get_next_frontier(destination_frontier)
    return halfway_nodes


def get_next_frontier(frontier_nodes):
    next_frontier = set()
    while frontier_nodes:
        next_frontier.update(frontier_nodes.pop().neighbors)
    return next_frontier

