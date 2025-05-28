"""
Write a program to open any text file and read it line by line. For each line, spilt the line into list of words
using the split function. For each word, check to gsee if the word is already in a list. If the word is not in the
list, add it to the list.

When the program completes, sort and print the resulting words in alphabetical order.
"""

inp = input("Enter file (e.g: file.txt): ")

file = open(inp)

for line in file:
    line.rstrip()
    line = line.split()
    print(line)