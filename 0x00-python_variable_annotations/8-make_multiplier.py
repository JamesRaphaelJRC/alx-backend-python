#!/usr/bin/env python3
''' Defines a type-annoted function 'make_multiplier' '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Takes a float 'multiplier' as argument

        Return: A function that multiplies a float by multiplier
    '''
    def multiply(num: float) -> float:
        ''' Multiplies multiplier by num '''
        return multiplier * num
    return multiply
