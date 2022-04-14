import itertools as it
from typing import List

"""No more than k variables take value 1."""
def no_more_than_k_are_1(x: List[int], k: int):
    return [[-i for i in c] for c in it.combinations(x, k+1)]


"""At least k variable take value 1."""
def at_least_k_are_1(x: List[int], k: int):
    n = len(x)
    return [x]


"""Exactly k variables take value 1."""
def exactly_k_are_1(x: List[int], k: int):
    # We can concatenate the CNFs because it's a conjunction
    return no_more_than_k_are_1(x,k) + at_least_k_are_1(x,k)

def exactly_one(x: List[int]):
    return exactly_k_are_1(x, 1) 
