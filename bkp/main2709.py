import random
import sys
import os.path
import numpy as np

from utils import readFile

def _generate_one_game(numbers):
    game = random.sample(numbers, k=15)
    game.sort()

    return ','.join([str(x) for x in game])

def _generate_games(numbers, all_games):
    games = []

    #generate 10 games
    i = 0
    while True:
        #if len(games) == 1000:
        #    break

        game = _generate_one_game(numbers)
        #if game in all_games:
            #print('Já foi sorteado')
        #    continue

        if game in games:
            print('Já tá na lista')
            continue

        print(i)

        games.append(game)
        i +=1

        today_game = '2,4,5,7,8,12,14,17,18,20,21,22,23,24,25'
        if today_game in games:
            print('perdemos a chance de ficar rico')
            print(i)
            break


    return games

def all_draws_to_string(list):
    strings = []

    for k,v in list.items():
        strings.append(','.join([str(x) for x in list[k]]))

    return strings


def main():
    all_draws = readFile.read("./resources/allDraws.json")

    all_draws_string = all_draws_to_string(all_draws)

    # read from user
    twenty_selected_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

    ten_games = _generate_games(twenty_selected_numbers, all_draws_string)

    today_game = '2,4,5,7,8,12,14,17,18,20,21,22,23,24,25'
    if today_game in ten_games:
        print('perdemos a chance de ficar rico')

    #for game in ten_games:
    #    print(game)

if __name__ == '__main__':
    main()
