"""
Write a comparator for a list of phonetic words for the letters of the greek
alphabet.


>>> greek_comparator('alpha', 'beta') < 0
>>> greek_comparator('psi', 'psi') == 0
>>> greek_comparator('upsilon', 'rho') > 0
"""
from typing import List, TypeVar


T = TypeVar("T")


greek_alphabet = (
    "alpha",
    "beta",
    "gamma",
    "delta",
    "epsilon",
    "zeta",
    "eta",
    "theta",
    "iota",
    "kappa",
    "lambda",
    "mu",
    "nu",
    "xi",
    "omicron",
    "pi",
    "rho",
    "sigma",
    "tau",
    "upsilon",
    "phi",
    "chi",
    "psi",
    "omega",
)


def find(l: List[T], T) -> int:
    """
    Return position of letter X in aplhabet L.
    """
    ...


def greek_comparator(x: T, y: T) -> int:
    ...
