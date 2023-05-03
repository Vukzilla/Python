import random

case = 0
rand = random.randint(1, 400)

while rand != 400 :
    rand = random.randint(1, 400)
    case += 1

if rand == 400 :
    print("It would take", case, " cases")
