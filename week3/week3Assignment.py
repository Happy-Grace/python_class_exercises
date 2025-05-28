# FILE

inp = input("Enter the file name (e.g: file.txt): ")



if inp == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!.")
    exit()

try:
    file = open(inp)

    count = 0
    for x in file:
        if x.startswith("Subject:"):
            count = count + 1
    print(f"There are {count} subject lines in {inp} document.\n")

except:
    print(f"File cannot be opened: {inp}")



