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
    new_node = []

    if node[0][0] == 0:
        new_node[0][0] = node[0][1]
        new_node[0][1] = node[0][0]
        child_nodes.append(new_node)
        new_node[0][0] = node[1][0]
        new_node[1][0] = node[0][0]
        child_nodes.append(new_node)
        return child_nodes
    elif node[0][1] == 0:
        new_node[0][1] = node[0][0]
        new_node[0][0] = node[0][1]
        child_nodes.append(new_node)
        new_node[0][1] = node[0][2]
        new_node[0][2] = node[0][1]
        child_nodes.append(new_node)
        new_node[0][1] = node[1][1]
        new_node[1][1] = node[0][1]
        child_nodes.append(new_node)
        return child_nodes
    elif node[0][2] == 0:
        new_node[0][2] = node[0][1]
        new_node[0][1] = node[0][2]
        child_nodes.append(new_node)
        new_node[0][2] = node[0][1]
        new_node[1][2] = node[0][2]
        child_nodes.append(new_node)
        return child_nodes
    elif node[1][0] == 0:
        new_node[1][0] = node[0][0]
        new_node[0][0] = node[1][0]
        child_nodes.append(new_node)
        new_node[1][0] = node[1][1]
        new_node[1][1] = node[1][0]
        child_nodes.append(new_node)
        new_node[1][0] = node[2][0]
        new_node[2][0] = node[1][0]
        child_nodes.append(new_node)
        return  child_nodes
    elif node[1][1] == 0:
        new_node[1][1] = node[0][1]
        new_node[0][1] = node[1][1]
        child_nodes.append(new_node)
        new_node[1][1] = node[1][0]
        new_node[1][0] = node[1][1]
        child_nodes.append(new_node)
        new_node[1][1] = node[1][2]
        new_node[1][2] = node[1][1]
        child_nodes.append(new_node)
        new_node[1][1] = node[2][1]
        new_node[2][1] = node[1][1]
        child_nodes.append(new_node)
        return child_nodes
    elif node[1][2] == 0:
        new_node[1][2] = node[0][2]
        new_node[0][2] = node[1][2]
        child_nodes.append(new_node)
        new_node[1][2] = node[1][1]
        new_node[1][1] = node[1][2]
        child_nodes.append(new_node)
        new_node[1][2] = node[2][2]
        new_node[2][2] = node[1][1]
        child_nodes.append(new_node)
        return child_nodes
    elif node[2][0] == 0:
        new_node[2][0] = node[1][0]
        new_node[1][0] = node[2][0]
        child_nodes.append(new_node)
        new_node[2][0] = node[2][1]
        new_node[2][1] = node[2][0]
        child_nodes.append(new_node)
        return child_nodes
    elif node[2][1] == 0:
        new_node[2][1] = node[2][0]
        new_node[2][0] = node[2][1]
        child_nodes.append(new_node)
        new_node[2][1] = node[1][1]
        new_node[1][1] = node[2][1]
        child_nodes.append(new_node)
        new_node[2][1] = node[2][2]
        new_node[2][2] = node[2][1]
        child_nodes.append(new_node)
        return child_nodes
    elif node[2][2] == 0:
        new_node[2][2] = node[1][2]
        new_node[1][2] = node[2][2]
        child_nodes.append(new_node)
        new_node[2][2] = node[2][1]
        new_node[2][1] = node[2][2]
        child_nodes.append(new_node)
        return child_nodes
    else:
        return []


def append(new_nodes, child_nodes):
    for node in child_nodes:
        new_nodes.append(node)
    return new_nodes
