import copy


class Node:
    def __init__(self, node):
        self.node = node
        self.child_nodes = []

    node = []
    child_nodes = []

    def descendants(self):
        zero_row, zero_col = self.find_zero_position()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for direction in directions:
            new_row, new_col = zero_row + direction[0], zero_col + direction[1]

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = self.copy_node()
                new_state[zero_row][zero_col], new_state[new_row][new_col] = (new_state[new_row][new_col],
                                                                              new_state[zero_row][zero_col])

                self.child_nodes.append(Node(new_state))

        return self.child_nodes

    def copy_node(self):
        return copy.deepcopy(self.node)

    def first_node(self):
        return copy.deepcopy(self.child_nodes[0])

    def remaining_nodes(self):
        node_list = []
        for node in self.child_nodes:
            if node != self.child_nodes[0]:
                node_list.append(node)
        return node_list

    def find_zero_position(self):
        for i, row in enumerate(self.node):
            for j, value in enumerate(row):
                if value == 0:
                    return i, j
