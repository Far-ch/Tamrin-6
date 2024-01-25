a = input().split()  # Read a line of space-separated numbers and split them into a list
b = int(input())  # Read an integer input
dict_a = {}  # Create an empty dictionary to store the index of each number in the input list

for i, x in enumerate(a):  # Iterate through the elements of the input list along with their index
    dict_a[int(x)] = i  # Add the number as key and its index as value to the dictionary

dict_m = {}  # Create an empty dictionary to store the sum of indices for pairs that add up to b

for j in dict_a.keys():  # Iterate through the keys (numbers) in the dictionary
    y = b - j  # Calculate the difference between b and the current number
    if y in dict_a and y != j:  # Check if the difference exists in the dictionary and is not the same as the current number
        d = dict_a[j] + dict_a[y]  # Calculate the sum of indices for the pair (j, y)
        if (y, j) not in dict_m.keys():  # Check if the pair (y, j) is not already added to the result
            dict_m[(j, y)] = d  # Add the pair (j, y) as key and its sum of indices as value to the dictionary

if not dict_m:  # If no pair is found that adds up to b
    print("Not Found!")  # Print "Not Found!"

else:  # If pairs are found
    for i in sorted(dict_m.values()):  # Iterate through the values (sum of indices) of the dictionary in sorted order
        print(i)  # Print the sum of indices for each pair
