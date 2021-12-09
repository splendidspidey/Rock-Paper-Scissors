from random import randint
choice = ["Rock", "Paper", "Scissors"]
ai = choice[randint(0,2)]
player = False
while player == False:
    player = input("Rock, Paper or Scissors? ")
    if player == ai:
        print("Haha, You played the same move!")
    elif player == "Rock":
        if ai == "Paper":
            print("Welp, You lost!", ai, "covers", player)
        else:
            print("Woohoo, You win!", player, "smashes", ai)
    elif player == "Paper":
        if ai == "Scissors":
            print("Welp, You lose!", ai, "cut", player)
        else:
            print("AYYY, You win!", player, "covers", ai)
    elif player == "Scissors":
        if ai == "Rock":
            print("You lose...", ai, "smashes", player)
        else:
            print("Nice one, You win!", player, "cut", ai)
    else:
        print("Are you sure you entered that correctly...")
    player = False
    ai = choice[randint(0,2)]
