"""
Write a while loop that starts at the last character in the string and works its way backwards
to the first character in the string, printing each letter on a separate line, except backwards.

Hint:
    e.g: use the give statement to reverse the string: name="Hello World"[::-1].
"""

inp = input("Enter a string of characters, i.e. a statement/sentence: ")

reversedInp = inp[::-1]

index = 0

print(f"\nThe statement is {inp}\n")

while (index < len(reversedInp)):
    print(f"{reversedInp[index]}")
    index += 1





