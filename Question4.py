import re

# Define a function named Word with parameters: difference, Sentence, Word
def Word(difference, Sentence, Word):
    # Initialize an empty list to store special words
    Sp_words = []

    try:
        # Remove specified characters [.:ØŒ] from the Sentence using regular expression
        Sentence = re.sub('[.:ØŒ]', '', Sentence)
    except:
        pass
    finally:
        # Split the Sentence into a list of words
        Words = Sentence.split()

        # Iterate through each word in the Sentence
        for i in Words:
            # Check if the length of the current word is within the allowed difference range
            if len(i) > len(Word) + difference or len(i) < len(Word) - difference:
                continue

            # Calculate the count of differing characters between the current word and the target word
            count = sum(1 for j in zip(i, Word) if j[0] != j[1])

            # Add the absolute difference in length between the two words to the count
            count += abs(len(i) - len(Word))

            # Check if the count is within the specified difference
            if count <= difference:
                # If so, add the current word to the list of special words
                Sp_words.append(i)

        # Print each special word
        for item in Sp_words:
            print(item)

# Read an integer value from the user
x = int(input())

# Read a Sentence from the user
y = input()

# Read a Word from the user
z = input()

# Call the Word function with the provided inputs
Word(x, y, z)
