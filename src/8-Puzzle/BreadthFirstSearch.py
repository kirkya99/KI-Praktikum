def breadth_search(node_list, target):
    new_nodes = []
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


def descendants(node):
    child_nodes = []
    print(node[0][0], node[0][1], node[0][2])
    return child_nodes


def append(new_nodes, child_nodes):
    for node in child_nodes:
        new_nodes.append(node)
    return new_nodes
