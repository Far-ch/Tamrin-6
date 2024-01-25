# Read input values for a and b
a, b = map(int, input().split(" "))

# Initialize a variable to count the non-prime numbers
c = 0

# Check if both a and b are greater than 1
if a > 1 and b > 1:
    # Check if a is less than or equal to b
    if a <= b:
        # Loop through the range from a to b (inclusive)
        for i in range(a, b + 1):
            # Check if i is a prime number
            for j in range(2, i):
                if i % j == 0:
                    c += 1  # Increment the count if i is not prime
                    break
        # Print the result for main order
        print("main order - amount: " + str(b - a - c + 1))
    else:
        # Loop through the range from b to a (inclusive)
        for i in range(b, a + 1):
            # Check if i is a prime number
            for j in range(2, i):
                if i % j == 0:
                    c += 1  # Increment the count if i is not prime
                    break
        # Print the result for reverse order
        print("reverse order - amount: " + str(a - b - c + 1))

# Check other specific cases
elif a == 0 and b == 1:
    print("main order - amount: ", 0)

elif a == 1 and b == 0:
    print("reverse order - amount: ", 0)

elif a == 1 or b == 1:
    # Similar logic as above, but without adding 1 to the result
    if a <= b:
        for i in range (a, b + 1):
            for j in range (2, i):
                if i % j == 0:
                    c += 1
                    break
        print("main order - amount: " + str(b - a - c))
    else:
         for i in range (b, a + 1):
            for j in range( 2, i):
                if i % j == 0:
                    c += 1
                    break
         print("reverse order - amount: " + str(a - b - c ))    

elif a == 0 or b == 0:
    # Similar logic as above, but subtracting 1 from the count
    if a <= b:
        for i in range (a, b + 1):
            for j in range (2, i):
                if i % j == 0:
                    c += 1
                    break
        print("main order - amount: " + str(b - a - c-1))
    else:
         for i in range (b, a + 1):
            for j in range (2, i):
                if i % j == 0:
                    c += 1
                    break
         print("reverse order - amount: " + str(a - b - c-1))  

