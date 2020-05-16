import random
import time

list_1 = []
start_time = 0
end_time = 0

def generate_rand_list(max_size):
    new_list = []
    for i in range(0, max_size):
        new_list.append(random.randint(1, 100))
    return new_list

list_1 = generate_rand_list(10)

# O(1) : An algorithm that executes in the same amount
# of time regardless of how big the list is
# A 10 item list or a 10,000 item list will always
# take the same amount of time with this operation
def add_item_to_list(num):
    list_1.append(num)

# O(N) : Algorithm thats time to complete is directly
# proportional to the amount of data supplied
# An example of this is a linear search because it
# requires us to look in each space of an array
# This is true even if we find the item during the 1st
# search because Big-O Notation describes the worst
# case situation through using the algorithm
def linear_search(val):
    val_found = "Value Not Found"
    for i in list_1:
        if i == val:
            val_found = "Value Found"
    print(val_found)


# print("Testing Linear Search")
# list_1 = generate_rand_list(10)
# start_time = time.time()
# linear_search(10000)
# print(f"{time.time() - start_time} seconds")
#
# list_1 = generate_rand_list(1000)
# start_time = time.time()
# linear_search(10000)
# print(f"{time.time() - start_time} seconds")
#
# list_1 = generate_rand_list(10000)
# start_time = time.time()
# linear_search(10000)
# print(f"{time.time() - start_time} seconds")
#
# list_1 = generate_rand_list(100000)
# start_time = time.time()
# linear_search(10000)
# print(f"{time.time() - start_time} seconds")

# O(N^2) : Algorithms thats time to complete is
# proportional to the square of the amount of data.
# A Bubble sort is an example because it contains
# nested iterations. Further nested iterations
# will result in O(N^3), O(N^4) performance
# Each pass through the outer loop O(N) requires
# us to go through the entire list again so N is
# squared

# The Bubble sort is a way to sort a list
# It works this way
# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of the list when the outer loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning of the loop
# 4. Check if list[Index] > list[Index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at the end of the list
# 7. Decrement the outer loop by 1


def bubble_sort():
    list_size = len(list_1)
    # Cycle through each value in the list
    for i in range(list_size):
        # We don't have to check previous i items
        # checked
        for j in range(0, list_size-i-1):
            # If the 1st value is greater then the
            # 2nd have them swap
            if list_1[j] > list_1[j+1]:
                list_1[j], list_1[j+1] = list_1[j+1], list_1[j]

            # Demonstrates how the Bubble sort works
            # for k in list_1:
            #     print(k, end=", ")
            # print()


# Shows Bubble Sort changes as it cycles
# list_1 = generate_rand_list(10)
# bubble_sort()

# Bubble Sort Tests
# list_1 = generate_rand_list(100)
# start_time = time.time()
# bubble_sort()
# print(f"{time.time() - start_time} seconds")
#
# list_1 = generate_rand_list(1000)
# start_time = time.time()
# bubble_sort()
# print(f"{time.time() - start_time} seconds")
#
# list_1 = generate_rand_list(10000)
# start_time = time.time()
# bubble_sort()
# print(f"{time.time() - start_time} seconds")











