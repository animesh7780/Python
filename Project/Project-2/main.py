import random


guess = random.randint(1, 100)
a= -1
guesses = 0

while(a!=guess):
    guesses = guesses + 1
    a = int(input("Guess a number between 1 and 100:"))
    if(a<guess):
        print("Too low")
    elif(a>guess):
        print("Too high")
        
print("You got it in ", guesses, "guesses")
        