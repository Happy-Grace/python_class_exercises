# PART 1: Increment by 1
# Print out the asterisk symbol in patterns with the increment of 1.


for i in range(1, 7):
    sym = ""
    for j in range(0, i):
        sym = sym + "*"
    print(sym)


print("")
print("")




# PART 2: Decrement by 1
# Print out the asterisk symbol in patterns with the decrement of 1.

for i in range(1, 7):
    output = ""
    for j in range(0, 7-i):
        output = output + "*"
    print(output)

print("")
print("")

# PART 3: Doubles if divisible by 2
# Print out the asterisk symbol in patterns is an even number .

for i in range(1, 7):
    pattern = ""
    for j in range(0, i):
        pattern = pattern + "*"
    if (i % 2 == 0):
        pattern = pattern + len(pattern) * "*"
    print(pattern)

print("")
print("")


# PART 4: The vice versa/ inverted version of Part 3.
# Print out the asterisk symbol in patterns inverted of Part 3 challenge .

for i in range(1, 7):
    word = ""
    for j in range(0, 7-i):
        word = word + "*"
    if (i % 2 == 0):
        word = word + len(word) * "*"
    print(word)

print("")
print("")
