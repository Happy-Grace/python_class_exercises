# 19th Feb, 2025.

#import string

# TRIAL

a = "Hello"

print("H" in a)


fruit1 = "Apple"
fruit2 = "apple"

print(fruit1 != fruit2)

i = 0
while i < len(a):
    print(a[i])
    i = i + 1


print("")
print("")


for x in range(0, len(a)):
    print(a[x])

print("")
print("")

# FORMAT OPERATOR
num = 20.7864346900
word = "There are %.4f people inside the flat" %num

print(word)

sweet = 20.7864346900
line = "There are %d sweets in the jar" %sweet

print(line)


# STRING MANIPULATION CLASSWORK
#First, we import the string methods to guide the users and get the punctuations found in a string


import  string

print("Below are the punctuation characters that can be used in a string: ")
print(string.punctuation)
print("")

# Prompt the user for the statement

word = input("Enter any statement(s) with punctuation: ")