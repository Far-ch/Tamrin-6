a = input().split()  # Read input and split it into a list of strings
a.sort(key = lambda x:int(x[1:]))  # Sort the list based on the numerical value of the characters from index 1 to the end of each string
for x in a:  # Iterate through the sorted list
    print(x[0], end = "")  # Print the first character of each string without a newline
