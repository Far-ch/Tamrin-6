def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Calculate the greatest common divisor using Euclid's algorithm
    return a  # Return the greatest common divisor


def lcd(a, b):
    return a * b / gcd(a, b)  # Calculate the least common multiple using the formula a * b / gcd(a, b)


def inputs():
    numbers = []  # Initialize an empty list to store input numbers
    while True:
        m = input()  # Read input from the user
        if m == "end":
            break  # If the input is "end", exit the loop
        else:
            number = int(m)  # Convert the input to an integer
            numbers.append(number)  # Add the number to the list of input numbers
    return numbers  # Return the list of input numbers


k = input()  # Read input value for k
if k == "sum":  # If k is "sum", calculate and print the sum of input numbers
    numbers = inputs()  # Get input numbers from the user
    print(sum(numbers))  # Print the sum of input numbers


elif k == "average":  # If k is "average", calculate and print the average of input numbers
    numbers = inputs()  # Get input numbers from the user
    average = sum(numbers) / len(numbers)  # Calculate the average of input numbers
    print(round(average, 2))  # Print the average rounded to two decimal places


elif k == "max":  # If k is "max", find and print the maximum of input numbers
    numbers = inputs()  # Get input numbers from the user
    print(max(numbers))  # Print the maximum of input numbers


elif k == "min":  # If k is "min", find and print the minimum of input numbers
    numbers = inputs()  # Get input numbers from the user
    print(min(numbers))  # Print the minimum of input numbers


elif k == "gcd":  # If k is "gcd", calculate and print the greatest common divisor of input numbers
    numbers = inputs()  # Get input numbers from the user
    x = numbers[0]  # Initialize x with the first number in the list
    for i in range(1, len(numbers)):
        x = gcd(x, numbers[i])  # Calculate the greatest common divisor iteratively
    print(x)  # Print the greatest common divisor


elif k == "lcd":  # If k is "lcd", calculate and print the least common multiple of input numbers
    numbers = inputs()  # Get input numbers from the user
    x = numbers[0]  # Initialize x with the first number in the list
    for i in range(1, len(numbers)):
        x = lcd(x, numbers[i])  # Calculate the least common multiple iteratively
    print(int(x))  # Print the least common multiple as an integer


else:
    print("Invalid command")  # If k is not one of the valid commands, print an error message
