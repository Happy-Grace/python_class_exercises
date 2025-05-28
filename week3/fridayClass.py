# 21th Feb, 2025 FRIDAY CLASS

# SEARCHING THROUGH FILES USING PYTHON


#1 Search Using if....and....startswith

file = open('C:\\Users\\iakuw\\PycharmProjects\\PythonClass\\mbox.txt')

# for x in file:
#     if x.startswith("From:"):
#         print(x)
# quit()


#2 Searching Using find() Function
# for i in file:
#     i.rstrip()# the rstrip() prints the info in the same format it's stored
#     if i.find("@gmail") == -1:
#         continue
#     print(i)
#
#
# # OR Using the lstrip() Function
# for i in file:
#     i.lstrip()# the rstrip() prints the info with spaces, not in the same format it is stored in the file
#     if i.find("@gmail") == -1:# You can use index[-1] or index[0].
#         continue
#     print(i)


# for i in file:
#
#     if i.find("@gmail") == -1:
#         i.rstrip()  # the rstrip() prints the info in the same format it's stored
#         continue
#     print(i)


#3 Searching for a File by prompting the user for a filename.

# fileDoc = input("Enter your file name(e.g: file.txt): ")
# files = open(fileDoc)
#
# count = 0
#
# for line in files:
#     if line.startswith("From:"):
#         count = count + 1
#
# print(f"There are {count} 'From:' lines in {fileDoc}")

# NOTE: The file have to be available in whichever directory you are calling it
# I first ran the user prompt and the 'mbox.txt' file didn't exist, I had to copy the file into this directory
# The whatever error I encountered previously was fixed and the program ran successfully.


# WRITING INTO A FILE

doc = open("testDoc.txt", "w")

line = "This is a new file \n Welcome to File Handling in Python Class."

print(doc.write(line))# It prints out the total number of characters in the file.

count = 0
for x in line:
    if x[0:] != "":

        count = count + 1
    print(x[0:])



# HANDLING EXCEPTIONS IN PYTHON USING try...except...and/or...else