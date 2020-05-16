# What I cover in this tutorial :
# Why we should use Primes when constructing Hash Tables
# How to increase hash table size even though I said to avoid it
# What clustering is and how to avoid it
# How to work with Double Hashing

# Why We Use Primes?
# Previously we calculated the index by using the value to
# store and shrunk it down to fit in the list using modulus
# We want to avoid collisions which are caused when we
# try to store similar data.
# N values with similar data actually cause N times the
# number of collisions.
# If we use lists with the size of a prime we can cut down
# on collisions.

class HashFunctions:
    def __init__(self, size):
        self.list_size = size
        self.the_list = []
        for i in range(size):
            self.the_list.append(None)

    # This is the hash function from the previous tut
    # Let's compare the number of collisions versus
    # using 30 and then 31 which is a prime number
    def hash_func_2(self, str_list):
        for k in str_list:
            str_int = int(k)
            index = str_int % 31
            # print(f"Mod Index : {index} Value : {str_int}")

            # Look for a collision
            while self.the_list[index] is not None:
                index += 1
                # print(f"Collision Try {index} Instead")
                # If we get to the end of the list go to index 0
                index %= self.list_size

            # We know we found an index where we can store
            self.the_list[index] = k

    # All prime numbers except 2 & 3 are of the form 6k +/- 1
    def is_prime(self, num):
        # 0 & 1 are Not Prime
        if num <= 1:
            return False
        # 2 & 3 are Prime
        if num <= 3:
            return True
        # We can eliminate values up to 25 by just checking
        # for divisibility of 2 or 3
        if num % 2 == 0 or num % 3 == 0:
            # print(f"{num} Divisible by 2 or 3")
            return False

        # We will test if num is not 6 * num +/- 1 and then increment
        # j by 6 each time
        j = 5

        # Let's square j instead of getting the square root of
        # num to avoid using the math module
        while j * j <= num:
            # print(f"J : {j} num : {num}")
            # print(f"num % j == 0 : {num % j}")
            # print(f"num % j + 2 == 0 : {num % (j + 2)}")
            # We only need to test if the number is divisible by
            # 5 & 7, 11 & 13, 17 & 19, ... because a prime
            # 6 * num +/- 1
            if num % j == 0 or num % (j + 2) == 0:
                return False

            # Increment to check the next grouping
            j = j + 6
        return True

    # Now that I can get primes I need a function that will
    # generate the next prime that is greater than the
    # minimum list size required
    def get_next_prime(self, min_size):
        while True:
            if self.is_prime(min_size):
                return min_size
            else:
                min_size += 1

    # Function that finds the next required array size
    def increase_list_size(self, min_size):
        new_list_size = self.get_next_prime(min_size)
        self.move_old_list(new_list_size)

    # This function will clear all values in the main list
    def fill_list_with_none(self):
        for k in range(self.list_size):
            self.the_list.append(None)

    # Removes moves all values in list to the beginning
    # of the list
    def remove_empty_spaces_in_list(self):
        temp_list = []

        # if a list item isn't None add it to the temp_list
        for j in self.the_list:
            if j is not None:
                temp_list.append(j)

        return temp_list

    def move_old_list(self, new_list_size):
        # Update list size
        self.list_size = new_list_size

        # Store old list in a new one with spaces removed
        clean_list = self.remove_empty_spaces_in_list()

        # Fill list with None values
        self.fill_list_with_none()

        # Store the same 30 items again in our new list
        self.hash_func_2(clean_list)


l_2 = ["30", "60", "90", "120", "150", "180", "210", "240", "270", "300", "330", "360", "390", "420", "450", "480",
       "510", "540", "570", "600", "989", "984", "320", "321", "400", "415", "450", "50", "660", "624"]

hash_func = HashFunctions(31)
hash_func.hash_func_2(l_2)
for i in range(hash_func.list_size):
    print(i, end=" ")
    print(hash_func.the_list[i])

# print("Find Primes")
# for i in range(500):
#     if hash_func.is_prime(i):
#         print(i)

hash_func.increase_list_size(60)
for i in range(hash_func.list_size):
    print(i, end=" ")
    print(hash_func.the_list[i])
