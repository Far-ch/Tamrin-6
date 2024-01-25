def khayam_paskal(L):
    # Define a function to generate the next row of Pascal's triangle
    new_list = [1]  # Start with the first element of the new row
    for i in range(len(L)):
        if i == len(L) - 1:
            new_list.append(1)  # Add 1 at the end of the new row
        else:
            new_element = L[i] + L[i+1]  # Calculate the next element in the new row
            new_list.append(new_element)  # Add the new element to the new row
    return new_list  # Return the new row of Pascal's triangle

n = int(input())  # Read input value for n
if n == 1:  # If n is 1, print 1 and exit
    print(1)
elif n == 2:  # If n is 2, print the first two rows of Pascal's triangle and exit
    print('1\n1 1')
else:  # For n greater than 2, print the first two rows of Pascal's triangle
    print('1\n1 1')
    L = [1, 1]  # Initialize the list with the first two elements of Pascal's triangle
    for i in range(2, n):  # Generate and print the next n-2 rows of Pascal's triangle
        L = khayam_paskal(L)  # Generate the next row using the khayam_paskal function
        for item in L:  # Print each element of the new row separated by a space
            print(item, end=" ")
        print()  # Move to the next line after printing all elements of the new row
