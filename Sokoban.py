import random

rand = random.randint(1,5)
rand1 = random.randint(1,6)

rand2 = random.randint(1,5)
rand3 = random.randint(1,6)

rand4 = random.randint(1,5)
rand5 = random.randint(1,6)

map = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

x = rand1
y = rand

x1 = rand3
y1 = rand2

x2 = rand5
y2 = rand4


if map[x][y] == map[x1][y1]:
    x = random.randint(1,6)
    y = random.randint(1,5)

if map[x][y] == map[x2][y2]:
    x = random.randint(1,6)
    y = random.randint(1,5)

if map[x1][y1] == map[x2][y2]:
    x1 = random.randint(1,6)
    y1 = random.randint(1,5)

map[x][y] = "@"
map[x1][y1] = "*"
map[x2][y2] = "$"

while True:
    print("\n\n\n\n\n\n")
    for row in map:
        print(" ".join(row))
    
    move = input("")

    map[x][y] = " "

    if move.lower() == "q":
         break

    if move.lower() == "d" and map[x][y+1] != "#":
           y += 1
           if map[x1][y1] == map[x][y]:
               if map[x1][y1+1] != "#":
                    y1 += 1
               else:
                    y -= 1

               
    if move.lower() == "w" and map[x-1][y] != "#":
           x -= 1
           if map[x1][y1] == map[x][y]:
            if map[x1-1][y1] != "#":
               x1 -= 1
            else:
                x += 1


    if move.lower() == "a" and map[x][y-1] != "#":
           y -= 1
           if map[x1][y1] == map[x][y]:
               if map[x1][y1-1] != "#":
                    y1 -= 1
               else:
                    y += 1


    if move.lower() == "s" and map[x+1][y] != "#":
           x += 1
           if map[x1][y1] == map[x][y]:
                if map[x1+1][y1] != "#":
                    x1 += 1
                else:
                    x -= 1
    
    
    map[x][y] = "@"
    map[x1][y1] = "*"
    map[x2][y2] = "$"
    
    if map[x1][y1] == map[x2][y2]:
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == '#':
                    map[i][j] = ' '

    if map[x][y] == map[x2][y2]:
        map[x2][y2] = "@"
