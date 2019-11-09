def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])



# import dis
# def swap(e,d):
#   e,d=d,e
#   return e,d
