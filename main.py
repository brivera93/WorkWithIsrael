from collections import defaultdict

import dictionary as dictionary

from Graph import Graph
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

# List of lists, used to store a graph


def breadth_first_search(graph, startNode: int):
    # for number in ra
    visited = [False] * len(graph)  # List which keeps track of nodes we have visited
    # List which holds current numbers to be processed, numbers added one layer at a time
    # Add the startNode to begin
    queue = [startNode]
    visited[startNode] = True
    while queue:
        currentNode = queue.pop(0)
        print("current node = " + str(currentNode), end=" ")
        for item in graph[currentNode]:
            if not visited[item]:
                queue.append(item)
                visited[item] = True
        print("\nqueue is currently " + str(queue))
        print(visited)


def DFS_stack(graph, startNode: int):
    visited = [False] * len(graph)
    stack = [startNode]
    while stack:
        currentNode = stack.pop()
        print("current node = " + str(currentNode), end=" ")
        for item in graph[currentNode]:
            if not visited[item]:
                stack.append(item)
                visited[item] = True
                currentNode = item
        print("\nstack is currently " + str(stack))
        print(visited)

#
# graph1 = defaultdict(list)
#
# graphNodes = [[0, 3], [1, 5, 6, 7], [2, 3, 7, 8], [3, 0, 2, 6], [4, 5, 9],
#               [5, 1, 4, 9], [6, 1, 3], [7, 1, 2, 9], [8, 2, 9], [9, 4, 5, 7, 8]]
# dict1 = dict()
#
# for number in range(len(graphNodes)):
#     dict1[graphNodes[number][0]] = False
#
# print(dict1)
# # print(graphNodes[0][0])
# # print(len(graphNodes))
# # alist = [False] * len(graphNodes)
# # print(len(alist))
# # for item in alist:
# #     print(item)
# breadth_first_search(graphNodes, 7)
# print(dict1)
# print("now lets use depth first search")
# for number in range(len(graphNodes)):
#     dict1[graphNodes[number][0]] = False
# DFS_stack(graphNodes, 7)
# print(dict1)


g = Graph()
g.add_edge(0, 3)
g.add_edge(1, 5)
g.add_edge(1, 6)
g.add_edge(1, 7)
g.add_edge(2, 3)
g.add_edge(2, 7)
g.add_edge(2, 8)
g.add_edge(3, 0)
g.add_edge(3, 2)
g.add_edge(3, 6)
g.add_edge(4, 5)
# g.add_edge(4, 9)
g.add_edge(5, 1)
g.add_edge(5, 4)
# g.add_edge(5, 9)
g.add_edge(6, 1)
g.add_edge(6, 3)
g.add_edge(7, 1)
g.add_edge(7, 2)
g.add_edge(7, 9)
g.add_edge(8, 2)
g.add_edge(8, 9)
# g.add_edge(9, 4)
# g.add_edge(9, 5)
g.add_edge(9, 7)
g.add_edge(9, 8)
print(g.graph)
g.DFS(8)








