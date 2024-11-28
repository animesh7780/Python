import random

def game():
    print("Welcome to the game")
    score = random.randint(1, 62)
    with open("hi-score.txt") as f:
        high_score = f.read()
        if(high_score!=""):
            high_score = int(high_score)
        else:
            high_score = 0
    print(score)
    if(score > high_score or high_score == 0):
        with open ("hi-score.txt", "w") as f:
            f.write(str(score))
    return score

game()