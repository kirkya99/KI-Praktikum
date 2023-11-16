import copy


class Node:
    def __init__(self, node):
        self.node = node
        self.child_nodes = []

    node = []
    child_nodes = []

    def descendants(self):
        if self.node[0][0] == 0:
            new_state = self.copy_node()
            new_state[0][0], new_state[0][1] = self.node[0][1], self.node[0][0]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[0][0], new_state[1][0] = self.node[1][0], self.node[0][0]
            self.child_nodes.append(Node(new_state))
        elif self.node[0][1] == 0:
            new_state = self.copy_node()
            new_state[0][1], new_state[0][0] = self.node[0][0], self.node[0][1]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[0][1], new_state[1][1] = self.node[1][1], self.node[0][1]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[0][1], new_state[0][2] = self.node[0][2], self.node[0][1]
            self.child_nodes.append(Node(new_state))
        elif self.node[0][2] == 0:
            new_state = self.copy_node()
            new_state[0][2], new_state[0][1] = self.node[0][1], self.node[0][2]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[0][2], new_state[1][2] = self.node[1][2], self.node[0][2]
            self.child_nodes.append(Node(new_state))
        elif self.node[1][0] == 0:
            new_state = self.copy_node()
            new_state[1][0], new_state[0][0] = self.node[0][0], self.node[1][0]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[1][0], new_state[1][1] = self.node[1][1], self.node[1][0]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[1][0], new_state[2][0] = self.node[2][0], self.node[1][0]
            self.child_nodes.append(Node(new_state))
        elif self.node[1][1] == 0:
            new_state = self.copy_node()
            new_state[1][1], new_state[0][1] = self.node[0][1], self.node[1][1]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[1][1], new_state[1][0] = self.node[1][0], self.node[1][1]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[1][1], new_state[1][2] = self.node[1][2], self.node[1][1]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[1][1], new_state[2][1] = self.node[2][1], self.node[1][1]
            self.child_nodes.append(Node(new_state))
        elif self.node[1][2] == 0:
            new_state = self.copy_node()
            new_state[1][2], new_state[0][2] = self.node[0][2], self.node[1][2]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[1][2], new_state[1][1] = self.node[1][1], self.node[1][2]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[1][2], new_state[2][2] = self.node[2][2], self.node[1][2]
            self.child_nodes.append(Node(new_state))
        elif self.node[2][0] == 0:
            new_state = self.copy_node()
            new_state[2][0], new_state[1][0] = self.node[1][0], self.node[2][0]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[2][0], new_state[2][1] = self.node[2][1], self.node[2][0]
            self.child_nodes.append(Node(new_state))
        elif self.node[2][1] == 0:
            new_state = self.copy_node()
            new_state[2][1], new_state[2][0] = self.node[2][0], self.node[2][1]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[2][1], new_state[1][1] = self.node[1][1], self.node[2][1]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[2][1], new_state[2][2] = self.node[2][2], self.node[2][1]
            self.child_nodes.append(Node(new_state))
        elif self.node[2][2] == 0:
            new_state = self.copy_node()
            new_state[2][2], new_state[1][2] = self.node[1][2], self.node[2][2]
            self.child_nodes.append(Node(new_state))
            new_state = self.copy_node()
            new_state[2][2], new_state[2][1] = self.node[2][1], self.node[2][2]
            self.child_nodes.append(Node(new_state))

        print("Parent:")
        print(self.node[0])
        print(self.node[1])
        print(self.node[2])
        print()
        print("Child nodes:")
        for node in self.child_nodes:
            print(node.node[0])
            print(node.node[1])
            print(node.node[2])
            print()
        print("--------------------")
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
