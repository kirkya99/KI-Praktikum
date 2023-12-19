from copy import deepcopy


class AStarNode:
    def __init__(self, node, previous=None):
        if previous is not None:
            self.initialize_with_two_params(node, previous)
        else:
            self.initialize_with_one_param(node)

    def initialize_with_two_params(self, node, previous):
        self.g_s = previous.g_s + 1
        self.h_s = deepcopy(self.heuristic())
        self.node = node
        self.child_nodes = []

    def initialize_with_one_param(self, node):
        self.h_s = deepcopy(self.heuristic())
        self.node = node
        self.child_nodes = []

    node = []
    child_nodes = []
    g_s = 0.0
    h_s = 0.0
    f_s = g_s + h_s

    def descendants(self):
        zero_row, zero_col = self.find_zero_position()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for direction in directions:
            new_row, new_col = zero_row + direction[0], zero_col + direction[1]

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = self.copy_node()
                new_state[zero_row][zero_col], new_state[new_row][new_col] = (new_state[new_row][new_col],
                                                                              new_state[zero_row][zero_col])

                self.child_nodes.append(AStarNode(new_state, self))

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
        for x in range(len(self.node)):
            for y in range(len(self.node[x])):
                if self.node[x][y] != number:
                    counter_wrong_location += 1
        return counter_wrong_location

    def h_2_heuristic(self):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        manhattan_distance = 0
        for searched_number in range(9):
            p_1 = self.return_position(self.node, searched_number)
            p_2 = self.return_position(goal, searched_number)
            manhattan_distance += self.calc_manhattan_distance(p_1, p_2)
        return manhattan_distance

    def find_zero_position(self):
        for i, row in enumerate(self.node):
            for j, value in enumerate(row):
                if value == 0:
                    return i, j

    @staticmethod
    def return_position(node, val_to_find):
        position = [0, 0]
        for y in range(len(node)):
            for x in (range(y)):
                if node[x][y] == val_to_find:
                    position = [x, y]
        return position

    @staticmethod
    def calc_manhattan_distance(p_1, p_2):
        return abs(p_1[0] - p_2[0]) + abs(p_1[1] - p_2[1])
