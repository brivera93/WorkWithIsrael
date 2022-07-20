from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, root, adjacent):
        self.graph[root].append(adjacent)

    def DFS_Util(self, currentNode, visited: set):
        visited.add(currentNode)
        print(currentNode, end=" ")
        for neighbor in self.graph[currentNode]:
            if neighbor not in visited:
                self.DFS_Util(neighbor, visited)

    def DFS(self, node):
        visited = set()
        self.DFS_Util(node, visited)
