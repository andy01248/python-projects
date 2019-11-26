# You pass an array in, and it gets converted to a set.
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
  best_station = None
  states_covered = set()
  for station, states in stations.items():
    covered = states_needed & states
    if len(covered) > len(states_covered):
      best_station = station
      states_covered = covered

  states_needed -= states_covered
  final_stations.add(best_station)

print (final_stations)


print(set([1,1,6,3,2,2,2,3,3,4,3,4,4,5,3,3]))
print(set([6,6,4,4,2,2,3,3,1,1,2]))
print(set([1,2,3,4]))
print(set(['a','a','b','b','c','c','d','d','f','f','e','e']))




states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

chosen_station=set()

while states_needed:
  best_station=None 
  best_covered=set()
  for current_station in stations.keys():
    current_covered = stations[current_station] & states_needed
    if len(current_covered) > len(best_covered):
      best_station=current_station
      best_covered=current_covered
  chosen_station.add(best_station)
  states_needed -= best_covered #this is the set difference -> delete the similar item between two set from set1 
  
print(chosen_station)

a=[1,2,3]
b=[2,3,4]
print(a+b)
