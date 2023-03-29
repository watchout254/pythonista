set1 = {'Ram','sham','jenny'}
set2 = {'jenny','jiya','akash'}
set3 = {'ankur','pardeep'}
#print(set1.union(set2,set3)) #union concatenates sets but does not repeat values that are similar
#print(set1 | set2 | set3)
#print(set1.union(('mohan','jenny')))
#set1.update(['jenny','mohan'])
#set1 |= set2
#print(set1)

#intersection = the one that appears twice/common in each set
#print(set1.intersection(['mohan','shiva']))
#print(set1 & set2)
#set1.intersection_update(set2)
#print(set1)

#print(set1.difference(set2)) #difference= item in set one but not in set 2
#print(set1-set2)
#print(set1.symmetric_difference(set2)) #set1 or set2 but not in both
#print(set1 ^ set2 ^ set3)

set5 = {1,2,3,4,5}
set6 = {4,10,7,8,-10,1,2,3,4,5}
print(set5.isdisjoint(set6))
print(set5.issubset(set6)) # similar
print(set5 <= set6)

print(set5.issuperset(set6)) #contains every element of the other set

set7 = {'Ram','shyam','jenny'}
set8 = {'jiya','akash'}
print(set7.isdisjoint(set8)) # nothing common
print(set7.issubset(set8))





