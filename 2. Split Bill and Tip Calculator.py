# Welcome message of the project
print("Welcome to the split bill and tip calculator!")

# Ask the user the details of the bill, tip percentage, and the number of people who will split the bill
totalBill = float(input("What was the total bill? \n₱"))
tipPercentage = int(input("What percentage (%) tip would you like to give? 0 10 12 15\n"))
people = int(input("How many people to split the bill? \n"))

# Backend calculation for the tip amount, final amount to be paid, and the amount to be paid individually after the split
tipAmount = totalBill*(tipPercentage/100)
billPlusTip = totalBill + tipAmount
indPay = billPlusTip / people
indPay = round(indPay, 2)

# Display message showing the breakdown of calculation and the final amount to be paid individually
print(f"The total bill (₱{totalBill}) + {tipPercentage}% tip (₱{tipAmount}) is ₱{billPlusTip}")
print(f"Each person should pay ₱{indPay}")
