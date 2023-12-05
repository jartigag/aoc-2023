#!/usr/bin/env python3.12

input = [line.strip() for line in open("input").readlines()]

def part1(input):
    nums = []
    for i in input:
        num = 0
        num_str = "".join([c if c.isdigit() else "" for c in i])
        if num_str.isdigit():
            num = int(num_str[0])*10 + int(num_str[-1])
        nums.append(num)
    return nums

print( sum(part1(input)) )
