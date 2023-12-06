from math import prod
limits={'red': 12,'green': 13, 'blue': 14}

def is_hand_impossible(game:str) -> bool:
    print(f'Game {game=}')
    for show in game.strip().split(', '):
        print(f'Show {show=}')
        number, colour = show.split(' ')
        if limits.get(colour) < int(number):
            return True
    
    return False


def is_game_possible(line:str):
    id,game=line.split(':')
    print(f'{id=}   {game=}')
    for g in game.strip().split(';'):
        if is_hand_impossible(g):
            return 0
    
    print(f'ID {id=}')
    return int(id.split(' ')[1])

def game_power(line:str):
    game=line.split(':')[1]
    print(f'game_power {game=}')
    maxes={'red': 0,'green': 0, 'blue': 0}
    for g in game.strip().split(';'):
        for show in g.strip().split(', '):
            number, colour = show.split(' ')
            if maxes.get(colour) < int(number):
                maxes[colour] = int(number)
    
    print(f'Maxes {maxes=}')
    # multiply the values together i.e. find product
    return prod(maxes.values())

def solve(filename: str):
    sum = 0
    with open(filename, 'r') as f:
        for original_line in f.readlines():
            sum += is_game_possible(original_line.strip())
    
    return sum

def solve2(filename: str):
    sum = 0
    with open(filename, 'r') as f:
        for original_line in f.readlines():
            sum += game_power(original_line.strip())
    
    return sum
    
if __name__ == "__main__":
    # print(solve('input.txt'))
    print(solve2('input.txt'))