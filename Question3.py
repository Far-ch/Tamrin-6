import re  # Import the regular expression module

a = input()  # Read the input text
a = re.sub(r' +', ' ', a.strip())  # Remove extra spaces and strip leading/trailing spaces
a = re.sub(r"\\n", "\n", a)  # Replace escaped newline characters with actual newline
b = list(a)  # Convert the formatted text into a list of characters
c = []  # Create an empty list to store the modified text
flag = 0  # Initialize a flag to track special characters

for i in b:  # Iterate through the characters in the input text
    if i == '@':  # Check if the character is '@'
        c.append(i)  # Add '@' to the modified text
        flag += 1  # Increment the flag to indicate the presence of '@'
    elif i == '#' and flag > 0:  # Check if the character is '#' and '@' was encountered before
        flag -= 1  # Decrement the flag to indicate the end of special sequence
    else:
        c.append(i)  # Add the character to the modified text

result = ''  # Initialize an empty string to store the final result

for i in c:  # Iterate through the modified text
    result += i  # Concatenate each character to the final result

print("Formatted Text: ", result)  # Print the formatted text
