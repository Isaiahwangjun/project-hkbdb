from fuzzywuzzy import fuzz


def completely(x, y):
    if x == y:
        return 100
    else:
        return 0


def partial_ratio(x, y):
    return fuzz.partial_ratio(x, y)


def token_sort_ratio(x, y):
    return fuzz.token_sort_ratio(x, y)
