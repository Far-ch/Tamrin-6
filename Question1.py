import re

# Define a class named Crab
class Crab:
    def init(self, dna):
        # Constructor to initialize the Crab instance with a DNA sequence
        self.build_dna(dna)

    # Method to build DNA by appending the first 10 characters to the end
    def build_dna(self, dna):
        dna_end = dna[0:10]
        self.dna = dna + dna_end

    # Method to display the modified DNA by replacing "tt" with "o"
    def display(self):
        self.dna = self.dna.replace("tt", "o")
        print(self.dna)

# Define a class named Bob that inherits from Crab
class Bob(Crab):
    def init(self, dna):
        # Constructor to call the parent class constructor
        super().init(dna)

    # Method to display the length of the DNA sequence in a sorted order
    def display(self):
        # Convert the length of DNA to a list of digits, sort them, and print the result as a number
        list_of_length = list(map(int, str(len(self.dna))))
        list_of_length = self.merge_sort(list_of_length)
        print(self.list_to_num(list_of_length))

    # Helper method for merge sort
    def merge_sort(self, lst):
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2
        left_list = lst[:mid]
        right_list = lst[mid:]

        left_list = self.merge_sort(left_list)
        right_list = self.merge_sort(right_list)

        return self.merge(left_list, right_list)

    # Helper method for merging two sorted lists
    def merge(self, left_list, right_list):
        sorted_list = []
        left_index = 0
        right_index = 0

        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] < right_list[right_index]:
                sorted_list.append(left_list[left_index])
                left_index += 1
            else:
                sorted_list.append(right_list[right_index])
                right_index += 1

        sorted_list += left_list[left_index:]
        sorted_list += right_list[right_index:]

        return sorted_list

    # Helper method to convert a list of digits to a number
    def list_to_num(self, lst):
        num = 0
        for digit in lst:
            num = num * 10 + digit
        return num

# Define a class named Octopus
class Octopus:
    def init(self, dna):
        # Constructor to initialize the Octopus instance with a DNA sequence
        self.build_dna(dna)

    # Method to build DNA by appending the index of the first occurrence of 'x'
    def build_dna(self, dna):
        idx = self.linear_search(dna)
        if idx != -1:
            self.dna = dna + str(idx)
        else:
            self.dna = dna

    # Helper method for linear search to find the index of the first occurrence of 'x'
    def linear_search(self, dna):
        for i in range(len(dna)):
            if dna[i] == 'x':
                return i
        return -1

    # Method to display the modified DNA by replacing consecutive repeating characters with '(0_0)'
    def display(self):
        pattern = r'(\w)\1{2}'
        print(re.sub(pattern, '(0_0)', self.dna))

# Function to reverse a string
def reverse_string(string):
    return string[::-1]

# Read input from the user
input_string = input()

# Check the conditions and create instances of the appropriate classes
if len(input_string) < 10 or len(input_string) > 1000:
    print('invalid input')
elif input_string[0] == 'm':
    crab = Crab(input_string)
    crab.display()
elif input_string[0] == 's' and input_string[1] == 'b':
    bob = Bob(input_string)
    bob.display()
elif input_string[0] == 's' and input_string[1] != 'b':
    octopus = Octopus(input_string)
    octopus.display()
elif input_string[-1] == 'm':
    crab = Crab(reverse_string(input_string))
    crab.display()
elif input_string[-1] == 's' and input_string[-2] == 'b':
    bob = Bob(reverse_string(input_string))
    bob.display()
elif input_string[-1] == 's' and input_string[-2] != 'b':
    octopus = Octopus(reverse_string(input_string))
    octopus.display()
else:
    print('invalid input')
