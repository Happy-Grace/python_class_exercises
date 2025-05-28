# Write a program which repeatedly reads numbers until the user enters 'done'.
# Once 'done' is entered, print out the total, count and average of the numbers.
# If the user enters anything other than a number,
    # detect their mistake using try...and...except; and print an error message and skip to the next number.


print("Enter set of numbers to calculate the total, count and average.")
print("Once you are done, enter the word 'done' to exit.")
print("")

count = 0
total = 0

#inpVal = ("Enter a number: \t")

while (True):
    inpVal = input("Enter a number: ")

    if inpVal == "done":
        break

    try:
        num = float(inpVal)
    except:
        print("Invalid Input (enter a number or 'done' to exit.): ")

        continue
    total = total + num
    count = count + 1

averageVal = total / count

print("")
print("Total: ", total, "\n")
print("Count: ", count, "\n")
print("Average: ", round(averageVal, 4), "\n")

print()


# SOLUTION FROM THE TEACHER
'''
tot = 0
counts = 0

inp = input("Enter a number: ")
while True:
    #inp = input("Enter a number: ")

    if inp == "done":
        break

    try:
        value = float(inp)
        len(value) <= 5

    except:
        print("Invalid Input (enter a number or 'done' to exit.): ")

        continue
    tot = tot + value
    counts = counts + 1

average = tot / counts

'''

