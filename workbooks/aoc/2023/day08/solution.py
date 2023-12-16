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



def solve2(filename: str):
    locs, mappings = parse(filename)
    starts = [k for k in list(mappings.keys()) if k.endswith('A')]
    pos = starts
    moves = 0
    for iter in range(100):
        for d in locs:
            for i, p in enumerate(pos):
                pos[i] = mappings[p][0] if d == 'L' else mappings[p][1]
            moves += 1
            if len([x for x in pos if not x.endswith('Z')]) != 0:
                return moves

if __name__ == "__main__":
    print(solve("input.txt"))
