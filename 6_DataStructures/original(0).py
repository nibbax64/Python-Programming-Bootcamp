import timeit


def get_sum(mn):
    sol = 0
    for i in range(1, mn + 1):
        sol += i
    return sol


def get_sum_2(mn):
    sol = 0
    i = 1
    while i < mn:
        sol += i
        i += 1
    return sol


def get_sum_3(mn):
    return mn * (mn + 1) / 2


print("Testing get_sum")
print(timeit.repeat(stmt='get_sum(100000)', repeat=5, number=1, globals=globals()))

print("Testing get_sum_2")
print(timeit.repeat(stmt='get_sum_2(100000)', repeat=5, number=1, globals=globals()))

print("Testing get_sum_3")
print(timeit.repeat(stmt='get_sum_3(100000)', repeat=5, number=1, globals=globals()))

# Big-O Notation

# 45n^3 + 20n^2 + 19 (n=1) = 84
# (n = 2) 84 to 459 + 19
# (n = 10) 47,019 n^2 = 100
# 45n^3 = 45,000
# n^3 or O(N^3)

# O(1)
# O(N)
# O(N^2)
# O(log N)
# O(N log N)







