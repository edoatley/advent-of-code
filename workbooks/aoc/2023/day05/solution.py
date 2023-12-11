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
            

def solve2(filename: str):
    pass
    

if __name__ == "__main__":
    print(solve('input.txt'))