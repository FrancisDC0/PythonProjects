import random

print("Welcome to the Rock, Paper, Scissors game!")
userHandSignal = int(input("Select your hand signals by typing 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if  userHandSignal >= 3 or userHandSignal <= -1:
    print("Invalid input. Please try again then type 0 for Rock, 1 for Paper, or 2 for Scissors.")
    exit()
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
userHandSignal = int(userHandSignal)
handSignalList = [rock, paper, scissors]
computerHandSignal = random.randint(0, 2)
print(handSignalList[userHandSignal])
print("Computer chose:")
print(handSignalList[computerHandSignal])
if computerHandSignal == userHandSignal:
    print("It's a draw")
elif computerHandSignal == 0 and userHandSignal == 1:
    print("You win!")
elif computerHandSignal == 0 and userHandSignal == 2:
    print("You lose.")
elif computerHandSignal == 1 and userHandSignal == 2:
    print("You win!")
elif computerHandSignal == 1 and userHandSignal == 0:
    print("You lose.")
elif computerHandSignal == 2 and userHandSignal == 0:
    print("You win!")
elif computerHandSignal == 2 and userHandSignal == 1:
    print("You lose.")
