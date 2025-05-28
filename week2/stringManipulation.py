# Write a Python program  to prompt any statement with punctuation characters,
# print the statement after removing all the punctuation characters in lower case by separating individual words

import string
from string import whitespace

print("Below are the punctuation characters that can be used in a string: ")
print(string.punctuation)

wordInput = input("Enter any statement with punctuation: ")

# Create a dictionary of string punctuation characters:
punctDict = str.maketrans("", "",string.punctuation)

print("")
print("Below is the statement you have entered that contains punctuation: ")
print(wordInput)
print("")

print("Statement after all punctuation characters has been removed:")
wordInput = wordInput.translate(punctDict)
print(wordInput)
print("")

print("All characters converted into lower case: ")
wordInput = wordInput.lower()
print(wordInput)
print("")

print("Each characters are split; separating individual characters:")
newWord = wordInput.split()
print(newWord)

