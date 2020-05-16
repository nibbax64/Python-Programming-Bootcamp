# I'll cover Binary Trees, How to create / add / delete nodes,
# tree traversal and how to find nodes.

# Root : Top Node of a Tree
# Path : Lines that Connect Nodes
# Leaf : Node without Children
# Subtree : Grouping of Parent Children in the Main Tree

# What is a Binary Tree
# It is a tree thats nodes will only ever have 2 children and the
# child on the left will have a value < than parent, while
# the child on the right has a value > than the parent.
# Parents can however only have 1 child node

# Unbalanced Trees are trees in which most of the Nodes are
# on one side. They are bad because they are slow.

# Why Use Trees?
# Fast Search, Insert & Delete
# Ordered Arrays are Bad at Insert & Delete
# Linked List Searching is Slow
# Tree Operations are O(log N)
# Trees are More Efficient if Many Different Operations
# are Needed

class BinaryTree:
    def __init__(self):
        # Every tree has a root node
        self.root = None

    def add_node(self, key, name):
        # Create and initialize the Node
        new_node = Node(key, name)

        # If no Root assign it
        if self.root is None:
            self.root = new_node
        else:
            # Set Root as the Node we will start with as
            # we traverse the tree
            focus_node = self.root

            while True:
                # Root is the top parent so we start there
                parent = focus_node

                # Check if new node should go on the left
                # or right
                if key < focus_node.key:
                    # Switch focus to the left child
                    focus_node = focus_node.left_child

                    # If the left_child has no children
                    if focus_node is None:
                        # Place the new node on the left
                        parent.left_child = new_node
                        # All Done with Adding
                        return True
                else:
                    # If here put the node on the right
                    focus_node = focus_node.right_child
                    # If the right child has no children
                    if focus_node is None:
                        # Place the new node on the right
                        parent.right_child = new_node
                        return True

    # Now that we can add nodes it would be nice to traverse
    # our Tree
    # In Order Traversal (SLIDE)
    # Start with left child, when None jump to Parent and to
    # the right child, back to parent and repeat
    def in_order_traverse(self, focus_node):
        # We visit nodes in ascending order
        # Recursion is used to go to 1 node and then to its
        # children nodes
        if focus_node is not None:
            self.in_order_traverse(focus_node.left_child)
            print(focus_node)
            self.in_order_traverse(focus_node.right_child)

    # With Preorder Traversal we hit our focus node root
    # and then cycle through all our left children after
    # that we jump up 1 parent and check for a right child
    # Then we go back up to root and work our way down
    # the right side.
    def preorder_traverse(self, focus_node):
        if focus_node is not None:
            print(focus_node)
            self.preorder_traverse(focus_node.left_child)
            self.preorder_traverse(focus_node.right_child)

    # With Post Order Traversal our Root is
    # going to come last. We start going to the
    # left child and then check both its children
    # The we'll check Roots Right Child and its children
    # finally checking Root last
    def postorder_traverse(self, focus_node):
        if focus_node is not None:
            self.postorder_traverse(focus_node.left_child)
            self.postorder_traverse(focus_node.right_child)
            print(focus_node)

    # In this function we will find Nodes
    def find(self, key):
        # Start at the top
        focus_node = self.root

        # While we haven't found it keep looking
        while focus_node.key != key:
            if key < focus_node.key:
                focus_node = focus_node.left_child
            else:
                focus_node = focus_node.right_child
            # If node wasn't found
            if focus_node is None:
                return None
        return focus_node


class Node:
    def __init__(self, key=0, name=""):
        self.key = key
        self.name = name
        # You can only have 1 left & right child
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"{self.name} has the key {self.key}"


tree = BinaryTree()
tree.add_node(50, "Boss")
tree.add_node(25, "Vice President")
tree.add_node(15, "Office Manager")
tree.add_node(30, "Secretary")
tree.add_node(75, "Sales Manager")
tree.add_node(85, "Salesman")

# Test Different Ways to Traverse
# As we traverse the Nodes the keys increase in order
print(tree.in_order_traverse(tree.root))
print(tree.preorder_traverse(tree.root))
print(tree.postorder_traverse(tree.root))

# Find the salesman
print(tree.find(85))
# Search for someone that doesn't exist
print(tree.find(9))

# In the next video I'll show how to delete Nodes in trees