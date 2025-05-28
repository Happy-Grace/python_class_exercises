# Write a program to accept time in 24hrs and then greet the user.

# Time between 0 - 12: Good Morning
# Time between 13 - 16: Good Afternoon
# Time between 17 - 20: Good Evening
# Time between 21 - 24: Good Night
# Otherwise: Wrong Input


# First, prompt and ask the user for time input, convert it into integer format

name = input("Our beloved user, please enter your name: \t")
timeFormat = int(input("Please enter the time in 24 hrs format (between 0 - 24): \t"))

if 0 <= timeFormat <= 12:
    print("Good Morning " + name + ", WELCOME!!!.")
elif 13 <= timeFormat <= 16:
    print("Good Afternoon " + name + ", WELCOME!!!.")
elif 17 <= timeFormat <= 20:
    print("Good Evening " + name + ", WELCOME!!!.")
elif 21 <= timeFormat <= 24:
    print("Good Night " + name + ", HAVE A GREAT REST!!!.")
else:
    print("Wrong Input!.")
