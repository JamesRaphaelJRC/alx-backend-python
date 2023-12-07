#!/usr/bin/env python3
''' Defines a type-annoted function 'sum_list' '''


def sum_list(input_list: list[float]) -> float:
    ''' Returns a sum of the elements in the input_list in float '''
    return sum(elem for elem in input_list)
