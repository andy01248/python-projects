from collections import deque

def person_is_seller(name):
      return name[-1] == 'm'    #same as return True if... else ..

print(person_is_seller('m'))
graph = {}
graph["you"] = ["alice", "bob", "claire"]  #array as the value of dict
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # This array is how you keep track of which people you've searched before.
    searched = []
    while search_queue:
        person = search_queue.popleft()       
        # Only search this person if you haven't already searched them.
        if not person in searched:
            if person_is_seller(person):
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]             
                # Marks this person as searched
                searched.append(person)
                #searched += person
    print('no seller here')
    return False
search("you")




tree=dict()
tree['YOU']=['ALICE','BOB','CLAIRE']
tree['ALICE']=['PEGGY']
tree['BOB']=['PEGGY','ANUJ']
tree['CLAIRE']=['JONNY','THOM']
tree['PEGGY']=[]
tree['ANUJ']=[]
tree['JONNY']=[]
tree['THOM']=[]

def check_name(name):
    if name=='ANUJ':
        return True
checked=[]

def search_it(name):
    current_queue=tree[name]
    while current_queue:
        current_node=current_queue.pop(0)  #pop(0) is slower than queue popleft
        if not current_node in checked:
            print(current_node)
            if check_name(current_node):
                print('The one we want is',current_node)
                return True
            else:
                current_queue+= tree[current_node] #add the array item
                checked.append(current_node) #add whole array 
    print('no such people here')
    return False
    
        
search_it('YOU')  

a=[1,2,3]
b=[2,3,4]
c=[1,2,3]
d=[2,3,4]
a.append(b)  #append everything include data type --array
c+=d         #add the array items
print(a)
print(c)