def process_map_line(line : str) -> (int, int, int):
    dest, source, length = [int(s) for s in line.split(' ')]
    delta = dest - source
    return (int(source), int(source) + int(length), delta)

def read_file_data_structure(filename: str) -> (list[int], list[list]):
    seeds = None
    maps = []
    maps_index = -1
    
    with open(filename, "r") as f:
        for original_line in f.readlines():
            line = original_line.strip()
            # print(f'{line=}')
            if line == '':
                # print('Skipping blank line')
                continue
            elif line.startswith('seeds: '):
                seeds = [int(s) for s in line.split(':')[1].strip().split(' ')]
                # print(f'Found seeds {seeds=}')
            elif 'map:' in line:
                # print(f'Found map {line=}')
                maps_index += 1
                maps.append([])
            else:
                # print(f'Adding map entry {line=} {maps_index=} {maps=}')
                maps[maps_index].append(process_map_line(line.strip()))
    
    return seeds, maps

def read_file_data_structure_to_ranges(filename: str) -> list[list]:
    ranges=[]
    index = 0
    
    with open(filename, "r") as f:
        for original_line in f.readlines():
            line = original_line.strip()
            if line == '':
                continue
            elif line.startswith('seeds: '):
                # iterate seeds 2 at a time
                seeds = [int(s) for s in line.split(':')[1].strip().split(' ')]
                for i in range(0, len(seeds), 2):
                    ss = seeds[i]
                    se = ss + seeds[i+1]
                    ds = seeds[i]
                    de = ss + seeds[i+1]
                    delta = ds - ss
                    ranges[index].append((ss, se, ds, de, delta))
                # prepare for mappings
                index = 1
                ranges.append([])
            elif 'map:' in line:
                index += 1
                ranges.append([])
            else:
                ds, ss, length = [int(s) for s in line.strip().split(' ')]
                se = ss + length
                de = ss + length
                delta = ds - ss
                ranges[index].append((ss, se, ds, de, delta))
    
    return ranges
                    
def map_seed(seed : int, maps : list[list]) -> int:
    mappings = [seed]

    for map in maps:
        temp = mappings[-1]
        for source, dest, delta in map:
            # print(f'{temp=} {source=} {dest=} {delta=}')
            if temp >= source and temp < dest:
                mappings.append(temp + delta)
                break

    # print(f'Created {mappings=} from {seed=} and {maps=}')
    return mappings[-1]
                

def solve(filename: str):
    seeds, maps = read_file_data_structure(filename)
    locations = []

    for s in seeds:
        location = map_seed(s, maps)
        print(f'{s=} ==> {location=}')
        locations.append(location)
    
    return min(locations)
            


   # think we need to be clever and start with the locations ranked in order desc and then test to see 
   # if there is a way to have a seed that matches the requirements
def solve2(filename: str):
    ranges = read_file_data_structure_to_ranges(filename) 
    # iterate last entry of ranges in order of the 2nd tuple entry (destination start)
    for location in sorted(ranges[-1], key=lambda x: x[2]):
        valid = find_valid_paths(ranges[:-1], (location[0], location[1]), len(ranges[:-1]) - 1)
        if valid:
            print(f'Found valid path {valid=}')
            return location[2]
            

def find_valid_paths(ranges: list[list], location: tuple, index: int) -> bool:
    for r in ranges[index]:
        if location[0] >= r[0] and location[1] <= r[1]:
            if index == 0:
                return True
            else:
                return find_valid_paths(ranges, (r[2], r[3]), index - 1)

if __name__ == "__main__":
    print(solve2('input.txt'))