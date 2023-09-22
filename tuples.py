#create a tuple

newTuple = 'a','b','c','d','e'

print(newTuple) 

#access elements in tuple
newTuple =( 'a','b','c','d','e')
print(newTuple[2])
print(newTuple[1:3 ])

# traversing in tuple
newTuple = ('a','b','c','d','e')

for i in newTuple:
    print(i)

for i in range(len(newTuple)):
    print(newTuple[i]) 

#search in tuple
newTuple = ('a','b','c','d','e')

print('a'in newTuple)
print('f' in newTuple)

print(newTuple.index('e'))


def searchTuple(p_tuple , element):
    for i in range(0, len(p_tuple)):
        if p_tuple[i] == element:
            return f"the {element} is found at {i} index"
    return "the element not found"

print(searchTuple(newTuple,'b'))
    
