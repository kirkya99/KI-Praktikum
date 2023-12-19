

def heuristic_search(start, target):
    node_list = [start]
    while True:
        if len(node_list) == 0 or node_list is None:
            return "Keine Lösung"
        node = node_list.pop(0)
        if target_found(node, target):
            return "Lösung gefunden", node
        node_list.extend(node.descendants())
        node_list = sort_nodes(node_list)


def target_found(node, target):
    return node == target


def sort_nodes(node_list):
    node_list.sort(key=lambda element: element.node)
    return node_list
