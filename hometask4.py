def find(greek_alphabet, x) -> int:
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
a = find(greek_alphabet, "alpha")
b = find(greek_alphabet, "beta")

def greek_comparator(a, b) -> int:
    return a - b
