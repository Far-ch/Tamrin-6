n = int(input())  # Read input value for n
m = int(input())  # Read input value for m
k = int(input())  # Read input value for k

while m:  # Start a while loop with condition m
    carry = n & m  # Calculate the bitwise AND of n and m and store it in carry
    n = n ^ m  # Calculate the bitwise XOR of n and m and update the value of n
    m = carry << 1  # Left shift the value of carry by 1 and update the value of m

print(n)  # Print the final value of n after the while loop

if n == k:  # Check if the final value of n is equal to k
    print("YES")  # Print "YES" if n is equal to k
else:
    print("NO")  # Print "NO" if n is not equal to k
