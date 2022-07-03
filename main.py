from Tree import Tree

tree = Tree(4)
tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(3)
tree.insert(6)
tree.insert(9)


ptr = tree.root
newTree = Tree.binary_search(ptr, 7)
Tree.in_order_traversal(newTree)
print("finished demo of binary search")

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
