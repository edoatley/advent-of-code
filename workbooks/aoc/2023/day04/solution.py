def to_sets(winner_list:str, numbers_list:str) -> tuple[set[str], set[int]]:
    winners = set([int(x) for x in winner_list.replace("  ", " ").strip().split(' ')])
    numbers = set([int(x) for x in numbers_list.replace("  ", " ").strip().split(' ')])
    return winners, numbers

# def pick_cards(ix: int, score: int) -> int:
#     return 

# def score_card(ix: int, scores: dict[int, int], parent='') -> int:
#     cards_won = 1
#     winnings = [ix + i for i in range(1, scores[ix]+1)]
#     for win in winnings:
#         parent = f"{parent} {win}"
#         cards_won += score_card(win, scores)

#     print(f"score_card({ix} {parent=}) winnings: {winnings} ==> {cards_won}")
#     return cards_won

# def calculate_total_score(scores: dict[int, int]) -> int:
#     print(f"calculate_total_score({scores})")
#     card_wins = 0
#     for ix in sorted(scores.keys()):
#          card_score = score_card(ix, scores)
#          print(f"Scoring card - {ix=} {card_score=}")
#          card_wins += card_score
#          print(f"New Total = {card_wins=}")

#     return card_wins

def calculate_total_score(scores: dict[int, int], cards_to_score: list[int]) -> int:
    won_cards = []
    print(f"calculate_total_score({cards_to_score})")
    if len(cards_to_score) == 0:
        return 0
    for ix in cards_to_score:
        winnings = [ix + i for i in range(1, scores[ix]+1)]
        print(f"{ix=} {winnings=}")
        won_cards.extend(winnings)

    return len(won_cards) + calculate_total_score(scores, won_cards)

def solve(filename: str):
    cards = None
    with open(filename, "r") as f:
        cards = [line.split(':')[1].strip() for line in f.readlines()]
    score = 0
    for card in cards:
        # note the * before card.split('|') - this is a python idiom that unpacks the tuple returned by to_sets
        winners, numbers = to_sets(*card.split('|'))
        matches = winners.intersection(numbers)
        if len(matches) > 0:
            score += (2 ** (len(matches) - 1 ))

    return score

def solve2(filename: str):
    cards = None
    with open(filename, "r") as f:
        cards = [line.split(':')[1].strip() for line in f.readlines()]
    
    scores = {}

    for ix, card in enumerate(cards):
        winners, numbers = to_sets(*card.split('|'))
        scores[ix+1] = len(winners.intersection(numbers))

    print(f"scores: {scores}")
    
    return calculate_total_score(scores, sorted(scores.keys())) + len(cards)
    

if __name__ == "__main__":
    #print(solve("input.txt"))
    print(solve2('input.txt'))