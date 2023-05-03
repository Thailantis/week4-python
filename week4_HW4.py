def binary_tree_decorator(func):
    node_list = ([])
    def wrapper(*args):
        if args in node_list:
            return node_list[args]
        result = func(*args)
        node_list[args] = result
        return result
    return wrapper 

@binary_tree_decorator
def binary_wrapper(bst):
    return bst

result = binary_wrapper(5)

result.add_node(10)
result.add_node(15)
result.add_node(20)

print(result)
