def breadth_search(node_list, target):

    new_nodes = []
    for node in node_list:
        if target_reached(node, target):
            return "Lösung gefunden", node
        new_nodes = append(new_nodes, node.descendants())
    if new_nodes is not None:
        return breadth_search(new_nodes, target)
    else:
        return "keine Lösung"


def target_reached(node, target):
    return node.node == target


def append(nodes, new_nodes):
    for node in new_nodes:
        nodes.append(node)
    return nodes


