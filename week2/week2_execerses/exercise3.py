# Calculating Pay via working pay rate per hours.
# Calculates Overwork time and payment for working Overtime

# Prompt the user for the hours and rate



try:
    def computepay(hours, rate):

        if hours > 40:
            overhours = hours - 40
            overwork_pay = overhours * (rate * 1.5)
            regular_pay = rate * 40
            total_pay = regular_pay + overwork_pay

        else:
            total_pay = hours * rate


        return total_pay


except ValueError:
    print("Error, please enter a numeric input!.")


hours = float(input("Enter hours: "))
print("")
rate = float(input("Enter rate: "))
print("")

pay = computepay(hours, rate)

print(f"Gross Pay: ${pay}")