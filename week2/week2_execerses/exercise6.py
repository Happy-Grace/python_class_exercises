"""
Write a program that counts the number of times a specified letter appears in a string using a function named count
and generalize it so that it accepts the string and the letter as arguements.

Executing the program will look as follows:

Enter a string: Banana
Enter character: a

a appears in banana 3 times.
"""

def count(stringInp, charInp):
    stringInp = input("Enter a String: ")
    charInp = input("Enter character: ")

    num = 0
    for x in range(len(stringInp)):
        line = stringInp.lower()
        char = charInp.lower()
        # x = 0
        if line[x] == char:
            num += 1

    if num == 1:
        print(f"The character '{charInp}' appears in the string '{line}' {num} time.")
    elif num == 0:
        print(f"The character '{charInp}' does not seem to appear in the string '{line}'.")
    else:
        print(f"The character '{charInp}' appears in the string '{line}' {num} times.")

count(stringInp="", charInp="")
