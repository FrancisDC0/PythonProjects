# Greeting at the start program.
print("Welcome to the Band Name Generator!")
# Confirmation from the user if they want to proceed.
proceed = input("Shall we proceed? Y/N?\n")
# The following lines will decide whether to create a band name or not based on the answer of the user.
if proceed == "Y" or proceed == "y":
    cityName = input("What is the name of the city you grew up in?\n")
    animalName = input("What is the plural name of your favorite animal?\n")
    print("Your band name could be the " + cityName + " " + animalName +"!")
elif proceed == "N" or proceed == "n":
    print("See you when you need a band name. Thank you!")
else:
    print("Unrecognized response, please try again and answer by typing 'Y' or 'N'. Thank you!")
