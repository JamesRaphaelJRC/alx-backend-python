#!/usr/bin/env python3
''' Defines an annoted function 'element_length' '''
from typing import Sequence, Tuple, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' lst - An iterable of sequence

        Return: A list pf tuples
    '''
    return [(i, len(i)) for i in lst]