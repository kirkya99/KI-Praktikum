from copy import deepcopy
from A_star_Node import Node


def heuristic_search(start, target):
    node_list = [start]
    while True:
        if node_list is None:
            return "Keine Lösung"
        node = first(node_list)
        node_list = rest(node_list)
        if target_found(node, target):
            return "Lösung gefunden", node
        node_list = sort_nodes(node.descendants(), node_list)


def first(node_list):
    return node_list[0]


def rest(node_list):
    new_node_list = []
    for node_index in range(1, len(node_list)):
        new_node_list.append(node_list(node_index))
    return new_node_list


def target_found(node, target):
    return node == target


def sort_nodes(descendants, node_list):
    return True