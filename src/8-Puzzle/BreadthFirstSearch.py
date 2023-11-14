from Node import Node

def breadth_search(node_list, target):

    for node in node_list:
        if target_reached(node, target):
            return "Lösung gefunden", node
        new_nodes = append(new_nodes, descendants(node))
    if new_nodes is not None:
        return breadth_search(new_nodes, target)
    else:
        return "keine Lösung"


def target_reached(node, target):
    return node == target

