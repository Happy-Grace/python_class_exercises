# Program that loops through 100, and prints out the multiple of 4.

numList = []

for i in range(1, 101):
    if i % 4 == 0:
        numList.append(i)

print(numList)

