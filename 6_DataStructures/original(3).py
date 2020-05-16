import time

# In this tutorial I'll cover the 2 Linear Data Structures
# Stacks and Queues. Next time I'll cover Deques and Lists.
# They differ based on how data is added or removed.

# STACKS : A collection where items are both added and removed
# from the top. This is known as a Last In First Out collection.
# Think of this as a stack of books where the last one added to
# the stack is the 1st to come off.

# Here we implement the functions of a Stack using a List


class Stack:
    def __init__(self):
        self.stack = []

    # Puts value in Stack
    def push(self, data):
        self.stack.insert(0, data)

    def is_empty(self):
        return self.stack == []

    # Returns and deletes value from Stack
    def pop(self):
        if self.is_empty():
            return "Stack Empty"
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

    # Lets create a function using our stack that reverses
    # a string
    def reverse_string(self):
        while True:
            if len(self.stack) == 0:
                break
            else:
                print(self.stack.pop(0), end="")


s_1 = Stack()
s_1.push("Cat")
s_1.push("Dog")
print(s_1.peek())
print(s_1.size())
print(s_1.pop())
print(s_1.pop())
print(s_1.pop())

# Reverses the characters passed in
s_1.push("C")
s_1.push("a")
s_1.push("t")
s_1.reverse_string()


# QUEUES : A collection that operates using First In
# First Out logic. An example of this in the real
# world would be a line. If you are the 1st there
# you are served 1st.

# Let's make a Queue using a List

class Queue:
    def __init__(self):
        self.queue = []

    # Adds value to Queue
    def enqueue(self, data):
        self.queue.insert(0, data)

    def is_empty(self):
        return self.queue == []

    # Returns and deletes a value from Queue
    def dequeue(self):
        if self.is_empty():
            return "Queue Empty"
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    # This function will pause as each item has
    # its turn
    def wait_your_turn(self):
        while True:
            if len(self.queue) == 0:
                break
            else:
                print(f"{self.dequeue()} takes their turn")
                # Pause 3 seconds
                time.sleep(3)


print()
q_1 = Queue()
q_1.enqueue("Cat")
q_1.enqueue("Dog")
print(q_1.size())
print(q_1.dequeue())
print(q_1.dequeue())
print(q_1.dequeue())

# Test turn taking function
q_1.enqueue("Cat")
q_1.enqueue("Dog")
q_1.wait_your_turn()

# Next time I'll cover Deques and Lists













