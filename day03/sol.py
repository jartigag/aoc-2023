#!/usr/bin/env python3.11

import re

input = [line.strip() for line in open("input").readlines()]

def part1(engine_schematic: list) -> list:
    symbol_adjacent = set()
    nums = []

    symbols_regex = r'[^.\d]'
    for i, line in enumerate(engine_schematic):
        for m in re.finditer(symbols_regex, line):
            j = m.start()
            symbol_adjacent |= {(r, c) for r in range(i-1, i+2) for c in range(j-1, j+2)}

    numbers_regex = r'\d+'
    for i, line in enumerate(engine_schematic):
        for m in re.finditer(numbers_regex, line):
            if any((i, j) in symbol_adjacent for j in range(*m.span())):
                nums.append( int(m.group()) )

    return nums

if __name__ == '__main__':
    print( sum(part1(input)) )
