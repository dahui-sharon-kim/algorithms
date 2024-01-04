class Node:
    # def __init__(self, value, next = None): 
    # This is the constructor of the Node class.
    # Automatically called when a new instance of the class is created.
    def __init__(self, value, next = None): 
        # `self` refers to the current instance of the class.
        # It's automatically passed as the first argument to instance methods and constructors in Python.
        # `value` is a parameter that will be passed to the constructor to set the value of the node.
        # `next = None` is an optional parameter with a default value of `None`.
        # This parameter is used to establish a link to the next node.
        # If it's not provided, it defaults to `None`, indicating that there's no next node.
        self.value = value
        self.next = next