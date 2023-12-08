def get_mapper(source:int, target:int, length:int):
    def mapper(value:int):
        if value >= source and value <= source + length:
            delta = source - target
            return value - delta
        return None
    return mapper


def solve(filename: str):
    pass

def solve2(filename: str):
    pass
    

if __name__ == "__main__":
    #print(solve("input.txt"))
    print(solve2('input.txt'))