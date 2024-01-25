n = int(input())  # Read the number of input lines
output = set()  # Create an empty set to store unique email domains
while n != 0 :  # Continue the loop until all input lines are processed
    k = input()  # Read each input line
    n -= 1  # Decrement the counter for the remaining input lines
    import re  # Import the regular expression module
    m = re.findall("@[A-Za-z]+.[A-Za-z]+",k)  # Use regular expression to find email domains in the input line
    for x in m:  # Iterate through the list of email domains found
        output.add(x[1:])  # Add the domain (excluding the '@' symbol) to the set
output = list(output)  # Convert the set to a list
output.sort()  # Sort the list of unique email domains
for item in output:  # Iterate through the sorted list
    print(item)  # Print each unique email domain
