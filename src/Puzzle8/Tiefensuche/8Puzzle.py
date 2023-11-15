from DepthFirstSearch import depth_first_search
from src.Puzzle8.Node import Node

# Init_State = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
Final_State = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# Init_State = [[1, 0, 3], [4, 2, 6], [7, 5, 8]]
Init_State = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
# Init_State = [[0, 1, 3], [4, 2, 6], [7, 5, 8]]


if __name__ == '__main__':
    node = Node(Init_State)

    res = depth_first_search(node, Final_State)

    print("--------------------")
    print("Startzustand:")
    print(Init_State[0])
    print(Init_State[1])
    print(Init_State[2])
    print("--------------------")
    print("--------------------")
    print("Tiefensuche:")
    print(res[0])
    print("--------------------")
