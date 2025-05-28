"""
Write a program to prompt for a file name, then read through the file and look for lines of the form:
'X-DSPAM-Confidence: 0.8475'

When you encounter a line that starts with 'X-DSPAM-Confidence:' pull apart the line to extract the floating-point
number on the line. Count these lines and then compute the total of the spam confidence values from these lines.
When you reach the end of the file, print out the average spam confidence.

For Example,

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
"""

inp = input("Enter the file name (e.g: file.txt): ")



try:
    file = open(inp)

    count = 0
    total = 0
    for line in file:
        if line.startswith("X-DSPAM-Confidence:"):
            if len(line) != 2:
                count += 1
                line = line.split()
                num = float(line[1])
            total += num

    avg = total / count

    print("")
    print(f"Average spam confidence: {avg}")
    print(f"Average spam confidence: ~ %.12f" %avg)

except:
    print("The file does not exist or cannot be found in this directory.")