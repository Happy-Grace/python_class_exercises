"""
Write a while loop that starts at the last character in the string and works its way backwards
to the first character in the string, printing each letter on a separate line, except backwards.

Hint:
    e.g: use the give statement to reverse the string: name="Hello World"[::-1].
"""


"""
Compared to 'exercise5.py' file:
This is another way of executing the program were it continually prompts and prints backwards until the user exits the code.
To terminate this, you enter the word "exit" (without minding the case-format: lower or upper-cased).
"""
while ("True"):
    line = input("Enter a string of characters, i.e. a statement/sentence: ")
    reversedLine = line[::-1]

    print(f"\nThe statement is {line}\n")

    num = 0

    if line.lower() == "exit":
        exit()

    else:
        while (num < len(reversedLine)):
            print(reversedLine[num])
            num += 1