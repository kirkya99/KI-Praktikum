from src.Puzzle8.Helper import *


def iterative_deepening(node, target):
    result = ""
    depth_barrier = 0
    while compare_strings(result, "Lösung gefunden") == 0:
        result = depth_first_search_b(node, target, 0, depth_barrier)
        depth_barrier = depth_barrier + 1


def depth_first_search_b(node, target, depth, depth_barrier):
    if target_reached(node, target):
        return "Lösung gefunden"
    new_nodes = node.descendants()
    while new_nodes is not None and depth_barrier:
        result = depth_first_search_b(node.first_node(), target, depth + 1, depth_barrier)
        if compare_strings(result, "Lösung gefunden") == 1:
            return "Lösung gefunden"
        else:
            new_nodes = node.remaining_nodes()
    return "Keine Lösung gefunden"
