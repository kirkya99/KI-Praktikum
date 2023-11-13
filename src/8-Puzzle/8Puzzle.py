from BreadthFirstSearch import breadth_search

Init_State = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
Final_State = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


if __name__ == '__main__':
    nodes = [Init_State]
    res = breadth_search(nodes, Final_State)
    print("Breitensuche:")
    print(res[0])
    if res[1] is not None:
        print(res[1])

