graph={}
graph['START']={}
graph['START']['A']=6
graph['START']['B']=2
graph['A']={}
graph['B']={}
graph['A']['FIN']=1
graph['B']['A']=3
graph['B']['FIN']=5
graph['FIN']={}

# The graph for edge and weights.  The same expression
graph = {
    'START':{
        'A':6,
        'B':2  
        },
    'A':{
        'FIN':1 
        },
    'B':{
        'A':3,
        'FIN':5 
        },
    'FIN':{}
}
# The costs hold the lastest costs for each node from START
costs = {'A':6, 'B':2, 'FIN':float('inf')}
# The parents hold the parent node for each node with min costs
parents= {'A':'START','B':'START','FIN':None}
processed=[]

# Find the min costs and non-processed node 
def find_node_with_min_costs(costs):
    cost=float('inf')
    Next_node=None
    for current_node in costs.keys():
        if costs[current_node] <cost and current_node not in processed:
            cost=costs[current_node]
            Next_node=current_node
    return Next_node

# def dijkstra_routing(node):
node=find_node_with_min_costs(costs)
while node :
    cost=costs[node]
    a=graph[node] #can be used as graph[node]
    for next_node in graph[node].keys():
        new_cost=cost + graph[node][next_node]
        if new_cost<costs[next_node]:
            costs[next_node]=new_cost
            parents[next_node]=node
    processed.append(node)
    node=find_node_with_min_costs(costs)
        
print('the cost to fin is', costs['FIN'])

print(costs)
print(parents)        

