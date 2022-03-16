from random import randint as r

games = []

while True:
    game = input('What is the name of the game?\n')
    if game == '':
        break
    games.append(game)

num = r(0, len(games) - 1)

print(games[num])