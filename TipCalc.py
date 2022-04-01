# This simple tip calculator accepts three variables
# Variable 1 is the number of diners.  Variable 2 is
# the total amount for the meal.  Variable 3 is the tip %
#you want to pay.  Upon entering these three variables you
#should receive the amount each person pays.

print("Welcome to ScaerieTale's Tip Calculator!")

groupSize = int(input("How many in the group are paying? "))
# Creates the "groupSize" variable and sets it
# as a number defined by the user.  The int() encapsulating the
# input SHOULD automagically convert the user's input from a string to an integer
# for further mathemagical operations below.

money = float(input("What did your meal cost? "))

tipPercent = float(input("Finally, what percent (as a whole number) do you want to tip? "))

tipAmount = money * (tipPercent / 100)

# print(tipAmount)
# Debugging statement to test that I've written the equation correctly.  We'll fix the
# formatting so that it reads like a normal dollar amount next :)
groupSize = float(groupSize)
# converts groupSize to a floating point decimal so that Python
# can divide the number into the final tally below

finalAmount = "${:,.2f}".format((money + tipAmount) / groupSize)
# The "${:,.2f}".format function converts the final result of the
# equation to a string, and formats it into USD

# print(finalAmount)
# another debugging statement.  We'll pretty it up in a sec once
# I'm confident it's working.

print(f"At a {tipPercent}% tip, each of {groupSize} will pay {finalAmount}.")
print("Thanks for using ScaerieTale's Tip Calculator!")
input("Press 'Enter' to exit.")