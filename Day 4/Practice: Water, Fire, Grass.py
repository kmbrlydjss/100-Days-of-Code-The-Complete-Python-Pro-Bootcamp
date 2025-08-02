water = '''
     ▒▒▒▒▒▒
---'  ▒▒▒▒▒▒))
     ▒▒▒▒▒▒))
    ▒▒▒▒▒▒▒))
    ▒▒▒▒▒▒▒)
---.__(____))
'''
fire = '''
     (  .      )
---'  )  ) )   )🔥
     (  ( . )🔥 )
    (   )  .  )🔥
     )🔥 (  ( . ) 
---.__(____🔥__)
'''
grass = '''
     ,--./,-.
---' /     🌿  \\
     |   🌿🌿   |
     \\   🌿   /
      `._,._.'
---.__(______)
'''

game_image = [water, fire, grass]

import random

user = int(input("What do you choose? Type 0 for Water, 1 for Fire or 2 for Grass "))
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
    print("You win!")
elif user == 1 and computer == 0:
    print("You lose!")
elif user == 1 and computer == 2:
    print("You win!")
elif user == 2 and computer == 1:
    print("You lose!")
elif user == 2 and computer == 0:
    print("You win!")
elif user == 0 and computer == 2:
    print("You lose!")
