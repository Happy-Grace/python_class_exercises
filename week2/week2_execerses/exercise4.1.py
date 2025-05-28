# Write a program that prompts for a list of numbers and at the end prints out both the max and min of the numbers.
# This program is works for both float and integer values

myList = []

while ("True"):

    inp = input("Please enter a number: ")

    if inp.lower() == "done": #The lower() function helps convert any input into a lowercase e.g. from "Done" to "done"
        break

    else:
        try:
            value = float(inp)
            myList.append(value)

        except:
            print("Invalid input! Enter an number (e.g: 12, 1.39 etc.)!")


minVal = None # OR = None
maxVal = None # OR = None

"""
Note: It's better to use 'None', as when i tried with the index of zero,
        it caused an error if the user does not input a number value and 
        straight up terminates the program with 'done'.
"""

if myList:
    for i in myList:
        if minVal is None or i < minVal:
            minVal = i
        elif maxVal is None or i > maxVal:
            maxVal = i
            # print(i)
else:
    print("\nNo number(s) entered!.")

print(f"\nList of values: {myList}")
print(f"Maximum Number: {maxVal}")
print(f"Minimum Number: {minVal}")