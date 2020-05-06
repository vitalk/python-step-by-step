"""
Написать функцию которая принимает два списка и возвращает список из элементов
которые есть в первом и во втором списке

>>> inner_join([1, 2, 3], [2, 3, 4])
[2, 3]
>>> inner_join([1, 2, 3], [5, 10, 11])
[]
>>> inner_join([7, 4, 10], [5, 10, 11])
[10]
"""
from typing import List, Any


def inner_join(l1: List[Any], l2: List[Any]) -> List[Any]:
    ...