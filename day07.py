dict = {}
print(type(dict))
s = set()
print(type(s))

# 5 non sequences
s.add(10)                               # set will not allow duplicates
s.add(3.2)
s.add(True)     
s.add(None)
s.add(2+2j)

# sequences                             
s.add("tejaa")                          # we can only add imutable sequences to a set.
s.add((1,2))
s.add(range(4))

s={1,2,3,4}
s.pop()
print(s)
s.remove(2)
print(s)
#s.remove(1)        raises error because 1 is already removed
s.discard(3)
print(s)
print(s.discard(1))         # returns None
print(s.clear())            # prints empty set

# non seq
print(s.update([100, 200, 300, 400, 500]))
# seq
s.update("world")               
s.update((6, 7, 8))               
s.update([9, 10, 11])             
s.update({12, 13})                
s.update(range(14, 16))

s = {1,2,3,4}
l = [3,4,5,6]
print(s.union(l))
print(s.intersection(l))
print(s.difference(l))
print(s.symmetric_difference(l))

s2 = {3, 4, 5, 6}
print("Union operator (|):", s | s2)
print("Intersection operator (&):", s & s2)
print("Difference operator (-):", s - s2)
print("Symmetric Difference operator (^):", s ^ s2)

# print("Union operator (|):", s | l)           returns an operand error, we cannot do that with list

dict = {}
dict.update({1 : "a", 2 : "b"})
dict.update([(3, "c"), (4 , "d")])
dict.update((('e', 5), ('f', 6)))
dict.update({('g', 7), ('h', 8)})
print(dict)

dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
dict.pop(4)
# dict.pop(100)      --> returns key error
print(dict.pop(100, 'z'))        # --> returns z if the key is missing
print(dict.popitem())       # --> removes last element
print(dict.clear())
print("get(4):", dict.get(4))

# get the value of key 100
print(dict.get(100))  # Returns None
print(dict.get(100, 'z'))

print(dict.setdefault(4))
print(dict.setdefault(100))
print(dict.setdefault(200, 'z'))

keys = dict.keys()
print("Keys:", keys, "| Type:", type(keys))

values = dict.values()
print("Values:", values, "| Type:", type(values))

items = dict.items()
print("Items:", items, "| Type:", type(items))
