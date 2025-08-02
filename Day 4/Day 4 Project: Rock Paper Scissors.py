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

game_image = [rock, paper, scissors]

import random

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
if user >= 0 and user <= 2:
    print(game_image[user])

computer = random.randint(0, 2)
print("Computer chose: ")
print(game_image[computer])

if user >= 3 or user < 0:
    print("You typed a wrong number. You lose!")
elif user == computer:
    print("It's a Draw")
elif user == 0 and computer == 1:
    print("You lose!")
elif user == 1 and computer == 0:
    print("You win!")
elif user == 1 and computer == 2:
    print("You lose!")
elif user == 2 and computer == 1:
    print("You win!")
elif user == 2 and computer == 0:
    print("You lose!")
elif user == 0 and computer == 2:
    print("You win!")
