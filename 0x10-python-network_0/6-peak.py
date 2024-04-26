#!/usr/bin/python3
"""module doc"""

def find_peak(list_of_integers):
    """Finds doc"""

    if list_of_integers == [] or list_of_integers is None:
        return None
    
    l, r = 0, len(list_of_integers)
    m = int(r / 2)

    if r == 1:
        return list_of_integers[l]

    if r == 2:
        return max(list_of_integers)

    if list_of_integers[m] > list_of_integers[m + 1] and\
            list_of_integers[m] > list_of_integers[m - 1]:
        return list_of_integers[m]

    if m > 0 and list_of_integers[m] <= list_of_integers[m + 1]:
        return find_peak(list_of_integers[m:])
    if m > 0 and list_of_integers[m] <= list_of_integers[m - 1]:
        return find_peak(list_of_integers[:m])
