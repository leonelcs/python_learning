from learning.trees.tree import Node, Tree

def main():
    print("iniciando")
    root = set_tree()
    print('in order')
    in_order_traversal(root)
    print('pre order')
    pre_order_traversal(root)
    print('post order')
    post_order_traversal(root)

def in_order_traversal(node):
    if (node is not None):
        in_order_traversal(node.left())
        visit(node)
        in_order_traversal(node.right())

def pre_order_traversal(node):
    if (node is not None):
        visit(node)
        in_order_traversal(node.left())
        in_order_traversal(node.right())

def post_order_traversal(node):
    if (node is not None):
        in_order_traversal(node.left())
        in_order_traversal(node.right())
        visit(node)

def visit(node):
    print(node.name)

def set_tree():
    root = Node()

    root.name = 10
    node1 = Node()
    node1.name = 5

    root.set_left(node1)

    node2 = Node()
    node2.name = 20
    node2.set_left(None)

    root.set_right(node2)

    node3 = Node()
    node3.name = 3
    node3.set_right(None)
    node3.set_left(None)

    node1.set_left(node3)

    node4 = Node()
    node4.name = 7
    node4.set_right(None)
    node4.set_left(None)
    
    node1.set_right(node4)

    node5 = Node()
    node5.name = 30
    node5.set_right(None)
    node5.set_left(None)
    
    node2.set_right(node5)

    return root



