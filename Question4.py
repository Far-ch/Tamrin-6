n = int(input())  # Read input for the size of the grid
List = ["."] * n  # Create a list of dots of length n
list = []  # Initialize an empty list to store the grid
list.extend([List.copy()])  # Add a copy of the list of dots to the grid
a = 0  # Initialize a variable to track the horizontal position
b = 0  # Initialize a variable to track the vertical position
list[0][0] = "*"  # Set the initial position in the grid as "*"

while True:
    m = input()  # Read input for the movement command
    if m == "END":
        break  # If the input is "END", exit the loop
    if m == "B":
        list.extend([List.copy()])  # Add a copy of the list of dots to the grid to create a new row
        b += 1  # Update the vertical position
    elif m == "L" and a != 0:
         a -= 1  # Move left if possible
    elif m == "R" and a < (n - 1):
        a += 1  # Move right if possible
    list[b][a] = "*"  # Set the current position in the grid as "*"

for item in list:
    print(*item)  # Print each row of the grid

if a != (n - 1):
    print("There's no way out!")  # If the final position is not at the rightmost edge, print "There's no way out!"
