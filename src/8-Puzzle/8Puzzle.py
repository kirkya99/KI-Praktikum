from BreadthFirstSearch import breadth_search
from Node import Node

#Init_State = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
Final_State = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
Init_State = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]


if __name__ == '__main__':
    node = Node(Init_State)
    nodes = [node]
    res = breadth_search(nodes, Final_State)
    
    print("Breitensuche:")
    if res[1] is None:
        print(res[0])
    if res[1] is not None:
        print(res[0],": ",res[1])

