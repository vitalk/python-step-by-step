"""
Написать функцию которая принимает список чисел l одним аргументом и число n
другим и возвращает наименьшее ближайшее число из списка l к числу n

>>> nearest_value([1, 2, 10, 5, 3], n=4)
3
>>> nearest_value([1, 2, 3, 4], n=10)
4
>>> nearest_value([100, 200, 0], n=1)
0
"""
from typing import List


def nearest_value(l: List[int], n: int) -> int:
    ...
