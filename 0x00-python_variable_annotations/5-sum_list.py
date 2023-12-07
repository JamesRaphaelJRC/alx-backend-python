#!/usr/bin/env python3
''' Defines a type-annoted function 'sum_list' '''
from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' Returns a sum of the elements in the input_list in float '''
    return sum(elem for elem in input_list)
