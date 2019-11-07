voted = {}
def check_voter(name):
  if voted.get(name):
    print ('kick them out!')
  else:
    voted[name] = True
    print ('let them vote!')

check_voter("tom")
check_voter("mike")
check_voter("mike")


food={'banana':1.2,'tomato':2,'price':'fair'}
food['where']='market'
print(food.get('banana'))
for i in food:
    print(food[i])

def vote_check(name,dic):
    if name in dic:
        print('go away')
    else:
        dic[name]='1'
        print('let him vote')
vote_check('banana',food)
vote_check('watermelon',food)
vote_check('watermelon',food)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily['child1'])
print(myfamily['child1']['name'])