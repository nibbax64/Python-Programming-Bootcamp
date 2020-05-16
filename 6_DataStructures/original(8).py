# In this tutorial I'm going to cover hashing strings

# When hashing strings we convert it into a number.
# We get the character code for each character
# (hash_val * 27 (total number of characters) + char_code)
# % array_size

class HashFunction:
    def __init__(self, size):
        self.list_size = size
        self.the_list = []
        for i in range(size):
            self.the_list.append("-1")

    def hash_string(self, str_to_hash):
        # Holds character hash value
        hash_val = 0
        # Holds sum of character hash values
        hash_sum = 0
        for i in range(len(str_to_hash)):
            # Character code for a is 97 so I'll subtract
            # 96 from it so we can start at 1
            # ord() returns the character code
            char_code = ord(str_to_hash[i]) - 96

            # Temporarily store hash key value
            hkv_temp = hash_val

            # Hash this character like we did before
            hash_sum += (hash_val * 27 + char_code)

        return hash_sum

    def hash_str_list(self, str_list):
        for str_to_hash in str_list:
            # Hash the individual string
            hash_sum = self.hash_string(str_to_hash)
            # Constrain the hash_value to the size of the list
            hash_sum = hash_sum % self.list_size

            # Used to avoid clustering
            step_distance = 7 - (hash_sum % 7)

            # Continue cycling until we find a -1 and then
            # place data there
            while self.the_list[hash_sum] != "-1":
                hash_sum += step_distance
                hash_sum %= self.list_size

            self.the_list[hash_sum] = str_to_hash

    def find(self, value):
        value_index = self.hash_string(value)
        step_distance = 7 - (value_index % 7)

        # Cycle through our list looking for the value and
        # then return the index
        while self.the_list[value_index] != "-1":
            if self.the_list[value_index] == value:
                print(f"{value} in Index {value_index}")
                return self.the_list[value_index]

            value_index += step_distance

            value_index %= self.list_size

            # If we are here that means we couldn't find it
        return False

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


words_to_add = ["ace", "act", "add", "age", "ago", "aid", "aim", "air", "all", "amp", "and", "ant", "any", "ape", "apt", "arc", "are", "ark", "arm", "art", "ash", "ask", "asp", "ate", "atm", "awe", "axe", "aye"]

hash_func = HashFunction(61)
hash_func.hash_str_list(words_to_add)
hash_func.print_list()
hash_func.find("ask")





