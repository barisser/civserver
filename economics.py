import commodities
import math
import settings


def calculate_standard_of_living(pop_object):
    s = 0
    for x in pop_object.consumption:
        s += x
    s = s / (pop_object.n + 1)
    return s
