# FRIDAY: 14th Feb. 2025

# while True:
#     line = input("Enter a word: ")
#     if line[0] == "#":
#         break
#     if line == "done":
#         continue
#     print(line)


# classNames = ["Mimi", "James", "Lili", "Lily"]
#
# for x in classNames:
#     print("Greetings: ", x)
#
#     if "Mary" not in classNames:
#         continue
#     else:
#         print("Welcome everyone, we still don't have a new student amongst us.")


largest = None

num = [3, 41, 12, 9, 74, 15]
for x in num:
    if largest is None or x > largest:
        largest = x
        #print(largest)
print("The largest number is: ", largest)