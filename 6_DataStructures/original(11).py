# What is a Heap?
# A heap is like a tree, but it is normally implemented
# as a list.
# With a heap every row must be complete. This means there
# must be a value in each node except for in the last row
# Parent nodes are larger than children, but unlike with a
# Binary Tree the left child isn't always bigger than the right
# Heaps can contain duplicates, and are fast at insertion,
# deletion and sorting.
# Heaps are slow when it comes to traversal & searching

# How Removal Works
# We pop off the top value and replace it with the lowest
# Then we percolate that value down as long as its value
# is greater than other values

# How Insertion Works
# Add the new value at the bottom and percolate up as long
# as its value is greater than others


class Node:
    def __init__(self, key):
        self.key = key

class Heap:
    def __init__(self, max_size):
        # Populate list with 31 Nones
        self.the_list = [None] * max_size
        self.max_size = max_size
        self.current_size = 0

    # Tests if list is empty
    def is_empty(self):
        return self.current_size == 0

    # Will insert a new Node using the provided key
    def insert(self, key):
        # Make sure list isn't full
        if self.current_size == self.max_size:
            return False

        # Create new node for the list
        new_node = Node(key)

        # Assign node after last assigned value
        self.the_list[self.current_size] = new_node

        # Keep track of the number of items in list
        self.current_size += 1

        # Pass the index for the new value which will be positioned
        self.percolate_up(self.current_size-1)
        return True

    def percolate_up(self, index):
        # Get the new nodes parent
        parent = int((index - 1) / 2)

        # The new node added
        bottom = self.the_list[index]

        # If not at top of list and new node is greater
        while index > 0 and self.the_list[parent].key < bottom.key:
            # Move new node up and prepare to test the next parent
            self.the_list[index] = self.the_list[parent]
            index = parent
            parent = int((parent - 1) / 2)

        # Assign current index with the new node
        self.the_list[index] = bottom

    # Remove max value
    def pop(self):
        # Get the root
        root = self.the_list[0]
        # Decrement to new list size
        self.current_size -= 1
        # Move bottom node to top
        self.the_list[0] = self.the_list[self.current_size]
        # Move all nodes into position starting at the top
        self.percolate_down(0)
        return root

    # This function moves values into position starting at the top
    def percolate_down(self, index):
        # Will hold the larger of the children nodes
        larger_child = 0

        # Gets the top node in the list
        top = self.the_list[index]

        # We don't have to check the bottom row
        while index < self.current_size / 2:
            # Gets the index for the left & right child
            left_child = 2 * index + 1
            right_child = left_child + 1

            # Avoid None valued Nodes and if left child is < right
            if right_child < self.current_size and self.the_list[left_child].key < self.the_list[right_child].key:

                # Then save the right child index as the largest
                larger_child = right_child
            else:
                # Otherwise the left child is the largest
                larger_child = left_child

            # If the top value is ever greater than the largest
            # child jump out of the while
            if top.key >= self.the_list[larger_child].key:
                break

            # Assign the largest node
            self.the_list[index] = self.the_list[larger_child]

            # Set the index to that largest node
            index = larger_child

        # After we finish cycling assign the top value
        self.the_list[index] = top


heap = Heap(31)
heap.insert(72)
heap.insert(44)
heap.insert(53)
heap.insert(21)
heap.insert(66)
heap.insert(100)
heap.insert(84)
heap.insert(35)
heap.insert(19)
heap.insert(90)

# Pop off the 100
heap.pop()

for i in heap.the_list:
    if i is None:
        print("N", end=", ")
    else:
        print(i.key, end=", ")
print()





