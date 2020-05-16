# O(log N) : Algorithms in which the amount of data
# is roughly decreased by 50% each time through
# the algorithm.

# If 10^2 = 100 then the log10(100) = 2, because
# a logarithm tells us what power is used to make
# a number

# Log N increases at a dramatically slower rate as
# N increases which makes them more efficient as
# N increases. [Slide]

# A Binary search is an example.
# The Binary Search is extremely fast, but the
# negative is that it only works with sorted lists.
# After the sort it starts searching in the middle of
# the list which allows it to eliminate 1/2 of the
# values after each cycle through the list.

# def binary_search(value: int):
#     list_size = len(list_1)
#     low_index = 0
#     high_index = list_size - 1
#     while low_index <= high_index:
#         mid_index = int((high_index + low_index) / 2)
#         if list_1[mid_index] < value:
#             low_index = mid_index + 1
#         elif list_1[mid_index] > value:
#             high_index = mid_index - 1
#         else:
#             print(f"Found a match for {value} at index {mid_index}")
#             low_index = high_index + 1
#
#
# list_1 = generate_rand_list(1000)
# bubble_sort()
# start_time = time.time()
# binary_search(150)
# print(f"{time.time() - start_time} seconds")
#
# list_1 = generate_rand_list(10000)
# bubble_sort()
# start_time = time.time()
# binary_search(150)
# print(f"{time.time() - start_time} seconds")

# O(n log n) : The Quick Sort is an example of this
# I'll explain the Quick Sort and then show how
# it matches with this Big-O

# With the Quick Sort we divide up all values in the
# list into 2 parts. Each part is called a
# partition. The value that lies in the middle of those
# 2 parts is called the pivot. As we cycle through
# the list if a value is greater then the pivot it
# goes to the right and if less it goes to the left.
# Slide


def partition(start, end):
    pivot = list_1[start]
    low = start + 1
    high = end
    while True:
        while low <= high and list_1[high] >= pivot:
            high = high - 1
        while low <= high and list_1[low] <= pivot:
            low = low + 1

        if low <= high:
            list_1[low], list_1[high] = list_1[high], list_1[low]
        else:
            break
    list_1[start], list_1[high] = list_1[high], list_1[start]
    return high


def quick_sort(start, end):
    # Demonstrates how the Quick sort works
    for k in list_1:
        print(k, end=", ")
    print()

    if start >= end:
        return
    part = partition(start, end)
    quick_sort(start, part - 1)
    quick_sort(part + 1, end)


list_1 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
quick_sort(0, len(list_1) - 1)
print(list_1)

# Most sorts are O(N) because every element must be
# looked at once. The Bubble Sort as we saw is O(N^2)
# To prove that the Quick Sort is O(n log n) we know
# that values are only compared once. So, each comparison
# will reduce the possible final sorted lists in half.
# So the number of comparisons is log n! (Factorial of N)
# Comparisons = log n + log(n-1) + ... + log(1)
# Evaluates to n log n