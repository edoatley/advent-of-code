numbers=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_first(line : str):
    for i in range(len(line)):
        # print(f'Testing {line[i] =}')
        if line[i].isdigit():
            # print(f'isdigit')
            return line[i]
        for digit, n in enumerate(numbers):
            # print(f'Testing {digit=} {n=} ({line[i:i+len(n)] =})')
            if line[i:i+len(n)] == n:
                # print('Match so should stop looking')
                return f'{digit+1}'
            
def get_last(line : str):
    for i in reversed(range(len(line))):
        # print(f'{i=} {line[i]=}')
        if line[i].isdigit():
            return line[i]
        for digit, n in enumerate(numbers):
            chunk = line[i-len(n)+1:i+1]
            # print(f'chunk for {n} is {chunk}')
            if chunk == n:
                return f'{digit+1}'
                
def process_line(line : str):
    # print(f'Processing line {line}')
    f = get_first(line)
    l = get_last(line)
    # print(f'{f=} {l=}')

    return int(f'{f}{l}')


def solve(filename: str):
    sum = 0
    with open(filename, 'r') as f:
        for original_line in f.readlines():
            sum += process_line(original_line.strip())
    
    return sum
    
if __name__ == "__main__":
    print(solve('input.txt'))