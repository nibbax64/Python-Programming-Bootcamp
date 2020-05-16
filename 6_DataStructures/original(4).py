# In this tutorial I'll cover the other 2 Linear Data Structures
# being Deques and Lists.

# DEQUES : A collection that allows you to add or remove data
# from either the front or end of the list.


class Deque:
    def __init__(self):
        self.deque = []

    def add_front(self, data):
        self.deque.append(data)

    def add_rear(self, data):
        self.deque.insert(0, data)

    def is_empty(self):
        return self.deque == []

    def remove_front(self):
        if self.is_empty():
            return "Empty Deque"
        else:
            return self.deque.pop()

    def remove_rear(self):
        if self.is_empty():
            return "Empty Deque"
        else:
            return self.deque.pop(0)

    def size(self):
        return len(self.deque)

    # Checks if string is a palindrome which
    # is the same word forward or backward
    # Racecar, Rotator, etc.
    def check_palindrome(self):
        is_palindrome = True
        while self.size() > 1 and is_palindrome:
            front = self.remove_front()
            rear = self.remove_rear()
            if front != rear:
                is_palindrome = False
        return is_palindrome



d_1 = Deque()
d_1.add_front("Dog")
d_1.add_rear("Cat")
d_1.add_rear("Mouse")
print(f"Front : {d_1.remove_front()}")
print(f"Rear : {d_1.remove_rear()}")
print(f"Size : {d_1.size()}")

# Check for palindrome
d_2 = Deque()
word = "racecar"
for i in word:
    d_2.add_rear(i)
print(f"Palindrome : {d_2.check_palindrome()}")

word_2 = "zero"
for i in word_2:
    d_2.add_rear(i)
print(f"Palindrome : {d_2.check_palindrome()}")

# LINKED LIST : A collection in which each item is only
# aware of the next item in the list. The last item in
# the list is also aware that there is no more values.
# Linked lists refer to each item in the list as a Node.

class Node:
    def __init__(self, data):
        self.data = data
        # Each node starts with no reference to the next
        self.next = None

    # Retrieves data stored
    def get_data(self):
        return self.data

    # Changes data stored
    def set_data(self, new_data):
        self.data = new_data

    # Stores the next node in the list
    def set_next(self, new_next):
        self.next = new_next

    # Retrieves the next node in the list
    def get_next(self):
        return self.next


class LinkedList:
    # The LinkedList will be assigned the 1st Node
    def __init__(self):
        self.head = None

    # We'll have to check if a head node exists
    def is_empty(self):
        return self.head is None

    # Adds nodes to the list by
    # 1. Creating a new node and assigning data
    # 2. Setting next as the previous head node
    # 3. Making the new node the lists new head node
    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # Removing a node requires us to :
    # 1. Start at the head node
    # 2. Check if it has the data we are searching for
    # 3. If not search for the next node in the list
    # 4. Repeat checking for data as long as nodes are left
    def remove(self, search_value):
        current_node = self.head
        # As we cycle this stores the previous node searched
        # so we can use it to find the next node in the list
        prev_node = None
        data_found = False

        # Check if matching data exists
        while not data_found:
            if current_node.get_data() == search_value:
                data_found = True
            # If not use the previously checked node to find
            # the next node in the list
            else:
                prev_node = current_node
                current_node = prev_node.get_next()
        # Assign current nodes next node to head
        if prev_node is None:
            self.head = current_node.get_next()
        else:
            # Assign the next node
            prev_node.set_next(current_node.get_next())

    # We could increment a length value each time a
    # new node is added, or we could cycle through
    # the LinkedList until get_next returns None
    def length(self):
        # Start cycling at the head
        current_node = self.head
        # Stores number of nodes
        total_nodes = 0
        # Cycle until the next node in the list = None
        while current_node is not None:
            total_nodes += 1
            current_node = current_node.get_next()
        return total_nodes

    # Searches for a value in the LinkedList and returns
    # True or False
    def search(self, search_value):
        current_node = self.head
        data_found = False
        # Cycle through LinkedList, skipping to next node
        # along the way until you find a match
        while current_node is not None and not data_found:
            if current_node.get_data() == search_value:
                data_found = True
            else:
                current_node = current_node.get_next()
        return data_found


ll = LinkedList()
ll.add(1)
ll.add(2)
print(f"Length : {ll.length()}")
print(f"1 : {ll.search(1)}")
ll.remove(1)
print(f"Length : {ll.length()}")
print(f"1 : {ll.search(1)}")










