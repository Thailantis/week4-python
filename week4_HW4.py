from Node import Node
from BinarySearchTree import BinarySearchTree

def binary_tree_decorator(func):
    node_list = {}
    def wrapper(*args):
        if args in node_list:
            return node_list(*args)
        result = func(*args)
        node_list[args] = result
        return result
    return wrapper 

@binary_tree_decorator
def binary_tree_decorator(bst):
    return bst

result = binary_tree_decorator(5)
print(result)
