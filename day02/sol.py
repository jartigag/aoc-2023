#!/usr/bin/env python3.11

input = [line.strip() for line in open("input").readlines()]

NUM_OF_RED_CUBES   = 12
NUM_OF_GREEN_CUBES = 13
NUM_OF_BLUE_CUBES  = 14

def would_have_been_possible(set_of_cubes: list) -> bool:
    for rgb_cubes in set_of_cubes:
        cubes = rgb_cubes.split(',')
        for cube in cubes:
            total_num_of_cubes, color = cube.strip().split(' ')
            if color == 'red'   and int(total_num_of_cubes) > NUM_OF_RED_CUBES:
                return False
            if color == 'blue'  and int(total_num_of_cubes) > NUM_OF_BLUE_CUBES:
                return False
            if color == 'green' and int(total_num_of_cubes) > NUM_OF_GREEN_CUBES:
                return False
    return True

def part1(input: list) -> int:
    sum_of_the_IDs_of_possible_games = 0
    for i in input:
        game, set_of_cubes = i.split(':')
        game_id            = int(game.split(' ')[1])
        set_of_cubes       = set_of_cubes.split(';')
        print(set_of_cubes)
        if would_have_been_possible(set_of_cubes):
            sum_of_the_IDs_of_possible_games += game_id
    return sum_of_the_IDs_of_possible_games

def part2(input: list, digits_dict: dict) -> list:
    return None

print( part1(input) )
