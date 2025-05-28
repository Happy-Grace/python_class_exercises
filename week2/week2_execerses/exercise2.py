# Calculating Pay via working pay rate per hours.

# Prompt the user for the hours and rate

while (True):
    try:
        hours = float(input("Enter hours: "))
        print("")
        rate = float(input("Enter rate: "))
        print("")

        pay = hours * rate

        print("Hours: %.3f hrs.\n " %hours)
        print(f"Rate: {rate}\n")
        print(f"Total Pay: $%.3f.\n" %pay)

        break
    except ValueError:
        print("Error, please enter a numeric input!.")