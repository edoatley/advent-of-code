from math import prod

def is_symbol(c: str) -> bool:
    return not (c.isdigit() or c == ".")


def check_adjacent_row(
    engine: list[str], row_index: int, start_index: int, end_index: int
) -> bool:
    rmin = max(0, start_index - 1)
    rmax = min(len(engine[row_index]) - 1, end_index + 1)
    for test_idx in range(rmin, rmax+1):
        if is_symbol(engine[row_index][test_idx]):
            return True
    return False


def check_for_symbol(engine: list[str], index: int, start_index: int, end_index: int) -> int:
    # if there is a row above check for a symbol
    not_symbol = True

    if index > 0 and check_adjacent_row(engine, index - 1, start_index, end_index):
        not_symbol = False

    # if there is a row below check for a symbol
    if (
        not_symbol
        and index + 1 < len(engine)
        and check_adjacent_row(engine, index + 1, start_index, end_index)
    ):
        not_symbol = False

    # check the character before and after for a symbol
    if not_symbol and start_index > 0 and is_symbol(engine[index][start_index - 1]):
        not_symbol = False

    if (
        not_symbol
        and end_index < (len(engine[index]) - 1)
        and is_symbol(engine[index][end_index + 1])
    ):
        not_symbol = False

    if not_symbol:
        return 0
    else:
        return int(engine[index][start_index : end_index + 1])


def process_line(engine: list[str], index: int) -> int:
    start_index = None
    end_index = None

    #print(f'process_line {index=}')
    
    part_sum = 0

    for c in range(len(engine[index])):
        if engine[index][c].isdigit():
            if start_index == None:
                start_index = c
                end_index = c
            else:
                end_index = c
        elif start_index != None and end_index != None:
            part_sum += check_for_symbol(engine, index, start_index, end_index)
            start_index = None
            end_index = None

    if start_index != None and end_index != None:
        part_sum += check_for_symbol(engine, index, start_index, end_index)
        start_index = None
        end_index = None

    return part_sum

# 0123456789
# ...$.*....   gear_index = 5 
# ..664.598.   C1 664 si=2 ei=4 C2 598 si=6 ei=8
# .664.598..   C3 598 si=5 ei=7
# .664..598.   C4 598 si=6 ei=8
# .66412598.   C5 66412598 si=1 ei=8
# so we need to check if the gear index is 
# a) between the start and end index inclusive (C3, C5)
# b) start_index == gear_index + 1 (C2, C4)
# c) end_index == gear_index - 1 (C1)
def extract_touching_numbers(engine: list[str], gear_index: int, check_index: int) -> list[int]:
    start_index = None
    end_index = None
    numbers=[]

    #print(f'extract_touching_numbers {gear_index=} {check_index=} {engine[check_index]=}')
    
    for c in range(len(engine[check_index])):
        # #print(f'A {c=} {engine[check_index][c]=} {start_index=} {end_index=} {gear_index=}')
        if engine[check_index][c].isdigit():
            # #print(f'B Found digit {c=} {engine[check_index][c]=}')
            if start_index == None:
                start_index = c
                end_index = c
            else:
                end_index = c
        elif start_index != None and end_index != None:
            # #print(f'C Found non-digit {c=} {engine[check_index][c]=} {start_index=} {end_index=} {gear_index=}')
            if (
                (start_index <= gear_index and end_index >= gear_index  ) or
                (start_index == gear_index + 1 or end_index == gear_index - 1 )
            ):
                # #print(f'D {start_index=} {end_index=} {gear_index=} {engine[check_index]=}')
                numbers.append(int(engine[check_index][start_index:end_index+1]))
            start_index = None
            end_index = None
                
    if start_index != None and end_index != None:
        if (
            (start_index <= gear_index and end_index >= gear_index  ) or
            (start_index == gear_index + 1 or end_index == gear_index - 1 )
        ):
            numbers.append(int(engine[check_index][start_index:end_index+1]))
    
    return numbers
            

def get_gear_parts(engine: list[str], engine_index: int, gear_index: int) -> list[int]:
    parts=[]
    row_length = len(engine[engine_index])

    #print(f'get_gear_parts(): {engine[engine_index]=} {engine_index=} {gear_index=} {engine[engine_index-1]=} {engine[engine_index+1]=}')
    
    # check line above
    if engine_index > 0:
        parts.extend(extract_touching_numbers(engine, gear_index, engine_index-1))
        #print(f'get_gear_parts above {parts=}')
    
    # check line below
    if engine_index + 1 < row_length:
        parts.extend(extract_touching_numbers(engine, gear_index, engine_index+1))
        #print(f'get_gear_parts below {parts=}')
    
    # check before
    test_idx = gear_index - 1
    if test_idx >= 0 and engine[engine_index][test_idx].isdigit():
        while test_idx >= 0 and engine[engine_index][test_idx].isdigit():
            #print(f'{test_idx=} {engine[engine_index][test_idx]=}')
            test_idx -= 1
        parts.append(int(engine[engine_index][test_idx+1:gear_index]))
        #print(f'get_gear_parts left {parts=}')
    
    # check after
    test_idx = gear_index + 1
    if test_idx < row_length and engine[engine_index][test_idx].isdigit():
        #print(f'Start after loop {test_idx=} {engine[engine_index][test_idx]=}')
        while test_idx < row_length and engine[engine_index][test_idx].isdigit():
            test_idx += 1
            #print(f'>>> {test_idx=} {engine[engine_index][test_idx]=}')
        parts.append(int(engine[engine_index][gear_index+1:test_idx]))
        #print(f'get_gear_parts right {parts=}')
    
    #print(f'get_gear_parts returning {parts=}')
    return parts
    
def process_gear(engine: list[str], index: int):
    sum = 0
    for i, c in enumerate(engine[index]):
        if c == '*':
            parts = get_gear_parts(engine, index, i)
            if len(parts) == 2:
                #print(f'{parts=}')
                sum += prod(parts)
    return sum

def solve(filename: str):
    engine = []
    with open(filename, "r") as f:
        for original_line in f.readlines():
            engine.append(original_line.strip())

    sum = 0

    for i in range(len(engine)):
        sum += process_line(engine, i)

    return sum

def solve2(filename: str):
    engine = []
    with open(filename, "r") as f:
        for original_line in f.readlines():
            engine.append(original_line.strip())

    sum = 0
    
    for i in range(len(engine)):
        if '*' in engine[i]:
            sum += process_gear(engine, i)
    
    return sum    

if __name__ == "__main__":
    #print(solve("input.txt"))
    print(solve2('input.txt'))
