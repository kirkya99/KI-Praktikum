from A_Star import heuristic_search
from A_Star_Node import AStarNode

Final_State = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
Init_State = [[2, 0, 4], [6, 7, 1], [8, 5, 3]]


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
    print("A*:")
    print(res[0])
    if res[1] is not None:
        print(res[1].node[0])
        print(res[1].node[1])
        print(res[1].node[2])
    print("--------------------")
