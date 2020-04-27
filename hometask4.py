def find(greek_alphabet, x) -> int:
    """ищет элементы в списке греческого алфавита и возвращает индекс"""
    for i, item in enumerate(greek_alphabet):
        if item == x:
            return i


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

find(greek_alphabet, "alpha")  # -> 0
find(greek_alphabet, "beta")  # -> 1
find(greek_alphabet, "eta")  # -> 6
    # a = position letter x in alphabet
    # b = position letter y in alphabet
a = find(greek_alphabet, "omicron")
b = find(greek_alphabet, "omega")

def greek_comparator(a, b) -> int:
    """сравнивает a и b, если равны возвращает 0, если a > b возвращает 1, если a < b возвращает -1"""
    if a == b:
        return 0
    if a > b:
        return 1
    if a < b:
        return -1
