import random

map = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

length = 1
body = []

x = 1
y = 3


apl1 = random.randint(1,6)
apl2 = random.randint(1,16)

if x == apl1 and y == apl2:
    apl1 = random.randint(1,6)
    apl2 = random.randint(1,16)
      

map[1][3] = "@"
body.append((x,y))


while True:

    if map[x][y] == map[apl1][apl2]:
        map[apl1][apl2] = "@"
        apl1 = random.randint(1,6)
        apl2 = random.randint(1,16)
        length += 1

    if map[apl1][apl2] == "@":
        apl1 = random.randint(1,6)
        apl2 = random.randint(1,16)
         

    map[apl1][apl2] = "*"

    print("\n\n\n\n\n\n\n\n")

    for row in map:
        print("".join(row))

    move = input()

    if move == "q":
        break


    if move.lower() == "d" and map[x][y+1] != "#":
           y += 1
    if move.lower() == "w" and map[x-1][y] != "#":
           x -= 1
    if move.lower() == "a" and map[x][y-1] != "#":
           y -= 1
    if move.lower() == "s" and map[x+1][y] != "#":
           x += 1

    body.append((x,y))

    if len(body) > length:
        old_x, old_y = body.pop(0)
        map[old_x][old_y] = " "

    map[x][y] = "@"
