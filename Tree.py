class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Tree:
    def __init__(self, root_value):
        self.root = Node(root_value)
        self.elements = [root_value]

    def insert(self, new_value):
        new_node = Node(new_value)
        ptr = self.root
        while ptr is not None:
            if new_node.data < ptr.data:
                if ptr.left is None:
                    ptr.left = new_node
                    self.elements.append(new_value)
                    break
                else:
                    ptr = ptr.left
            else:  # new_node.data >= ptr.data
                if ptr.right is None:
                    ptr.right = new_node
                    self.elements.append(new_value)
                    break
                else:
                    ptr = ptr.right

            # balance_here
    # def balance_tree(self):

    def print_tree(self):
        print(self.elements)

    def mirror(self):
        if self.root is None:
            return
        queue = [self.root]
        while len(queue):
            current = queue[0]
            queue.pop(0)
            current.left, current.right = current.right, current.left
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    # def printTree(self):
    #     ptr = self.root
    #     list = []
    #     while ptr is not None:
    #         list.append(ptr.data)
    #         ptr = ptr.left
    #         list.append(ptr.data)
    #         ptr =

    def in_order_traversal(self, ptr):
        if ptr is not None:
            self.in_order_traversal(ptr.left)
            print(ptr.data)
            self.in_order_traversal(ptr.right)

    @staticmethod
    def in_order_traversal(ptr):
        if ptr is not None:
            Tree.in_order_traversal(ptr.left)
            print(ptr.data)
            Tree.in_order_traversal(ptr.right)

    @staticmethod
    def binary_search(root_node: Node, value):
        if root_node is None:
            print("there is no root node")
            return None
        elif root_node.data > value:
            return Tree.binary_search(root_node.left, value)
        elif root_node.data < value:
            return Tree.binary_search(root_node.right, value)
        else:
            return root_node




