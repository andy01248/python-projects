import math

def andy(n):
    if n >= 2:
        a = n*andy(n-1)
        return a
    else:
        return 1
a=andy(5)

print(a)

# boolean
def are_you_ok(experiment,simulation):
    if experiment and simulation:
        return True
    else:
        return False


print(are_you_ok(True,True))

def c_d_e(c ,d, e):
    return c+d>e

# list
b=[]
a=[1,2,3,4,5,6]
for x in a:
    b.append(3+x)

for x in range(1,10,2):
    b.append(3+x)

print(b)

c = [math.sqrt(x) for x in a]
print(c)

# set  set reject the duplicate.   remove the duplicate
# TODO: give more time for it

a=[1 ,2,3,1,2,4]
new_set=set()

for i in a:
    new_set.add(i)
print(new_set)

d=[1,3,4,1,3]
set1=set()
for x in d:
    set1.add(x)
print(sum(set1))