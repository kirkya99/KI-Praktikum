class Node:
    def __init__(self, node):
        self.node = node
        self.child_nodes = []

    global node
    child_nodes = []

    def calc_child_nodes(self):
        temp = self.node.copy()
        if self.node[0][0] == 0:
            new_node = temp.copy()
            new_node[0][0] = self.node[0][1]
            new_node[0][1] = self.node[0][0]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[0][0] = self.node[1][0]
            new_node[1][0] = self.node[0][0]
            self.child_nodes.append(new_node)
            return
        elif self.node[0][1] == 0:
            new_node = temp.copy()
            new_node[0][1] = self.node[0][0]
            new_node[0][0] = self.node[0][1]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[0][1] = self.node[0][2]
            new_node[0][2] = self.node[0][1]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[0][1] = self.node[1][1]
            new_node[1][1] = self.node[0][1]
            self.child_nodes.append(new_node)
            return
        elif self.node[0][2] == 0:
            new_node = temp.copy()
            new_node[0][2] = self.node[0][1]
            new_node[0][1] = self.node[0][2]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[0][2] = self.node[0][1]
            new_node[1][2] = self.node[0][2]
            self.child_nodes.append(new_node)
            return
        elif self.node[1][0] == 0:
            new_node = temp.copy()
            new_node[1][0] = self.node[0][0]
            new_node[0][0] = self.node[1][0]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[1][0] = self.node[1][1]
            new_node[1][1] = self.node[1][0]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[1][0] = self.node[2][0]
            new_node[2][0] = self.node[1][0]
            self.child_nodes.append(new_node)
            return
        elif self.node[1][1] == 0:
            new_node = temp.copy()
            new_node[1][1] = self.node[0][1]
            new_node[0][1] = self.node[1][1]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[1][1] = self.node[1][0]
            new_node[1][0] = self.node[1][1]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[1][1] = self.node[1][2]
            new_node[1][2] = self.node[1][1]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[1][1] = self.node[2][1]
            new_node[2][1] = self.node[1][1]
            self.child_nodes.append(new_node)
            return
        elif self.node[1][2] == 0:
            new_node = temp.copy()
            new_node[1][2] = self.node[0][2]
            new_node[0][2] = self.node[1][2]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[1][2] = self.node[1][1]
            new_node[1][1] = self.node[1][2]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[1][2] = self.node[2][2]
            new_node[2][2] = self.node[1][1]
            self.child_nodes.append(new_node)
            return
        elif self.node[2][0] == 0:
            new_node = temp.copy()
            new_node[2][0] = self.node[1][0]
            new_node[1][0] = self.node[2][0]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[2][0] = self.node[2][1]
            new_node[2][1] = self.node[2][0]
            self.child_nodes.append(new_node)
            return
        elif self.node[2][1] == 0:
            new_node = temp.copy()
            new_node[2][1] = self.node[2][0]
            new_node[2][0] = self.node[2][1]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[2][1] = self.node[1][1]
            new_node[1][1] = self.node[2][1]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[2][1] = self.node[2][2]
            new_node[2][2] = self.node[2][1]
            self.child_nodes.append(new_node)
            return
        elif self.node[2][2] == 0:
            new_node = temp.copy()
            new_node[2][2] = self.node[1][2]
            new_node[1][2] = self.node[2][2]
            self.child_nodes.append(new_node)
            new_node = temp.copy()
            new_node[2][2] = self.node[2][1]
            new_node[2][1] = self.node[2][2]
            self.child_nodes.append(new_node)
            return
