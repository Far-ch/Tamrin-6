# Read input values for a, b, and c
a = int(input())  # Assuming a is a 32-bit integer
b = int(input())  # Assuming b is a 32-bit integer
c = int(input())

# Loop c times to process additional inputs
while c:
    d = int(input())  # Read the value of d
    if d <= 31:
        # Check if the d-th bit of a is set
        if a & (1 << d):
            print("yes")  # Print "yes" if the bit is set
        else:
            print("no")   # Print "no" if the bit is not set
    else:
        # Check if the (d-32)-th bit of b is set
        if b & (1 << (d - 32)):
            print("yes")  # Print "yes" if the bit is set
        else:
            print("no")   # Print "no" if the bit is not set
    c -= 1  # Decrement the loop counter
