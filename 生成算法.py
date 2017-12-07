"""
Some implementation of generating permutations and combinations.
Chapter 4 in **Introductory Combinatorics** by Richard Brualdi.
"""

def generate_permutation(n):
    """
    n: int, first n integers
    return: list of all possible permutations
    """
    permutations = []
    if n == 1:
        return [[1]];
    else:
        for last_permutation in generate_permutation(n-1):
            for pos in range(len(last_permutation)+1):
                temp = last_permutation[:]
                temp.insert(pos, n)
                permutations.append(temp)
    return permutations

"""
This recursion model is based on Johnson-Trotter algorithm. 
The idea is that evary permutation of n can be genarated by inserting n in all possible positions in permutations of n-1.
"""

def genarate_subset(items):
    """
    set: a list of elements
    yield all subsets (including the empty set and the set itself)
    """
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        subset = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                subset.append(items[j])
        yield subset

def generate_more_subset(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    for i in range(3**N):
        bag1 = []
        bag2 = []
        combo = (bag1,bag2)
        for j in range(N):
            if (i//(3**j)) % 3 == 1:
                bag1.append(items[j])
            if (i//(3**j)) % 3 == 2:
                bag2.append(items[j])
        yield combo

# def generate_gray(n):
#     """
#     n: int, n-bit binary string
#     return: all possible binary string, in gray code order
#     """
#     bistring = [False]*n
#     while bistring != [True]+[False]*(n-1):
#         if sum(bistring)%2 == 0:
#             bistring[n] = bool(bistring[n] - 1)
#         else:

