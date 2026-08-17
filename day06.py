# INSERT OPERATIONS

# create a list with 3 elements
list1 = [1, 2, 3]

# APPENDING
list1.append(10)
list1.append(10.5)
list1.append(True)
list1.append(3 + 4j)
list1.append(None)
print(list1)  # [1, 2, 3, 10, 10.5, True, (3+4j), None]
list1.append("hello")
list1.append([4, 5])
list1.append((6, 7))
list1.append(range(2))
list1.append(b"abc")
print(list1)  # [1, 2, 3, 10, 10.5, True, (3+4j), None, 'hello', [4, 5], (6, 7), range(0, 2), b'abc']

# EXTENDING

list1 = [1, 2, 3]

# add 5 types of non-sequence elements to it with extend
# list1.extend(10)              # TypeError
# list1.extend(10.5)            # TypeError
# list1.extend(True)             # TypeError
# list1.extend(3 + 4j)           # TypeError
# list1.extend(None)             # TypeError
list1.extend("abc")
print(list1)  # [1, 2, 3, 'a', 'b', 'c']

list1.extend([4, 5])
print(list1)  # [1, 2, 3, 'a', 'b', 'c', 4, 5]

list1.extend((6, 7))
print(list1)  # [1, 2, 3, 'a', 'b', 'c', 4, 5, 6, 7]

list1.extend(range(8, 11))
print(list1)  # [1, 2, 3, 'a', 'b', 'c', 4, 5, 6, 7, 8, 9, 10]

list1.extend(b"xyz")
print(list1)  # [1, 2, 3, 'a', 'b', 'c', 4, 5, 6, 7, 8, 9, 10, 120, 121, 122]

# INSERTING

list1 = [1, 2, 3]
list1.insert(1, 100)
print(list1)  # [1, 100, 2, 3]
list1.insert(-1, 200)
print(list1)  # [1, 100, 2, 200, 3]
list1.insert(10000, 300)
print(list1)  # [1, 100, 2, 200, 3, 300]
list1.insert(-10000, 400)
print(list1)  # [400, 1, 100, 2, 200, 3, 300]

# DELETE OPERATIONS
list1 = [1, 2, 1, 3, 4, 1]
print(list1.pop(3))  # 3
print(list1)        # [1, 2, 1, 4, 1]
print(list1.pop())  # 1
print(list1)        # [1, 2, 1, 4]
list1.remove(1)
print(list1)  # [2, 1, 4]
list1.clear()
print(list1)  # []

# UPDATE OPERATIONS
list1 = [3, 2, 1, 5, 4]
list1.sort()
print(list1)  # [1, 2, 3, 4, 5]
list1 = [3, 2, 1, 5, 4]
list1.sort(reverse=True)
print(list1)  # [5, 4, 3, 2, 1]
list1 = [3, 2, 1, 5, 4]
list1.reverse()
print(list1)  # [4, 5, 1, 2, 3]
# READ OPERATIONS
list1 = [1, 2, 1, 3, 1, 2]
print(list1.count(1))  # 3
print(list1.count(2))  # 2
print(list1.index(1))  # 0
print(list1.index(1, 2))  # 2
# print(list1.index(1, 5))  # ValueError: 1 is not in list

# TUPLE 
tuple1 = (1, 2, 1, 3, 1, 2)
print(tuple1.count(1))  # 3
print(tuple1.count(2))  # 2
print(tuple1.index(1))  # 0
print(tuple1.index(1, 2))  # 2
# print(tuple1.index(1, 5))  # ValueError: tuple.index(x): x not in tuple