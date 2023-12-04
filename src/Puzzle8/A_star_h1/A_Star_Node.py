from copy import deepcopy


class AStarNode:
    def __init__(self, node, previous):
        self.g_s = previous.f_s
        self.h_s = self.heuristic()
        self.node = node
        self.child_nodes = []

    node = []
    child_nodes = []
    g_s = 0.0
    h_s = 0.0
    f_s = g_s + h_s

    def descendants(self):
        if self.node[0][0] == 0:
            new_state = self.copy_node()
            new_state[0][0], new_state[0][1] = self.node[0][1], self.node[0][0]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[0][0], new_state[1][0] = self.node[1][0], self.node[0][0]
            self.child_nodes.append(AStarNode(new_state, self))
        elif self.node[0][1] == 0:
            new_state = self.copy_node()
            new_state[0][1], new_state[0][0] = self.node[0][0], self.node[0][1]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[0][1], new_state[1][1] = self.node[1][1], self.node[0][1]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[0][1], new_state[0][2] = self.node[0][2], self.node[0][1]
            self.child_nodes.append(AStarNode(new_state, self))
        elif self.node[0][2] == 0:
            new_state = self.copy_node()
            new_state[0][2], new_state[0][1] = self.node[0][1], self.node[0][2]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[0][2], new_state[1][2] = self.node[1][2], self.node[0][2]
            self.child_nodes.append(AStarNode(new_state, self))
        elif self.node[1][0] == 0:
            new_state = self.copy_node()
            new_state[1][0], new_state[0][0] = self.node[0][0], self.node[1][0]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[1][0], new_state[1][1] = self.node[1][1], self.node[1][0]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[1][0], new_state[2][0] = self.node[2][0], self.node[1][0]
            self.child_nodes.append(AStarNode(new_state, self))
        elif self.node[1][1] == 0:
            new_state = self.copy_node()
            new_state[1][1], new_state[0][1] = self.node[0][1], self.node[1][1]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[1][1], new_state[1][0] = self.node[1][0], self.node[1][1]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[1][1], new_state[1][2] = self.node[1][2], self.node[1][1]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[1][1], new_state[2][1] = self.node[2][1], self.node[1][1]
            self.child_nodes.append(AStarNode(new_state, self))
        elif self.node[1][2] == 0:
            new_state = self.copy_node()
            new_state[1][2], new_state[0][2] = self.node[0][2], self.node[1][2]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[1][2], new_state[1][1] = self.node[1][1], self.node[1][2]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[1][2], new_state[2][2] = self.node[2][2], self.node[1][2]
            self.child_nodes.append(AStarNode(new_state, self))
        elif self.node[2][0] == 0:
            new_state = self.copy_node()
            new_state[2][0], new_state[1][0] = self.node[1][0], self.node[2][0]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[2][0], new_state[2][1] = self.node[2][1], self.node[2][0]
            self.child_nodes.append(AStarNode(new_state, self))
        elif self.node[2][1] == 0:
            new_state = self.copy_node()
            new_state[2][1], new_state[2][0] = self.node[2][0], self.node[2][1]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[2][1], new_state[1][1] = self.node[1][1], self.node[2][1]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[2][1], new_state[2][2] = self.node[2][2], self.node[2][1]
            self.child_nodes.append(AStarNode(new_state, self))
        elif self.node[2][2] == 0:
            new_state = self.copy_node()
            new_state[2][2], new_state[1][2] = self.node[1][2], self.node[2][2]
            self.child_nodes.append(AStarNode(new_state, self))
            new_state = self.copy_node()
            new_state[2][2], new_state[2][1] = self.node[2][1], self.node[2][2]
            self.child_nodes.append(AStarNode(new_state, self))

        # print("Node:")
        # print(self.node[0])
        # print(self.node[1])
        # print(self.node[2])
        # print()
        # print("Child nodes:")
        # for node in self.child_nodes:
        #     print(node.node[0])
        #     print(node.node[1])
        #     print(node.node[2])
        #     print()
        # print("--------------------")
        return self.child_nodes

    def copy_node(self):
        return deepcopy(self.node)

    def first_node(self):
        return deepcopy(self.child_nodes[0])

    def remaining_nodes(self):
        node_list = []
        for node in self.child_nodes:
            if node != self.child_nodes[0]:
                node_list.append(node)
        return node_list

    def heuristic(self):
        # return self.h_1_heuristic()
        return self.h_2_heuristic()

    def h_1_heuristic(self):
        number = 1
        counter_wrong_location = 0
        for x in range(0,2):
            for y in range(0,2):
                if counter_wrong_location == 8:
                    self.h_s = deepcopy(counter_wrong_location)
                elif self.node[x][y] != number:
                    counter_wrong_location += 1
        self.h_s = deepcopy(counter_wrong_location)

    def h_2_heuristic(self):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        manhattan_distance = 0
        for i in range(9):
            p_1 = return_position(self.node, i)
            p_2 = return_position(goal, i)
            manhattan_distance += calc_manhattan_distance(p_1, p_2)
        return 0


def return_position(node, val_to_find):
    position = [0, 0]
    for y in range(len(node)):
        for x in (range(y)):
            if node[x][y] == val_to_find:
                position = [x, y]
    return position


def calc_manhattan_distance(p_1, p_2):
    return abs(p_1[0]-p_2[0]) - abs(p_1[1]-p_2[1])
