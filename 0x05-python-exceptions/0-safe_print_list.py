#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for ele in my_list:
            if (i >= x):
                break
            print("{}".format(ele), end="")
            i += 1
        print("".format())
        return i
    except ValueError:
        print("ValueError error")
