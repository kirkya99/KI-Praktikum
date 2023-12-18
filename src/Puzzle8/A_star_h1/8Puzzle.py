from A_Star import heuristic_search
from A_Star_Node import AStarNode

# Init_State = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
Final_State = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
Init_State = [[1, 0, 3], [4, 2, 6], [7, 5, 8]]
#  = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
# Init_State = [[0, 1, 3], [4, 2, 6], [7, 5, 8]]


if __name__ == '__main__':
    node = AStarNode(Init_State)
    res = heuristic_search(node, Final_State)

    print("--------------------")
    print("Startzustand:")
    print(Init_State[0])
    print(Init_State[1])
    print(Init_State[2])
    print("--------------------")
    print("--------------------")
    print("Breitensuche:")
    print(res[0])
    if res[1] is not None:
        print(res[1].node[0])
        print(res[1].node[1])
        print(res[1].node[2])
    print("--------------------")
