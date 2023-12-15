five_of_a_kind = 999
four_of_a_kind = 900
full_house = 800
three_of_a_kind = 700
two_pair = 600
one_pair = 500
high_card = 400

def parse(filename: str):
    with open(filename, "r") as f:
        lines = f.readlines()

    game = []
    for line in lines:
        hand, bid = line.strip().split()
        game.append((hand, int(bid)))

    return game

def evaluate_card_mappings(card_map: dict):
    if len(card_map) == 1:
        return five_of_a_kind
    elif len(card_map) == 2:
        if 4 in card_map.values():
            return four_of_a_kind
        else:
            return full_house
    elif len(card_map) == 3:
        if 3 in card_map.values():
            return three_of_a_kind
        else:
            return two_pair
    elif len(card_map) == 4:
        return one_pair
    else:
        return high_card
    
def hand_type(hand: str):
    distinct_cards = set(hand)
    card_map = {}
    for card in distinct_cards:
        card_map[card] = hand.count(card)
    
    return evaluate_card_mappings(card_map)

    
def hand_type2(hand: str):
    joker_count = hand.count('J')
    if joker_count == 5:
        return five_of_a_kind
    
    distinct_cards = set(hand.replace('J', ''))
    card_map = {}
    
    for card in distinct_cards:
        card_map[card] = hand.count(card)

    if joker_count > 0:
        best_options = [ k for k,v in card_map.items() if v == max(card_map.values()) ]
        if len(best_options) > 0:
            updated_count = card_map[f'{best_options[0]}'] + joker_count
            card_map[f'{best_options[0]}'] = updated_count

    return evaluate_card_mappings(card_map)
    

def ranker(game):
    lexical_hand=game[0].replace('A', 'Z').replace('J', 'W').replace('Q', 'X').replace('K', 'Y')
    ranking = f'{hand_type(game[0])}{lexical_hand}'
    # print(f'{ranking=} {game=}')
    return ranking


def ranker2(game):
    lexical_hand=game[0].replace('A', 'Z').replace('J', '1').replace('Q', 'X').replace('K', 'Y')
    ranking = f'{hand_type2(game[0])}{lexical_hand}'
    # print(f'{ranking=} {game=}')
    return ranking


def solve(filename: str):
    games = parse(filename)
    ranked_games = sorted(games, key=ranker)
    # print(f'{ranked_games=}')
    scored_games = [ (i+1) * s[1] for i, s in enumerate(ranked_games) ]
    # print(f'{scored_games=}')
    return sum(scored_games)

def solve2(filename: str):
    games = parse(filename)
    ranked_games = sorted(games, key=ranker2)
    for r, g in enumerate(ranked_games):
        print(f'Rank={r+1}: {g=} hand_type2={hand_type2(g[0])} ranker2={ranker2(g)}')
    # print(f'{ranked_games=}')
    scored_games = [ (i+1) * s[1] for i, s in enumerate(ranked_games) ]
    # print(f'{scored_games=}')
    return sum(scored_games)


if __name__ == "__main__":
    print(solve2("input.txt"))
