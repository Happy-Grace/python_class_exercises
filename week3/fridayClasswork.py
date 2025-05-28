
inp = input("Enter your file name (e.g: file.txt): ")



print("")

try:
    file = open(inp)
    count = 0

    for x in file:

        if x.startswith("Subject:"):
            count = count + 1
    print(f"There are {count} subject lines in {inp} file document.\n")
except:
    print(f"File cannot be opened: {inp}\n")
