import copy


class Node:
    def __init__(self, node):
        self.node = node
        self.child_nodes = []

    node = []
    child_nodes = []

    def descendants(self):

        if self.node[0][0] == 0:
            print()
        elif self.node[2][0] == 0:
            new_state = copy_node(self)
            new_state[2][0], new_state[1][0] = self.node[1][0], self.node[2][0]
            self.child_nodes.append(Node(new_state))
            new_state = copy_node(self)
            new_state[2][0], new_state[2][1] = self.node[2][1], self.node[2][0]
            self.child_nodes.append(Node(new_state))

        elif self.node[2][1] == 0:
            new_state = copy_node(self)
            new_state[2][1], new_state[2][0] = self.node[2][0], self.node[2][1]
            self.child_nodes.append(Node(new_state))
            new_state = copy_node(self)
            new_state[2][1], new_state[1][1] = self.node[1][1], self.node[2][1]
            self.child_nodes.append(Node(new_state))
            new_state = copy_node(self)
            new_state[2][1], new_state[2][2] = self.node[2][2], self.node[2][1]
            self.child_nodes.append(Node(new_state))

        return self.child_nodes


def copy_node(self):
    return copy.deepcopy(self.node)
