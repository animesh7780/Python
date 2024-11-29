'''
1 for snake
2 for water
3 for gun
'''
import random
computer = random.randint(1, 3)
user = input("Enter your choice: ")
choice={"snake":1, "water":2, "gun":3}
reverseChoice = {1:"snake", 2:"water", 3:"gun"}
userChoice = choice[user]

print("Computer Choice: ", reverseChoice[computer])
print("User Choice: ", reverseChoice[userChoice])

if computer == userChoice:
    print("Tie")

elif computer == 1 and userChoice == 2:
    print("You Win")

elif computer == 1 and userChoice == 3:
    print("You Lose")

elif computer == 2 and userChoice == 1:
    print("You Lose")

elif computer == 2 and userChoice == 3:
    print("You Win")

elif computer == 3 and userChoice == 1:
    print("You Win")

elif computer == 3 and userChoice == 2:
    print("You Lose")