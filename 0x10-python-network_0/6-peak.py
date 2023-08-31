#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    
    lo = 0
    hi = len(list_of_integers) - 1
    
    while lo < hi:
        mid = lo + (hi - lo) // 2
        
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
            
    return list_of_integers[lo]
