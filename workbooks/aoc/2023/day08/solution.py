start = 'AAA'
end = 'ZZZ'

def parse(filename: str) -> (str, dict[tuple]):
    directions = None
    map = {}
    with open(filename, "r") as f:
        directions = f.readline().strip()
        f.readline()
        for line in f.readlines():
            loc = line[0:3]
            left = line[7:10]
            right = line[12:15]
            # print(f'{loc=}, {left=}, {right=}')
            map[loc] = (left, right)

        return directions, map

def solve(filename: str) -> int:
    locs, map = parse(filename)
    pos = start
    moves = 0
    for iter in range(100):
        for d in locs:
            new_pos = map[pos][0] if d == 'L' else map[pos][1]
            moves += 1
            pos = new_pos
            if pos == end:
                return moves
    
    raise Exception("No solution found in 100 iterations")

def all_z_end(pos: list[str]) -> bool:
    z_end = [x for x in pos if x.endswith('Z')]
    return len(z_end) == len(pos)

def solve2(filename: str):
    iterations_to_try = 1000000
    locs, mappings = parse(filename)
    starts = [k for k in list(mappings.keys()) if k.endswith('A')]
    pos = starts
    moves = 0
    big_directions = locs * 1000
    for iter in range(iterations_to_try):
        print(f'Iteration count = {iter}')
        for d in big_directions:
            #print(f'Before {pos=}')
            for i, p in enumerate(pos):
                pos[i] = mappings[p][0] if d == 'L' else mappings[p][1]
            moves += 1
            #print(f'After {pos=} ){moves=}')
            if all_z_end(pos):
                return moves
    raise Exception(f"No solution found in {iterations_to_try} iterations")

if __name__ == "__main__":
    print(solve2("input.txt"))
