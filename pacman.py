
points = 5000
lives = 3
ghost = 200
extra = 10000

points_dict = {
    'dot': 10,
    'cherry': 100,
    'strawberry': 300,
    'orange': 500,
    'apple': 700,
    'melon': 1000,
    'galaxian': 2000,
    'bell': 3000,
    'key': 5000
}

read = open('game.txt', 'r+')
path = read.read().split(',')
print(path)


def loop():

    for dot in path:
        points = points + 10
        print(points)

    for cherry in path:
        points = points + 100
        print(points)

    for strawberry in path:
        points = points + 300
        print(points)

    for orange in path:
        points = points + 500
        print(points)

    for apple in path:
        points = points + 700
        print(points)

    for melon in path:
        points = points + 1000
        print(points)

    for galaxian in path:
        points = points + 2000
        print(points)

    for bell in path:
        points = points + 3000
        print(points)

    for key in path:
        points = points + 5000
        print(points)

    if VulnerableGhost in path:
        lives - 1
        

def add_life():
    if points > 10000:
        lives = lives + 1
    

def death():
    if lives == 0:
        print('you lose')
        print('points')
        exit()

