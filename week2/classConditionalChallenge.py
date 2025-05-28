# Class Challenge

# timeInp = float(input("Enter time in 24hrs format (between 0 - 24, e.g 1pm - 13): \t"))
#
# if (timeInp >= 0 and timeInp < 13):
#     print("Good Morning")
# elif (timeInp >= 13 and timeInp < 17):
#     print("Good Afternoon")
# elif (timeInp >= 17 and timeInp < 21):
#     print("Good Evening")
# elif (timeInp >= 21 and timeInp <= 24):
#     print("Good Night")
# else:
#     print("Wrong Input")


# CLASS PRACTICE
# import math


# x = 20.4
# y = str(x)
# p = math.ceil(x)
#
# print(p)
#
# print(y)
#
# z = y + "New"
# print(z)

def chop(list1):
    list1.pop(0)
    list1.pop()

def middle(list1):
    del list1[1:-1]
    return list1



list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

chop(list1)
print(list1)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list1_1 = middle(list1)
print(list1_1)

