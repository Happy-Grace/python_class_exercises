"""
Write a program to read through a file and print the contents of the file (line by line) all in upper case.

Test your file on mbox-short.txt files.
"""

#Prompt the user to enter the file name
inp = input("Enter the file name (e.g: file.txt): ")

try:
    file = open(inp)

    for line in file:
        line = line.rstrip()
        doc = line.upper()
        print(doc)
except:
    print("The file doc does not exist or cannot be found in this directory.")