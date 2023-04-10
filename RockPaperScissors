import random
import getpass


username = getpass.getuser()

pc_score = 0
player_score = 0

print("")
print("First to 3 wins!!!")
print("")
print("1.Rock")
print("2.Paper")
print("3.Scissors")

while player_score != 3 and pc_score != 3:
    n = input()
    rand = random.randint(1, 3)

    if n == "1" and rand == 1:
        print("COMPUTER played ROCK")
        print("DRAW")
    if n == "1" and rand == 2:
        print("COMPUTER played PAPER")
        print("+ 1 point for the COMPUTER")
        pc_score += 1
    if n == "1" and rand == 3:
        print("COMPUTER played SCISSORS")
        print("+ 1 point for", username)
        player_score += 1
    if n == "2" and rand == 2:
        print("COMPUTER played PAPER")
        print("DRAW")
    if n == "2" and rand == 3:
        print("COMPUTER played SCISSORS")
        print("+ 1 point for the COMPUTER")
        pc_score += 1
    if n == "2" and rand == 1:
        print("COMPUTER played ROCK")
        print("+ 1 point for", username)
        player_score += 1
    if n == "3" and rand == 3:
        print("COMPUTER played SCISSORS")
        print("DRAW")
    if n == "3" and rand == 1:
        print("COMPUTER played ROCK")
        print("+ 1 point for the COMPUTER")
        pc_score += 1
    if n == "3" and rand == 2:
        print("COMPUTER played PAPER")
        print("+ 1 point for", username)
        player_score += 1


if player_score == 3:
    print(username, "WON!!!")
elif pc_score == 3:
    print("the COMPUTER WON!!!")

#1 is rock
#2 is paper
#3 is scissors
