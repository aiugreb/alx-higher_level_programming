#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    j = 0
    for ele in my_list:
        try:
            if (i >= x):
                break
            print("{:d}".format(ele), end="")
            i += 1
        except (ValueError, TypeError):
            j += 1
    if (i+j < x):
        raise IndexError("list index out of range")
    print("".format())
    return i
