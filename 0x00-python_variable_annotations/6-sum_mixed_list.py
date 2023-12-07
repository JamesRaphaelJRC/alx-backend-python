#!/usr/bin/env python3
''' Defines a type-anoted function 'sum_mixed_list' '''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Returns the sum of the elements in mxd_list in float datatype

        mxd_list: Can contain ints, floats or both

        in python 3.10+ use | i:
            def sum_mixed_list(mxd_list: List[int | float]) -> float:
    '''
    return sum(elem for elem in mxd_lst)
