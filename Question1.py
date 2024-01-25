# Input two numbers
a = int(input())
b = int(input())
# Calculate the XOR of the two numbers
c = a ^ b
d = str(bin(c))
# Initialize a count to keep track of the set bits
x = 0
# Count the set bits in the XOR result
for i in d:
    if i == '1':
        x += 1
#print the number of bits to change
print(x)



