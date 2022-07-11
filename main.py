from Tree import Tree


# tree = Tree(4)
# tree.insert(2)
# tree.insert(7)
# tree.insert(1)
# tree.insert(3)
# tree.insert(6)
# tree.insert(9)
#
#
# ptr = tree.root
# newTree = Tree.binary_search(ptr, 7)
# Tree.in_order_traversal(newTree)
# print("finished demo of binary search")

# print(Tree.binary_search(ptr, 7))
# ptr = tree.root
# tree.in_order_traversal(ptr)
# tree.print_tree()
# tree.mirror()
# ptr = tree.root
# tree.in_order_traversal(ptr)
# ptr = tree.root
# newTree = Tree.binary_search(ptr, 7)
# Tree.in_order_traversal(newTree)

#  List of lists, used to store a graph


def breadth_first_search(graph, startNode: int):
    visited = [False] * len(graph)  # List which keeps track of nodes we have visited
    # List which holds current numbers to be processed, numbers added one layer at a time
    # Add the startNode to begin
    queue = [startNode]
    visited[startNode] = True
    currentLayer = 1
    while queue:
        nextLevel = []
        currentNode = queue.pop(0)
        print("current node = " + str(currentNode), end=" ")
        for item in graph[currentNode]:
            if not visited[item]:
                # print(item, end=" ")
                queue.append(item)
                # nextLevel.append(item)
                visited[item] = True
        # queue = nextLevel
        print("\nqueue is currently " + str(queue))


graphNodes = [[0, 3], [1, 5, 6, 7], [2, 3, 7, 8], [3, 0, 2, 6], [4, 5, 9],
              [5, 1, 4, 9], [6, 1, 3], [7, 1, 2, 9], [8, 2, 9], [9, 4, 5, 7, 8]]
# print(graphNodes[0][0])
# print(len(graphNodes))
# alist = [False] * len(graphNodes)
# print(len(alist))
# for item in alist:
#     print(item)
breadth_first_search(graphNodes, 7)
