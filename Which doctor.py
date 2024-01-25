a = int(input())
b = int(input())
c = a ^ b
d = str(bin(c))
x = 0
for i in d:
    if i == '1':
        x += 1
print(x)



