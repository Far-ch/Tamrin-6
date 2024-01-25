def sum_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)  # Find all the divisors of n and store them in a list
    return sum(divisors)  # Return the sum of the divisors


def base_conversion(a, b):
    L = []
    while a != 0:
        L.append(a % b)  # Calculate the remainder when a is divided by b and store it in a list
        a = a // b  # Update the value of a by integer division
    L.reverse()  # Reverse the list of remainders
    s = ''
    for i in L:
        s = s + str(i)  # Convert each remainder to a string and concatenate it to form the converted number
    s = int(s)  # Convert the concatenated string back to an integer
    return s  # Return the converted number


inputs = []  # Initialize an empty list to store converted numbers
flag = 0  # Initialize a flag variable to check for invalid base
while True:
    n, b = map(int, input().split())  # Read input values for n and b
    if n == -1 and b == -1:
        break  # If n and b are both -1, exit the loop
    elif 2 <= b <= 9:
        converted_num = base_conversion(sum_divisors(n), b)  # Calculate the converted number using sum of divisors and base
        inputs.append(converted_num)  # Add the converted number to the list of inputs
    else:
        flag = 1  # Set the flag to 1 if the base is invalid

if flag == 1:
    print("invalid base!")  # If the flag is set to 1, print "invalid base"
else:
    print(sum(inputs))  # Print the sum of all converted numbers
