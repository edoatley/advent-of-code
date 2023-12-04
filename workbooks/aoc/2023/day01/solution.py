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


# def replace_words(line: str) -> str:
#     # print(f'replace_words({line})')
#     if len([n for n in numbers if n in line]) == 0 or line.isnumeric():
#        return line
#     # loop through characters of the word
#     for i in range(len(line)):
#         for digit, n in enumerate(numbers):
#               if line[i:i+len(n)] == n:
#                   # think this is needed as indexes mess up after replacement
#                   return replace_words(line[:i] + f'{digit+1}' + line[i+len(n):])
#     # print(f'Failed to find more replacements return ({line})')
#     return line

# # need to be cleverer and do it from right to left for last digit!!!
# def replace_words_backwards(line: str) -> str:
#     # print(f'replace_words({line})')
#     if len([n for n in numbers if n in line]) == 0 or line.isnumeric():
#        return line
#     # loop through characters of the word
#     for i in range(len(line)):
#         for digit, n in enumerate(numbers):
#               if line[i:i+len(n)] == n:
#                   # think this is needed as indexes mess up after repalcement
#                   return replace_words(line[:i] + f'{digit+1}' + line[i+len(n):])
#     # print(f'Failed to find more replacements return ({line})')
#     return line
              
# def extract_digits(line : str):
#     digits = [c for c in line if c.isdigit()]
#     first = digits[0]
#     last = digits[0]
#     if len(digits) > 1:
#         last = digits[len(digits) - 1]

#     return first, last


# def solve(filename: str):
#     sum = 0
#     with open(filename, 'r') as f:
#         for original_line in f.readlines():
#             line = replace_words(original_line.strip())
#             first_digit, last_digit = extract_digits(line)            
#             calculated_value = int(f'{first_digit}{last_digit}')
#             print(f'Original={original_line.strip()} converted to {line} with value {calculated_value}')
#             sum += calculated_value
#         return sum
    
if __name__ == "__main__":
    print(solve('input.txt'))