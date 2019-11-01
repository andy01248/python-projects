def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


# loop way to find the highest number in array
def findmax(list):
    max_index = 0
    value = list[0]
    for i in range(0, len(list)):
        if list[i] > value:
            max_index = i+1
            value = list[i]
    return max_index, value


print(findmax([1, 2, 3, 4, 5, 8, 2, 1]))

# recursive max way


def re_findmax(list):
    if len(list) == 1:
        return list[0]
    else:
        sub_value = re_findmax(list[1:])
        if sub_value > list[0]:
            return sub_value
        else:
            return list[0]


print(re_findmax([1, 2, 3, 4, 5, 8, 2, 1]))


def re_binary_search(list, value, high, low):
    mid = (high+low)//2
    if high >= low:
        if list[mid] == value:
            return mid
        elif list[mid] > value:
            high = mid-1
            return re_binary_search(list, value, high, low)
        else:
            low = mid+1
            return re_binary_search(list, value, high, low)
    else:
        return None


list = [1, 2, 3, 4, 5, 8, 9, 10]
high = len(list)-1
low = 0
print(re_binary_search(list, 2, high, low))
