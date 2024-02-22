import random
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

man_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choose = random.randint(0,2)
list_choose = [rock, paper, scissors]

if man_choose >= 3 or man_choose < 0:
    print("Error Valid, You lose")
else:
    man_check = (list_choose[man_choose])
    print(f"You chose: \n{man_check}")
    computer_check = (list_choose[computer_choose])
    print(f"Computer chose: \n{computer_check}")

    if man_choose == 0 and computer_choose == 2:
        print("You win")
    elif man_choose == 1 and computer_choose == 0:
        print("You win")
    elif man_choose == 2 and computer_choose == 1:
        print("You win")
    elif man_choose == computer_choose:
        print("You draw")
    else:
        print("You lose")