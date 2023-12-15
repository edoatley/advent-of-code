from math import prod
def distance(time_holding: int, time_limit : int):
    return time_holding * (time_limit - time_holding)

def calculate_winning_combinations(time_limit: int, distance_required: int):
    return [i for i in range(time_limit) if distance(i, time_limit) > distance_required]

def read_file_data_structure(filename: str) -> [(int, int)]:
    races = []
    with open(filename, "r") as f:
        times = " ".join(f.readline().strip().split(":")[1].split()).split(" ")
        distances = " ".join(f.readline().strip().split(":")[1].split()).split(" ")
        for i in range(len(times)):
            races.append( ( int(times[i]), int(distances[i]) ) )  
    # print(f'{races=}')
    return races

def solve(filename: str):
    races = read_file_data_structure(filename)
    results = []
    for t, d in races:
        results.append(calculate_winning_combinations(t, d))
    
    # print(f'{results=}')
    return prod([len(x) for x in results])


def solve2():
    t = 52947594
    d = 426137412791216
    combos = calculate_winning_combinations(t, d)
    print(f'{len(combos)=}')

if __name__ == "__main__":
    # print(solve("input.txt"))
    print(solve2())
