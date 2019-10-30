def sum(arr):
  total = 0
  for x in arr:
    total += x
  return total

print (sum([1, 2, 3, 4]))


def summation(arr):
  total=0
  for i in arr:
    total += i
  return total


print(summation([1, 2, 3, 4, 5, 6]))

# recursive with first out-- in recursive we dont need to specificlly define a sum or total value variable
def recur_sum(arr):
  if len(arr)==1:
    return arr[0]
  else:
    return (arr[0]+recur_sum(arr[1:]))
print(recur_sum([1, 2, 3, 4, 5, 6]))

# recursive with pop
def recur_sum1(arr):
  total=0
  if arr==[]:
    total += 0
  else:
    total += (arr.pop() +recur_sum1(arr))
  return total
print(recur_sum1([1, 2, 3, 4, 5, 6]))

# recursive with pop
def recur_sum2(arr):
  if arr==[]:
    return 0
  else:
    return  (arr[0]+recur_sum2(arr[1:]))
print(recur_sum2([1, 2, 3, 4, 5, 6]))