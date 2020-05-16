# In this video we will focus on avoiding clustering
# Since each time we have a collision we just move
# down 1 index that causes large clusters of data.
# The more collisions we have increases the odds of
# more collisions. That is why we'll have both large
# empty parts as well as large clusters in our lists.

class HashFunctions:
    def __init__(self, size):
        self.list_size = size
        self.the_list = []
        for i in range(size):
            self.the_list.append("-1")

    # Let'd change our hash function to avoid
    # cluster creation
    # We will do this by creating a double hash
    def dbl_hash_func(self, str_list):
        for k in str_list:
            str_int = int(k)
            index = str_int % 61
            # Look for a collision and if found go to the next available
            # This is bad because it causes clustering.
            # We can avoid that by changing the step distance
            # using a prime number.
            # That step will be between 1 and 7
            # If this list was very large you will see much more clustering
            step_distance = 7 - (int(self.the_list[index]) % 7)

            while self.the_list[index] != "-1":

                # Replace this
                # index += 1
                # with this
                index += step_distance

                # At end of list -> go to index 0
                index %= self.list_size
            # We have a place to store
            self.the_list[index] = k
            self.print_list()
            print()

    def print_list(self):
        # Used to print each row of columns 10 at a time
        increment = 0
        # I want to allow for 10 columns per row
        num_of_rows = int((self.list_size / 10) + 1)
        for j in range(num_of_rows):
            self.print_line(78)
            # Get the next row of columns to print
            increment += 10
            # Print a row of indexes and then a row of data
            self.print_row(increment, False)
            self.print_line(78)
            self.print_row(increment, True)
        self.print_line(78)

    # Print a horizontal line for the table
    def print_line(self, num_of_lines):
        for l in range(num_of_lines):
            print("-", end="")
        print()

    # Used to print indexes and data for the table
    # Receives the row of data to print and whether it is data
    # or indexes
    def print_row(self, increment, is_data):
        k = increment - 10
        while k <= increment:
            # If past the end of the array print blank spaces
            if k > self.list_size - 1:
                print("|     ", end=" ")
            else:
                if not is_data:
                    # Print value with 3 spaces and right justify
                    # Print index numbers
                    print("| {:>3} ".format(k), end=" ")
                else:
                    # Print list data values or nothing if -1
                    if self.the_list[k] == "-1":
                        print("| {:>3} ".format(" "), end=" ")
                    else:
                        print("| {:>3} ".format(self.the_list[k]), end=" ")
            k += 1
        print("|")

    # Now we need to update our find function using double hashing
    def find_key(self, key):
        # Use the same formula used to store the value
        list_index_hash = int(key) % 61

        # NEW Add this to calculate step distance
        step_distance = 7 - (int(self.the_list[list_index_hash]) % 7)

        # Cycle through our list looking for the value and
        # then return the index
        while self.the_list[list_index_hash] != "-1":
            if self.the_list[list_index_hash] == key:
                print(f"{key} in Index {list_index_hash}")
                return self.the_list[list_index_hash]

            # NEW We change this
            # list_index_hash += 1
            # to this
            list_index_hash += step_distance

            # If we get to the end of the list go to index 0
            list_index_hash %= self.list_size

        # If we are here that means we couldn't find it
        return False


l_2 = ["100", "510", "170", "214", "268", "398",
              "235", "802", "900", "723", "699", "1", "16",
              "999", "890", "725", "998", "990", "989", "984",
              "320", "321", "400", "415", "450", "50", "660", "624"]

hash_func = HashFunctions(61)
hash_func.dbl_hash_func(l_2)
hash_func.find_key("170")








