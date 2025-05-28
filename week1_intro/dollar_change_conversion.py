from math import floor

# Coins: 20 dollars, 5 dollars, 1 dollar. 25 cents, 10 cents and 1 cent

# Input: charge in $
# Output: breakdown in bills and coins

# THE DOLLAR COUNTING SYSTEM
# Penny => 1 cent (1/100th of a dollar: $0.01)
# Nickel => 5 cents (1/20th of a dollar: $0.05)
# Dime => 10 cents (1/10th of a dollar: $0.10)
# Quarter => 25 cents (1/4th of a dollar: $0.25)

#Two ways of solving this problem: floor division and modulus (%) operator method

# Modulus (%) Operator Method:
chargeInput = input("Enter the charge (in dollars)?: \t")
floatInput = float(chargeInput)


# Floor Division Method:
print("Twenties")
resultOutput = floor((floatInput / 20))
print(format(resultOutput, ".4f"))


print("Twenties")
resultOutput = (floatInput - (floatInput % 20)) / 20
print(format(resultOutput, ".4f"))
print("\n")


# Carrying out operation using the modulus (%) method

print("Fives")
resultOutput = (floatInput - (floatInput % 5)) / 5
print(format(resultOutput, ".4f"))
print("\n")


print("Ones")
resultOutput = (floatInput - (floatInput % 1)) / 1
print(format(resultOutput, ".4f"))
print("\n")


print("Quarters")
resultOutput = (floatInput - (floatInput % .25)) / .25
print(format(resultOutput, ".4f"))
print("\n")


print("Dimes")
resultOutput = (floatInput - (floatInput % .10)) / .10
print(format(resultOutput, ".4f"))
print("\n")


print("Pennies")
resultOutput = (floatInput - (floatInput % .01)) / .01
print(format(resultOutput, ".4f"))
print("\n")
