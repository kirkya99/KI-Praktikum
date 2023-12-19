

def heuristic_search(start, target):
    node_list = [start]
    while True:
        if len(node_list) == 0 or node_list is None:
            return "Keine Lösung"
        node = node_list.pop(0)
        print(node.node, " Kosten:", node.f_s)
        if target_found(node.node, target) is True:
            return "Lösung gefunden", node
        node_list.extend(node.descendants())
        node_list = sort_nodes(node_list)


def target_found(node, target):
    return node == target


def sort_nodes(node_list):
    node_list.sort(key=lambda node_list_entry: node_list_entry.node)
    return node_list
