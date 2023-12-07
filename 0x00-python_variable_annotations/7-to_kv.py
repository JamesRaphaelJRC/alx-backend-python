#!/usr/bin/env python3
''' Defines a type-annoted function 'to_kv' '''
from typing import Tuple, Union


def to_kv(k: str, v: [Union[int, float]]) -> Tuple[str, float]:
    ''' Takes a string k and an int or float v as arguments

        Return: A tuple (k, v^2)
            where k is a string and v^2 a float
    '''
    return k, v * v
