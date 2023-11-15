def depth_first_search (node, target):
    if target_reached(node, target):
        return "Lösung gefunden"
    new_nodes = node.descendants()
    while new_nodes is not None:
        result = depth_first_search(node.first_node(), target)
        if result == "Lösung gefunden":
            return "Lösung gefunden"
        else:
            new_nodes = node.remaining_nodes()
    return "Keine Lösung gefunden"



def target_reached (node, target):
    return node.node == target