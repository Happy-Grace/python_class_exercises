fhand = open("mbox.txt", "r")


try:

    count = 0

    print(f"The emails will be separated from the 'From' statement.\n")
    for line in fhand:
        count += 1
        words = line.split()

        # print(f"Debug: {words}")

        if len(words) == 0:
            continue
        if words[0] != "From:":
            continue
        print(f"Email: {words[1]}")
    print("")
    print(f"The total number of emails are {count}.")


        #This is incorrect as words having been split has the length of two items (indexes of 0 and 1)

except:
    print("Check through, your code properly to print the correct info\nThe list 'words' has a len of 2 items")