def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print (quicksort([10, 5, 2, 3]))


def qsort(list):
  small=[]
  large=[]
  if len(list)<2:
    return list
  else:
    pivot=list[0]
    for i in list[1:]:
      if i<pivot:
        small=small+[i]
      else:
        large.append(i)
    a=qsort(small)
    b=qsort(large)
    return a + [pivot] + b
  
def qsort_easy(list):
  if len(list)<2:
    return list
  else:
    pivot=list[0]
    small=[ i for i in list[1:] if i<pivot]
    large=[ i for i in list[1:] if i>=pivot]

    return qsort_easy(small) + [pivot] + qsort_easy(large)
  
print(qsort([7 ,8 ,2 ,3,4]))
print(qsort_easy([7 ,8 ,2 ,3,4]))


a=[1,2,3,4,5,6,7,8]
b= 2 if a[0]<1 else 3
c= [ i for i in a[2:] if i <5]
print(b)
print(c)
