def process_map_line(maps: list[list], map_index : int, line : str):
    source, dest, length = [int(s) for s in line.split(' ')]
    delta = dest - source
    return (int(source), int(source) + int(length)), delta

def read_file_data_structure(filename: str) -> (list[int], list[list]):
    seeds = None
    maps = []
    maps_index = -1
    
    with open(filename, "r") as f:
        for original_line in f.readlines():
            if original_line.strip == '':
                continue
            elif original_line.startswith('seeds: '):
                seeds = [int(s) for s in original_line.split(':')[1].strip().split(' ')]
            elif original_line.contains('map:'):
                maps_index += 1
                maps[maps_index] = []
            else:
                process_map_line(maps, maps_index, original_line.strip())
    
    return seeds, maps
                    
def map_seed()                

                


def solve(filename: str):
    seeds, maps = read_file_data_structure(filename)
    
    min_location = None
    for s in seeds:
        location = map_seed(s, maps)
        print(f'{s=} ==> {location=}')
        if min_location == None or location < min_location:
            min_location = location
            print(f'{min_location=}')
            


def solve2(filename: str):
    pass
    

if __name__ == "__main__":
    #print(solve("input.txt"))
    print(solve2('input.txt'))