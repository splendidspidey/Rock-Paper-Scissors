from random import randint
choice = ["Rock", "Paper", "Scissors"]
computer = choice[randint(0,2)]
player = False
while player == False:
    player = input("Rock, Paper or Scissors? ")
    if player == computer:
        print("Haha, You played the same move!")
    elif player == "Rock":
        if computer == "Paper":
            print("Welp, You lost!", computer, "covers", player)
        else:
            print("Woohoo, You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("Welp, You lose!", computer, "cut", player)
        else:
            print("AYYY, You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("Nice one, You win!", player, "cut", computer)
    else:
        print("Are you sure you entered that correctly...")
    player = False
    computer = choice[randint(0,2)]
