def sum(list):
  if list == []:
    return 0
  return list[0] + sum(list[1:])


# recursive count
def count(arr):
  if arr==[]:
    return 0
  else:
    return 1+count(arr[1:])

print(count([1,2,3,4,5,3,2,1]))


