

a='hello word asdf {}'

print(a)
b=1
c=3
print(a.format(b))
print('hello world', b,'aa')

d = 0
index = 0
lista = [1, 2, 3, 4]
while index<len(lista):
    d += lista[index]
    index+=1
    if lista[index-1] == 2:
        break
print(d)

lista.insert(2,10)
print(lista)

lista.pop(2)
print(lista)
e=lista.copy()
lista.pop(2)
print(lista)
print(e)


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist[0])


class Person:
    def genderman(self):
        print('the gender of this person is ' + self.gender)


p1 = Person()
p1.gender = 'male'
p1.height = 186
p1.weight = 50
p1.genderman()
print(p1.height, 'aaa', p1.weight)

class pet:
    def __init__(self, gender, height, weight, master, test):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.master = master
        self.aaa = test
    def genderpet(self):
        print('the gender of this pet is ' + self.gender)


p2=pet('female',177,60,p1, 1000)
p2.genderpet()
p2.aaa
print(p2.master.height)
p2.master.weight




